import cryoet_metadata._base._models as _models


class CTFMetadata(_models.CTFMetadata):
    # Some additional validation logic added here
    pass


class AcquisitionMetadataMixin(_models.AcquisitionMetadataMixin):
    # Some additional validation logic added here
    pass


class GainFile(_models.Image2D):
    # Some additional validation logic added here
    pass


class DefectFile(_models.Image2D):
    # Some additional validation logic added here
    pass


class MovieFrame(_models.Image2D):
    # Some additional validation logic added here
    pass


class MovieStack(_models.ImageStack2D):
    # Some additional validation logic added here
    pass


class ProjectionImage(_models.Image2D):
    # Some additional validation logic added here
    pass


# class MovieStackSeries(_models.ImageStackSeries):
#     # Some additional validation logic added here
#     pass


class TiltSeries(_models.ImageStack2D):
    # Some additional validation logic added here
    pass


class SubProjectionImage(_models.ProjectionImage):
    # Some additional validation logic added here
    pass


class Tomogram(_models.Image3D):
    # Some additional validation logic added here
    pass


class ParticleMap(_models.Image3D):
    # Some additional validation logic added here
    pass
