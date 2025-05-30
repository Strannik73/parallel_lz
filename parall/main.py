from mult_pt import m_pt

from asyn import asyn_c

def main():
    pr = asyn_c
    pr = m_pt
    pr.process_image()
    pr.write_file()
    pr.calculate_chunk()
    pr.apply_filter()
    pr.split_data()
    pr.async_requests()
    pr.interv()
if __name__ == '__main__':
    main()