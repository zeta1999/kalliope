import logging

from kalliope.core.Utils.Utils import Utils
from kalliope.core.ConfigurationManager.SettingLoader import SettingLoader

logging.basicConfig()
logger = logging.getLogger("kalliope")


class NeuronLauncher:

    def __init__(self):
        pass

    @classmethod
    def start_neuron(cls, neuron):
        """
        Start a neuron plugin
        :param neuron: neuron object
        :type neuron: Neuron
        :return:
        """
        logger.debug("Run plugin \"%s\" with parameters %s" % (neuron.name, neuron.parameters))
        sl = SettingLoader()
        settings = sl.settings
        return Utils.get_dynamic_class_instantiation(package_name="neurons",
                                                     module_name=neuron.name.capitalize(),
                                                     parameters=neuron.parameters,
                                                     resources_dir= settings.resource_dir)
