from marshmallow import Schema, fields

class CrawlResponse(Schema):
    status = fields.Int()
    elapse = fields.Float()
    #headers = >?< it's CMultiDict from aiohttp structure. How to discribe use marshmallow? 
    html = fields.Str()