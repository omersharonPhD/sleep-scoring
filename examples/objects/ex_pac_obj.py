"""
Phase-Amplitude Coupling (PAC)  object
======================================

The PAC measure the degree of coupling between the phase of slow oscillations
and the amplitude of fatser oscillations. To compute PAC, you'll need to
install the tensorpac package (see https://github.com/EtienneCmb/tensorpac).

The PacmapObj can be use to visualize three things :

    * The comodulogram of amplitude frequencies as a function of low frequency
      phase.
    * The evolution of coupling across time for several frequency phase
    * The evolution of coupling across time for several frequency amplitude

.. image:: ../../picture/picobjects/ex_pac_obj.png
"""
import numpy as np

from tensorpac.utils import pac_signals_wavelet

from sleep_scoring.objects import PacmapObj, SceneObj

"""Generate artificillly coupled signals :
- First coupling between 10hz phase with a 80hz amplitude
- Second coupling between 5hz phase with a 100hz amplitude

The final signal is the concatenation of both
"""
sf = 1024.
s_1 = pac_signals_wavelet(sf=sf, fpha=10., famp=80., ntrials=1, npts=5000)[0]
s_2 = pac_signals_wavelet(sf=sf, fpha=5., famp=100., ntrials=1, npts=5000)[0]
sig = np.c_[s_1, s_2]

sc = SceneObj()

print("""
# =============================================================================
#                              Comodulogram
# =============================================================================
""")
pac_obj_como = PacmapObj('como', sig, sf=sf, f_pha=(2, 30, 1, .5),
                         f_amp=(60, 150, 10, 1), interpolation='bicubic')
sc.add_to_subplot(pac_obj_como, row=0, col=0, title='Comodulogram')

print("""
# =============================================================================
#                         Optimal phase frequency
# =============================================================================
""")
pac_pha_como = PacmapObj('como', sig, sf=sf, f_pha=(2, 30, 1, .5),
                         f_amp=[70., 110.], n_window=500, cmap='plasma')
sc.add_to_subplot(pac_pha_como, row=0, col=1, title='Optimal phase frequency')

print("""
# =============================================================================
#                         Optimal amplitude frequency
# =============================================================================
""")
pac_amp_como = PacmapObj('como', sig, sf=sf, f_pha=[2, 20],
                         f_amp=(60, 150, 10, 1), n_window=500, cmap='inferno')
sc.add_to_subplot(pac_amp_como, row=0, col=2,
                  title='Optimal amplitude frequency')
sc.preview()
