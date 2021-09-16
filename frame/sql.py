class Sql:
    custselone = "SELECT * FROM customer WHERE id='%s'"
    custselall = "SELECT * FROM customer"
    custinsert = "INSERT INTO customer(id, pwd, name, age, height, weight) VALUES ('%s', '%s', '%s', %d, %f, %d)"
    custupdate6 = "UPDATE customer SET pwd='%s', name='%s', age=%d, height=%f, weight=%d WHERE id='%s'"
    custupdate7 = "UPDATE customer SET pwd='%s', name='%s', age=%d, height=%f, weight=%d, right_size='%s' WHERE id='%s'"
    custdelete = "DELETE FROM customer WHERE id='%s'"

    linkselone = "SELECT mf, yoox, mt, net FROM link WHERE size='%s'"