class Sql:
    custselone = "SELECT * FROM customer WHERE id='%s'"
    custselall = "SELECT * FROM customer"
    custinsert = "INSERT INTO customer(id, pwd, name, age, height, weight) VALUES ('%s', '%s', '%s', %d, %f, %d)"
    # Update의 경우, right_size를 NULL로 넣어야 하는 경우를 고려해서 따옴표 제거
    custupdate = "UPDATE customer SET pwd='%s', name='%s', age=%d, height=%f, weight=%d, right_size=%s WHERE id='%s'"
    custdelete = "DELETE FROM customer WHERE id='%s'"

    linkselone = "SELECT mf, yoox, mt, net FROM link WHERE size='%s'"