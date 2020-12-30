#!/usr/bin/bash
# https://docs.fluxcd.io/en/1.18.0/tutorials/get-started.html
# https://medium.com/@berndonline/how-to-manage-kubernetes-clusters-the-gitops-way-with-flux-cd-c5cf9103a315

#install
sudo wget -O /usr/local/bin/fluxctl https://github.com/fluxcd/flux/releases/download/1.18.0/fluxctl_linux_amd64
sudo chmod 755 /usr/local/bin/fluxctl

# set user for Github
export GHUSER=falenn

# setup flux operator
fluxctl install \
 --git-user=${GHUSER} \
 --git-email=${GHUSER}@users.noreply.github.com \
 --git-url=${GHUSER}@github.com:${GHUSER}/python-gitops \
 --git-path=namespaces,production \
 --namespace=flux | kubectl apply -f -

# check if ready
kubectl -n flux rollout status deployment/flux

# get github deploy key
fluxctl identity --k8s-fwd-ns flux
