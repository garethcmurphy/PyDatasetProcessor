#!/usr/bin/env python3
import json
import os


from dataset import Dataset

class PyDatasetProcessor:
    def __init__(self):
        self.mydir = "./data"
        self.mydir = "static"
        #self.mydir = "/users/detector/experiments/multiblade/data/brightness"

    def walk_tree(self):

        datasets = {}
        orig_data = {}
        i = 0

        for dirpath, dirnames, filenames in os.walk(self.mydir):
            if not dirnames:
                print(dirpath, "has 0 subdirectories and", len(filenames), "files")
                print(filenames)
                i = i + 1
                basename = os.path.basename(dirpath)
                year = "2018"
                if basename[:3] == '201':
                    year = basename[:4]
                print('gm', year)

                d= Dataset()
                my_dataset = d.dataset
                my_dataset["pid"] = "MB" + str(i).zfill(5),
                print(my_dataset["pid"])
                filelist = []
                totalfilesize = 0
                for file in filenames:
                    longname = dirpath + '/' + file
                    
                    statinfo = os.stat(longname)
                    relpath = longname.replace('/users/detector', '/static')
                    file_size = statinfo.st_size
                    totalfilesize += file_size
                    file_entry = {
                        "path": relpath,
                        "size": file_size,
                        "time": "2018-04-23T09:23:47.000Z",
                        "chk": "string",
                        "uid": "string",
                        "gid": "string",
                        "perm": "string"
                    }
                    filelist.append(file_entry)
                my_dataset["size"] = totalfilesize
                my_dataset["packedSize"] = totalfilesize
                my_orig = {
                    "size": totalfilesize,
                    "dataFileList": filelist,
                    "ownerGroup": "brightness",
                    "accessGroups": [
                        "brightness"
                    ],
                    "createdBy": "ingestor",
                    "updatedBy": "ingestor",
                    "datasetId": "10.17199/"+str(my_dataset["pid"]),
                    "rawDatasetId": "string",
                    "derivedDatasetId": "string",
                    "createdAt": "2018-04-23T09:23:47.918Z",
                    "updatedAt": "2018-04-23T09:59:04.506Z"
                }
                scicat_entries = {"dataset": my_dataset, "orig": my_orig}
                orig_data["orig" + str(i)] = my_orig
                datasets["orig" + str(i)] = scicat_entries

        json_orig_data = json.dumps(orig_data)
        print(json_orig_data)
        json_datasets = json.dumps(datasets)
        print(json_datasets)

        with open('datasets.json', 'w') as f:
            json.dump(datasets, f, ensure_ascii=False)

        with open('orig.json', 'w') as f:
            json.dump(orig_data, f, ensure_ascii=False)


if __name__ == '__main__':
    g = PyDatasetProcessor()
    g.walk_tree()
