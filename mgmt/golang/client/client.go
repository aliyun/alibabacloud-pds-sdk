// This file is auto-generated, don't edit it. Thanks.
/**
 *
 */
package client

import (
  util  "github.com/alibabacloud-go/tea-utils/service"
  roautil  "github.com/alibabacloud-go/tea-roa-utils/service"
  credential  "github.com/aliyun/credentials-go/credentials"
  "github.com/alibabacloud-go/tea/tea"
)

type RuntimeOptions struct {
  // whether to try again
  Autoretry *bool `json:"autoretry,omitempty" xml:"autoretry,omitempty"`
  // ignore SSL validation
  IgnoreSSL *bool `json:"ignoreSSL,omitempty" xml:"ignoreSSL,omitempty"`
  // maximum number of retries
  MaxAttempts *int `json:"maxAttempts,omitempty" xml:"maxAttempts,omitempty"`
  // backoff policy
  BackoffPolicy *string `json:"backoffPolicy,omitempty" xml:"backoffPolicy,omitempty"`
  // backoff period
  BackoffPeriod *int `json:"backoffPeriod,omitempty" xml:"backoffPeriod,omitempty"`
  // read timeout
  ReadTimeout *int `json:"readTimeout,omitempty" xml:"readTimeout,omitempty"`
  // connect timeout
  ConnectTimeout *int `json:"connectTimeout,omitempty" xml:"connectTimeout,omitempty"`
  // http proxy url
  HttpProxy *string `json:"httpProxy,omitempty" xml:"httpProxy,omitempty"`
  // https Proxy url
  HttpsProxy *string `json:"httpsProxy,omitempty" xml:"httpsProxy,omitempty"`
  // agent blacklist
  NoProxy *string `json:"noProxy,omitempty" xml:"noProxy,omitempty"`
  // maximum number of connections
  MaxIdleConns *int `json:"maxIdleConns,omitempty" xml:"maxIdleConns,omitempty"`
  // local addr
  LocalAddr *string `json:"localAddr,omitempty" xml:"localAddr,omitempty"`
  // SOCKS5 proxy
  Socks5Proxy *string `json:"socks5Proxy,omitempty" xml:"socks5Proxy,omitempty"`
  // SOCKS5 netWork
  Socks5NetWork *string `json:"socks5NetWork,omitempty" xml:"socks5NetWork,omitempty"`
}

func (s RuntimeOptions) String() string {
  return tea.Prettify(s)
}

func (s RuntimeOptions) GoString() string {
  return s.String()
}

func (s *RuntimeOptions) SetAutoretry(v bool) *RuntimeOptions {
  s.Autoretry = &v
  return s
}

func (s *RuntimeOptions) SetIgnoreSSL(v bool) *RuntimeOptions {
  s.IgnoreSSL = &v
  return s
}

func (s *RuntimeOptions) SetMaxAttempts(v int) *RuntimeOptions {
  s.MaxAttempts = &v
  return s
}

func (s *RuntimeOptions) SetBackoffPolicy(v string) *RuntimeOptions {
  s.BackoffPolicy = &v
  return s
}

func (s *RuntimeOptions) SetBackoffPeriod(v int) *RuntimeOptions {
  s.BackoffPeriod = &v
  return s
}

func (s *RuntimeOptions) SetReadTimeout(v int) *RuntimeOptions {
  s.ReadTimeout = &v
  return s
}

func (s *RuntimeOptions) SetConnectTimeout(v int) *RuntimeOptions {
  s.ConnectTimeout = &v
  return s
}

func (s *RuntimeOptions) SetHttpProxy(v string) *RuntimeOptions {
  s.HttpProxy = &v
  return s
}

func (s *RuntimeOptions) SetHttpsProxy(v string) *RuntimeOptions {
  s.HttpsProxy = &v
  return s
}

func (s *RuntimeOptions) SetNoProxy(v string) *RuntimeOptions {
  s.NoProxy = &v
  return s
}

func (s *RuntimeOptions) SetMaxIdleConns(v int) *RuntimeOptions {
  s.MaxIdleConns = &v
  return s
}

func (s *RuntimeOptions) SetLocalAddr(v string) *RuntimeOptions {
  s.LocalAddr = &v
  return s
}

func (s *RuntimeOptions) SetSocks5Proxy(v string) *RuntimeOptions {
  s.Socks5Proxy = &v
  return s
}

func (s *RuntimeOptions) SetSocks5NetWork(v string) *RuntimeOptions {
  s.Socks5NetWork = &v
  return s
}

type Config struct {
  Endpoint *string `json:"endpoint,omitempty" xml:"endpoint,omitempty"`
  Region *string `json:"region,omitempty" xml:"region,omitempty"`
  Protocol *string `json:"protocol,omitempty" xml:"protocol,omitempty"`
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  SecurityToken *string `json:"securityToken,omitempty" xml:"securityToken,omitempty"`
  AccessKeyId *string `json:"accessKeyId,omitempty" xml:"accessKeyId,omitempty"`
  AccessKeySecret *string `json:"accessKeySecret,omitempty" xml:"accessKeySecret,omitempty"`
  Nickname *string `json:"nickname,omitempty" xml:"nickname,omitempty"`
  UserAgent *string `json:"userAgent,omitempty" xml:"userAgent,omitempty"`
}

func (s Config) String() string {
  return tea.Prettify(s)
}

func (s Config) GoString() string {
  return s.String()
}

func (s *Config) SetEndpoint(v string) *Config {
  s.Endpoint = &v
  return s
}

func (s *Config) SetRegion(v string) *Config {
  s.Region = &v
  return s
}

func (s *Config) SetProtocol(v string) *Config {
  s.Protocol = &v
  return s
}

func (s *Config) SetType(v string) *Config {
  s.Type = &v
  return s
}

func (s *Config) SetSecurityToken(v string) *Config {
  s.SecurityToken = &v
  return s
}

func (s *Config) SetAccessKeyId(v string) *Config {
  s.AccessKeyId = &v
  return s
}

func (s *Config) SetAccessKeySecret(v string) *Config {
  s.AccessKeySecret = &v
  return s
}

func (s *Config) SetNickname(v string) *Config {
  s.Nickname = &v
  return s
}

func (s *Config) SetUserAgent(v string) *Config {
  s.UserAgent = &v
  return s
}

type CreateAppModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *GetAppResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s CreateAppModel) String() string {
  return tea.Prettify(s)
}

func (s CreateAppModel) GoString() string {
  return s.String()
}

func (s *CreateAppModel) SetHeaders(v map[string]*string) *CreateAppModel {
  s.Headers = v
  return s
}

func (s *CreateAppModel) SetBody(v *GetAppResponse) *CreateAppModel {
  s.Body = v
  return s
}

type DeleteAppModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s DeleteAppModel) String() string {
  return tea.Prettify(s)
}

func (s DeleteAppModel) GoString() string {
  return s.String()
}

func (s *DeleteAppModel) SetHeaders(v map[string]*string) *DeleteAppModel {
  s.Headers = v
  return s
}

type GetAppModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *GetAppResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetAppModel) String() string {
  return tea.Prettify(s)
}

func (s GetAppModel) GoString() string {
  return s.String()
}

func (s *GetAppModel) SetHeaders(v map[string]*string) *GetAppModel {
  s.Headers = v
  return s
}

func (s *GetAppModel) SetBody(v *GetAppResponse) *GetAppModel {
  s.Body = v
  return s
}

type GetPublicKeyModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *GetAppPublicKeyResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetPublicKeyModel) String() string {
  return tea.Prettify(s)
}

func (s GetPublicKeyModel) GoString() string {
  return s.String()
}

func (s *GetPublicKeyModel) SetHeaders(v map[string]*string) *GetPublicKeyModel {
  s.Headers = v
  return s
}

func (s *GetPublicKeyModel) SetBody(v *GetAppPublicKeyResponse) *GetPublicKeyModel {
  s.Body = v
  return s
}

type ListAppModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *ListAppsResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ListAppModel) String() string {
  return tea.Prettify(s)
}

func (s ListAppModel) GoString() string {
  return s.String()
}

func (s *ListAppModel) SetHeaders(v map[string]*string) *ListAppModel {
  s.Headers = v
  return s
}

func (s *ListAppModel) SetBody(v *ListAppsResponse) *ListAppModel {
  s.Body = v
  return s
}

type ListPublishedAppModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *ListAppsResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ListPublishedAppModel) String() string {
  return tea.Prettify(s)
}

func (s ListPublishedAppModel) GoString() string {
  return s.String()
}

func (s *ListPublishedAppModel) SetHeaders(v map[string]*string) *ListPublishedAppModel {
  s.Headers = v
  return s
}

func (s *ListPublishedAppModel) SetBody(v *ListAppsResponse) *ListPublishedAppModel {
  s.Body = v
  return s
}

type SetPublicKeyModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s SetPublicKeyModel) String() string {
  return tea.Prettify(s)
}

func (s SetPublicKeyModel) GoString() string {
  return s.String()
}

func (s *SetPublicKeyModel) SetHeaders(v map[string]*string) *SetPublicKeyModel {
  s.Headers = v
  return s
}

type UpdateAppModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *GetAppResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s UpdateAppModel) String() string {
  return tea.Prettify(s)
}

func (s UpdateAppModel) GoString() string {
  return s.String()
}

func (s *UpdateAppModel) SetHeaders(v map[string]*string) *UpdateAppModel {
  s.Headers = v
  return s
}

func (s *UpdateAppModel) SetBody(v *GetAppResponse) *UpdateAppModel {
  s.Body = v
  return s
}

type AddStoreModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *AddStoreResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s AddStoreModel) String() string {
  return tea.Prettify(s)
}

func (s AddStoreModel) GoString() string {
  return s.String()
}

func (s *AddStoreModel) SetHeaders(v map[string]*string) *AddStoreModel {
  s.Headers = v
  return s
}

func (s *AddStoreModel) SetBody(v *AddStoreResponse) *AddStoreModel {
  s.Body = v
  return s
}

type CreateDomainModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *CreateDomainResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s CreateDomainModel) String() string {
  return tea.Prettify(s)
}

func (s CreateDomainModel) GoString() string {
  return s.String()
}

func (s *CreateDomainModel) SetHeaders(v map[string]*string) *CreateDomainModel {
  s.Headers = v
  return s
}

func (s *CreateDomainModel) SetBody(v *CreateDomainResponse) *CreateDomainModel {
  s.Body = v
  return s
}

type DeleteBizCnameCertModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s DeleteBizCnameCertModel) String() string {
  return tea.Prettify(s)
}

func (s DeleteBizCnameCertModel) GoString() string {
  return s.String()
}

func (s *DeleteBizCnameCertModel) SetHeaders(v map[string]*string) *DeleteBizCnameCertModel {
  s.Headers = v
  return s
}

type DeleteDomainModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s DeleteDomainModel) String() string {
  return tea.Prettify(s)
}

func (s DeleteDomainModel) GoString() string {
  return s.String()
}

func (s *DeleteDomainModel) SetHeaders(v map[string]*string) *DeleteDomainModel {
  s.Headers = v
  return s
}

type DeleteBizCnameAndCertModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s DeleteBizCnameAndCertModel) String() string {
  return tea.Prettify(s)
}

func (s DeleteBizCnameAndCertModel) GoString() string {
  return s.String()
}

func (s *DeleteBizCnameAndCertModel) SetHeaders(v map[string]*string) *DeleteBizCnameAndCertModel {
  s.Headers = v
  return s
}

type DeleteDataCnameAndCertModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s DeleteDataCnameAndCertModel) String() string {
  return tea.Prettify(s)
}

func (s DeleteDataCnameAndCertModel) GoString() string {
  return s.String()
}

func (s *DeleteDataCnameAndCertModel) SetHeaders(v map[string]*string) *DeleteDataCnameAndCertModel {
  s.Headers = v
  return s
}

type GetDomainModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *GetDomainResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetDomainModel) String() string {
  return tea.Prettify(s)
}

func (s GetDomainModel) GoString() string {
  return s.String()
}

func (s *GetDomainModel) SetHeaders(v map[string]*string) *GetDomainModel {
  s.Headers = v
  return s
}

func (s *GetDomainModel) SetBody(v *GetDomainResponse) *GetDomainModel {
  s.Body = v
  return s
}

type GetBizCnameInfoModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *GetBizCNameInfoResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetBizCnameInfoModel) String() string {
  return tea.Prettify(s)
}

func (s GetBizCnameInfoModel) GoString() string {
  return s.String()
}

func (s *GetBizCnameInfoModel) SetHeaders(v map[string]*string) *GetBizCnameInfoModel {
  s.Headers = v
  return s
}

func (s *GetBizCnameInfoModel) SetBody(v *GetBizCNameInfoResponse) *GetBizCnameInfoModel {
  s.Body = v
  return s
}

type GetCorsRuleListModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *ListDomainCORSRuleResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetCorsRuleListModel) String() string {
  return tea.Prettify(s)
}

func (s GetCorsRuleListModel) GoString() string {
  return s.String()
}

func (s *GetCorsRuleListModel) SetHeaders(v map[string]*string) *GetCorsRuleListModel {
  s.Headers = v
  return s
}

func (s *GetCorsRuleListModel) SetBody(v *ListDomainCORSRuleResponse) *GetCorsRuleListModel {
  s.Body = v
  return s
}

type GetDataCnameInfoModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *GetBizCNameInfoResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetDataCnameInfoModel) String() string {
  return tea.Prettify(s)
}

func (s GetDataCnameInfoModel) GoString() string {
  return s.String()
}

func (s *GetDataCnameInfoModel) SetHeaders(v map[string]*string) *GetDataCnameInfoModel {
  s.Headers = v
  return s
}

func (s *GetDataCnameInfoModel) SetBody(v *GetBizCNameInfoResponse) *GetDataCnameInfoModel {
  s.Body = v
  return s
}

type ListDomainModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *ListDomainsResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ListDomainModel) String() string {
  return tea.Prettify(s)
}

func (s ListDomainModel) GoString() string {
  return s.String()
}

func (s *ListDomainModel) SetHeaders(v map[string]*string) *ListDomainModel {
  s.Headers = v
  return s
}

func (s *ListDomainModel) SetBody(v *ListDomainsResponse) *ListDomainModel {
  s.Body = v
  return s
}

type ListStoresModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *ListStoresResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ListStoresModel) String() string {
  return tea.Prettify(s)
}

func (s ListStoresModel) GoString() string {
  return s.String()
}

func (s *ListStoresModel) SetHeaders(v map[string]*string) *ListStoresModel {
  s.Headers = v
  return s
}

func (s *ListStoresModel) SetBody(v *ListStoresResponse) *ListStoresModel {
  s.Body = v
  return s
}

type RemoveStoreModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s RemoveStoreModel) String() string {
  return tea.Prettify(s)
}

func (s RemoveStoreModel) GoString() string {
  return s.String()
}

func (s *RemoveStoreModel) SetHeaders(v map[string]*string) *RemoveStoreModel {
  s.Headers = v
  return s
}

type SetBizCnameModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *SetBizCNameResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s SetBizCnameModel) String() string {
  return tea.Prettify(s)
}

func (s SetBizCnameModel) GoString() string {
  return s.String()
}

func (s *SetBizCnameModel) SetHeaders(v map[string]*string) *SetBizCnameModel {
  s.Headers = v
  return s
}

func (s *SetBizCnameModel) SetBody(v *SetBizCNameResponse) *SetBizCnameModel {
  s.Body = v
  return s
}

type SetBizCnameCertModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *SetBizCNameCertResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s SetBizCnameCertModel) String() string {
  return tea.Prettify(s)
}

func (s SetBizCnameCertModel) GoString() string {
  return s.String()
}

func (s *SetBizCnameCertModel) SetHeaders(v map[string]*string) *SetBizCnameCertModel {
  s.Headers = v
  return s
}

func (s *SetBizCnameCertModel) SetBody(v *SetBizCNameCertResponse) *SetBizCnameCertModel {
  s.Body = v
  return s
}

type SetCorsRuleListModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *ListDomainCORSRuleResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s SetCorsRuleListModel) String() string {
  return tea.Prettify(s)
}

func (s SetCorsRuleListModel) GoString() string {
  return s.String()
}

func (s *SetCorsRuleListModel) SetHeaders(v map[string]*string) *SetCorsRuleListModel {
  s.Headers = v
  return s
}

func (s *SetCorsRuleListModel) SetBody(v *ListDomainCORSRuleResponse) *SetCorsRuleListModel {
  s.Body = v
  return s
}

type SetDataCnameModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *SetDataCNameResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s SetDataCnameModel) String() string {
  return tea.Prettify(s)
}

func (s SetDataCnameModel) GoString() string {
  return s.String()
}

func (s *SetDataCnameModel) SetHeaders(v map[string]*string) *SetDataCnameModel {
  s.Headers = v
  return s
}

func (s *SetDataCnameModel) SetBody(v *SetDataCNameResponse) *SetDataCnameModel {
  s.Body = v
  return s
}

type UpdateDomainModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *UpdateDomainResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s UpdateDomainModel) String() string {
  return tea.Prettify(s)
}

func (s UpdateDomainModel) GoString() string {
  return s.String()
}

func (s *UpdateDomainModel) SetHeaders(v map[string]*string) *UpdateDomainModel {
  s.Headers = v
  return s
}

func (s *UpdateDomainModel) SetBody(v *UpdateDomainResponse) *UpdateDomainModel {
  s.Body = v
  return s
}

/**
 * 
 */
type AddStoreRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // 存储公共前缀
  BasePath *string `json:"base_path,omitempty" xml:"base_path,omitempty"`
  // bucket名称
  Bucket *string `json:"bucket,omitempty" xml:"bucket,omitempty"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // 存储访问地址
  Endpoint *string `json:"endpoint,omitempty" xml:"endpoint,omitempty" require:"true"`
  // 存储归属，system表示系统提供，custom表示使用自己的存储
  Ownership *string `json:"ownership,omitempty" xml:"ownership,omitempty"`
  // 访问Bucket的角色ARN
  RoleArn *string `json:"role_arn,omitempty" xml:"role_arn,omitempty"`
  // 存储类型，当前只支持oss
  Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
}

func (s AddStoreRequest) String() string {
  return tea.Prettify(s)
}

func (s AddStoreRequest) GoString() string {
  return s.String()
}

func (s *AddStoreRequest) SetHeaders(v map[string]*string) *AddStoreRequest {
  s.Headers = v
  return s
}

func (s *AddStoreRequest) SetBasePath(v string) *AddStoreRequest {
  s.BasePath = &v
  return s
}

func (s *AddStoreRequest) SetBucket(v string) *AddStoreRequest {
  s.Bucket = &v
  return s
}

func (s *AddStoreRequest) SetDomainId(v string) *AddStoreRequest {
  s.DomainId = &v
  return s
}

func (s *AddStoreRequest) SetEndpoint(v string) *AddStoreRequest {
  s.Endpoint = &v
  return s
}

func (s *AddStoreRequest) SetOwnership(v string) *AddStoreRequest {
  s.Ownership = &v
  return s
}

func (s *AddStoreRequest) SetRoleArn(v string) *AddStoreRequest {
  s.RoleArn = &v
  return s
}

func (s *AddStoreRequest) SetType(v string) *AddStoreRequest {
  s.Type = &v
  return s
}

/**
 * 
 */
type AddStoreResponse struct {
  // 全球加速地址
  AccelerateEndpoint *string `json:"accelerate_endpoint,omitempty" xml:"accelerate_endpoint,omitempty"`
  // 存储公共前缀
  BasePath *string `json:"base_path,omitempty" xml:"base_path,omitempty"`
  // bucket名称
  Bucket *string `json:"bucket,omitempty" xml:"bucket,omitempty" require:"true"`
  // 内容分发地址
  CdnEndpoint *string `json:"cdn_endpoint,omitempty" xml:"cdn_endpoint,omitempty"`
  // 自定义全球加速地址
  CustomizedAccelerateEndpoint *string `json:"customized_accelerate_endpoint,omitempty" xml:"customized_accelerate_endpoint,omitempty"`
  // 自定义内容分发地址
  CustomizedCdnEndpoint *string `json:"customized_cdn_endpoint,omitempty" xml:"customized_cdn_endpoint,omitempty"`
  // 自定义Public访问地址
  CustomizedEndpoint *string `json:"customized_endpoint,omitempty" xml:"customized_endpoint,omitempty"`
  // 自定义vpc访问地址
  CustomizedInternalEndpoint *string `json:"customized_internal_endpoint,omitempty" xml:"customized_internal_endpoint,omitempty"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // Public访问地址
  Endpoint *string `json:"endpoint,omitempty" xml:"endpoint,omitempty" require:"true"`
  // vpc访问地址
  InternalEndpoint *string `json:"internal_endpoint,omitempty" xml:"internal_endpoint,omitempty"`
  // 地点
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // 存储归属，system表示系统提供，custom表示使用自己的存储
  Ownership *string `json:"ownership,omitempty" xml:"ownership,omitempty" require:"true"`
  // Policy授权,system类型store会将bucket权限授予当前云账号
  Policy *string `json:"policy,omitempty" xml:"policy,omitempty" require:"true"`
  // 访问Bucket的角色ARN
  RoleArn *string `json:"role_arn,omitempty" xml:"role_arn,omitempty"`
  // store ID
  StoreId *string `json:"store_id,omitempty" xml:"store_id,omitempty" require:"true"`
  // 存储类型，当前只支持oss
  Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
}

func (s AddStoreResponse) String() string {
  return tea.Prettify(s)
}

func (s AddStoreResponse) GoString() string {
  return s.String()
}

func (s *AddStoreResponse) SetAccelerateEndpoint(v string) *AddStoreResponse {
  s.AccelerateEndpoint = &v
  return s
}

func (s *AddStoreResponse) SetBasePath(v string) *AddStoreResponse {
  s.BasePath = &v
  return s
}

func (s *AddStoreResponse) SetBucket(v string) *AddStoreResponse {
  s.Bucket = &v
  return s
}

func (s *AddStoreResponse) SetCdnEndpoint(v string) *AddStoreResponse {
  s.CdnEndpoint = &v
  return s
}

func (s *AddStoreResponse) SetCustomizedAccelerateEndpoint(v string) *AddStoreResponse {
  s.CustomizedAccelerateEndpoint = &v
  return s
}

func (s *AddStoreResponse) SetCustomizedCdnEndpoint(v string) *AddStoreResponse {
  s.CustomizedCdnEndpoint = &v
  return s
}

func (s *AddStoreResponse) SetCustomizedEndpoint(v string) *AddStoreResponse {
  s.CustomizedEndpoint = &v
  return s
}

func (s *AddStoreResponse) SetCustomizedInternalEndpoint(v string) *AddStoreResponse {
  s.CustomizedInternalEndpoint = &v
  return s
}

func (s *AddStoreResponse) SetDomainId(v string) *AddStoreResponse {
  s.DomainId = &v
  return s
}

func (s *AddStoreResponse) SetEndpoint(v string) *AddStoreResponse {
  s.Endpoint = &v
  return s
}

func (s *AddStoreResponse) SetInternalEndpoint(v string) *AddStoreResponse {
  s.InternalEndpoint = &v
  return s
}

func (s *AddStoreResponse) SetLocation(v string) *AddStoreResponse {
  s.Location = &v
  return s
}

func (s *AddStoreResponse) SetOwnership(v string) *AddStoreResponse {
  s.Ownership = &v
  return s
}

func (s *AddStoreResponse) SetPolicy(v string) *AddStoreResponse {
  s.Policy = &v
  return s
}

func (s *AddStoreResponse) SetRoleArn(v string) *AddStoreResponse {
  s.RoleArn = &v
  return s
}

func (s *AddStoreResponse) SetStoreId(v string) *AddStoreResponse {
  s.StoreId = &v
  return s
}

func (s *AddStoreResponse) SetType(v string) *AddStoreResponse {
  s.Type = &v
  return s
}

/**
 * 
 */
type AppAccessStrategy struct {
  Effect *string `json:"effect,omitempty" xml:"effect,omitempty"`
  ExceptAppIdList []*string `json:"except_app_id_list,omitempty" xml:"except_app_id_list,omitempty" type:"Repeated"`
}

func (s AppAccessStrategy) String() string {
  return tea.Prettify(s)
}

func (s AppAccessStrategy) GoString() string {
  return s.String()
}

func (s *AppAccessStrategy) SetEffect(v string) *AppAccessStrategy {
  s.Effect = &v
  return s
}

func (s *AppAccessStrategy) SetExceptAppIdList(v []*string) *AppAccessStrategy {
  s.ExceptAppIdList = v
  return s
}

/**
 * 
 */
type AuthConfig struct {
  AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty"`
  AppSecret *string `json:"app_secret,omitempty" xml:"app_secret,omitempty"`
  CallbackSecurity *bool `json:"callback_security,omitempty" xml:"callback_security,omitempty"`
  Enable *bool `json:"enable,omitempty" xml:"enable,omitempty"`
  Endpoint *string `json:"endpoint,omitempty" xml:"endpoint,omitempty"`
  EnterpriseId *string `json:"enterprise_id,omitempty" xml:"enterprise_id,omitempty"`
  LdapConfig *LdapConfig `json:"ldap_config,omitempty" xml:"ldap_config,omitempty"`
  LoginPageHeaders map[string]interface{} `json:"login_page_headers,omitempty" xml:"login_page_headers,omitempty"`
  LoginPageTemplate *string `json:"login_page_template,omitempty" xml:"login_page_template,omitempty"`
  LoginPageVars map[string]interface{} `json:"login_page_vars,omitempty" xml:"login_page_vars,omitempty"`
  WhiteListConfig map[string]interface{} `json:"white_list_config,omitempty" xml:"white_list_config,omitempty"`
  WhiteListEnable *bool `json:"white_list_enable,omitempty" xml:"white_list_enable,omitempty"`
}

func (s AuthConfig) String() string {
  return tea.Prettify(s)
}

func (s AuthConfig) GoString() string {
  return s.String()
}

func (s *AuthConfig) SetAppId(v string) *AuthConfig {
  s.AppId = &v
  return s
}

func (s *AuthConfig) SetAppSecret(v string) *AuthConfig {
  s.AppSecret = &v
  return s
}

func (s *AuthConfig) SetCallbackSecurity(v bool) *AuthConfig {
  s.CallbackSecurity = &v
  return s
}

func (s *AuthConfig) SetEnable(v bool) *AuthConfig {
  s.Enable = &v
  return s
}

func (s *AuthConfig) SetEndpoint(v string) *AuthConfig {
  s.Endpoint = &v
  return s
}

func (s *AuthConfig) SetEnterpriseId(v string) *AuthConfig {
  s.EnterpriseId = &v
  return s
}

func (s *AuthConfig) SetLdapConfig(v *LdapConfig) *AuthConfig {
  s.LdapConfig = v
  return s
}

func (s *AuthConfig) SetLoginPageHeaders(v map[string]interface{}) *AuthConfig {
  s.LoginPageHeaders = v
  return s
}

func (s *AuthConfig) SetLoginPageTemplate(v string) *AuthConfig {
  s.LoginPageTemplate = &v
  return s
}

func (s *AuthConfig) SetLoginPageVars(v map[string]interface{}) *AuthConfig {
  s.LoginPageVars = v
  return s
}

func (s *AuthConfig) SetWhiteListConfig(v map[string]interface{}) *AuthConfig {
  s.WhiteListConfig = v
  return s
}

func (s *AuthConfig) SetWhiteListEnable(v bool) *AuthConfig {
  s.WhiteListEnable = &v
  return s
}

/**
 * base domain response
 */
type BaseDomainResponse struct {
  // Domain APICName
  ApiCname *string `json:"api_cname,omitempty" xml:"api_cname,omitempty"`
  // Domain AppCName
  AppCname *string `json:"app_cname,omitempty" xml:"app_cname,omitempty"`
  // 支付宝 App Id
  AuthAlipayAppId *string `json:"auth_alipay_app_id,omitempty" xml:"auth_alipay_app_id,omitempty"`
  // 是否开启了支付宝认证
  AuthAlipayEnable *bool `json:"auth_alipay_enable,omitempty" xml:"auth_alipay_enable,omitempty"`
  // 支付宝 App Secret
  AuthAlipayPrivateKey *string `json:"auth_alipay_private_key,omitempty" xml:"auth_alipay_private_key,omitempty"`
  // Domain AuthCName
  AuthCname *string `json:"auth_cname,omitempty" xml:"auth_cname,omitempty"`
  // 登录相关信息
  AuthConfig map[string]interface{} `json:"auth_config,omitempty" xml:"auth_config,omitempty"`
  // 钉钉 App Id
  AuthDingdingAppId *string `json:"auth_dingding_app_id,omitempty" xml:"auth_dingding_app_id,omitempty"`
  // 钉钉 App Secret
  AuthDingdingAppSecret *string `json:"auth_dingding_app_secret,omitempty" xml:"auth_dingding_app_secret,omitempty"`
  // 是否开启了钉钉认证
  AuthDingdingEnable *bool `json:"auth_dingding_enable,omitempty" xml:"auth_dingding_enable,omitempty"`
  AuthEndpointEnable *bool `json:"auth_endpoint_enable,omitempty" xml:"auth_endpoint_enable,omitempty"`
  // RAM App Id
  AuthRamAppId *string `json:"auth_ram_app_id,omitempty" xml:"auth_ram_app_id,omitempty"`
  // RAM App Secret
  AuthRamAppSecret *string `json:"auth_ram_app_secret,omitempty" xml:"auth_ram_app_secret,omitempty"`
  // 是否开启了 RAM 认证
  AuthRamEnable *bool `json:"auth_ram_enable,omitempty" xml:"auth_ram_enable,omitempty"`
  // Domain 创建时间
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // 数据 Hash 算法
  DataHashName *string `json:"data_hash_name,omitempty" xml:"data_hash_name,omitempty"`
  // Domain 描述
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // Domain 描述
  DomainName *string `json:"domain_name,omitempty" xml:"domain_name,omitempty"`
  // 事件通知 MNS 匹配文件名
  EventFilenameMatches *string `json:"event_filename_matches,omitempty" xml:"event_filename_matches,omitempty"`
  // 事件通知 MNS Endpoint
  EventMnsEndpoint *string `json:"event_mns_endpoint,omitempty" xml:"event_mns_endpoint,omitempty"`
  // 事件通知 MNS Topic
  EventMnsTopic *string `json:"event_mns_topic,omitempty" xml:"event_mns_topic,omitempty"`
  // 事件名列表
  EventNames []*string `json:"event_names,omitempty" xml:"event_names,omitempty" type:"Repeated"`
  // 事件通知 Role Arn
  EventRoleArn *string `json:"event_role_arn,omitempty" xml:"event_role_arn,omitempty"`
  // 是否开启了自动初始化 Drive
  InitDriveEnable *bool `json:"init_drive_enable,omitempty" xml:"init_drive_enable,omitempty"`
  // 自动初始化 Drive 大小
  InitDriveSize *int64 `json:"init_drive_size,omitempty" xml:"init_drive_size,omitempty"`
  // 自动初始化 Drive 所用 Store ID
  InitDriveStoreId *string `json:"init_drive_store_id,omitempty" xml:"init_drive_store_id,omitempty"`
  // Domain 类型
  Mode *string `json:"mode,omitempty" xml:"mode,omitempty"`
  // Domain 类型
  PathType *string `json:"path_type,omitempty" xml:"path_type,omitempty"`
  PublishedAppAccessStrategy *AppAccessStrategy `json:"published_app_access_strategy,omitempty" xml:"published_app_access_strategy,omitempty"`
  // 是否开启了分享
  Sharable *bool `json:"sharable,omitempty" xml:"sharable,omitempty"`
  // 存储级别
  StoreLevel *string `json:"store_level,omitempty" xml:"store_level,omitempty"`
  // 存储 Region 列表
  StoreRegionList []*string `json:"store_region_list,omitempty" xml:"store_region_list,omitempty" type:"Repeated"`
  // Domain 更新时间
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s BaseDomainResponse) String() string {
  return tea.Prettify(s)
}

func (s BaseDomainResponse) GoString() string {
  return s.String()
}

func (s *BaseDomainResponse) SetApiCname(v string) *BaseDomainResponse {
  s.ApiCname = &v
  return s
}

func (s *BaseDomainResponse) SetAppCname(v string) *BaseDomainResponse {
  s.AppCname = &v
  return s
}

func (s *BaseDomainResponse) SetAuthAlipayAppId(v string) *BaseDomainResponse {
  s.AuthAlipayAppId = &v
  return s
}

func (s *BaseDomainResponse) SetAuthAlipayEnable(v bool) *BaseDomainResponse {
  s.AuthAlipayEnable = &v
  return s
}

func (s *BaseDomainResponse) SetAuthAlipayPrivateKey(v string) *BaseDomainResponse {
  s.AuthAlipayPrivateKey = &v
  return s
}

func (s *BaseDomainResponse) SetAuthCname(v string) *BaseDomainResponse {
  s.AuthCname = &v
  return s
}

func (s *BaseDomainResponse) SetAuthConfig(v map[string]interface{}) *BaseDomainResponse {
  s.AuthConfig = v
  return s
}

func (s *BaseDomainResponse) SetAuthDingdingAppId(v string) *BaseDomainResponse {
  s.AuthDingdingAppId = &v
  return s
}

func (s *BaseDomainResponse) SetAuthDingdingAppSecret(v string) *BaseDomainResponse {
  s.AuthDingdingAppSecret = &v
  return s
}

func (s *BaseDomainResponse) SetAuthDingdingEnable(v bool) *BaseDomainResponse {
  s.AuthDingdingEnable = &v
  return s
}

func (s *BaseDomainResponse) SetAuthEndpointEnable(v bool) *BaseDomainResponse {
  s.AuthEndpointEnable = &v
  return s
}

func (s *BaseDomainResponse) SetAuthRamAppId(v string) *BaseDomainResponse {
  s.AuthRamAppId = &v
  return s
}

func (s *BaseDomainResponse) SetAuthRamAppSecret(v string) *BaseDomainResponse {
  s.AuthRamAppSecret = &v
  return s
}

func (s *BaseDomainResponse) SetAuthRamEnable(v bool) *BaseDomainResponse {
  s.AuthRamEnable = &v
  return s
}

func (s *BaseDomainResponse) SetCreatedAt(v string) *BaseDomainResponse {
  s.CreatedAt = &v
  return s
}

func (s *BaseDomainResponse) SetDataHashName(v string) *BaseDomainResponse {
  s.DataHashName = &v
  return s
}

func (s *BaseDomainResponse) SetDescription(v string) *BaseDomainResponse {
  s.Description = &v
  return s
}

func (s *BaseDomainResponse) SetDomainId(v string) *BaseDomainResponse {
  s.DomainId = &v
  return s
}

func (s *BaseDomainResponse) SetDomainName(v string) *BaseDomainResponse {
  s.DomainName = &v
  return s
}

func (s *BaseDomainResponse) SetEventFilenameMatches(v string) *BaseDomainResponse {
  s.EventFilenameMatches = &v
  return s
}

func (s *BaseDomainResponse) SetEventMnsEndpoint(v string) *BaseDomainResponse {
  s.EventMnsEndpoint = &v
  return s
}

func (s *BaseDomainResponse) SetEventMnsTopic(v string) *BaseDomainResponse {
  s.EventMnsTopic = &v
  return s
}

func (s *BaseDomainResponse) SetEventNames(v []*string) *BaseDomainResponse {
  s.EventNames = v
  return s
}

func (s *BaseDomainResponse) SetEventRoleArn(v string) *BaseDomainResponse {
  s.EventRoleArn = &v
  return s
}

func (s *BaseDomainResponse) SetInitDriveEnable(v bool) *BaseDomainResponse {
  s.InitDriveEnable = &v
  return s
}

func (s *BaseDomainResponse) SetInitDriveSize(v int64) *BaseDomainResponse {
  s.InitDriveSize = &v
  return s
}

func (s *BaseDomainResponse) SetInitDriveStoreId(v string) *BaseDomainResponse {
  s.InitDriveStoreId = &v
  return s
}

