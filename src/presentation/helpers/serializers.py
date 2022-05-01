def serialize_photo(photo):
    bson_id = photo["_id"]
    photo["_id"] = str(bson_id)
    return photo
