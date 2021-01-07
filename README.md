# this is the readme


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


## cmds
fluxctl identity --k8s-fwd-ns flux
fluxctl sync --k8s-fwd-ns flux
