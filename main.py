
from data_base import main_bd
from gui import main_window


if __name__ == "__main__":
    main_bd.ExecuteQuery().execute_query(main_bd.ConnectBD().create_connection('E:\\sm_app.sqlite'),
                                         main_bd.sqlite_insert_with_param)
    root = main_window.tk.Tk()
    app = main_window.PasswordGeneratorApp(root)
    root.mainloop()