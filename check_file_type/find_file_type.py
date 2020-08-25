from . import ole
from . import hexdump
import sys
import struct
from . import about_property
import zlib

def get_header_info(fp):
    header = {}
    header_block = ole.ReadBlock(fp, -1)
    header['magic_number'] = hexdump.Dump(header_block, 0, 8) # d0 cf 11 e0 a1 b1 1a e1
    header['number_bbat_depot'] = struct.unpack('<I',hexdump.Dump(header_block, 44, 4))[0]
    header['start_entry_of_property'] = struct.unpack('<I', hexdump.Dump(header_block, 48, 4))[0]
    header['start_cluster_of_sbat'] = struct.unpack('<I', hexdump.Dump(header_block, 60 ,4))[0]
    header['number_sbat_depot'] = struct.unpack('<I', hexdump.Dump(header_block, 64, 4))[0]
    iter_bbat = struct.iter_unpack('<I', hexdump.Dump(header_block, 76, 4 * header['number_bbat_depot']))
    header['array_bbat'] = []
    for _ in range(0, header['number_bbat_depot']):
        header['array_bbat'].append(next(iter_bbat)[0])
    return header

def get_all_block(entry_list, fp):
    blocks = b""
    for idx in entry_list:
        blocks += hexdump.Dump(ole.ReadBlock(fp, idx), 0)

    return blocks

def get_all_small_block(small_blocks, entry_list):
    blocks = b""
    for idx in entry_list:
        blocks += small_blocks[idx * 0x40: (idx + 1) * 0x40]

    return blocks


def get_entry_list(bat, start_entry) : # 일반적인 entry list를 얻을 때 사용
    cluster = start_entry
    cluster_list = [cluster]
    while True:
        cluster_bytes =  bat[cluster * 4 : (cluster + 1) * 4]
        cluster = struct.unpack('<I', cluster_bytes)[0]
        if cluster == 0xfffffffe:
            break
        
        cluster_list.append(cluster)
    return cluster_list

def get_all_property(bbat, start_entry_of_property, fp): # property에 관한 entry list와 blocks을 얻을 수 있음
    property_entry_list = get_entry_list(bbat, start_entry_of_property)
    property_blocks = get_all_block(property_entry_list, fp)
    return property_blocks

def get_property_info(property_blocks, index): 
    property_data = hexdump.Dump(property_blocks, index * 0x80, 0x80)
    dic_property = {}
    dic_property['name'] = property_data[:40].decode('utf-16')
    return dic_property



def get_file_type(file_name):
    fp = open(file_name, 'rb')
    header = get_header_info(fp)
    bbat = get_all_block(header['array_bbat'], fp)
    property_data = get_all_property(bbat, header['start_entry_of_property'], fp)
    idx = 1
    while idx < 5:
        property_stream_info = get_property_info(property_data, idx)
        if "PowerPoint"  in property_stream_info['name']:
            return "PPT"
        if "Word"  in property_stream_info['name']:
            return "DOC"    
        if "Book"  in property_stream_info['name'] or "Workbook"  in property_stream_info['name']:
            return "XLS" 
        elif "Hwp" in property_stream_info['name']:
            return "HWP"
        idx += 1
    return "ETC"


if __name__ == "__main__":
    print(get_file_type(sys.argv[1]))

