# Wide table DB models are put here
import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel

class RomanceTestResult(DjangoCassandraModel):
    testID = columns.UUID(default=uuid.uuid4(), primary_key=True)
    user = columns.Integer()
    startDateTime = columns.DateTime()
    endDateTime = columns.DateTime()
    testTypes = columns.List(value_type=columns.Text()) # aerbs, nouns, etc.
    testIDs = columns.List(value_type=columns.Integer()) # IDs of the tests
    answers = columns.List(value_type=columns.Text()) # answers given
    correct = columns.List(value_type=columns.Boolean()) # correct?
    correctSansAccents = columns.List(value_type=columns.Boolean())
    correctDiffAccents = columns.List(value_type=columns.Boolean())
    difficulty = columns.List(value_type=columns.Integer())
    flags = columns.List(value_type=columns.Text())


class RomanceTestID_by_user_and_language(DjangoCassandraModel):
    user = columns.Integer(primary_key=True)
    language = columns.Text(primary_key=True)
    testID = columns.UUID(default=uuid.uuid4(), primary_key=True)
    class Meta:
        get_pk_field='user'


class RomanceTestID_by_user_and_start_date(DjangoCassandraModel):
    user = columns.Integer(primary_key=True)
    endDateTime = columns.DateTime(primary_key=True)
    testID = columns.UUID(default=uuid.uuid4())
    class Meta:
        get_pk_field='user'


class RomanceTestResult_by_user_and_date(DjangoCassandraModel):
    user = columns.Integer(primary_key=True)
    startDateTime = columns.DateTime(primary_key=True)
    testID = columns.UUID(default=uuid.uuid4()) 
    class Meta:
        get_pk_field='user'

