#! -*- coding: utf-8 -*-
import os

from ga_storage_manager import StorageManager

db = StorageManager(storage_manager_engine=StorageManager.STORAGE_MANAGER_ENGINE_MODE_FILESYSTEM,
                    storage_manager_file_path=os.getenv('DATABASE_PATH',
                                                        os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                                     os.getenv('DATABASE_NAME', "db.json"))))

auth_db = StorageManager(storage_manager_engine=StorageManager.STORAGE_MANAGER_ENGINE_MODE_FILESYSTEM,
                         storage_manager_file_path=os.getenv('DATABASE_PATH',
                                                             os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                                                          os.getenv('DATABASE_AUTH_NAME',
                                                                                    "auth.json"))))
