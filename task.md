Реализовать приложение, состоящее из клиентской и серверной части. В качестве клиента - gui приложение. Реализовать
при помощи tkinter. Форма состоит из трех кнопок - сгенерировать список записей, добавить новую запись, получить список записей.
Взаимодействие между клиентом и сервером происходит по REST.

По нажатию на "добавить новую запись" открывается форма, состоящая из полей имя, фамилия, отчество, дата рождения и кнопок "сохранить" и "отмена".
По нажатию на "сохранить" данные отправляются серверу. Далее форма добавления закрывается и выходит соответсnвующее сообщение либо
об успешности сохранения либо о неудаче сохранения.

По нажатию на "сгенерировать список записей" запрос отправляется серверу, но его обработка должна происходить асинхронно
(мы нажали кнопку сгенерировать и работа клиента не должна блокироваться, например, мы можем заново открыть форму добавления).
Сервер, получив запрос должен запустить celery задачу, в которой должна быть реализована подгрузка всех записей из базы и сохранение их в файл на сервере.

По нажатию на "получить список записей" запрос отправляется серверу и происходит считывание этих записей из файла и последующее отображение данных в отдельном окне клиента.

В случае возникновения непредвиденной ошибки клиента выводить сообщение об ошибке в отдельном окне и логировать ошибку в лог файл. Также в этом же окне реализовать кнопку, по нажатию на которую происходит считывание лог файла и вывод содержимого в этом же окне.
В случае возникновения непредвиденной ошибки на сервере логировать ошибку в лог файл на сервере.

В качестве хранилища использовать БД.
Обязательно к использованию: python 2, tkinter, celery.