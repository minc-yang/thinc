import sys

SHAPE_ERR_TEMPLATE = '''

In the context of {context}:\n

Shape1 != Shape2

Where:

Shape1={shape1}
Shape2={shape2}
'''

class ShapeError(ValueError):
    def __init__(self, shape1, shape2, context):
        msg = SHAPE_ERR_TEMPLATE.strip().format(
            shape1=shape1, shape2=shape2, context=context)
        ValueError.__init__(self, msg)
        self.tb = sys.exc_info()[2]

    @classmethod
    def dimensions_mismatch(cls, shape1, shape2, context):
        if shape1 == shape2:
            return None
        else:
            return cls(shape1, shape2, context)
    
    @classmethod
    def dim_mismatch(cls, expected, observed):
        return cls("Dimension mismatch: %s vs %s" % (expected, observed))
