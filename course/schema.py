from marshmallow import Schema, fields

class PlainDegreeSchema(Schema):
    id =                    fields.Str(dump_only=True)
    degree_track =          fields.Str(required=True)
    degree_name =           fields.Str(required=True)
    degree_desc =           fields.Str(required=True)
    curriculum_difficulty = fields.Float(required=True)

class PlainInstitutionSchema(Schema):
    id =            fields.Str(dump_only=True)
    inst_type =     fields.Str(required=True)
    uni_name =      fields.Str(required=True)
    uni_type =      fields.Str(required=True)
    uni_welcome =   fields.Str(required=True)
    uni_cost =      fields.Float(required=True)

class DegreeUpdateSchema(Schema):
    id =                    fields.Str(dump_only=True)
    degree_track =          fields.Str(required=True)
    degree_name =           fields.Str(required=True)
    degree_desc =           fields.Str(required=True)
    curriculum_difficulty = fields.Float(required=True)

class InstitutionUpdateSchema(Schema):
    id =            fields.Str(dump_only=True)
    inst_type =     fields.Str(required=True)
    uni_name =      fields.Str(required=True)
    uni_type =      fields.Str(required=True)
    uni_welcome =   fields.Str(required=True)
    uni_cost =      fields.Float(required=True)

class DegreeSchema(PlainDegreeSchema):
    institutions = fields.Nested(PlainInstitutionSchema(), dump_only=True)

class InstitutionSchema(PlainInstitutionSchema):
    degrees = fields.List(fields.Nested(PlainDegreeSchema), dump_only=True)