func (s *BaseDomainResponse) SetMode(v string) *BaseDomainResponse {
  s.Mode = &v
  return s
}

func (s *BaseDomainResponse) SetPathType(v string) *BaseDomainResponse {
  s.PathType = &v
  return s
}

func (s *BaseDomainResponse) SetPublishedAppAccessStrategy(v *AppAccessStrategy) *BaseDomainResponse {
  s.PublishedAppAccessStrategy = v
  return s
}

func (s *BaseDomainResponse) SetSharable(v bool) *BaseDomainResponse {
  s.Sharable = &v
  return s
}

func (s *BaseDomainResponse) SetStoreLevel(v string) *BaseDomainResponse {
  s.StoreLevel = &v
  return s
}

func (s *BaseDomainResponse) SetStoreRegionList(v []*string) *BaseDomainResponse {
  s.StoreRegionList = v
  return s
}

func (s *BaseDomainResponse) SetUpdatedAt(v string) *BaseDomainResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * 
 */
type CNameStatus struct {
  // binding state
  BingdingState *string `json:"bingding_state,omitempty" xml:"bingding_state,omitempty" require:"true"`
  // legal state
  LegalState *string `json:"legal_state,omitempty" xml:"legal_state,omitempty" require:"true"`
  // remark
  Remark *string `json:"remark,omitempty" xml:"remark,omitempty" require:"true"`
}

func (s CNameStatus) String() string {
  return tea.Prettify(s)
}

func (s CNameStatus) GoString() string {
  return s.String()
}

func (s *CNameStatus) SetBingdingState(v string) *CNameStatus {
  s.BingdingState = &v
  return s
}

func (s *CNameStatus) SetLegalState(v string) *CNameStatus {
  s.LegalState = &v
  return s
}

func (s *CNameStatus) SetRemark(v string) *CNameStatus {
  s.Remark = &v
  return s
}

/**
 * 
 */
type Captcha struct {
  // 图片验证码，base64格式
  Captcha *string `json:"captcha,omitempty" xml:"captcha,omitempty" require:"true"`
  // 图片格式
  CaptchaFormat *string `json:"captcha_format,omitempty" xml:"captcha_format,omitempty" require:"true"`
  // 图片验证码ID
  CaptchaId *string `json:"captcha_id,omitempty" xml:"captcha_id,omitempty" require:"true"`
}

func (s Captcha) String() string {
  return tea.Prettify(s)
}

func (s Captcha) GoString() string {
  return s.String()
}

func (s *Captcha) SetCaptcha(v string) *Captcha {
  s.Captcha = &v
  return s
}

func (s *Captcha) SetCaptchaFormat(v string) *Captcha {
  s.CaptchaFormat = &v
  return s
}

func (s *Captcha) SetCaptchaId(v string) *Captcha {
  s.CaptchaId = &v
  return s
}

/**
 * 
 */
type CorsRule struct {
  // AllowedHeader
  AllowedHeader []*string `json:"allowed_header,omitempty" xml:"allowed_header,omitempty" type:"Repeated"`
  // AllowedMethod
  AllowedMethod []*string `json:"allowed_method,omitempty" xml:"allowed_method,omitempty" type:"Repeated"`
  // AllowedOrigin
  AllowedOrigin []*string `json:"allowed_origin,omitempty" xml:"allowed_origin,omitempty" type:"Repeated"`
  // ExposeHeader
  ExposeHeader []*string `json:"expose_header,omitempty" xml:"expose_header,omitempty" type:"Repeated"`
  // MaxAgeSeconds
  MaxAgeSeconds *int64 `json:"max_age_seconds,omitempty" xml:"max_age_seconds,omitempty"`
}

func (s CorsRule) String() string {
  return tea.Prettify(s)
}

func (s CorsRule) GoString() string {
  return s.String()
}

func (s *CorsRule) SetAllowedHeader(v []*string) *CorsRule {
  s.AllowedHeader = v
  return s
}

func (s *CorsRule) SetAllowedMethod(v []*string) *CorsRule {
  s.AllowedMethod = v
  return s
}

func (s *CorsRule) SetAllowedOrigin(v []*string) *CorsRule {
  s.AllowedOrigin = v
  return s
}

func (s *CorsRule) SetExposeHeader(v []*string) *CorsRule {
  s.ExposeHeader = v
  return s
}

func (s *CorsRule) SetMaxAgeSeconds(v int64) *CorsRule {
  s.MaxAgeSeconds = &v
  return s
}

/**
 * 
 */
type CreateAppRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // App名称
  AppName *string `json:"app_name,omitempty" xml:"app_name,omitempty" require:"true" maxLength:"128" minLength:"1"`
  // App描述
  Description *string `json:"description,omitempty" xml:"description,omitempty" maxLength:"128" minLength:"0"`
  // 是否是domain私有App
  IsThirdParty *bool `json:"is_third_party,omitempty" xml:"is_third_party,omitempty"`
  // App图标
  Logo *string `json:"logo,omitempty" xml:"logo,omitempty" require:"true"`
  // RSA加密算法的公钥, PEM格式
  PublicKey *string `json:"public_key,omitempty" xml:"public_key,omitempty" require:"true"`
  // App回调地址
  RedirectUri *string `json:"redirect_uri,omitempty" xml:"redirect_uri,omitempty"`
  // App权限列表
  Scope []*string `json:"scope,omitempty" xml:"scope,omitempty" require:"true" type:"Repeated"`
  // App类型
  Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
}

func (s CreateAppRequest) String() string {
  return tea.Prettify(s)
}

func (s CreateAppRequest) GoString() string {
  return s.String()
}

func (s *CreateAppRequest) SetHeaders(v map[string]*string) *CreateAppRequest {
  s.Headers = v
  return s
}

func (s *CreateAppRequest) SetAppName(v string) *CreateAppRequest {
  s.AppName = &v
  return s
}

func (s *CreateAppRequest) SetDescription(v string) *CreateAppRequest {
  s.Description = &v
  return s
}

func (s *CreateAppRequest) SetIsThirdParty(v bool) *CreateAppRequest {
  s.IsThirdParty = &v
  return s
}

func (s *CreateAppRequest) SetLogo(v string) *CreateAppRequest {
  s.Logo = &v
  return s
}

func (s *CreateAppRequest) SetPublicKey(v string) *CreateAppRequest {
  s.PublicKey = &v
  return s
}

func (s *CreateAppRequest) SetRedirectUri(v string) *CreateAppRequest {
  s.RedirectUri = &v
  return s
}

func (s *CreateAppRequest) SetScope(v []*string) *CreateAppRequest {
  s.Scope = v
  return s
}

func (s *CreateAppRequest) SetType(v string) *CreateAppRequest {
  s.Type = &v
  return s
}

/**
 * create domain request
 */
type CreateDomainRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // 登录相关信息
  AuthConfig map[string]interface{} `json:"auth_config,omitempty" xml:"auth_config,omitempty"`
  // 钉钉 App Id
  AuthDingdingAppId *string `json:"auth_dingding_app_id,omitempty" xml:"auth_dingding_app_id,omitempty"`
  // 钉钉 App Secret
  AuthDingdingAppSecret *string `json:"auth_dingding_app_secret,omitempty" xml:"auth_dingding_app_secret,omitempty"`
  // 启用钉钉认证
  AuthDingdingEnable *bool `json:"auth_dingding_enable,omitempty" xml:"auth_dingding_enable,omitempty"`
  AuthEndpointEnable *bool `json:"auth_endpoint_enable,omitempty" xml:"auth_endpoint_enable,omitempty"`
  // RAM App Id
  AuthRamAppId *string `json:"auth_ram_app_id,omitempty" xml:"auth_ram_app_id,omitempty"`
  // RAM App Secret
  AuthRamAppSecret *string `json:"auth_ram_app_secret,omitempty" xml:"auth_ram_app_secret,omitempty"`
  // 启用 RAM 认证
  AuthRamEnable *bool `json:"auth_ram_enable,omitempty" xml:"auth_ram_enable,omitempty"`
  // 数据 Hash 算法
  DataHashName *string `json:"data_hash_name,omitempty" xml:"data_hash_name,omitempty"`
  // Domain 描述
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Domain 名称
  DomainName *string `json:"domain_name,omitempty" xml:"domain_name,omitempty" require:"true"`
  // 事件通知 MNS 匹配文件名
  EventFilenameMatches *string `json:"event_filename_matches,omitempty" xml:"event_filename_matches,omitempty"`
  // 事件通知 MNS Endpoint
  EventMnsEndpoint *string `json:"event_mns_endpoint,omitempty" xml:"event_mns_endpoint,omitempty"`
  // 事件通知 MNS Topic
  EventMnsTopic *string `json:"event_mns_topic,omitempty" xml:"event_mns_topic,omitempty"`
  // 事件名列表
  EventNames []*string `json:"event_names,omitempty" xml:"event_names,omitempty" type:"Repeated"`
  // 事件通知 Role Arn
  EventRoleArn *string `json:"event_role_arn,omitempty" xml:"event_role_arn,omitempty"`
  // 开启自动初始化 Drive
  InitDriveEnable *bool `json:"init_drive_enable,omitempty" xml:"init_drive_enable,omitempty"`
  // 自动初始化 Drive 大小
  InitDriveSize *int64 `json:"init_drive_size,omitempty" xml:"init_drive_size,omitempty"`
  // Domain 类型
  Mode *string `json:"mode,omitempty" xml:"mode,omitempty" require:"true"`
  // Domain 类型
  PathType *string `json:"path_type,omitempty" xml:"path_type,omitempty"`
  PublishedAppAccessStrategy *AppAccessStrategy `json:"published_app_access_strategy,omitempty" xml:"published_app_access_strategy,omitempty"`
  // 开启分享
  Sharable *bool `json:"sharable,omitempty" xml:"sharable,omitempty"`
  // 存储级别
  StoreLevel *string `json:"store_level,omitempty" xml:"store_level,omitempty"`
  // 存储 Region 列表
  StoreRegionList []*string `json:"store_region_list,omitempty" xml:"store_region_list,omitempty" require:"true" type:"Repeated"`
}

func (s CreateDomainRequest) String() string {
  return tea.Prettify(s)
}

func (s CreateDomainRequest) GoString() string {
  return s.String()
}

func (s *CreateDomainRequest) SetHeaders(v map[string]*string) *CreateDomainRequest {
  s.Headers = v
  return s
}

func (s *CreateDomainRequest) SetAuthConfig(v map[string]interface{}) *CreateDomainRequest {
  s.AuthConfig = v
  return s
}

func (s *CreateDomainRequest) SetAuthDingdingAppId(v string) *CreateDomainRequest {
  s.AuthDingdingAppId = &v
  return s
}

func (s *CreateDomainRequest) SetAuthDingdingAppSecret(v string) *CreateDomainRequest {
  s.AuthDingdingAppSecret = &v
  return s
}

func (s *CreateDomainRequest) SetAuthDingdingEnable(v bool) *CreateDomainRequest {
  s.AuthDingdingEnable = &v
  return s
}

func (s *CreateDomainRequest) SetAuthEndpointEnable(v bool) *CreateDomainRequest {
  s.AuthEndpointEnable = &v
  return s
}

func (s *CreateDomainRequest) SetAuthRamAppId(v string) *CreateDomainRequest {
  s.AuthRamAppId = &v
  return s
}

func (s *CreateDomainRequest) SetAuthRamAppSecret(v string) *CreateDomainRequest {
  s.AuthRamAppSecret = &v
  return s
}

func (s *CreateDomainRequest) SetAuthRamEnable(v bool) *CreateDomainRequest {
  s.AuthRamEnable = &v
  return s
}

func (s *CreateDomainRequest) SetDataHashName(v string) *CreateDomainRequest {
  s.DataHashName = &v
  return s
}

func (s *CreateDomainRequest) SetDescription(v string) *CreateDomainRequest {
  s.Description = &v
  return s
}

func (s *CreateDomainRequest) SetDomainName(v string) *CreateDomainRequest {
  s.DomainName = &v
  return s
}

func (s *CreateDomainRequest) SetEventFilenameMatches(v string) *CreateDomainRequest {
  s.EventFilenameMatches = &v
  return s
}

func (s *CreateDomainRequest) SetEventMnsEndpoint(v string) *CreateDomainRequest {
  s.EventMnsEndpoint = &v
  return s
}

func (s *CreateDomainRequest) SetEventMnsTopic(v string) *CreateDomainRequest {
  s.EventMnsTopic = &v
  return s
}

func (s *CreateDomainRequest) SetEventNames(v []*string) *CreateDomainRequest {
  s.EventNames = v
  return s
}

func (s *CreateDomainRequest) SetEventRoleArn(v string) *CreateDomainRequest {
  s.EventRoleArn = &v
  return s
}

func (s *CreateDomainRequest) SetInitDriveEnable(v bool) *CreateDomainRequest {
  s.InitDriveEnable = &v
  return s
}

func (s *CreateDomainRequest) SetInitDriveSize(v int64) *CreateDomainRequest {
  s.InitDriveSize = &v
  return s
}

func (s *CreateDomainRequest) SetMode(v string) *CreateDomainRequest {
  s.Mode = &v
  return s
}

func (s *CreateDomainRequest) SetPathType(v string) *CreateDomainRequest {
  s.PathType = &v
  return s
}

func (s *CreateDomainRequest) SetPublishedAppAccessStrategy(v *AppAccessStrategy) *CreateDomainRequest {
  s.PublishedAppAccessStrategy = v
  return s
}

func (s *CreateDomainRequest) SetSharable(v bool) *CreateDomainRequest {
  s.Sharable = &v
  return s
}

func (s *CreateDomainRequest) SetStoreLevel(v string) *CreateDomainRequest {
  s.StoreLevel = &v
  return s
}

func (s *CreateDomainRequest) SetStoreRegionList(v []*string) *CreateDomainRequest {
  s.StoreRegionList = v
  return s
}

/**
 * create domain response
 */
type CreateDomainResponse struct {
  // Domain APICName
  ApiCname *string `json:"api_cname,omitempty" xml:"api_cname,omitempty"`
  // Domain AppCName
  AppCname *string `json:"app_cname,omitempty" xml:"app_cname,omitempty"`
  // 支付宝 App Id
  AuthAlipayAppId *string `json:"auth_alipay_app_id,omitempty" xml:"auth_alipay_app_id,omitempty"`
  // 是否开启了支付宝认证
  AuthAlipayEnable *bool `json:"auth_alipay_enable,omitempty" xml:"auth_alipay_enable,omitempty"`
  // 支付宝 App Secret
  AuthAlipayPrivateKey *string `json:"auth_alipay_private_key,omitempty" xml:"auth_alipay_private_key,omitempty"`
  // Domain AuthCName
  AuthCname *string `json:"auth_cname,omitempty" xml:"auth_cname,omitempty"`
  // 登录相关信息
  AuthConfig map[string]interface{} `json:"auth_config,omitempty" xml:"auth_config,omitempty"`
  // 钉钉 App Id
  AuthDingdingAppId *string `json:"auth_dingding_app_id,omitempty" xml:"auth_dingding_app_id,omitempty"`
  // 钉钉 App Secret
  AuthDingdingAppSecret *string `json:"auth_dingding_app_secret,omitempty" xml:"auth_dingding_app_secret,omitempty"`
  // 是否开启了钉钉认证
  AuthDingdingEnable *bool `json:"auth_dingding_enable,omitempty" xml:"auth_dingding_enable,omitempty"`
  AuthEndpointEnable *bool `json:"auth_endpoint_enable,omitempty" xml:"auth_endpoint_enable,omitempty"`
  // RAM App Id
  AuthRamAppId *string `json:"auth_ram_app_id,omitempty" xml:"auth_ram_app_id,omitempty"`
  // RAM App Secret
  AuthRamAppSecret *string `json:"auth_ram_app_secret,omitempty" xml:"auth_ram_app_secret,omitempty"`
  // 是否开启了 RAM 认证
  AuthRamEnable *bool `json:"auth_ram_enable,omitempty" xml:"auth_ram_enable,omitempty"`
  // Domain 创建时间
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // 数据 Hash 算法
  DataHashName *string `json:"data_hash_name,omitempty" xml:"data_hash_name,omitempty"`
  // Domain 描述
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // Domain 描述
  DomainName *string `json:"domain_name,omitempty" xml:"domain_name,omitempty"`
  // 事件通知 MNS 匹配文件名
  EventFilenameMatches *string `json:"event_filename_matches,omitempty" xml:"event_filename_matches,omitempty"`
  // 事件通知 MNS Endpoint
  EventMnsEndpoint *string `json:"event_mns_endpoint,omitempty" xml:"event_mns_endpoint,omitempty"`
  // 事件通知 MNS Topic
  EventMnsTopic *string `json:"event_mns_topic,omitempty" xml:"event_mns_topic,omitempty"`
  // 事件名列表
  EventNames []*string `json:"event_names,omitempty" xml:"event_names,omitempty" type:"Repeated"`
  // 事件通知 Role Arn
  EventRoleArn *string `json:"event_role_arn,omitempty" xml:"event_role_arn,omitempty"`
  // 是否开启了自动初始化 Drive
  InitDriveEnable *bool `json:"init_drive_enable,omitempty" xml:"init_drive_enable,omitempty"`
  // 自动初始化 Drive 大小
  InitDriveSize *int64 `json:"init_drive_size,omitempty" xml:"init_drive_size,omitempty"`
  // 自动初始化 Drive 所用 Store ID
  InitDriveStoreId *string `json:"init_drive_store_id,omitempty" xml:"init_drive_store_id,omitempty"`
  // Domain 类型
  Mode *string `json:"mode,omitempty" xml:"mode,omitempty"`
  // Domain 类型
  PathType *string `json:"path_type,omitempty" xml:"path_type,omitempty"`
  PublishedAppAccessStrategy *AppAccessStrategy `json:"published_app_access_strategy,omitempty" xml:"published_app_access_strategy,omitempty"`
  // 是否开启了分享
  Sharable *bool `json:"sharable,omitempty" xml:"sharable,omitempty"`
  // 存储级别
  StoreLevel *string `json:"store_level,omitempty" xml:"store_level,omitempty"`
  // 存储 Region 列表
  StoreRegionList []*string `json:"store_region_list,omitempty" xml:"store_region_list,omitempty" type:"Repeated"`
  // Domain 更新时间
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s CreateDomainResponse) String() string {
  return tea.Prettify(s)
}

