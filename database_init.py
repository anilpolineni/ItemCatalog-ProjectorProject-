from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from database_setup import *

engine = create_engine("sqlite:///projector.db")

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

# session.query(Owner).delete()

# session.query(Category).delete()

# session.query(Item_Details).delete()

# Create Owner
owner1 = Owner(owner_name="Polineni Anil",
               owner_email="anilpolineni09@gmail.com",
               owner_picture="https://lh3.googleusercontent.com/a-/"
               "AAuE7mC5iFOdtIN8N8IkHwT-7mJxgV7MWYuWDayxdPpolB8=s640-rw-il")
session.add(owner1)
session.commit()
print("Done..!")

# Create Categories

category1 = Category(name="LED_Projectors", owner_id=1)
session.add(category1)
session.commit()

category2 = Category(name="LCD_Projectors", owner_id=1)
session.add(category2)
session.commit()

category3 = Category(name="DLP_Projectors", owner_id=1)
session.add(category3)
session.commit()

category4 = Category(name="CRT_Projectors", owner_id=1)
session.add(category4)
session.commit()


# Item_Details
product1 = Item_Details(brandname="Epson",
                        model="V11H842040",
                        image="https://assets.pcmag.com/media/images/"
                        "315833-epson-ex3212-svga-3lcd-projector."
                        "jpg?width=1000&height=449",
                        color="white",
                        price="30000",
                        description="Epson has the"
                        "best projector for your business",
                        category_id="1",
                        ownerid=1)
session.add(product1)
session.commit()

product2 = Item_Details(brandname="Benq",
                        model="506p",
                        image="https://cf4.s3.souqcdn.com/item/2016/10/09/"
                        "11/65/92/24/item_XL_11659224_16790974.jpg",
                        color="White",
                        price="25000",
                        description="Benq has the best"
                        "projector for your business",
                        category_id="2",
                        ownerid=1)
session.add(product2)
session.commit()

product3 = Item_Details(brandname="Sony",
                        model="VPL-DX221",
                        image="https://rukminim1.flixcart.com/"
                        "image/704/704/projector/z/p/q/vpl-dx220"
                        "-vpl-dx220-sony-original-imaerf7qnzs9kd2q.jpeg?q=70",
                        color="white",
                        price="40000",
                        description="Sony has the best"
                        "projector for your business.",
                        category_id="3",
                        ownerid=1)
session.add(product3)
session.commit()

product4 = Item_Details(brandname="Canon",
                        model="Canon XEED WUX450ST",
                        image="https://lscdn.blob.core.windows.net/"
                        "products/projector/images/Canon-"
                        "XEED-WUX450ST-LCOS-Projector.jpg",
                        color="white",
                        price="35000",
                        description="Canon is a brand known for"
                        "its commendable cameras and their captures.",
                        category_id="4",
                        ownerid=1)
session.add(product4)
session.commit()

print("Brands are Added..!")
