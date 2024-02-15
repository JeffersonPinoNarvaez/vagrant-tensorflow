# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  if Vagrant.has_plugin? "vagrant-vbguest"
    config.vbguest.no_install  = true
    config.vbguest.auto_update = false
    config.vbguest.no_remote   = true    
  end

  config.vm.define :tensorFlowClient do |tensorFlowClient|
    tensorFlowClient.vm.box = "JeffersonPino/ubuntu-tensorflow"
    tensorFlowClient.vm.box_version = "0.1.0"
    tensorFlowClient.vm.synced_folder "./sharedFolder", "/home/vagrant/sharedFolder"
    tensorFlowClient.vm.hostname = "tensorFlowClient"    
  end
end