func (s CreateDomainResponse) GoString() string {
  return s.String()
}

func (s *CreateDomainResponse) SetApiCname(v string) *CreateDomainResponse {
  s.ApiCname = &v
  return s
}

func (s *CreateDomainResponse) SetAppCname(v string) *CreateDomainResponse {
  s.AppCname = &v
  return s
}

func (s *CreateDomainResponse) SetAuthAlipayAppId(v string) *CreateDomainResponse {
  s.AuthAlipayAppId = &v
  return s
}

func (s *CreateDomainResponse) SetAuthAlipayEnable(v bool) *CreateDomainResponse {
  s.AuthAlipayEnable = &v
  return s
}

func (s *CreateDomainResponse) SetAuthAlipayPrivateKey(v string) *CreateDomainResponse {
  s.AuthAlipayPrivateKey = &v
  return s
}

func (s *CreateDomainResponse) SetAuthCname(v string) *CreateDomainResponse {
  s.AuthCname = &v
  return s
}

func (s *CreateDomainResponse) SetAuthConfig(v map[string]interface{}) *CreateDomainResponse {
  s.AuthConfig = v
  return s
}

func (s *CreateDomainResponse) SetAuthDingdingAppId(v string) *CreateDomainResponse {
  s.AuthDingdingAppId = &v
  return s
}

func (s *CreateDomainResponse) SetAuthDingdingAppSecret(v string) *CreateDomainResponse {
  s.AuthDingdingAppSecret = &v
  return s
}

func (s *CreateDomainResponse) SetAuthDingdingEnable(v bool) *CreateDomainResponse {
  s.AuthDingdingEnable = &v
  return s
}

func (s *CreateDomainResponse) SetAuthEndpointEnable(v bool) *CreateDomainResponse {
  s.AuthEndpointEnable = &v
  return s
}

func (s *CreateDomainResponse) SetAuthRamAppId(v string) *CreateDomainResponse {
  s.AuthRamAppId = &v
  return s
}

func (s *CreateDomainResponse) SetAuthRamAppSecret(v string) *CreateDomainResponse {
  s.AuthRamAppSecret = &v
  return s
}

func (s *CreateDomainResponse) SetAuthRamEnable(v bool) *CreateDomainResponse {
  s.AuthRamEnable = &v
  return s
}

func (s *CreateDomainResponse) SetCreatedAt(v string) *CreateDomainResponse {
  s.CreatedAt = &v
  return s
}

func (s *CreateDomainResponse) SetDataHashName(v string) *CreateDomainResponse {
  s.DataHashName = &v
  return s
}

func (s *CreateDomainResponse) SetDescription(v string) *CreateDomainResponse {
  s.Description = &v
  return s
}

func (s *CreateDomainResponse) SetDomainId(v string) *CreateDomainResponse {
  s.DomainId = &v
  return s
}

func (s *CreateDomainResponse) SetDomainName(v string) *CreateDomainResponse {
  s.DomainName = &v
  return s
}

func (s *CreateDomainResponse) SetEventFilenameMatches(v string) *CreateDomainResponse {
  s.EventFilenameMatches = &v
  return s
}

func (s *CreateDomainResponse) SetEventMnsEndpoint(v string) *CreateDomainResponse {
  s.EventMnsEndpoint = &v
  return s
}

func (s *CreateDomainResponse) SetEventMnsTopic(v string) *CreateDomainResponse {
  s.EventMnsTopic = &v
  return s
}

func (s *CreateDomainResponse) SetEventNames(v []*string) *CreateDomainResponse {
  s.EventNames = v
  return s
}

func (s *CreateDomainResponse) SetEventRoleArn(v string) *CreateDomainResponse {
  s.EventRoleArn = &v
  return s
}

func (s *CreateDomainResponse) SetInitDriveEnable(v bool) *CreateDomainResponse {
  s.InitDriveEnable = &v
  return s
}

func (s *CreateDomainResponse) SetInitDriveSize(v int64) *CreateDomainResponse {
  s.InitDriveSize = &v
  return s
}

func (s *CreateDomainResponse) SetInitDriveStoreId(v string) *CreateDomainResponse {
  s.InitDriveStoreId = &v
  return s
}

func (s *CreateDomainResponse) SetMode(v string) *CreateDomainResponse {
  s.Mode = &v
  return s
}

func (s *CreateDomainResponse) SetPathType(v string) *CreateDomainResponse {
  s.PathType = &v
  return s
}

func (s *CreateDomainResponse) SetPublishedAppAccessStrategy(v *AppAccessStrategy) *CreateDomainResponse {
  s.PublishedAppAccessStrategy = v
  return s
}

func (s *CreateDomainResponse) SetSharable(v bool) *CreateDomainResponse {
  s.Sharable = &v
  return s
}

func (s *CreateDomainResponse) SetStoreLevel(v string) *CreateDomainResponse {
  s.StoreLevel = &v
  return s
}

func (s *CreateDomainResponse) SetStoreRegionList(v []*string) *CreateDomainResponse {
  s.StoreRegionList = v
  return s
}

func (s *CreateDomainResponse) SetUpdatedAt(v string) *CreateDomainResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * 
 */
type DataCName struct {
  // datacname
  DataCname *string `json:"data_cname,omitempty" xml:"data_cname,omitempty" require:"true"`
  // data location
  Location *string `json:"location,omitempty" xml:"location,omitempty" require:"true"`
}

func (s DataCName) String() string {
  return tea.Prettify(s)
}

func (s DataCName) GoString() string {
  return s.String()
}

func (s *DataCName) SetDataCname(v string) *DataCName {
  s.DataCname = &v
  return s
}

func (s *DataCName) SetLocation(v string) *DataCName {
  s.Location = &v
  return s
}

/**
 * 
 */
type DeleteAppRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // App ID
  AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
}

func (s DeleteAppRequest) String() string {
  return tea.Prettify(s)
}

func (s DeleteAppRequest) GoString() string {
  return s.String()
}

func (s *DeleteAppRequest) SetHeaders(v map[string]*string) *DeleteAppRequest {
  s.Headers = v
  return s
}

func (s *DeleteAppRequest) SetAppId(v string) *DeleteAppRequest {
  s.AppId = &v
  return s
}

/**
 * 
 */
type DeleteBizCNameAndCertRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // api cname
  BizCname *string `json:"biz_cname,omitempty" xml:"biz_cname,omitempty"`
  // cname type
  CnameType *string `json:"cname_type,omitempty" xml:"cname_type,omitempty" require:"true"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // vpc
  IsVpc *bool `json:"is_vpc,omitempty" xml:"is_vpc,omitempty"`
}

func (s DeleteBizCNameAndCertRequest) String() string {
  return tea.Prettify(s)
}

func (s DeleteBizCNameAndCertRequest) GoString() string {
  return s.String()
}

func (s *DeleteBizCNameAndCertRequest) SetHeaders(v map[string]*string) *DeleteBizCNameAndCertRequest {
  s.Headers = v
  return s
}

func (s *DeleteBizCNameAndCertRequest) SetBizCname(v string) *DeleteBizCNameAndCertRequest {
  s.BizCname = &v
  return s
}

func (s *DeleteBizCNameAndCertRequest) SetCnameType(v string) *DeleteBizCNameAndCertRequest {
  s.CnameType = &v
  return s
}

func (s *DeleteBizCNameAndCertRequest) SetDomainId(v string) *DeleteBizCNameAndCertRequest {
  s.DomainId = &v
  return s
}

func (s *DeleteBizCNameAndCertRequest) SetIsVpc(v bool) *DeleteBizCNameAndCertRequest {
  s.IsVpc = &v
  return s
}

/**
 * 
 */
type DeleteBizCNameCertRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // biz cname
  BizCname *string `json:"biz_cname,omitempty" xml:"biz_cname,omitempty"`
  // cert id
  CertId *string `json:"cert_id,omitempty" xml:"cert_id,omitempty"`
  // cname type
  CnameType *string `json:"cname_type,omitempty" xml:"cname_type,omitempty" require:"true"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // is vpc
  IsVpc *bool `json:"is_vpc,omitempty" xml:"is_vpc,omitempty"`
}

func (s DeleteBizCNameCertRequest) String() string {
  return tea.Prettify(s)
}

func (s DeleteBizCNameCertRequest) GoString() string {
  return s.String()
}

func (s *DeleteBizCNameCertRequest) SetHeaders(v map[string]*string) *DeleteBizCNameCertRequest {
  s.Headers = v
  return s
}

func (s *DeleteBizCNameCertRequest) SetBizCname(v string) *DeleteBizCNameCertRequest {
  s.BizCname = &v
  return s
}

func (s *DeleteBizCNameCertRequest) SetCertId(v string) *DeleteBizCNameCertRequest {
  s.CertId = &v
  return s
}

func (s *DeleteBizCNameCertRequest) SetCnameType(v string) *DeleteBizCNameCertRequest {
  s.CnameType = &v
  return s
}

func (s *DeleteBizCNameCertRequest) SetDomainId(v string) *DeleteBizCNameCertRequest {
  s.DomainId = &v
  return s
}

func (s *DeleteBizCNameCertRequest) SetIsVpc(v bool) *DeleteBizCNameCertRequest {
  s.IsVpc = &v
  return s
}

/**
 * 
 */
type DeleteDataCNameAndCertRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // cn-shanghai data cname
  DataCname *string `json:"data_cname,omitempty" xml:"data_cname,omitempty" require:"true"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty" require:"true"`
}

func (s DeleteDataCNameAndCertRequest) String() string {
  return tea.Prettify(s)
}

func (s DeleteDataCNameAndCertRequest) GoString() string {
  return s.String()
}

func (s *DeleteDataCNameAndCertRequest) SetHeaders(v map[string]*string) *DeleteDataCNameAndCertRequest {
  s.Headers = v
  return s
}

func (s *DeleteDataCNameAndCertRequest) SetDataCname(v string) *DeleteDataCNameAndCertRequest {
  s.DataCname = &v
  return s
}

func (s *DeleteDataCNameAndCertRequest) SetDomainId(v string) *DeleteDataCNameAndCertRequest {
  s.DomainId = &v
  return s
}

func (s *DeleteDataCNameAndCertRequest) SetLocation(v string) *DeleteDataCNameAndCertRequest {
  s.Location = &v
  return s
}

/**
 * delete domain request
 */
type DeleteDomainRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
}

func (s DeleteDomainRequest) String() string {
  return tea.Prettify(s)
}

func (s DeleteDomainRequest) GoString() string {
  return s.String()
}

func (s *DeleteDomainRequest) SetHeaders(v map[string]*string) *DeleteDomainRequest {
  s.Headers = v
  return s
}

func (s *DeleteDomainRequest) SetDomainId(v string) *DeleteDomainRequest {
  s.DomainId = &v
  return s
}

/**
 * 
 */
type DomainCNameResponse struct {
  // data cname list
  DataCnameList []*DataCName `json:"data_cname_list,omitempty" xml:"data_cname_list,omitempty" require:"true" type:"Repeated"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
}

func (s DomainCNameResponse) String() string {
  return tea.Prettify(s)
}

func (s DomainCNameResponse) GoString() string {
  return s.String()
}

func (s *DomainCNameResponse) SetDataCnameList(v []*DataCName) *DomainCNameResponse {
  s.DataCnameList = v
  return s
}

func (s *DomainCNameResponse) SetDomainId(v string) *DomainCNameResponse {
  s.DomainId = &v
  return s
}

/**
 * 
 */
type GetAppPublicKeyRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // App ID
  AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
}

func (s GetAppPublicKeyRequest) String() string {
  return tea.Prettify(s)
}

func (s GetAppPublicKeyRequest) GoString() string {
  return s.String()
}

func (s *GetAppPublicKeyRequest) SetHeaders(v map[string]*string) *GetAppPublicKeyRequest {
  s.Headers = v
  return s
}

func (s *GetAppPublicKeyRequest) SetAppId(v string) *GetAppPublicKeyRequest {
  s.AppId = &v
  return s
}

/**
 * 
 */
type GetAppPublicKeyResponse struct {
  // App ID
  AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
  // RSA加密算法的公钥, PEM格式
  PublicKey *string `json:"public_key,omitempty" xml:"public_key,omitempty" require:"true"`
}

func (s GetAppPublicKeyResponse) String() string {
  return tea.Prettify(s)
}

func (s GetAppPublicKeyResponse) GoString() string {
  return s.String()
}

func (s *GetAppPublicKeyResponse) SetAppId(v string) *GetAppPublicKeyResponse {
  s.AppId = &v
  return s
}

func (s *GetAppPublicKeyResponse) SetPublicKey(v string) *GetAppPublicKeyResponse {
  s.PublicKey = &v
  return s
}

/**
 * 
 */
type GetAppRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // App ID
  AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
}

func (s GetAppRequest) String() string {
  return tea.Prettify(s)
}

func (s GetAppRequest) GoString() string {
  return s.String()
}

func (s *GetAppRequest) SetHeaders(v map[string]*string) *GetAppRequest {
  s.Headers = v
  return s
}

func (s *GetAppRequest) SetAppId(v string) *GetAppRequest {
  s.AppId = &v
  return s
}

/**
 * 
 */
type GetAppResponse struct {
  // App 拥有者
  AliOwnerId *string `json:"ali_owner_id,omitempty" xml:"ali_owner_id,omitempty" require:"true"`
  // App ID
  AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
  // App名称
  AppName *string `json:"app_name,omitempty" xml:"app_name,omitempty" require:"true" maxLength:"128" minLength:"1" pattern:"[0-9a-zA-Z]+"`
  // App 秘钥
  AppSecret *string `json:"app_secret,omitempty" xml:"app_secret,omitempty" require:"true"`
  // App 创建时间
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty" require:"true"`
  // App描述
  Description *string `json:"description,omitempty" xml:"description,omitempty" require:"true" maxLength:"128" minLength:"0"`
  // App图标
  Logo *string `json:"logo,omitempty" xml:"logo,omitempty" require:"true"`
  // App 提供方
  Provider *string `json:"provider,omitempty" xml:"provider,omitempty" require:"true"`
  // App回调地址
  RedirectUri *string `json:"redirect_uri,omitempty" xml:"redirect_uri,omitempty" require:"true"`
  // App权限列表
  Scope []*string `json:"scope,omitempty" xml:"scope,omitempty" require:"true" type:"Repeated"`
  // App 屏幕截图
  Screenshots []*string `json:"screenshots,omitempty" xml:"screenshots,omitempty" require:"true" type:"Repeated"`
  // App 当前阶段
  Stage *string `json:"stage,omitempty" xml:"stage,omitempty" require:"true"`
  // App类型
  Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
  // App 修改时间
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty" require:"true"`
}

func (s GetAppResponse) String() string {
  return tea.Prettify(s)
}

func (s GetAppResponse) GoString() string {
  return s.String()
}

func (s *GetAppResponse) SetAliOwnerId(v string) *GetAppResponse {
  s.AliOwnerId = &v
  return s
}

func (s *GetAppResponse) SetAppId(v string) *GetAppResponse {
  s.AppId = &v
  return s
}

func (s *GetAppResponse) SetAppName(v string) *GetAppResponse {
  s.AppName = &v
  return s
}

func (s *GetAppResponse) SetAppSecret(v string) *GetAppResponse {
  s.AppSecret = &v
  return s
}

func (s *GetAppResponse) SetCreatedAt(v string) *GetAppResponse {
  s.CreatedAt = &v
  return s
}

func (s *GetAppResponse) SetDescription(v string) *GetAppResponse {
  s.Description = &v
  return s
}

func (s *GetAppResponse) SetLogo(v string) *GetAppResponse {
  s.Logo = &v
  return s
}

func (s *GetAppResponse) SetProvider(v string) *GetAppResponse {
  s.Provider = &v
  return s
}

func (s *GetAppResponse) SetRedirectUri(v string) *GetAppResponse {
  s.RedirectUri = &v
  return s
}

func (s *GetAppResponse) SetScope(v []*string) *GetAppResponse {
  s.Scope = v
  return s
}

func (s *GetAppResponse) SetScreenshots(v []*string) *GetAppResponse {
  s.Screenshots = v
  return s
}

func (s *GetAppResponse) SetStage(v string) *GetAppResponse {
  s.Stage = &v
  return s
}

func (s *GetAppResponse) SetType(v string) *GetAppResponse {
  s.Type = &v
  return s
}

func (s *GetAppResponse) SetUpdatedAt(v string) *GetAppResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * 
 */
type GetBizCNameInfoRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // cname type
  CnameType *string `json:"cname_type,omitempty" xml:"cname_type,omitempty" require:"true"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // is vpc
  IsVpc *bool `json:"is_vpc,omitempty" xml:"is_vpc,omitempty"`
}

func (s GetBizCNameInfoRequest) String() string {
  return tea.Prettify(s)
}

func (s GetBizCNameInfoRequest) GoString() string {
  return s.String()
}

func (s *GetBizCNameInfoRequest) SetHeaders(v map[string]*string) *GetBizCNameInfoRequest {
  s.Headers = v
  return s
}

func (s *GetBizCNameInfoRequest) SetCnameType(v string) *GetBizCNameInfoRequest {
  s.CnameType = &v
  return s
}

func (s *GetBizCNameInfoRequest) SetDomainId(v string) *GetBizCNameInfoRequest {
  s.DomainId = &v
  return s
}

func (s *GetBizCNameInfoRequest) SetIsVpc(v bool) *GetBizCNameInfoRequest {
  s.IsVpc = &v
  return s
}

/**
 * 
 */
type GetBizCNameInfoResponse struct {
  // biz cname
  BizCname *string `json:"biz_cname,omitempty" xml:"biz_cname,omitempty"`
  // cert name
  CertId *string `json:"cert_id,omitempty" xml:"cert_id,omitempty"`
  // cert name
  CertName *string `json:"cert_name,omitempty" xml:"cert_name,omitempty"`
  CnameStatus *CNameStatus `json:"cname_status,omitempty" xml:"cname_status,omitempty"`
  // cname type
  CnameType *string `json:"cname_type,omitempty" xml:"cname_type,omitempty"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // is vpc
  IsVpc *bool `json:"is_vpc,omitempty" xml:"is_vpc,omitempty"`
}

