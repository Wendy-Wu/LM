'''
Created on Sep 27, 2015

@author: wuw7
'''
import xlrd
from dao.daos import InvDao
from model.models import Inventory

def _parse_file_to_list(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = [[sheet.cell_value(r, col) 
                for col in range(sheet.ncols)] 
                    for r in range(sheet.nrows)]
    return data

def parse_by_row(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    inv_args = []
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            inv_args.append(sheet.cell_value(row, col))
        inv = Inventory(inv_args[0], inv_args[1], inv_args[2], inv_args[3], inv_args[4], inv_args[5], inv_args[6], inv_args[7])
        InvDao.add_inventory()
    
