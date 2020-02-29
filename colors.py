from . import np
import matplotlib

class ContinuousColormapper(object):
    def __init__(self, vmin, vmax, cmap="Blues", kind="hex"):
        """ Creates an object that can map from a continuous value to a color
            based on a colormap specified.

        Args:
            vmin, vmax: (float) set the extreme values for colormap
            cmap:       (str) matplotlib colormap
                        https://matplotlib.org/tutorials/colors/colormaps.html
            kind:       (str) how to return the colors.
                        - "hex" returns colors as hexadecinal notation
                        - "rgba" returns colors as a tuple of 4 floats (r,g,b,a)
        """
        assert vmin < vmax, "vmin must be smaller than vmax"
        assert kind.lower() in ["hex", "rgba"], 'kind must be one of ["hex", "rgba"]'
        self.vmin = vmin
        self.vmax = vmax
        self.cmap = cmap
        self.kind = kind

        # Normalize range of vals
        norm = matplotlib.colors.Normalize(vmin=vmin, vmax=vmax, clip=True)
        self.mapper = matplotlib.cm.ScalarMappable(norm=norm, cmap=cmap)
        # def create_continuous_colormapper(vmin, vmax, cmap="Greys_r"):

    def __call__(self, x):
        # HANDLE SCALAR INPUT
        is_scalar = np.isscalar(x)
        xx = np.asarray([x]) if is_scalar else np.asarray(x)
        shape = xx.shape
        xx  = xx.flatten()

        # MAP VALUES TO COLORS
        output = self.mapper.to_rgba(xx)
        if self.kind == "hex":
            output = np.array([matplotlib.colors.to_hex(val) for val in output])
            output = output.reshape(shape)
        else:
            output = output
            # an extra dimension with 4 elements beceuse it is now tuples of 4
            output = output.reshape(shape + (4,))


        # HANDLE OUTPUT
        if is_scalar:
            # output = np.squeeze(output).item()
            output = output[0]
        return output