func (s GetBizCNameInfoResponse) String() string {
  return tea.Prettify(s)
}

func (s GetBizCNameInfoResponse) GoString() string {
  return s.String()
}

func (s *GetBizCNameInfoResponse) SetBizCname(v string) *GetBizCNameInfoResponse {
  s.BizCname = &v
  return s
}

func (s *GetBizCNameInfoResponse) SetCertId(v string) *GetBizCNameInfoResponse {
  s.CertId = &v
  return s
}

func (s *GetBizCNameInfoResponse) SetCertName(v string) *GetBizCNameInfoResponse {
  s.CertName = &v
  return s
}

func (s *GetBizCNameInfoResponse) SetCnameStatus(v *CNameStatus) *GetBizCNameInfoResponse {
  s.CnameStatus = v
  return s
}

func (s *GetBizCNameInfoResponse) SetCnameType(v string) *GetBizCNameInfoResponse {
  s.CnameType = &v
  return s
}

func (s *GetBizCNameInfoResponse) SetDomainId(v string) *GetBizCNameInfoResponse {
  s.DomainId = &v
  return s
}

func (s *GetBizCNameInfoResponse) SetIsVpc(v bool) *GetBizCNameInfoResponse {
  s.IsVpc = &v
  return s
}

/**
 * 
 */
type GetCorsRuleListRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
}

func (s GetCorsRuleListRequest) String() string {
  return tea.Prettify(s)
}

func (s GetCorsRuleListRequest) GoString() string {
  return s.String()
}

func (s *GetCorsRuleListRequest) SetHeaders(v map[string]*string) *GetCorsRuleListRequest {
  s.Headers = v
  return s
}

func (s *GetCorsRuleListRequest) SetDomainId(v string) *GetCorsRuleListRequest {
  s.DomainId = &v
  return s
}

/**
 * 
 */
type GetDataCNameInfoRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
}

func (s GetDataCNameInfoRequest) String() string {
  return tea.Prettify(s)
}

func (s GetDataCNameInfoRequest) GoString() string {
  return s.String()
}

func (s *GetDataCNameInfoRequest) SetHeaders(v map[string]*string) *GetDataCNameInfoRequest {
  s.Headers = v
  return s
}

func (s *GetDataCNameInfoRequest) SetDomainId(v string) *GetDataCNameInfoRequest {
  s.DomainId = &v
  return s
}

/**
 * get domain request
 */
type GetDomainRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
}

func (s GetDomainRequest) String() string {
  return tea.Prettify(s)
}

func (s GetDomainRequest) GoString() string {
  return s.String()
}

func (s *GetDomainRequest) SetHeaders(v map[string]*string) *GetDomainRequest {
  s.Headers = v
  return s
}

func (s *GetDomainRequest) SetDomainId(v string) *GetDomainRequest {
  s.DomainId = &v
  return s
}

/**
 * get domain response
 */
type GetDomainResponse struct {
  // Domain APICName
  ApiCname *string `json:"api_cname,omitempty" xml:"api_cname,omitempty"`
  // Domain AppCName
  AppCname *string `json:"app_cname,omitempty" xml:"app_cname,omitempty"`
  // 支付宝 App Id
  AuthAlipayAppId *string `json:"auth_alipay_app_id,omitempty" xml:"auth_alipay_app_id,omitempty"`
  // 是否开启了支付宝认证
  AuthAlipayEnable *bool `json:"auth_alipay_enable,omitempty" xml:"auth_alipay_enable,omitempty"`
  // 支付宝 App Secret
  AuthAlipayPrivateKey *string `json:"auth_alipay_private_key,omitempty" xml:"auth_alipay_private_key,omitempty"`
  // Domain AuthCName
  AuthCname *string `json:"auth_cname,omitempty" xml:"auth_cname,omitempty"`
  // 登录相关信息
  AuthConfig map[string]interface{} `json:"auth_config,omitempty" xml:"auth_config,omitempty"`
  // 钉钉 App Id
  AuthDingdingAppId *string `json:"auth_dingding_app_id,omitempty" xml:"auth_dingding_app_id,omitempty"`
  // 钉钉 App Secret
  AuthDingdingAppSecret *string `json:"auth_dingding_app_secret,omitempty" xml:"auth_dingding_app_secret,omitempty"`
  // 是否开启了钉钉认证
  AuthDingdingEnable *bool `json:"auth_dingding_enable,omitempty" xml:"auth_dingding_enable,omitempty"`
  AuthEndpointEnable *bool `json:"auth_endpoint_enable,omitempty" xml:"auth_endpoint_enable,omitempty"`
  // RAM App Id
  AuthRamAppId *string `json:"auth_ram_app_id,omitempty" xml:"auth_ram_app_id,omitempty"`
  // RAM App Secret
  AuthRamAppSecret *string `json:"auth_ram_app_secret,omitempty" xml:"auth_ram_app_secret,omitempty"`
  // 是否开启了 RAM 认证
  AuthRamEnable *bool `json:"auth_ram_enable,omitempty" xml:"auth_ram_enable,omitempty"`
  // Domain 创建时间
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // 数据 Hash 算法
  DataHashName *string `json:"data_hash_name,omitempty" xml:"data_hash_name,omitempty"`
  // Domain 描述
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // Domain 描述
  DomainName *string `json:"domain_name,omitempty" xml:"domain_name,omitempty"`
  // 事件通知 MNS 匹配文件名
  EventFilenameMatches *string `json:"event_filename_matches,omitempty" xml:"event_filename_matches,omitempty"`
  // 事件通知 MNS Endpoint
  EventMnsEndpoint *string `json:"event_mns_endpoint,omitempty" xml:"event_mns_endpoint,omitempty"`
  // 事件通知 MNS Topic
  EventMnsTopic *string `json:"event_mns_topic,omitempty" xml:"event_mns_topic,omitempty"`
  // 事件名列表
  EventNames []*string `json:"event_names,omitempty" xml:"event_names,omitempty" type:"Repeated"`
  // 事件通知 Role Arn
  EventRoleArn *string `json:"event_role_arn,omitempty" xml:"event_role_arn,omitempty"`
  // 是否开启了自动初始化 Drive
  InitDriveEnable *bool `json:"init_drive_enable,omitempty" xml:"init_drive_enable,omitempty"`
  // 自动初始化 Drive 大小
  InitDriveSize *int64 `json:"init_drive_size,omitempty" xml:"init_drive_size,omitempty"`
  // 自动初始化 Drive 所用 Store ID
  InitDriveStoreId *string `json:"init_drive_store_id,omitempty" xml:"init_drive_store_id,omitempty"`
  // Domain 类型
  Mode *string `json:"mode,omitempty" xml:"mode,omitempty"`
  // Domain 类型
  PathType *string `json:"path_type,omitempty" xml:"path_type,omitempty"`
  PublishedAppAccessStrategy *AppAccessStrategy `json:"published_app_access_strategy,omitempty" xml:"published_app_access_strategy,omitempty"`
  // 是否开启了分享
  Sharable *bool `json:"sharable,omitempty" xml:"sharable,omitempty"`
  // 存储级别
  StoreLevel *string `json:"store_level,omitempty" xml:"store_level,omitempty"`
  // 存储 Region 列表
  StoreRegionList []*string `json:"store_region_list,omitempty" xml:"store_region_list,omitempty" type:"Repeated"`
  // Domain 更新时间
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s GetDomainResponse) String() string {
  return tea.Prettify(s)
}

func (s GetDomainResponse) GoString() string {
  return s.String()
}

func (s *GetDomainResponse) SetApiCname(v string) *GetDomainResponse {
  s.ApiCname = &v
  return s
}

func (s *GetDomainResponse) SetAppCname(v string) *GetDomainResponse {
  s.AppCname = &v
  return s
}

func (s *GetDomainResponse) SetAuthAlipayAppId(v string) *GetDomainResponse {
  s.AuthAlipayAppId = &v
  return s
}

func (s *GetDomainResponse) SetAuthAlipayEnable(v bool) *GetDomainResponse {
  s.AuthAlipayEnable = &v
  return s
}

func (s *GetDomainResponse) SetAuthAlipayPrivateKey(v string) *GetDomainResponse {
  s.AuthAlipayPrivateKey = &v
  return s
}

func (s *GetDomainResponse) SetAuthCname(v string) *GetDomainResponse {
  s.AuthCname = &v
  return s
}

func (s *GetDomainResponse) SetAuthConfig(v map[string]interface{}) *GetDomainResponse {
  s.AuthConfig = v
  return s
}

func (s *GetDomainResponse) SetAuthDingdingAppId(v string) *GetDomainResponse {
  s.AuthDingdingAppId = &v
  return s
}

func (s *GetDomainResponse) SetAuthDingdingAppSecret(v string) *GetDomainResponse {
  s.AuthDingdingAppSecret = &v
  return s
}

func (s *GetDomainResponse) SetAuthDingdingEnable(v bool) *GetDomainResponse {
  s.AuthDingdingEnable = &v
  return s
}

func (s *GetDomainResponse) SetAuthEndpointEnable(v bool) *GetDomainResponse {
  s.AuthEndpointEnable = &v
  return s
}

func (s *GetDomainResponse) SetAuthRamAppId(v string) *GetDomainResponse {
  s.AuthRamAppId = &v
  return s
}

func (s *GetDomainResponse) SetAuthRamAppSecret(v string) *GetDomainResponse {
  s.AuthRamAppSecret = &v
  return s
}

func (s *GetDomainResponse) SetAuthRamEnable(v bool) *GetDomainResponse {
  s.AuthRamEnable = &v
  return s
}

func (s *GetDomainResponse) SetCreatedAt(v string) *GetDomainResponse {
  s.CreatedAt = &v
  return s
}

func (s *GetDomainResponse) SetDataHashName(v string) *GetDomainResponse {
  s.DataHashName = &v
  return s
}

func (s *GetDomainResponse) SetDescription(v string) *GetDomainResponse {
  s.Description = &v
  return s
}

func (s *GetDomainResponse) SetDomainId(v string) *GetDomainResponse {
  s.DomainId = &v
  return s
}

func (s *GetDomainResponse) SetDomainName(v string) *GetDomainResponse {
  s.DomainName = &v
  return s
}

func (s *GetDomainResponse) SetEventFilenameMatches(v string) *GetDomainResponse {
  s.EventFilenameMatches = &v
  return s
}

func (s *GetDomainResponse) SetEventMnsEndpoint(v string) *GetDomainResponse {
  s.EventMnsEndpoint = &v
  return s
}

func (s *GetDomainResponse) SetEventMnsTopic(v string) *GetDomainResponse {
  s.EventMnsTopic = &v
  return s
}

func (s *GetDomainResponse) SetEventNames(v []*string) *GetDomainResponse {
  s.EventNames = v
  return s
}

func (s *GetDomainResponse) SetEventRoleArn(v string) *GetDomainResponse {
  s.EventRoleArn = &v
  return s
}

func (s *GetDomainResponse) SetInitDriveEnable(v bool) *GetDomainResponse {
  s.InitDriveEnable = &v
  return s
}

func (s *GetDomainResponse) SetInitDriveSize(v int64) *GetDomainResponse {
  s.InitDriveSize = &v
  return s
}

func (s *GetDomainResponse) SetInitDriveStoreId(v string) *GetDomainResponse {
  s.InitDriveStoreId = &v
  return s
}

func (s *GetDomainResponse) SetMode(v string) *GetDomainResponse {
  s.Mode = &v
  return s
}

func (s *GetDomainResponse) SetPathType(v string) *GetDomainResponse {
  s.PathType = &v
  return s
}

func (s *GetDomainResponse) SetPublishedAppAccessStrategy(v *AppAccessStrategy) *GetDomainResponse {
  s.PublishedAppAccessStrategy = v
  return s
}

func (s *GetDomainResponse) SetSharable(v bool) *GetDomainResponse {
  s.Sharable = &v
  return s
}

func (s *GetDomainResponse) SetStoreLevel(v string) *GetDomainResponse {
  s.StoreLevel = &v
  return s
}

func (s *GetDomainResponse) SetStoreRegionList(v []*string) *GetDomainResponse {
  s.StoreRegionList = v
  return s
}

func (s *GetDomainResponse) SetUpdatedAt(v string) *GetDomainResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * 
 */
type LdapConfig struct {
  AdminDn *string `json:"admin_dn,omitempty" xml:"admin_dn,omitempty"`
  AdminPassword *string `json:"admin_password,omitempty" xml:"admin_password,omitempty"`
  BaseDn *string `json:"base_dn,omitempty" xml:"base_dn,omitempty"`
  Host *string `json:"host,omitempty" xml:"host,omitempty"`
  Port *int64 `json:"port,omitempty" xml:"port,omitempty"`
  Uid *string `json:"uid,omitempty" xml:"uid,omitempty"`
}

func (s LdapConfig) String() string {
  return tea.Prettify(s)
}

func (s LdapConfig) GoString() string {
  return s.String()
}

func (s *LdapConfig) SetAdminDn(v string) *LdapConfig {
  s.AdminDn = &v
  return s
}

func (s *LdapConfig) SetAdminPassword(v string) *LdapConfig {
  s.AdminPassword = &v
  return s
}

func (s *LdapConfig) SetBaseDn(v string) *LdapConfig {
  s.BaseDn = &v
  return s
}

func (s *LdapConfig) SetHost(v string) *LdapConfig {
  s.Host = &v
  return s
}

func (s *LdapConfig) SetPort(v int64) *LdapConfig {
  s.Port = &v
  return s
}

func (s *LdapConfig) SetUid(v string) *LdapConfig {
  s.Uid = &v
  return s
}

/**
 * 
 */
type ListAppsRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // 返回结果数据
  Limit *int32 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
  // 下次查询游标
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
}

func (s ListAppsRequest) String() string {
  return tea.Prettify(s)
}

func (s ListAppsRequest) GoString() string {
  return s.String()
}

func (s *ListAppsRequest) SetHeaders(v map[string]*string) *ListAppsRequest {
  s.Headers = v
  return s
}

func (s *ListAppsRequest) SetLimit(v int32) *ListAppsRequest {
  s.Limit = &v
  return s
}

func (s *ListAppsRequest) SetMarker(v string) *ListAppsRequest {
  s.Marker = &v
  return s
}

/**
 * 
 */
type ListAppsResponse struct {
  // App 列表
  Items []*GetAppResponse `json:"items,omitempty" xml:"items,omitempty" require:"true" type:"Repeated"`
  // App 分批查询游标
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ListAppsResponse) String() string {
  return tea.Prettify(s)
}

func (s ListAppsResponse) GoString() string {
  return s.String()
}

func (s *ListAppsResponse) SetItems(v []*GetAppResponse) *ListAppsResponse {
  s.Items = v
  return s
}

func (s *ListAppsResponse) SetNextMarker(v string) *ListAppsResponse {
  s.NextMarker = &v
  return s
}

/**
 * list domain cors response
 */
type ListDomainCORSRuleResponse struct {
  // cors rule 列表
  CorsRuleList []*CorsRule `json:"cors_rule_list,omitempty" xml:"cors_rule_list,omitempty" type:"Repeated"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
}

func (s ListDomainCORSRuleResponse) String() string {
  return tea.Prettify(s)
}

func (s ListDomainCORSRuleResponse) GoString() string {
  return s.String()
}

func (s *ListDomainCORSRuleResponse) SetCorsRuleList(v []*CorsRule) *ListDomainCORSRuleResponse {
  s.CorsRuleList = v
  return s
}

func (s *ListDomainCORSRuleResponse) SetDomainId(v string) *ListDomainCORSRuleResponse {
  s.DomainId = &v
  return s
}

/**
 * list domain request
 */
type ListDomainsRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // 分页大小
  Limit *int32 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
  // 查询游标
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
}

func (s ListDomainsRequest) String() string {
  return tea.Prettify(s)
}

func (s ListDomainsRequest) GoString() string {
  return s.String()
}

func (s *ListDomainsRequest) SetHeaders(v map[string]*string) *ListDomainsRequest {
  s.Headers = v
  return s
}

func (s *ListDomainsRequest) SetLimit(v int32) *ListDomainsRequest {
  s.Limit = &v
  return s
}

func (s *ListDomainsRequest) SetMarker(v string) *ListDomainsRequest {
  s.Marker = &v
  return s
}

/**
 * list domain response
 */
type ListDomainsResponse struct {
  // domain 列表
  Items []*BaseDomainResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
  // 下次分页查询游标
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ListDomainsResponse) String() string {
  return tea.Prettify(s)
}

func (s ListDomainsResponse) GoString() string {
  return s.String()
}

func (s *ListDomainsResponse) SetItems(v []*BaseDomainResponse) *ListDomainsResponse {
  s.Items = v
  return s
}

func (s *ListDomainsResponse) SetNextMarker(v string) *ListDomainsResponse {
  s.NextMarker = &v
  return s
}

/**
 * 
 */
type ListStoresRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
}

func (s ListStoresRequest) String() string {
  return tea.Prettify(s)
}

func (s ListStoresRequest) GoString() string {
  return s.String()
}

func (s *ListStoresRequest) SetHeaders(v map[string]*string) *ListStoresRequest {
  s.Headers = v
  return s
}

func (s *ListStoresRequest) SetDomainId(v string) *ListStoresRequest {
  s.DomainId = &v
  return s
}

/**
 * 
 */
type ListStoresResponse struct {
  // Store 列表
  Items []*Store `json:"items,omitempty" xml:"items,omitempty" require:"true" type:"Repeated"`
}

func (s ListStoresResponse) String() string {
  return tea.Prettify(s)
}

func (s ListStoresResponse) GoString() string {
  return s.String()
}

func (s *ListStoresResponse) SetItems(v []*Store) *ListStoresResponse {
  s.Items = v
  return s
}

/**
 * 
 */
type RemoveStoreRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // store ID
  StoreId *string `json:"store_id,omitempty" xml:"store_id,omitempty" require:"true"`
}

func (s RemoveStoreRequest) String() string {
  return tea.Prettify(s)
}

func (s RemoveStoreRequest) GoString() string {
  return s.String()
}

func (s *RemoveStoreRequest) SetHeaders(v map[string]*string) *RemoveStoreRequest {
  s.Headers = v
  return s
}

func (s *RemoveStoreRequest) SetDomainId(v string) *RemoveStoreRequest {
  s.DomainId = &v
  return s
}

func (s *RemoveStoreRequest) SetStoreId(v string) *RemoveStoreRequest {
  s.StoreId = &v
  return s
}

/**
 * 
 */
type SetAppPublicKeyRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // App ID
  AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
  // RSA加密算法的公钥, PEM格式
  PublicKey *string `json:"public_key,omitempty" xml:"public_key,omitempty" require:"true"`
}

func (s SetAppPublicKeyRequest) String() string {
  return tea.Prettify(s)
}

func (s SetAppPublicKeyRequest) GoString() string {
  return s.String()
}

func (s *SetAppPublicKeyRequest) SetHeaders(v map[string]*string) *SetAppPublicKeyRequest {
  s.Headers = v
  return s
}

func (s *SetAppPublicKeyRequest) SetAppId(v string) *SetAppPublicKeyRequest {
  s.AppId = &v
  return s
}

func (s *SetAppPublicKeyRequest) SetPublicKey(v string) *SetAppPublicKeyRequest {
  s.PublicKey = &v
  return s
}

/**
 * 
 */
type SetBizCNameCertRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  CertID *string `json:"CertID,omitempty" xml:"CertID,omitempty"`
  // biz cname
  BizCname *string `json:"biz_cname,omitempty" xml:"biz_cname,omitempty"`
  // cert body
  CertBody *string `json:"cert_body,omitempty" xml:"cert_body,omitempty" require:"true"`
  // cert name
  CertName *string `json:"cert_name,omitempty" xml:"cert_name,omitempty" require:"true"`
  // cert privatekey
  CertPrivatekey *string `json:"cert_privatekey,omitempty" xml:"cert_privatekey,omitempty" require:"true"`
  // cname type
  CnameType *string `json:"cname_type,omitempty" xml:"cname_type,omitempty" require:"true"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // biz cname
  IsVpc *bool `json:"is_vpc,omitempty" xml:"is_vpc,omitempty"`
}

