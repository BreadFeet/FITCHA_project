class Sql:
    custselone = "SELECT * FROM customer WHERE id='%s'"
    custselall = "SELECT * FROM customer"
    custinsert6 = "INSERT INTO customer(id, pwd, name, age, height, weight) VALUES ('%s', '%s', '%s', %d, %f, %d)"
    custinsert7 = "INSERT INTO customer VALUES ('%s', '%s', '%s', %d, %f, %d, '%s')"
    custupdate = "UPDATE customer SET pwd='%s', name='%s', age=%d, height=%f, weight=%d size='%s' WHERE id='%s'"
    custdelete = "DELETE FROM customer WHERE id='%s'"

    linkselone = "SELECT mf, yoox FROM link WHERE size='%s'"