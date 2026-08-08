{{- define "ci-cd-demo.name" -}}
{{ default "ci-cd-demo" .Values.name }}
{{- end -}}

{{- define "ci-cd-demo.fullname" -}}
{{ template "ci-cd-demo.name" . }}-{{ .Release.Name }}
{{- end -}}

{{- define "ci-cd-demo.selectorLabels" -}}
app: {{ template "ci-cd-demo.name" . }}
release: {{ .Release.Name }}
{{- end -}}
