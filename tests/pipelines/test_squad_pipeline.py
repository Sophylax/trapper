import json

import pytest
from transformers import set_seed

from trapper.common.constants import SpanTuple
from trapper.common.params import Params
from trapper.pipelines.pipeline import _create_pipeline
from trapper.pipelines.question_answering_pipeline import (
    SquadQuestionAnsweringPipeline,
)


@pytest.fixture(scope="module")
def roberta_base_squad_pipeline_params():
    params = {
        "model_wrapper": {
            "type": "question_answering"
        },
        "tokenizer_wrapper": {
            "type": "question-answering"
        },
        "dataset_loader": {
            "type": "default",
            "data_adapter": {
                "type": "question-answering"
            },
            "data_processor": {
                "type": "squad-question-answering"
            }
        },
    }
    return Params(params)

@pytest.fixture(scope="module")
def roberta_base_squad_pipeline(roberta_base_squad_pipeline_params):
    set_seed(100)
    return _create_pipeline('roberta-base', roberta_base_squad_pipeline_params, 'squad-question-answering')

@pytest.fixture(scope="module")
def roberta_base_squad_pipeline_sample_input():
    return [
        {'context': 'Super Bowl 50 was an American football game to determine the champion of the National Football League (NFL) for the 2015 season. The American Football Conference (AFC) champion Denver Broncos defeated the National Football Conference (NFC) champion Carolina Panthers 24–10 to earn their third Super Bowl title. The game was played on February 7, 2016, at Levi\'s Stadium in the San Francisco Bay Area at Santa Clara, California. As this was the 50th Super Bowl, the league emphasized the "golden anniversary" with various gold-themed initiatives, as well as temporarily suspending the tradition of naming each Super Bowl game with Roman numerals (under which the game would have been known as "Super Bowl L"), so that the logo could prominently feature the Arabic numerals 50.',
        'question': 'Which NFL team represented the AFC at Super Bowl 50?',
        'id': '0'}
    ]

@pytest.fixture(scope="module")
def roberta_base_squad_pipeline_expected_output():
    return {'score': 6.733023474225774e-05,
            'answer': SpanTuple(text='so that the logo could prominently feature the Arabic', start=709)
            }

def test_pipeline_execution(roberta_base_squad_pipeline, roberta_base_squad_pipeline_sample_input, roberta_base_squad_pipeline_expected_output):
    actual_output = roberta_base_squad_pipeline(roberta_base_squad_pipeline_sample_input)
    assert actual_output == roberta_base_squad_pipeline_expected_output