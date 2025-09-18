
kubectl create serviceaccount my-user

kubectl create clusterrolebinding admin-user-binding --clusterrole=cluster-admin --serviceaccount=default:my-user

kubectl create token my-user


kubectl config set-cluster my-cluster --server=https://192.168.0.52:6443 --certificate-authority=ca.crt
kubectl config set-credentials remote-user --token=<TOKEN>
kubectl config set-context remote-context --cluster=my-cluster --user=remote-user
kubectl config use-context remote-context

kubectl config set-credentials mwhited --token=eyJhbGciOiJSUzI1NiIsImtpZCI6ImdwVDBvZlVXekMtN3dUVnNYcmNxdlBGdUp4MVFaa214WWRDVm5lVmxrNEUifQ.eyJhdWQiOlsiaHR0cHM6Ly9rdWJlcm5ldGVzLmRlZmF1bHQuc3ZjLmNsdXN0ZXIubG9jYWwiLCJrM3MiXSwiZXhwIjoxNzQxODAyMzg2LCJpYXQiOjE3NDE3OTg3ODYsImlzcyI6Imh0dHBzOi8va3ViZXJuZXRlcy5kZWZhdWx0LnN2Yy5jbHVzdGVyLmxvY2FsIiwianRpIjoiZDdlNjcxNzUtYTg3Zi00YjQ3LThlZGUtZDZhMDVhZTI0MjEyIiwia3ViZXJuZXRlcy5pbyI6eyJuYW1lc3BhY2UiOiJkZWZhdWx0Iiwic2VydmljZWFjY291bnQiOnsibmFtZSI6Im13aGl0ZWQiLCJ1aWQiOiI1NWI3MDc2OC00NjZkLTRmYzYtYWE3Mi01MTNlYmEyM2IzNzAifX0sIm5iZiI6MTc0MTc5ODc4Niwic3ViIjoic3lzdGVtOnNlcnZpY2VhY2NvdW50OmRlZmF1bHQ6bXdoaXRlZCJ9.CRQLvZE6JH0FLOh9NCr2y37J4yNRXkh0_JrK7Ui86SJ-01WNxRarGrJYNhNPE8Gp7-BlrRt7NtdTiLY05olSE_zFtB7NMRMNljdfj47J8oGjVYqapHCNRgJfy4J504-KdblD9fOr8X6bn_21xrGXeG6zq34sNDCP-HxLyLfFCJc5xad2-55jpS_GbBQO9akjJE4DpbQUWyQw5EEBRUH7lbKuytbcbG0QBVqGY-FrPb3GKwe6Kl0xqnPJRtVTk5VpvjOFRj8gkTCd5FzB_4eb3JDQwWh2TGkXfk0Y37BqLwAN7AAHoCuE8_WU_DCa6sjrdITrx_hBH0e2Qf54I--ZUg

kubectl config set-context linux-cluster --cluster=linux-cluster --user=mwhited
kubectl config use-context linux-cluster
kubectl config set-cluster linux-cluster --server=https://192.168.0.52:6443 --insecure-skip-tls-verify=true