func (s SetBizCNameCertRequest) String() string {
  return tea.Prettify(s)
}

func (s SetBizCNameCertRequest) GoString() string {
  return s.String()
}

func (s *SetBizCNameCertRequest) SetHeaders(v map[string]*string) *SetBizCNameCertRequest {
  s.Headers = v
  return s
}

func (s *SetBizCNameCertRequest) SetCertID(v string) *SetBizCNameCertRequest {
  s.CertID = &v
  return s
}

func (s *SetBizCNameCertRequest) SetBizCname(v string) *SetBizCNameCertRequest {
  s.BizCname = &v
  return s
}

func (s *SetBizCNameCertRequest) SetCertBody(v string) *SetBizCNameCertRequest {
  s.CertBody = &v
  return s
}

func (s *SetBizCNameCertRequest) SetCertName(v string) *SetBizCNameCertRequest {
  s.CertName = &v
  return s
}

func (s *SetBizCNameCertRequest) SetCertPrivatekey(v string) *SetBizCNameCertRequest {
  s.CertPrivatekey = &v
  return s
}

func (s *SetBizCNameCertRequest) SetCnameType(v string) *SetBizCNameCertRequest {
  s.CnameType = &v
  return s
}

func (s *SetBizCNameCertRequest) SetDomainId(v string) *SetBizCNameCertRequest {
  s.DomainId = &v
  return s
}

func (s *SetBizCNameCertRequest) SetIsVpc(v bool) *SetBizCNameCertRequest {
  s.IsVpc = &v
  return s
}

/**
 * 
 */
type SetBizCNameCertResponse struct {
  // biz cname
  BizCname *string `json:"biz_cname,omitempty" xml:"biz_cname,omitempty"`
  // cert name
  CertName *string `json:"cert_name,omitempty" xml:"cert_name,omitempty"`
  // cname type
  CnameType *string `json:"cname_type,omitempty" xml:"cname_type,omitempty"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // is vpc
  IsVpc *bool `json:"is_vpc,omitempty" xml:"is_vpc,omitempty"`
}

func (s SetBizCNameCertResponse) String() string {
  return tea.Prettify(s)
}

func (s SetBizCNameCertResponse) GoString() string {
  return s.String()
}

func (s *SetBizCNameCertResponse) SetBizCname(v string) *SetBizCNameCertResponse {
  s.BizCname = &v
  return s
}

func (s *SetBizCNameCertResponse) SetCertName(v string) *SetBizCNameCertResponse {
  s.CertName = &v
  return s
}

func (s *SetBizCNameCertResponse) SetCnameType(v string) *SetBizCNameCertResponse {
  s.CnameType = &v
  return s
}

func (s *SetBizCNameCertResponse) SetDomainId(v string) *SetBizCNameCertResponse {
  s.DomainId = &v
  return s
}

func (s *SetBizCNameCertResponse) SetIsVpc(v bool) *SetBizCNameCertResponse {
  s.IsVpc = &v
  return s
}

/**
 * 
 */
type SetBizCNameRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // biz cname
  BizCname *string `json:"biz_cname,omitempty" xml:"biz_cname,omitempty" require:"true"`
  // cname type
  CnameType *string `json:"cname_type,omitempty" xml:"cname_type,omitempty" require:"true"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // biz cname
  IsVpc *bool `json:"is_vpc,omitempty" xml:"is_vpc,omitempty"`
}

func (s SetBizCNameRequest) String() string {
  return tea.Prettify(s)
}

func (s SetBizCNameRequest) GoString() string {
  return s.String()
}

func (s *SetBizCNameRequest) SetHeaders(v map[string]*string) *SetBizCNameRequest {
  s.Headers = v
  return s
}

func (s *SetBizCNameRequest) SetBizCname(v string) *SetBizCNameRequest {
  s.BizCname = &v
  return s
}

func (s *SetBizCNameRequest) SetCnameType(v string) *SetBizCNameRequest {
  s.CnameType = &v
  return s
}

func (s *SetBizCNameRequest) SetDomainId(v string) *SetBizCNameRequest {
  s.DomainId = &v
  return s
}

func (s *SetBizCNameRequest) SetIsVpc(v bool) *SetBizCNameRequest {
  s.IsVpc = &v
  return s
}

/**
 * 
 */
type SetBizCNameResponse struct {
  // biz cname
  BizCname *string `json:"biz_cname,omitempty" xml:"biz_cname,omitempty"`
  CnameStatus *CNameStatus `json:"cname_status,omitempty" xml:"cname_status,omitempty"`
  // cname type
  CnameType *string `json:"cname_type,omitempty" xml:"cname_type,omitempty"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // is vpc
  IsVpc *bool `json:"is_vpc,omitempty" xml:"is_vpc,omitempty"`
}

func (s SetBizCNameResponse) String() string {
  return tea.Prettify(s)
}

func (s SetBizCNameResponse) GoString() string {
  return s.String()
}

func (s *SetBizCNameResponse) SetBizCname(v string) *SetBizCNameResponse {
  s.BizCname = &v
  return s
}

func (s *SetBizCNameResponse) SetCnameStatus(v *CNameStatus) *SetBizCNameResponse {
  s.CnameStatus = v
  return s
}

func (s *SetBizCNameResponse) SetCnameType(v string) *SetBizCNameResponse {
  s.CnameType = &v
  return s
}

func (s *SetBizCNameResponse) SetDomainId(v string) *SetBizCNameResponse {
  s.DomainId = &v
  return s
}

func (s *SetBizCNameResponse) SetIsVpc(v bool) *SetBizCNameResponse {
  s.IsVpc = &v
  return s
}

/**
 * list cors rule request
 */
type SetCorsRuleListRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // cors rule list
  CorsRuleList []*CorsRule `json:"cors_rule_list,omitempty" xml:"cors_rule_list,omitempty" require:"true" type:"Repeated"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
}

func (s SetCorsRuleListRequest) String() string {
  return tea.Prettify(s)
}

func (s SetCorsRuleListRequest) GoString() string {
  return s.String()
}

func (s *SetCorsRuleListRequest) SetHeaders(v map[string]*string) *SetCorsRuleListRequest {
  s.Headers = v
  return s
}

func (s *SetCorsRuleListRequest) SetCorsRuleList(v []*CorsRule) *SetCorsRuleListRequest {
  s.CorsRuleList = v
  return s
}

func (s *SetCorsRuleListRequest) SetDomainId(v string) *SetCorsRuleListRequest {
  s.DomainId = &v
  return s
}

/**
 * 
 */
type SetDataCNameRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // cn-shanghai data cname
  DataCname *string `json:"data_cname,omitempty" xml:"data_cname,omitempty" require:"true"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty" require:"true"`
}

func (s SetDataCNameRequest) String() string {
  return tea.Prettify(s)
}

func (s SetDataCNameRequest) GoString() string {
  return s.String()
}

func (s *SetDataCNameRequest) SetHeaders(v map[string]*string) *SetDataCNameRequest {
  s.Headers = v
  return s
}

func (s *SetDataCNameRequest) SetDataCname(v string) *SetDataCNameRequest {
  s.DataCname = &v
  return s
}

func (s *SetDataCNameRequest) SetDomainId(v string) *SetDataCNameRequest {
  s.DomainId = &v
  return s
}

func (s *SetDataCNameRequest) SetLocation(v string) *SetDataCNameRequest {
  s.Location = &v
  return s
}

/**
 * 
 */
