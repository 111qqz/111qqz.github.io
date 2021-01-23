---
title: "k8s nodes is forbidden user cannot list resource nodes in api group at the cluster scope"
date: 2020-05-07T16:01:52+08:00
draft: false
author: "111qqz"
type: post
url: /2020/05/install-k8s-get-nodes-forbidden-error/
categories:
- 其他

tags:

- k8s

---


继续将k8s用于模型转换和部署的自动化流程...然后发现之前安装k8s的文档不work了．．
时间是2020年5月7日，当前最新的k8s版本是　v1.18.2

报错如下:

```shell


<2kzzqw6rsjid0   --discovery-token-ca-cert-hash sha256:c6c72bdc96c0ff4d59559ff915eee61ba7ac5e8b93c0b2f9e11e813412387ec2  --v=5                                                                
W0507 15:45:12.608784    4768 join.go:346] [preflight] WARNING: JoinControlPane.controlPlane settings will be ignored when control-plane flag is not set.                                     
I0507 15:45:12.608822    4768 join.go:371] [preflight] found NodeName empty; using OS hostname as NodeName                                                                                    
I0507 15:45:12.608853    4768 initconfiguration.go:103] detected and using CRI socket: /var/run/dockershim.sock                                                                               
[preflight] Running pre-flight checks                                                                                                                                                         
I0507 15:45:12.608902    4768 preflight.go:90] [preflight] Running general checks                                                                                                             
I0507 15:45:12.608933    4768 checks.go:249] validating the existence and emptiness of directory /etc/kubernetes/manifests                                                                    
I0507 15:45:12.608966    4768 checks.go:286] validating the existence of file /etc/kubernetes/kubelet.conf                                                                                    
I0507 15:45:12.608975    4768 checks.go:286] validating the existence of file /etc/kubernetes/bootstrap-kubelet.conf                                                                          
I0507 15:45:12.608985    4768 checks.go:102] validating the container runtime                                                                                                                 
I0507 15:45:12.685381    4768 checks.go:128] validating if the service is enabled and active                                                                                                  
        [WARNING IsDockerSystemdCheck]: detected "cgroupfs" as the Docker cgroup driver. The recommended driver is "systemd". Please follow the guide at https://kubernetes.io/docs/setup/cri/
I0507 15:45:12.765669    4768 checks.go:335] validating the contents of file /proc/sys/net/bridge/bridge-nf-call-iptables                                                                     
I0507 15:45:12.765720    4768 checks.go:335] validating the contents of file /proc/sys/net/ipv4/ip_forward                                                                                    
I0507 15:45:12.765752    4768 checks.go:649] validating whether swap is enabled or not                                                                                                        
I0507 15:45:12.765780    4768 checks.go:376] validating the presence of executable conntrack                                                                                                  
I0507 15:45:12.765804    4768 checks.go:376] validating the presence of executable ip                                                                                                         
I0507 15:45:12.765826    4768 checks.go:376] validating the presence of executable iptables                                                                                                   
I0507 15:45:12.765844    4768 checks.go:376] validating the presence of executable mount                                                                                                      
I0507 15:45:12.765864    4768 checks.go:376] validating the presence of executable nsenter                                                                                                    
I0507 15:45:12.765882    4768 checks.go:376] validating the presence of executable ebtables                                                                                                   
I0507 15:45:12.765902    4768 checks.go:376] validating the presence of executable ethtool                                                                                                    
I0507 15:45:12.765920    4768 checks.go:376] validating the presence of executable socat                                                                                                      
I0507 15:45:12.765935    4768 checks.go:376] validating the presence of executable tc                                                                                                         
I0507 15:45:12.765953    4768 checks.go:376] validating the presence of executable touch                                                                                                      
I0507 15:45:12.765973    4768 checks.go:520] running all checks                                                                                                                               
I0507 15:45:12.844881    4768 checks.go:406] checking whether the given node name is reachable using net.LookupHost                                                                           
I0507 15:45:12.845030    4768 checks.go:618] validating kubelet version
I0507 15:45:12.888056    4768 checks.go:128] validating if the service is enabled and active
I0507 15:45:12.893254    4768 checks.go:201] validating availability of port 10250
I0507 15:45:12.893373    4768 checks.go:286] validating the existence of file /etc/kubernetes/pki/ca.crt
I0507 15:45:12.893388    4768 checks.go:432] validating if the connectivity type is via proxy or direct
I0507 15:45:12.893414    4768 join.go:441] [preflight] Discovering cluster-info
I0507 15:45:12.893440    4768 token.go:78] [discovery] Created cluster-info discovery client, requesting info from "172.20.52.117:6443"
I0507 15:45:13.033539    4768 token.go:116] [discovery] Requesting info from "172.20.52.117:6443" again to validate TLS against the pinned public key
I0507 15:45:13.172634    4768 token.go:133] [discovery] Cluster info signature and contents are valid and TLS certificate validates against pinned roots, will use API Server "172.20.52.117:6443"
I0507 15:45:13.172653    4768 discovery.go:51] [discovery] Using provided TLSBootstrapToken as authentication credentials for the join process
I0507 15:45:13.172660    4768 join.go:455] [preflight] Fetching init configuration
I0507 15:45:13.172669    4768 join.go:493] [preflight] Retrieving KubeConfig objects
[preflight] Reading configuration from the cluster...
[preflight] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -oyaml'
I0507 15:45:13.541858    4768 interface.go:400] Looking for default routes with IPv4 addresses
I0507 15:45:13.541871    4768 interface.go:405] Default route transits interface "eth0"
I0507 15:45:13.541941    4768 interface.go:208] Interface eth0 is up
I0507 15:45:13.541978    4768 interface.go:256] Interface "eth0" has 2 addresses :[10.198.21.97/22 fe80::f816:3eff:fe5e:88f1/64].
I0507 15:45:13.541998    4768 interface.go:223] Checking addr  10.198.21.97/22.
I0507 15:45:13.542008    4768 interface.go:230] IP found 10.198.21.97
I0507 15:45:13.542016    4768 interface.go:262] Found valid IPv4 address 10.198.21.97 for interface "eth0".
I0507 15:45:13.542023    4768 interface.go:411] Found active IP 10.198.21.97 
I0507 15:45:13.542057    4768 preflight.go:101] [preflight] Running configuration dependant checks
I0507 15:45:13.542072    4768 controlplaneprepare.go:211] [download-certs] Skipping certs download
I0507 15:45:13.542080    4768 kubelet.go:111] [kubelet-start] writing bootstrap kubelet config file at /etc/kubernetes/bootstrap-kubelet.conf
I0507 15:45:13.542775    4768 kubelet.go:119] [kubelet-start] writing CA certificate at /etc/kubernetes/pki/ca.crt
I0507 15:45:13.543283    4768 kubelet.go:145] [kubelet-start] Checking for an existing Node in the cluster with name "host-10-198-21-97" and status "Ready"
nodes "host-10-198-21-97" is forbidden: User "system:bootstrap:0752yx" cannot get resource "nodes" in API group "" at the cluster scope
cannot get Node "host-10-198-21-97"
k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/join.runKubeletStartJoinPhase
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/join/kubelet.go:148
k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/workflow.(*Runner).Run.func1
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/workflow/runner.go:234
k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/workflow.(*Runner).visitAll
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/workflow/runner.go:422
k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/workflow.(*Runner).Run
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/workflow/runner.go:207
k8s.io/kubernetes/cmd/kubeadm/app/cmd.NewCmdJoin.func1
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/app/cmd/join.go:170
k8s.io/kubernetes/vendor/github.com/spf13/cobra.(*Command).execute
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/vendor/github.com/spf13/cobra/command.go:826
k8s.io/kubernetes/vendor/github.com/spf13/cobra.(*Command).ExecuteC
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/vendor/github.com/spf13/cobra/command.go:914
k8s.io/kubernetes/vendor/github.com/spf13/cobra.(*Command).Execute
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/vendor/github.com/spf13/cobra/command.go:864
k8s.io/kubernetes/cmd/kubeadm/app.Run
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/app/kubeadm.go:50
main.main
        _output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/kubeadm.go:25
runtime.main
        /usr/local/go/src/runtime/proc.go:203
runtime.goexit
        /usr/local/go/src/runtime/asm_amd64.s:1357
error execution phase kubelet-start
k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/workflow.(*Runner).Run.func1
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/workflow/runner.go:235
k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/workflow.(*Runner).visitAll
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/workflow/runner.go:422
k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/workflow.(*Runner).Run
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/app/cmd/phases/workflow/runner.go:207
k8s.io/kubernetes/cmd/kubeadm/app/cmd.NewCmdJoin.func1
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/app/cmd/join.go:170
k8s.io/kubernetes/vendor/github.com/spf13/cobra.(*Command).execute
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/vendor/github.com/spf13/cobra/command.go:826
k8s.io/kubernetes/vendor/github.com/spf13/cobra.(*Command).ExecuteC
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/vendor/github.com/spf13/cobra/command.go:914
k8s.io/kubernetes/vendor/github.com/spf13/cobra.(*Command).Execute
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/vendor/github.com/spf13/cobra/command.go:864
k8s.io/kubernetes/cmd/kubeadm/app.Run
        /workspace/anago-v1.18.2-beta.0.14+a78cd082e8c913/src/k8s.io/kubernetes/_output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/app/kubeadm.go:50
main.main
        _output/dockerized/go/src/k8s.io/kubernetes/cmd/kubeadm/kubeadm.go:25
runtime.main
        /usr/local/go/src/runtime/proc.go:203
runtime.goexit
        /usr/local/go/src/runtime/asm_amd64.s:1357

```

看起来重点的报错在这一句

```shell

nodes "host-10-198-21-97" is forbidden: User "system:bootstrap:0752yx" cannot get resource "nodes" in API group "" at the cluster scope
cannot get Node "host-10-198-21-97"

```

然后google发现大概是权限相关的原因...Role-Based Access Contro　相关的．　但是似乎都不是在搭建集群的时候遇到的．

然后打算重新看一遍最新的搭建手册，发现troubleshooting里面

[Not possible to join a v1.18 Node to a v1.17 cluster due to missing RBAC](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/troubleshooting-kubeadm/#not-possible-to-join-a-v1-18-node-to-a-v1-17-cluster-due-to-missing-rbac)

原来是v1.18增加了权限控制，1.18的slave机器没办法加入到1.17的master节点上...看来就是这个问题．


然后在控制节点上apply了如下内容:

```yaml

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: kubeadm:get-nodes
rules:
- apiGroups:
  - ""
  resources:
  - nodes
  verbs:
  - get
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kubeadm:get-nodes
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: kubeadm:get-nodes
subjects:
- apiGroup: rbac.authorization.k8s.io
  kind: Group
  name: system:bootstrappers:kubeadm:default-node-token

```

重新尝试加入，已经可以了．