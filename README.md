# this is the readme


# Installing FluxCD

```
fluxctl install \
--git-user=${GHUSER} \
--git-email=${GHUSER}@users.noreply.github.com \
--git-url=git@github.com:${GHUSER}/gitops-example \
--git-path=python \
--namespace=flux | kubectl apply -f -
```
