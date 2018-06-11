#!/usr/bin/env python3
import json
import os
import sys
import datetime

from dataset import Dataset
from orig import Orig

import re

class PyDatasetProcessor:
    def __init__(self):
        self.mydir = "./data"
        self.mydir = "static"
        # self.mydir = "/users/detector/experiments/multiblade/data/brightness"
        self.year_month_regex = '20[0-9]{2}_[0-1][0-9]'

    def walk_tree(self):

        datasets = {}
        i = 0

        for dirpath, dirnames, filenames in os.walk(self.mydir):
            if not dirnames:
                print(dirpath, "has 0 subdirectories and", len(filenames), "files")
                print(filenames)
                i = i + 1
                basename = os.path.basename(dirpath)

                year_month= "1999_09"
                year_month = re.search(self.year_month_regex,dirpath).group(0)
                #print('gm',year_month)
                year= year_month[0:4]
                month = year_month[5:7]

                data_date = datetime.datetime(int(year),int(month), 1)
                experiment_date_time=data_date.isoformat()


                d = Dataset()
                my_data_set = d.dataset
                my_data_set["pid"] = "MB" + str(i).zfill(5)
                print(my_data_set["pid"])
                file_list = []
                total_file_size = 0
                for file in filenames:
                    longname = dirpath + '/' + file

                    statinfo = os.stat(longname)
                    relpath = longname.replace('/users/detector', '/static')
                    file_size = statinfo.st_size
                    total_file_size += file_size
                    file_entry = {
                        "path": relpath,
                        "size": file_size,
                        "time": "2018-04-23T09:23:47.000Z",
                        "chk": "string",
                        "uid": "string",
                        "gid": "string",
                        "perm": "string"
                    }
                    file_list.append(file_entry)
                my_data_set["size"] = total_file_size
                my_data_set["packedSize"] = total_file_size
                my_data_set["creationTime"] = experiment_date_time
                my_data_set["endTime"] = experiment_date_time
                my_data_set["createdAt"] = experiment_date_time
                my_data_set["updatedAt"] = experiment_date_time
                orig = Orig()
                my_orig = orig.orig
                my_orig["datasetId"] = "10.17199/" + str(my_data_set["pid"])
                my_orig["dataFileList"] = file_list
                my_orig["size"] = total_file_size

                scicat_entries = {"dataset": my_data_set, "orig": my_orig}
                datasets["orig" + str(i).zfill(5)] = scicat_entries

        json.dump(datasets, sys.stdout, indent=2)

        with open('datasets.json', 'w') as f:
            json.dump(datasets, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    g = PyDatasetProcessor()
    g.walk_tree()
