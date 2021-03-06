import _plotly_utils.basevalidators


class DomainValidator(_plotly_utils.basevalidators.InfoArrayValidator):

    def __init__(
        self, plotly_name='domain', parent_name='layout.yaxis', **kwargs
    ):
        super(DomainValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot',
            items=[
                {
                    'valType': 'number',
                    'min': 0,
                    'max': 1,
                    'editType': 'plot'
                }, {
                    'valType': 'number',
                    'min': 0,
                    'max': 1,
                    'editType': 'plot'
                }
            ],
            role='info',
            **kwargs
        )
