# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  if Vagrant.has_plugin? "vagrant-vbguest"
    config.vbguest.no_install  = true
    config.vbguest.auto_update = false
    config.vbguest.no_remote   = true    
  end

  config.vm.define :tensorFlowClientFromZero do |tensorFlowClientFromZero|
    tensorFlowClientFromZero.vm.box = "bento/ubuntu-22.04"
    tensorFlowClientFromZero.vm.synced_folder "./sharedFolder", "/home/vagrant/sharedFolder"
    tensorFlowClientFromZero.vm.hostname = "tensorFlowClientFromZero"    
  end
end
