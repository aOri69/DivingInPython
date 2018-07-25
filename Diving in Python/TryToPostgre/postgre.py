import postgresql.exceptions as exc
import postgresql.driver as pg_driver


def main():
    try:
        with pg_driver.connect(user='alex', password='123', host='127.0.0.1', database='mydb', port='5432') as db:
            sql = db.prepare("SELECT * FROM public.users")
            for n in sql:
                print(f"{n[0]} - {n[1]}")

    except exc.Error as err:
        print(f"connection error: {err.args}")


if __name__ == '__main__':
    main()