type SetDataCNameResponse struct {
  // datacname
  DataCname *string `json:"data_cname,omitempty" xml:"data_cname,omitempty" require:"true"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // data location
  Location *string `json:"location,omitempty" xml:"location,omitempty" require:"true"`
}

func (s SetDataCNameResponse) String() string {
  return tea.Prettify(s)
}

func (s SetDataCNameResponse) GoString() string {
  return s.String()
}

func (s *SetDataCNameResponse) SetDataCname(v string) *SetDataCNameResponse {
  s.DataCname = &v
  return s
}

func (s *SetDataCNameResponse) SetDomainId(v string) *SetDataCNameResponse {
  s.DomainId = &v
  return s
}

func (s *SetDataCNameResponse) SetLocation(v string) *SetDataCNameResponse {
  s.Location = &v
  return s
}

/**
 * 
 */
type Store struct {
  // 全球加速地址
  AccelerateEndpoint *string `json:"accelerate_endpoint,omitempty" xml:"accelerate_endpoint,omitempty"`
  // 存储公共前缀
  BasePath *string `json:"base_path,omitempty" xml:"base_path,omitempty"`
  // bucket名称
  Bucket *string `json:"bucket,omitempty" xml:"bucket,omitempty" require:"true"`
  // 内容分发地址
  CdnEndpoint *string `json:"cdn_endpoint,omitempty" xml:"cdn_endpoint,omitempty"`
  // 自定义全球加速地址
  CustomizedAccelerateEndpoint *string `json:"customized_accelerate_endpoint,omitempty" xml:"customized_accelerate_endpoint,omitempty"`
  // 自定义内容分发地址
  CustomizedCdnEndpoint *string `json:"customized_cdn_endpoint,omitempty" xml:"customized_cdn_endpoint,omitempty"`
  // 自定义Public访问地址
  CustomizedEndpoint *string `json:"customized_endpoint,omitempty" xml:"customized_endpoint,omitempty"`
  // 自定义vpc访问地址
  CustomizedInternalEndpoint *string `json:"customized_internal_endpoint,omitempty" xml:"customized_internal_endpoint,omitempty"`
  // Public访问地址
  Endpoint *string `json:"endpoint,omitempty" xml:"endpoint,omitempty" require:"true"`
  // vpc访问地址
  InternalEndpoint *string `json:"internal_endpoint,omitempty" xml:"internal_endpoint,omitempty"`
  // 地点
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // 存储归属，system表示系统提供，custom表示使用自己的存储
  Ownership *string `json:"ownership,omitempty" xml:"ownership,omitempty" require:"true"`
  // Policy授权,system类型store会将bucket权限授予当前云账号
  Policy *string `json:"policy,omitempty" xml:"policy,omitempty" require:"true"`
  // 访问Bucket的角色ARN
  RoleArn *string `json:"role_arn,omitempty" xml:"role_arn,omitempty"`
  // store ID
  StoreId *string `json:"store_id,omitempty" xml:"store_id,omitempty" require:"true"`
  // 存储类型，当前只支持oss
  Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
}

func (s Store) String() string {
  return tea.Prettify(s)
}

func (s Store) GoString() string {
  return s.String()
}

func (s *Store) SetAccelerateEndpoint(v string) *Store {
  s.AccelerateEndpoint = &v
  return s
}

func (s *Store) SetBasePath(v string) *Store {
  s.BasePath = &v
  return s
}

func (s *Store) SetBucket(v string) *Store {
  s.Bucket = &v
  return s
}

func (s *Store) SetCdnEndpoint(v string) *Store {
  s.CdnEndpoint = &v
  return s
}

func (s *Store) SetCustomizedAccelerateEndpoint(v string) *Store {
  s.CustomizedAccelerateEndpoint = &v
  return s
}

func (s *Store) SetCustomizedCdnEndpoint(v string) *Store {
  s.CustomizedCdnEndpoint = &v
  return s
}

func (s *Store) SetCustomizedEndpoint(v string) *Store {
  s.CustomizedEndpoint = &v
  return s
}

func (s *Store) SetCustomizedInternalEndpoint(v string) *Store {
  s.CustomizedInternalEndpoint = &v
  return s
}

func (s *Store) SetEndpoint(v string) *Store {
  s.Endpoint = &v
  return s
}

func (s *Store) SetInternalEndpoint(v string) *Store {
  s.InternalEndpoint = &v
  return s
}

func (s *Store) SetLocation(v string) *Store {
  s.Location = &v
  return s
}

func (s *Store) SetOwnership(v string) *Store {
  s.Ownership = &v
  return s
}

func (s *Store) SetPolicy(v string) *Store {
  s.Policy = &v
  return s
}

func (s *Store) SetRoleArn(v string) *Store {
  s.RoleArn = &v
  return s
}

func (s *Store) SetStoreId(v string) *Store {
  s.StoreId = &v
  return s
}

func (s *Store) SetType(v string) *Store {
  s.Type = &v
  return s
}

/**
 * 
 */
type UpdateAppRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // App ID
  AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
  // App名称
  AppName *string `json:"app_name,omitempty" xml:"app_name,omitempty" maxLength:"128" minLength:"1"`
  // App描述
  Description *string `json:"description,omitempty" xml:"description,omitempty" maxLength:"1024" minLength:"0"`
  // App图标
  Logo *string `json:"logo,omitempty" xml:"logo,omitempty"`
  // App回调地址
  RedirectUri *string `json:"redirect_uri,omitempty" xml:"redirect_uri,omitempty"`
  // App权限列表
  Scope []*string `json:"scope,omitempty" xml:"scope,omitempty" type:"Repeated"`
  // App类型
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
}

func (s UpdateAppRequest) String() string {
  return tea.Prettify(s)
}

func (s UpdateAppRequest) GoString() string {
  return s.String()
}

func (s *UpdateAppRequest) SetHeaders(v map[string]*string) *UpdateAppRequest {
  s.Headers = v
  return s
}

func (s *UpdateAppRequest) SetAppId(v string) *UpdateAppRequest {
  s.AppId = &v
  return s
}

func (s *UpdateAppRequest) SetAppName(v string) *UpdateAppRequest {
  s.AppName = &v
  return s
}

func (s *UpdateAppRequest) SetDescription(v string) *UpdateAppRequest {
  s.Description = &v
  return s
}

func (s *UpdateAppRequest) SetLogo(v string) *UpdateAppRequest {
  s.Logo = &v
  return s
}

func (s *UpdateAppRequest) SetRedirectUri(v string) *UpdateAppRequest {
  s.RedirectUri = &v
  return s
}

func (s *UpdateAppRequest) SetScope(v []*string) *UpdateAppRequest {
  s.Scope = v
  return s
}

func (s *UpdateAppRequest) SetType(v string) *UpdateAppRequest {
  s.Type = &v
  return s
}

/**
 * update domain request
 */
type UpdateDomainRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  AuthConfig map[string]interface{} `json:"auth_config,omitempty" xml:"auth_config,omitempty"`
  // 钉钉 App Id
  AuthDingdingAppId *string `json:"auth_dingding_app_id,omitempty" xml:"auth_dingding_app_id,omitempty"`
  // 钉钉 App Secret
  AuthDingdingAppSecret *string `json:"auth_dingding_app_secret,omitempty" xml:"auth_dingding_app_secret,omitempty"`
  // 启用钉钉认证
  AuthDingdingEnable *bool `json:"auth_dingding_enable,omitempty" xml:"auth_dingding_enable,omitempty"`
  AuthEndpointEnable *bool `json:"auth_endpoint_enable,omitempty" xml:"auth_endpoint_enable,omitempty"`
  // RAM App Id
  AuthRamAppId *string `json:"auth_ram_app_id,omitempty" xml:"auth_ram_app_id,omitempty"`
  // RAM App Secret
  AuthRamAppSecret *string `json:"auth_ram_app_secret,omitempty" xml:"auth_ram_app_secret,omitempty"`
  // 启用 RAM 认证
  AuthRamEnable *bool `json:"auth_ram_enable,omitempty" xml:"auth_ram_enable,omitempty"`
  // 数据 Hash 算法
  DataHashName *string `json:"data_hash_name,omitempty" xml:"data_hash_name,omitempty"`
  // Domain 描述
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // Domain 名称
  DomainName *string `json:"domain_name,omitempty" xml:"domain_name,omitempty"`
  // 事件通知 MNS 匹配文件名
  EventFilenameMatches *string `json:"event_filename_matches,omitempty" xml:"event_filename_matches,omitempty"`
  // 事件通知 MNS Endpoint
  EventMnsEndpoint *string `json:"event_mns_endpoint,omitempty" xml:"event_mns_endpoint,omitempty"`
  // 事件通知 MNS Topic
  EventMnsTopic *string `json:"event_mns_topic,omitempty" xml:"event_mns_topic,omitempty"`
  // 事件名列表
  EventNames []*string `json:"event_names,omitempty" xml:"event_names,omitempty" type:"Repeated"`
  // 事件通知 Role Arn
  EventRoleArn *string `json:"event_role_arn,omitempty" xml:"event_role_arn,omitempty"`
  // 开启自动初始化 Drive
  InitDriveEnable *bool `json:"init_drive_enable,omitempty" xml:"init_drive_enable,omitempty"`
  // 自动初始化 Drive 大小
  InitDriveSize *int64 `json:"init_drive_size,omitempty" xml:"init_drive_size,omitempty"`
  // 自动初始化 Drive 使用 Store ID
  InitDriveStoreId *string `json:"init_drive_store_id,omitempty" xml:"init_drive_store_id,omitempty"`
  PublishedAppAccessStrategy *AppAccessStrategy `json:"published_app_access_strategy,omitempty" xml:"published_app_access_strategy,omitempty"`
  // 开启分享
  Sharable *bool `json:"sharable,omitempty" xml:"sharable,omitempty"`
}

func (s UpdateDomainRequest) String() string {
  return tea.Prettify(s)
}

func (s UpdateDomainRequest) GoString() string {
  return s.String()
}

func (s *UpdateDomainRequest) SetHeaders(v map[string]*string) *UpdateDomainRequest {
  s.Headers = v
  return s
}

func (s *UpdateDomainRequest) SetAuthConfig(v map[string]interface{}) *UpdateDomainRequest {
  s.AuthConfig = v
  return s
}

func (s *UpdateDomainRequest) SetAuthDingdingAppId(v string) *UpdateDomainRequest {
  s.AuthDingdingAppId = &v
  return s
}

func (s *UpdateDomainRequest) SetAuthDingdingAppSecret(v string) *UpdateDomainRequest {
  s.AuthDingdingAppSecret = &v
  return s
}

func (s *UpdateDomainRequest) SetAuthDingdingEnable(v bool) *UpdateDomainRequest {
  s.AuthDingdingEnable = &v
  return s
}

func (s *UpdateDomainRequest) SetAuthEndpointEnable(v bool) *UpdateDomainRequest {
  s.AuthEndpointEnable = &v
  return s
}

func (s *UpdateDomainRequest) SetAuthRamAppId(v string) *UpdateDomainRequest {
  s.AuthRamAppId = &v
  return s
}

func (s *UpdateDomainRequest) SetAuthRamAppSecret(v string) *UpdateDomainRequest {
  s.AuthRamAppSecret = &v
  return s
}

func (s *UpdateDomainRequest) SetAuthRamEnable(v bool) *UpdateDomainRequest {
  s.AuthRamEnable = &v
  return s
}

func (s *UpdateDomainRequest) SetDataHashName(v string) *UpdateDomainRequest {
  s.DataHashName = &v
  return s
}

func (s *UpdateDomainRequest) SetDescription(v string) *UpdateDomainRequest {
  s.Description = &v
  return s
}

func (s *UpdateDomainRequest) SetDomainId(v string) *UpdateDomainRequest {
  s.DomainId = &v
  return s
}

func (s *UpdateDomainRequest) SetDomainName(v string) *UpdateDomainRequest {
  s.DomainName = &v
  return s
}

func (s *UpdateDomainRequest) SetEventFilenameMatches(v string) *UpdateDomainRequest {
  s.EventFilenameMatches = &v
  return s
}

func (s *UpdateDomainRequest) SetEventMnsEndpoint(v string) *UpdateDomainRequest {
  s.EventMnsEndpoint = &v
  return s
}

func (s *UpdateDomainRequest) SetEventMnsTopic(v string) *UpdateDomainRequest {
  s.EventMnsTopic = &v
  return s
}

func (s *UpdateDomainRequest) SetEventNames(v []*string) *UpdateDomainRequest {
  s.EventNames = v
  return s
}

func (s *UpdateDomainRequest) SetEventRoleArn(v string) *UpdateDomainRequest {
  s.EventRoleArn = &v
  return s
}

func (s *UpdateDomainRequest) SetInitDriveEnable(v bool) *UpdateDomainRequest {
  s.InitDriveEnable = &v
  return s
}

func (s *UpdateDomainRequest) SetInitDriveSize(v int64) *UpdateDomainRequest {
  s.InitDriveSize = &v
  return s
}

func (s *UpdateDomainRequest) SetInitDriveStoreId(v string) *UpdateDomainRequest {
  s.InitDriveStoreId = &v
  return s
}

func (s *UpdateDomainRequest) SetPublishedAppAccessStrategy(v *AppAccessStrategy) *UpdateDomainRequest {
  s.PublishedAppAccessStrategy = v
  return s
}

func (s *UpdateDomainRequest) SetSharable(v bool) *UpdateDomainRequest {
  s.Sharable = &v
  return s
}

/**
 * create domain response
 */
type UpdateDomainResponse struct {
  // Domain APICName
  ApiCname *string `json:"api_cname,omitempty" xml:"api_cname,omitempty"`
  // Domain AppCName
  AppCname *string `json:"app_cname,omitempty" xml:"app_cname,omitempty"`
  // 支付宝 App Id
  AuthAlipayAppId *string `json:"auth_alipay_app_id,omitempty" xml:"auth_alipay_app_id,omitempty"`
  // 是否开启了支付宝认证
  AuthAlipayEnable *bool `json:"auth_alipay_enable,omitempty" xml:"auth_alipay_enable,omitempty"`
  // 支付宝 App Secret
  AuthAlipayPrivateKey *string `json:"auth_alipay_private_key,omitempty" xml:"auth_alipay_private_key,omitempty"`
  // Domain AuthCName
  AuthCname *string `json:"auth_cname,omitempty" xml:"auth_cname,omitempty"`
  // 登录相关信息
  AuthConfig map[string]interface{} `json:"auth_config,omitempty" xml:"auth_config,omitempty"`
  // 钉钉 App Id
  AuthDingdingAppId *string `json:"auth_dingding_app_id,omitempty" xml:"auth_dingding_app_id,omitempty"`
  // 钉钉 App Secret
  AuthDingdingAppSecret *string `json:"auth_dingding_app_secret,omitempty" xml:"auth_dingding_app_secret,omitempty"`
  // 是否开启了钉钉认证
  AuthDingdingEnable *bool `json:"auth_dingding_enable,omitempty" xml:"auth_dingding_enable,omitempty"`
  AuthEndpointEnable *bool `json:"auth_endpoint_enable,omitempty" xml:"auth_endpoint_enable,omitempty"`
  // RAM App Id
  AuthRamAppId *string `json:"auth_ram_app_id,omitempty" xml:"auth_ram_app_id,omitempty"`
  // RAM App Secret
  AuthRamAppSecret *string `json:"auth_ram_app_secret,omitempty" xml:"auth_ram_app_secret,omitempty"`
  // 是否开启了 RAM 认证
  AuthRamEnable *bool `json:"auth_ram_enable,omitempty" xml:"auth_ram_enable,omitempty"`
  // Domain 创建时间
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // 数据 Hash 算法
  DataHashName *string `json:"data_hash_name,omitempty" xml:"data_hash_name,omitempty"`
  // Domain 描述
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // Domain 描述
  DomainName *string `json:"domain_name,omitempty" xml:"domain_name,omitempty"`
  // 事件通知 MNS 匹配文件名
  EventFilenameMatches *string `json:"event_filename_matches,omitempty" xml:"event_filename_matches,omitempty"`
  // 事件通知 MNS Endpoint
  EventMnsEndpoint *string `json:"event_mns_endpoint,omitempty" xml:"event_mns_endpoint,omitempty"`
  // 事件通知 MNS Topic
  EventMnsTopic *string `json:"event_mns_topic,omitempty" xml:"event_mns_topic,omitempty"`
  // 事件名列表
  EventNames []*string `json:"event_names,omitempty" xml:"event_names,omitempty" type:"Repeated"`
  // 事件通知 Role Arn
  EventRoleArn *string `json:"event_role_arn,omitempty" xml:"event_role_arn,omitempty"`
  // 是否开启了自动初始化 Drive
  InitDriveEnable *bool `json:"init_drive_enable,omitempty" xml:"init_drive_enable,omitempty"`
  // 自动初始化 Drive 大小
  InitDriveSize *int64 `json:"init_drive_size,omitempty" xml:"init_drive_size,omitempty"`
  // 自动初始化 Drive 所用 Store ID
  InitDriveStoreId *string `json:"init_drive_store_id,omitempty" xml:"init_drive_store_id,omitempty"`
  // Domain 类型
  Mode *string `json:"mode,omitempty" xml:"mode,omitempty"`
  // Domain 类型
  PathType *string `json:"path_type,omitempty" xml:"path_type,omitempty"`
  PublishedAppAccessStrategy *AppAccessStrategy `json:"published_app_access_strategy,omitempty" xml:"published_app_access_strategy,omitempty"`
  // 是否开启了分享
  Sharable *bool `json:"sharable,omitempty" xml:"sharable,omitempty"`
  // 存储级别
  StoreLevel *string `json:"store_level,omitempty" xml:"store_level,omitempty"`
  // 存储 Region 列表
  StoreRegionList []*string `json:"store_region_list,omitempty" xml:"store_region_list,omitempty" type:"Repeated"`
  // Domain 更新时间
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s UpdateDomainResponse) String() string {
  return tea.Prettify(s)
}

func (s UpdateDomainResponse) GoString() string {
  return s.String()
}

func (s *UpdateDomainResponse) SetApiCname(v string) *UpdateDomainResponse {
  s.ApiCname = &v
  return s
}

func (s *UpdateDomainResponse) SetAppCname(v string) *UpdateDomainResponse {
  s.AppCname = &v
  return s
}

func (s *UpdateDomainResponse) SetAuthAlipayAppId(v string) *UpdateDomainResponse {
  s.AuthAlipayAppId = &v
  return s
}

func (s *UpdateDomainResponse) SetAuthAlipayEnable(v bool) *UpdateDomainResponse {
  s.AuthAlipayEnable = &v
  return s
}

func (s *UpdateDomainResponse) SetAuthAlipayPrivateKey(v string) *UpdateDomainResponse {
  s.AuthAlipayPrivateKey = &v
  return s
}

func (s *UpdateDomainResponse) SetAuthCname(v string) *UpdateDomainResponse {
  s.AuthCname = &v
  return s
}

func (s *UpdateDomainResponse) SetAuthConfig(v map[string]interface{}) *UpdateDomainResponse {
  s.AuthConfig = v
  return s
}

func (s *UpdateDomainResponse) SetAuthDingdingAppId(v string) *UpdateDomainResponse {
  s.AuthDingdingAppId = &v
  return s
}

func (s *UpdateDomainResponse) SetAuthDingdingAppSecret(v string) *UpdateDomainResponse {
  s.AuthDingdingAppSecret = &v
  return s
}

func (s *UpdateDomainResponse) SetAuthDingdingEnable(v bool) *UpdateDomainResponse {
  s.AuthDingdingEnable = &v
  return s
}

func (s *UpdateDomainResponse) SetAuthEndpointEnable(v bool) *UpdateDomainResponse {
  s.AuthEndpointEnable = &v
  return s
}

func (s *UpdateDomainResponse) SetAuthRamAppId(v string) *UpdateDomainResponse {
  s.AuthRamAppId = &v
  return s
}

func (s *UpdateDomainResponse) SetAuthRamAppSecret(v string) *UpdateDomainResponse {
  s.AuthRamAppSecret = &v
  return s
}

func (s *UpdateDomainResponse) SetAuthRamEnable(v bool) *UpdateDomainResponse {
  s.AuthRamEnable = &v
  return s
}

func (s *UpdateDomainResponse) SetCreatedAt(v string) *UpdateDomainResponse {
  s.CreatedAt = &v
  return s
}

func (s *UpdateDomainResponse) SetDataHashName(v string) *UpdateDomainResponse {
  s.DataHashName = &v
  return s
}

func (s *UpdateDomainResponse) SetDescription(v string) *UpdateDomainResponse {
  s.Description = &v
  return s
}

func (s *UpdateDomainResponse) SetDomainId(v string) *UpdateDomainResponse {
  s.DomainId = &v
  return s
}

func (s *UpdateDomainResponse) SetDomainName(v string) *UpdateDomainResponse {
  s.DomainName = &v
  return s
}

func (s *UpdateDomainResponse) SetEventFilenameMatches(v string) *UpdateDomainResponse {
  s.EventFilenameMatches = &v
  return s
}

func (s *UpdateDomainResponse) SetEventMnsEndpoint(v string) *UpdateDomainResponse {
  s.EventMnsEndpoint = &v
  return s
}

func (s *UpdateDomainResponse) SetEventMnsTopic(v string) *UpdateDomainResponse {
  s.EventMnsTopic = &v
  return s
}

func (s *UpdateDomainResponse) SetEventNames(v []*string) *UpdateDomainResponse {
  s.EventNames = v
  return s
}

func (s *UpdateDomainResponse) SetEventRoleArn(v string) *UpdateDomainResponse {
  s.EventRoleArn = &v
  return s
}

func (s *UpdateDomainResponse) SetInitDriveEnable(v bool) *UpdateDomainResponse {
  s.InitDriveEnable = &v
  return s
}

func (s *UpdateDomainResponse) SetInitDriveSize(v int64) *UpdateDomainResponse {
  s.InitDriveSize = &v
  return s
}

func (s *UpdateDomainResponse) SetInitDriveStoreId(v string) *UpdateDomainResponse {
  s.InitDriveStoreId = &v
  return s
}

func (s *UpdateDomainResponse) SetMode(v string) *UpdateDomainResponse {
  s.Mode = &v
  return s
}

func (s *UpdateDomainResponse) SetPathType(v string) *UpdateDomainResponse {
  s.PathType = &v
  return s
}

func (s *UpdateDomainResponse) SetPublishedAppAccessStrategy(v *AppAccessStrategy) *UpdateDomainResponse {
  s.PublishedAppAccessStrategy = v
  return s
}

func (s *UpdateDomainResponse) SetSharable(v bool) *UpdateDomainResponse {
  s.Sharable = &v
  return s
}

func (s *UpdateDomainResponse) SetStoreLevel(v string) *UpdateDomainResponse {
  s.StoreLevel = &v
  return s
}

func (s *UpdateDomainResponse) SetStoreRegionList(v []*string) *UpdateDomainResponse {
  s.StoreRegionList = v
  return s
}

func (s *UpdateDomainResponse) SetUpdatedAt(v string) *UpdateDomainResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * 
 */
type UserAuthentication struct {
  // 认证类型
  AuthenticationType *string `json:"AuthenticationType,omitempty" xml:"AuthenticationType,omitempty" require:"true"`
  // 创建时间
  CreatedAt *int64 `json:"CreatedAt,omitempty" xml:"CreatedAt,omitempty" require:"true"`
  // 详情
  Detail *string `json:"Detail,omitempty" xml:"Detail,omitempty" require:"true"`
  // Domain ID
  DomainID *string `json:"DomainID,omitempty" xml:"DomainID,omitempty" require:"true"`
  // 唯一身份标识
  Identity *string `json:"Identity,omitempty" xml:"Identity,omitempty" require:"true"`
  // 最后登录时间
  LastLoginTime *int64 `json:"LastLoginTime,omitempty" xml:"LastLoginTime,omitempty" require:"true"`
  // 状态
  Status *string `json:"Status,omitempty" xml:"Status,omitempty" require:"true"`
  // 用户ID
  UserID *string `json:"UserID,omitempty" xml:"UserID,omitempty" require:"true"`
  // 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
  Extra *string `json:"extra,omitempty" xml:"extra,omitempty"`
}

func (s UserAuthentication) String() string {
  return tea.Prettify(s)
}

func (s UserAuthentication) GoString() string {
  return s.String()
}

func (s *UserAuthentication) SetAuthenticationType(v string) *UserAuthentication {
  s.AuthenticationType = &v
  return s
}

func (s *UserAuthentication) SetCreatedAt(v int64) *UserAuthentication {
  s.CreatedAt = &v
  return s
}

func (s *UserAuthentication) SetDetail(v string) *UserAuthentication {
  s.Detail = &v
  return s
}

func (s *UserAuthentication) SetDomainID(v string) *UserAuthentication {
  s.DomainID = &v
  return s
}

func (s *UserAuthentication) SetIdentity(v string) *UserAuthentication {
  s.Identity = &v
  return s
}

func (s *UserAuthentication) SetLastLoginTime(v int64) *UserAuthentication {
  s.LastLoginTime = &v
  return s
}

func (s *UserAuthentication) SetStatus(v string) *UserAuthentication {
  s.Status = &v
  return s
}

func (s *UserAuthentication) SetUserID(v string) *UserAuthentication {
  s.UserID = &v
  return s
}

func (s *UserAuthentication) SetExtra(v string) *UserAuthentication {
  s.Extra = &v
  return s
}

type Client struct {
  Region  *string
  Endpoint  *string
  Protocol  *string
  Nickname  *string
  UserAgent  *string
  Credential  credential.Credential
}

func NewClient(config *Config)(*Client, error) {
  client := new(Client)
  err := client.Init(config)
  return client, err
}

func (client *Client)Init(config *Config)(_err error) {
  if tea.BoolValue(util.IsUnset(tea.ToMap(config))) {
    _err = tea.NewSDKError(map[string]interface{}{
      "name": "ParameterMissing",
      "message": "'config' can not be unset",
    })
    return _err
  }

  _err = util.ValidateModel(config)
  if _err != nil {
    return _err
  }
  if !tea.BoolValue(util.Empty(config.AccessKeyId)) {
    if tea.BoolValue(util.Empty(config.Type)) {
      config.Type = tea.String("access_key")
    }

    credentialConfig := &credential.Config{
      AccessKeyId: config.AccessKeyId,
      Type: config.Type,
      AccessKeySecret: config.AccessKeySecret,
      SecurityToken: config.SecurityToken,
    }
    client.Credential, _err = credential.NewCredential(credentialConfig)
    if _err != nil {
      return _err
    }

  }

  client.Endpoint = config.Endpoint
  client.Protocol = config.Protocol
  client.UserAgent = config.UserAgent
  client.Nickname = config.Nickname
  client.Region = config.Region
  return nil
}


/**
 * 创建App
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) CreateAppEx(request *CreateAppRequest, runtime *RuntimeOptions) (_result *CreateAppModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &CreateAppModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*CreateAppModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/app/create"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(201))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &CreateAppModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 删除App
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) DeleteAppEx(request *DeleteAppRequest, runtime *RuntimeOptions) (_result *DeleteAppModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &DeleteAppModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*DeleteAppModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/app/delete"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(204))) {
        _result = &DeleteAppModel{}
        _err = tea.Convert(map[string]map[string]*string{
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 查询App
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetAppEx(request *GetAppRequest, runtime *RuntimeOptions) (_result *GetAppModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &GetAppModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*GetAppModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/app/get"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &GetAppModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 查询App设置的公钥
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetPublicKeyEx(request *GetAppPublicKeyRequest, runtime *RuntimeOptions) (_result *GetPublicKeyModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &GetPublicKeyModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*GetPublicKeyModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/app/get_public_key"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &GetPublicKeyModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 查询App列表
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) ListAppEx(request *ListAppsRequest, runtime *RuntimeOptions) (_result *ListAppModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &ListAppModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*ListAppModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/app/list"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &ListAppModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 查询已发布的App列表
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) ListPublishedAppEx(request *ListAppsRequest, runtime *RuntimeOptions) (_result *ListPublishedAppModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &ListPublishedAppModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*ListPublishedAppModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/app/list_published"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &ListPublishedAppModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 设置App公钥
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetPublicKeyEx(request *SetAppPublicKeyRequest, runtime *RuntimeOptions) (_result *SetPublicKeyModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &SetPublicKeyModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*SetPublicKeyModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/app/set_public_key"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(204))) {
        _result = &SetPublicKeyModel{}
        _err = tea.Convert(map[string]map[string]*string{
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 修改App
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) UpdateAppEx(request *UpdateAppRequest, runtime *RuntimeOptions) (_result *UpdateAppModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &UpdateAppModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*UpdateAppModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/app/update"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &UpdateAppModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 添加Store
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) AddStoreEx(request *AddStoreRequest, runtime *RuntimeOptions) (_result *AddStoreModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &AddStoreModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*AddStoreModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/add_store"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &AddStoreModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 创建 Domain
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CreateDomainEx(request *CreateDomainRequest, runtime *RuntimeOptions) (_result *CreateDomainModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &CreateDomainModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*CreateDomainModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/create"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &CreateDomainModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 删除domain业务面自定义域名的证书
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) DeleteBizCnameCertEx(request *DeleteBizCNameCertRequest, runtime *RuntimeOptions) (_result *DeleteBizCnameCertModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &DeleteBizCnameCertModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*DeleteBizCnameCertModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/del_biz_cname_cert"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        _result = &DeleteBizCnameCertModel{}
        _err = tea.Convert(map[string]map[string]*string{
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 删除 Domain
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) DeleteDomainEx(request *DeleteDomainRequest, runtime *RuntimeOptions) (_result *DeleteDomainModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &DeleteDomainModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*DeleteDomainModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/delete"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(204))) {
        _result = &DeleteDomainModel{}
        _err = tea.Convert(map[string]map[string]*string{
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 删除domain业务面自定义域名和证书
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) DeleteBizCnameAndCertEx(request *DeleteBizCNameAndCertRequest, runtime *RuntimeOptions) (_result *DeleteBizCnameAndCertModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &DeleteBizCnameAndCertModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*DeleteBizCnameAndCertModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/delete_biz_cname_and_cert"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        _result = &DeleteBizCnameAndCertModel{}
        _err = tea.Convert(map[string]map[string]*string{
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 删除domain数据面自定义域名和证书
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) DeleteDataCnameAndCertEx(request *DeleteDataCNameAndCertRequest, runtime *RuntimeOptions) (_result *DeleteDataCnameAndCertModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &DeleteDataCnameAndCertModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*DeleteDataCnameAndCertModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/delete_data_cname_and_cert"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        _result = &DeleteDataCnameAndCertModel{}
        _err = tea.Convert(map[string]map[string]*string{
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 获取 Domain
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetDomainEx(request *GetDomainRequest, runtime *RuntimeOptions) (_result *GetDomainModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &GetDomainModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*GetDomainModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/get"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &GetDomainModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 获取domain业务面自定义域名信息
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetBizCnameInfoEx(request *GetBizCNameInfoRequest, runtime *RuntimeOptions) (_result *GetBizCnameInfoModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &GetBizCnameInfoModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*GetBizCnameInfoModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/get_biz_cname_info"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &GetBizCnameInfoModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 获取 domain 跨域规则列表
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetCorsRuleListEx(request *GetCorsRuleListRequest, runtime *RuntimeOptions) (_result *GetCorsRuleListModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &GetCorsRuleListModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*GetCorsRuleListModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/get_cors_rules"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &GetCorsRuleListModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 获取domain数据面自定义域名信息
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetDataCnameInfoEx(request *GetDataCNameInfoRequest, runtime *RuntimeOptions) (_result *GetDataCnameInfoModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &GetDataCnameInfoModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*GetDataCnameInfoModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/get_data_cname_info"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &GetDataCnameInfoModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 列举 Domain
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error undefined undefined
 */
func (client *Client) ListDomainEx(request *ListDomainsRequest, runtime *RuntimeOptions) (_result *ListDomainModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &ListDomainModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*ListDomainModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/list"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &ListDomainModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 查询Store列表
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) ListStoresEx(request *ListStoresRequest, runtime *RuntimeOptions) (_result *ListStoresModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &ListStoresModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*ListStoresModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/list_stores"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &ListStoresModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 移除Store
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) RemoveStoreEx(request *RemoveStoreRequest, runtime *RuntimeOptions) (_result *RemoveStoreModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &RemoveStoreModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*RemoveStoreModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/remove_store"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(204))) {
        _result = &RemoveStoreModel{}
        _err = tea.Convert(map[string]map[string]*string{
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 设置domain业务面cname
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetBizCnameEx(request *SetBizCNameRequest, runtime *RuntimeOptions) (_result *SetBizCnameModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &SetBizCnameModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*SetBizCnameModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/set_biz_cname"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &SetBizCnameModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 设置domain业务面自定义域名的证书
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetBizCnameCertEx(request *SetBizCNameCertRequest, runtime *RuntimeOptions) (_result *SetBizCnameCertModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &SetBizCnameCertModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*SetBizCnameCertModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/set_biz_cname_cert"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &SetBizCnameCertModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 增加 domain 跨域规则
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetCorsRuleListEx(request *SetCorsRuleListRequest, runtime *RuntimeOptions) (_result *SetCorsRuleListModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &SetCorsRuleListModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*SetCorsRuleListModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/set_cors_rules"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &SetCorsRuleListModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 设置domain数据面cname
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetDataCnameEx(request *SetDataCNameRequest, runtime *RuntimeOptions) (_result *SetDataCnameModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &SetDataCnameModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*SetDataCnameModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/set_data_cname"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &SetDataCnameModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}

/**
 * 更新 Domain
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) UpdateDomainEx(request *UpdateDomainRequest, runtime *RuntimeOptions) (_result *UpdateDomainModel, _err error) {
  _err = tea.Validate(request)
  if _err != nil {
    return _result, _err
  }
  _err = tea.Validate(runtime)
  if _err != nil {
    return _result, _err
  }
  _runtime := map[string]interface{}{
    "timeouted": "retry",
    "readTimeout": tea.IntValue(runtime.ReadTimeout),
    "connectTimeout": tea.IntValue(runtime.ConnectTimeout),
    "localAddr": tea.StringValue(runtime.LocalAddr),
    "httpProxy": tea.StringValue(runtime.HttpProxy),
    "httpsProxy": tea.StringValue(runtime.HttpsProxy),
    "noProxy": tea.StringValue(runtime.NoProxy),
    "maxIdleConns": tea.IntValue(runtime.MaxIdleConns),
    "socks5Proxy": tea.StringValue(runtime.Socks5Proxy),
    "socks5NetWork": tea.StringValue(runtime.Socks5NetWork),
    "retry": map[string]interface{}{
      "retryable": tea.BoolValue(runtime.Autoretry),
      "maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
    },
    "backoff": map[string]interface{}{
      "policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
      "period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
    },
    "ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
  }

  _resp := &UpdateDomainModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*UpdateDomainModel, error){
      request_ := tea.NewRequest()
      accesskeyId, _err := client.GetAccessKeyId()
      if _err != nil {
        return _result, _err
      }

      accessKeySecret, _err := client.GetAccessKeySecret()
      if _err != nil {
        return _result, _err
      }

      securityToken, _err := client.GetSecurityToken()
      if _err != nil {
        return _result, _err
      }

      realReq := util.ToMap(request)
      request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
      request_.Method = tea.String("POST")
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/update"))
      request_.Headers = tea.Merge(map[string]*string{
        "user-agent": client.GetUserAgent(),
        "host": util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.Region) + ".admin.aliyunpds.com")),
        "content-type": tea.String("application/json; charset=utf-8"),
        },request.Headers)
      realReq["headers"] = nil
      if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
        if !tea.BoolValue(util.Empty(securityToken)) {
          request_.Headers["x-acs-security-token"] = securityToken
        }

        request_.Headers["date"] = util.GetDateUTCString()
        request_.Headers["accept"] = tea.String("application/json")
        request_.Headers["x-acs-signature-method"] = tea.String("HMAC-SHA1")
        request_.Headers["x-acs-signature-version"] = tea.String("1.0")
        stringToSign := roautil.GetStringToSign(request_)
        request_.Headers["authorization"] = tea.String("acs " + tea.StringValue(accesskeyId) + ":" + tea.StringValue(roautil.GetSignature(stringToSign, accessKeySecret)))
      }

      request_.Body = tea.ToReader(util.ToJSONString(realReq))
      response_, _err := tea.DoRequest(request_, _runtime)
      if _err != nil {
        return _result, _err
      }
      var respMap map[string]interface{}
      var obj interface{}
      if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(200))) {
        obj, _err = util.ReadAsJSON(response_.Body)
        if _err != nil {
          return _result, _err
        }

        respMap = util.AssertAsMap(obj)
        _result = &UpdateDomainModel{}
        _err = tea.Convert(map[string]interface{}{
          "body": respMap,
          "headers": response_.Headers,
        }, &_result)
        return _result, _err
      }

      if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
        _err = tea.NewSDKError(map[string]interface{}{
          "data": map[string]interface{}{
            "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
            "statusCode": tea.IntValue(response_.StatusCode),
            "statusMessage": tea.StringValue(response_.StatusMessage),
          },
          "message": tea.StringValue(response_.Headers["x-ca-error-message"]),
        })
        return _result, _err
      }

      obj, _err = util.ReadAsJSON(response_.Body)
      if _err != nil {
        return _result, _err
      }

      respMap = util.AssertAsMap(obj)
      _err = tea.NewSDKError(tea.ToMap(map[string]interface{}{
        "data": map[string]interface{}{
          "requestId": tea.StringValue(response_.Headers["x-ca-request-id"]),
          "statusCode": tea.IntValue(response_.StatusCode),
          "statusMessage": tea.StringValue(response_.StatusMessage),
        },
        },respMap))
      return _result, _err
    }()
    if !tea.BoolValue(tea.Retryable(_err)) {
      break
    }
  }

  return _resp, _err
}


/**
 * 创建App
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) CreateApp (request *CreateAppRequest) (_result *CreateAppModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &CreateAppModel{}
  _body, _err := client.CreateAppEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 删除App
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) DeleteApp (request *DeleteAppRequest) (_result *DeleteAppModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &DeleteAppModel{}
  _body, _err := client.DeleteAppEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 查询App
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetApp (request *GetAppRequest) (_result *GetAppModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &GetAppModel{}
  _body, _err := client.GetAppEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 查询App设置的公钥
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetPublicKey (request *GetAppPublicKeyRequest) (_result *GetPublicKeyModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &GetPublicKeyModel{}
  _body, _err := client.GetPublicKeyEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 查询App列表
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) ListApp (request *ListAppsRequest) (_result *ListAppModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &ListAppModel{}
  _body, _err := client.ListAppEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 查询已发布的App列表
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) ListPublishedApp (request *ListAppsRequest) (_result *ListPublishedAppModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &ListPublishedAppModel{}
  _body, _err := client.ListPublishedAppEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 设置App公钥
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetPublicKey (request *SetAppPublicKeyRequest) (_result *SetPublicKeyModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &SetPublicKeyModel{}
  _body, _err := client.SetPublicKeyEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 修改App
 * @tags app
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) UpdateApp (request *UpdateAppRequest) (_result *UpdateAppModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &UpdateAppModel{}
  _body, _err := client.UpdateAppEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 添加Store
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) AddStore (request *AddStoreRequest) (_result *AddStoreModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &AddStoreModel{}
  _body, _err := client.AddStoreEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 创建 Domain
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CreateDomain (request *CreateDomainRequest) (_result *CreateDomainModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &CreateDomainModel{}
  _body, _err := client.CreateDomainEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 删除domain业务面自定义域名的证书
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) DeleteBizCnameCert (request *DeleteBizCNameCertRequest) (_result *DeleteBizCnameCertModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &DeleteBizCnameCertModel{}
  _body, _err := client.DeleteBizCnameCertEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 删除 Domain
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) DeleteDomain (request *DeleteDomainRequest) (_result *DeleteDomainModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &DeleteDomainModel{}
  _body, _err := client.DeleteDomainEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 删除domain业务面自定义域名和证书
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) DeleteBizCnameAndCert (request *DeleteBizCNameAndCertRequest) (_result *DeleteBizCnameAndCertModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &DeleteBizCnameAndCertModel{}
  _body, _err := client.DeleteBizCnameAndCertEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 删除domain数据面自定义域名和证书
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) DeleteDataCnameAndCert (request *DeleteDataCNameAndCertRequest) (_result *DeleteDataCnameAndCertModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &DeleteDataCnameAndCertModel{}
  _body, _err := client.DeleteDataCnameAndCertEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 获取 Domain
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetDomain (request *GetDomainRequest) (_result *GetDomainModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &GetDomainModel{}
  _body, _err := client.GetDomainEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 获取domain业务面自定义域名信息
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetBizCnameInfo (request *GetBizCNameInfoRequest) (_result *GetBizCnameInfoModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &GetBizCnameInfoModel{}
  _body, _err := client.GetBizCnameInfoEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 获取 domain 跨域规则列表
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetCorsRuleList (request *GetCorsRuleListRequest) (_result *GetCorsRuleListModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &GetCorsRuleListModel{}
  _body, _err := client.GetCorsRuleListEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 获取domain数据面自定义域名信息
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetDataCnameInfo (request *GetDataCNameInfoRequest) (_result *GetDataCnameInfoModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &GetDataCnameInfoModel{}
  _body, _err := client.GetDataCnameInfoEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 列举 Domain
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error undefined undefined
 */
func (client *Client) ListDomain (request *ListDomainsRequest) (_result *ListDomainModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &ListDomainModel{}
  _body, _err := client.ListDomainEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 查询Store列表
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) ListStores (request *ListStoresRequest) (_result *ListStoresModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &ListStoresModel{}
  _body, _err := client.ListStoresEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 移除Store
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) RemoveStore (request *RemoveStoreRequest) (_result *RemoveStoreModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &RemoveStoreModel{}
  _body, _err := client.RemoveStoreEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 设置domain业务面cname
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetBizCname (request *SetBizCNameRequest) (_result *SetBizCnameModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &SetBizCnameModel{}
  _body, _err := client.SetBizCnameEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 设置domain业务面自定义域名的证书
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetBizCnameCert (request *SetBizCNameCertRequest) (_result *SetBizCnameCertModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &SetBizCnameCertModel{}
  _body, _err := client.SetBizCnameCertEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 增加 domain 跨域规则
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetCorsRuleList (request *SetCorsRuleListRequest) (_result *SetCorsRuleListModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &SetCorsRuleListModel{}
  _body, _err := client.SetCorsRuleListEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 设置domain数据面cname
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetDataCname (request *SetDataCNameRequest) (_result *SetDataCnameModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &SetDataCnameModel{}
  _body, _err := client.SetDataCnameEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 更新 Domain
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) UpdateDomain (request *UpdateDomainRequest) (_result *UpdateDomainModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &UpdateDomainModel{}
  _body, _err := client.UpdateDomainEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

func (client *Client) GetPathname (nickname *string, path *string) (_result *string) {
  if tea.BoolValue(util.Empty(nickname)) {
    _result = path
    return _result
  }

  _result = tea.String("/" + tea.StringValue(nickname) + tea.StringValue(path))
  return _result
}

func (client *Client) SetUserAgent (userAgent *string) {
  client.UserAgent = userAgent
}

func (client *Client) AppendUserAgent (userAgent *string) {
  client.UserAgent = tea.String(tea.StringValue(client.UserAgent) + " " + tea.StringValue(userAgent))
}

func (client *Client) GetUserAgent () (_result *string) {
  userAgent := util.GetUserAgent(client.UserAgent)
  _result = userAgent
  return _result
}

func (client *Client) GetAccessKeyId () (_result *string, _err error) {
  if tea.BoolValue(util.IsUnset(client.Credential)) {
    _result = tea.String("")
    return _result, _err
  }

  accessKeyId, _err := client.Credential.GetAccessKeyId()
  if _err != nil {
    return _result, _err
  }

  _result = accessKeyId
  return _result , _err
}

func (client *Client) GetAccessKeySecret () (_result *string, _err error) {
  if tea.BoolValue(util.IsUnset(client.Credential)) {
    _result = tea.String("")
    return _result, _err
  }

  secret, _err := client.Credential.GetAccessKeySecret()
  if _err != nil {
    return _result, _err
  }

  _result = secret
  return _result , _err
}

func (client *Client) GetSecurityToken () (_result *string, _err error) {
  if tea.BoolValue(util.IsUnset(client.Credential)) {
    _result = tea.String("")
    return _result, _err
  }

  token, _err := client.Credential.GetSecurityToken()
  if _err != nil {
    return _result, _err
  }

  _result = token
  return _result , _err
}

