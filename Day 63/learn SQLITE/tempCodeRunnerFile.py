with app.app_context():
#     book_to_update=db.session.execute(db.select(Book).where(Book.title=="Test")).scalar()
#     book_to_update.title="Road Taken"
#     db.session.commit()