from ipykernel.kernelapp import IPKernelApp
from .kernel import CMakeKernel
IPKernelApp.launch_instance(kernel_class=CMakeKernel)
