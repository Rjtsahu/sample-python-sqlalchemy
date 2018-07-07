from db.db_main import fetch_all_person,create_test_record,create_database

if __name__ == '__main__':
    create_database()
    create_test_record()
    fetch_all_person()
