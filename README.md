# Gitops-example
Using Github pipeline and FluxCD (Continuous Deployment), we are able to invoke new Docker Image builds upon branch check-in and deployment via Flux Operater and deploy key.

https://hub.docker.com/r/falenn/python-gitops/tags?page=1&ordering=last_updated


# Set the Github user for this operator
export GHUSER=<your username>

# Installing FluxCD

```
fluxctl install \
--git-user=${GHUSER} \
--git-branch=main \
--git-email=${GHUSER}@users.noreply.github.com \
--git-url=git@github.com:${GHUSER}/gitops-example \
--git-path=namespaces,workloads \
--namespace=flux | kubectl apply -f -
```
# check install rollout
Why do we do this?  Flux is running an operator as a deployment to manage this particular application
```
kubectl -n flux rollout status deployments/flux
```
# Get the flux identity for this operator
fluxctl identity --k8s-fwd-ns flux

# Setup the Github deploykey
Goto github, repo, settings, deploy keys.  Create the key, select allow write

# sync the operator
fluxctl sync --k8s-fwd-ns flux

kubectl get namespaces

kubectl get pods -n <namespce configured for the deploymnet in your namespaces / workloads directories in the repo.

Score!
