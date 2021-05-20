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

type ListIdentityBenefitPkgModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *ListIdentityBenefitPkgResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ListIdentityBenefitPkgModel) String() string {
  return tea.Prettify(s)
}

func (s ListIdentityBenefitPkgModel) GoString() string {
  return s.String()
}

func (s *ListIdentityBenefitPkgModel) SetHeaders(v map[string]*string) *ListIdentityBenefitPkgModel {
  s.Headers = v
  return s
}

func (s *ListIdentityBenefitPkgModel) SetBody(v *ListIdentityBenefitPkgResponse) *ListIdentityBenefitPkgModel {
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

type SearchModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *ListDomainsResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s SearchModel) String() string {
  return tea.Prettify(s)
}

func (s SearchModel) GoString() string {
  return s.String()
}

func (s *SearchModel) SetHeaders(v map[string]*string) *SearchModel {
  s.Headers = v
  return s
}

func (s *SearchModel) SetBody(v *ListDomainsResponse) *SearchModel {
  s.Body = v
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

type SetShareLinkStatusModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *BaseDomainResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s SetShareLinkStatusModel) String() string {
  return tea.Prettify(s)
}

func (s SetShareLinkStatusModel) GoString() string {
  return s.String()
}

func (s *SetShareLinkStatusModel) SetHeaders(v map[string]*string) *SetShareLinkStatusModel {
  s.Headers = v
  return s
}

func (s *SetShareLinkStatusModel) SetBody(v *BaseDomainResponse) *SetShareLinkStatusModel {
  s.Body = v
  return s
}

type SetShareStatusModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *BaseDomainResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s SetShareStatusModel) String() string {
  return tea.Prettify(s)
}

func (s SetShareStatusModel) GoString() string {
  return s.String()
}

func (s *SetShareStatusModel) SetHeaders(v map[string]*string) *SetShareStatusModel {
  s.Headers = v
  return s
}

func (s *SetShareStatusModel) SetBody(v *BaseDomainResponse) *SetShareStatusModel {
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

type UpdateNameModel struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  Body *GetDomainResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s UpdateNameModel) String() string {
  return tea.Prettify(s)
}

func (s UpdateNameModel) GoString() string {
  return s.String()
}

func (s *UpdateNameModel) SetHeaders(v map[string]*string) *UpdateNameModel {
  s.Headers = v
  return s
}

func (s *UpdateNameModel) SetBody(v *GetDomainResponse) *UpdateNameModel {
  s.Body = v
  return s
}

/**
 * 
 */
type AccountAccessTokenResponse struct {
  // 用于调用业务接口的accessToken
  AccessToken *string `json:"access_token,omitempty" xml:"access_token,omitempty" require:"true"`
  // 当前用户头像
  Avatar *string `json:"avatar,omitempty" xml:"avatar,omitempty"`
  // Default Drive ID
  DefaultDriveId *string `json:"default_drive_id,omitempty" xml:"default_drive_id,omitempty"`
  // Default Sbox Drive ID
  DefaultSboxDriveId *string `json:"default_sbox_drive_id,omitempty" xml:"default_sbox_drive_id,omitempty"`
  // device_id 通过device flow 绑定的设备ID
  DeviceId *string `json:"device_id,omitempty" xml:"device_id,omitempty"`
  // device_name 通过device flow 绑定的设备名
  DeviceName *string `json:"device_name,omitempty" xml:"device_name,omitempty"`
  // 当前用户已存在的登录方式
  ExistLink []*LinkInfo `json:"exist_link,omitempty" xml:"exist_link,omitempty" type:"Repeated"`
  // accessToken过期时间，ISO时间
  ExpireTime *string `json:"expire_time,omitempty" xml:"expire_time,omitempty"`
  // accessToken过期时间，单位秒
  ExpiresIn *int64 `json:"expires_in,omitempty" xml:"expires_in,omitempty"`
  // 用户是否为第一次登录
  IsFirstLogin *bool `json:"is_first_login,omitempty" xml:"is_first_login,omitempty"`
  // 是否需要绑定
  NeedLink *bool `json:"need_link,omitempty" xml:"need_link,omitempty" require:"true"`
  // 用户是否需要进行的实人认证
  NeedRpVerify *bool `json:"need_rp_verify,omitempty" xml:"need_rp_verify,omitempty"`
  // 当前用户昵称
  NickName *string `json:"nick_name,omitempty" xml:"nick_name,omitempty"`
  // 用户的数据密码是否设置过
  PinSetup *bool `json:"pin_setup,omitempty" xml:"pin_setup,omitempty"`
  // 用于刷新accessToken
  RefreshToken *string `json:"refresh_token,omitempty" xml:"refresh_token,omitempty"`
  // 当前用户角色
  Role *string `json:"role,omitempty" xml:"role,omitempty"`
  // 临时权限，用于登录成功后设置密码
  State *string `json:"state,omitempty" xml:"state,omitempty"`
  // 当前用户状态
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // subdomain_id 用户登录的subdomain_id
  SubdomainId *string `json:"subdomain_id,omitempty" xml:"subdomain_id,omitempty"`
  // accessToken类型，Bearer
  TokenType *string `json:"token_type,omitempty" xml:"token_type,omitempty"`
  // 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
  UserData map[string]interface{} `json:"user_data,omitempty" xml:"user_data,omitempty"`
  // 当前用户ID
  UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty"`
  // 当前用户名
  UserName *string `json:"user_name,omitempty" xml:"user_name,omitempty"`
}

func (s AccountAccessTokenResponse) String() string {
  return tea.Prettify(s)
}

func (s AccountAccessTokenResponse) GoString() string {
  return s.String()
}

func (s *AccountAccessTokenResponse) SetAccessToken(v string) *AccountAccessTokenResponse {
  s.AccessToken = &v
  return s
}

func (s *AccountAccessTokenResponse) SetAvatar(v string) *AccountAccessTokenResponse {
  s.Avatar = &v
  return s
}

func (s *AccountAccessTokenResponse) SetDefaultDriveId(v string) *AccountAccessTokenResponse {
  s.DefaultDriveId = &v
  return s
}

func (s *AccountAccessTokenResponse) SetDefaultSboxDriveId(v string) *AccountAccessTokenResponse {
  s.DefaultSboxDriveId = &v
  return s
}

func (s *AccountAccessTokenResponse) SetDeviceId(v string) *AccountAccessTokenResponse {
  s.DeviceId = &v
  return s
}

func (s *AccountAccessTokenResponse) SetDeviceName(v string) *AccountAccessTokenResponse {
  s.DeviceName = &v
  return s
}

func (s *AccountAccessTokenResponse) SetExistLink(v []*LinkInfo) *AccountAccessTokenResponse {
  s.ExistLink = v
  return s
}

func (s *AccountAccessTokenResponse) SetExpireTime(v string) *AccountAccessTokenResponse {
  s.ExpireTime = &v
  return s
}

func (s *AccountAccessTokenResponse) SetExpiresIn(v int64) *AccountAccessTokenResponse {
  s.ExpiresIn = &v
  return s
}

func (s *AccountAccessTokenResponse) SetIsFirstLogin(v bool) *AccountAccessTokenResponse {
  s.IsFirstLogin = &v
  return s
}

func (s *AccountAccessTokenResponse) SetNeedLink(v bool) *AccountAccessTokenResponse {
  s.NeedLink = &v
  return s
}

func (s *AccountAccessTokenResponse) SetNeedRpVerify(v bool) *AccountAccessTokenResponse {
  s.NeedRpVerify = &v
  return s
}

func (s *AccountAccessTokenResponse) SetNickName(v string) *AccountAccessTokenResponse {
  s.NickName = &v
  return s
}

func (s *AccountAccessTokenResponse) SetPinSetup(v bool) *AccountAccessTokenResponse {
  s.PinSetup = &v
  return s
}

func (s *AccountAccessTokenResponse) SetRefreshToken(v string) *AccountAccessTokenResponse {
  s.RefreshToken = &v
  return s
}

func (s *AccountAccessTokenResponse) SetRole(v string) *AccountAccessTokenResponse {
  s.Role = &v
  return s
}

func (s *AccountAccessTokenResponse) SetState(v string) *AccountAccessTokenResponse {
  s.State = &v
  return s
}

func (s *AccountAccessTokenResponse) SetStatus(v string) *AccountAccessTokenResponse {
  s.Status = &v
  return s
}

func (s *AccountAccessTokenResponse) SetSubdomainId(v string) *AccountAccessTokenResponse {
  s.SubdomainId = &v
  return s
}

func (s *AccountAccessTokenResponse) SetTokenType(v string) *AccountAccessTokenResponse {
  s.TokenType = &v
  return s
}

func (s *AccountAccessTokenResponse) SetUserData(v map[string]interface{}) *AccountAccessTokenResponse {
  s.UserData = v
  return s
}

func (s *AccountAccessTokenResponse) SetUserId(v string) *AccountAccessTokenResponse {
  s.UserId = &v
  return s
}

func (s *AccountAccessTokenResponse) SetUserName(v string) *AccountAccessTokenResponse {
  s.UserName = &v
  return s
}

/**
 * 
 */
type ActionDetail struct {
  Create *CreateDetail `json:"create,omitempty" xml:"create,omitempty"`
  Delete *DeleteDetail `json:"delete,omitempty" xml:"delete,omitempty"`
  Edit *EditDetail `json:"edit,omitempty" xml:"edit,omitempty"`
  Move *MoveDetail `json:"move,omitempty" xml:"move,omitempty"`
  Rename *RenameDetail `json:"rename,omitempty" xml:"rename,omitempty"`
  Restore *RestoreDetail `json:"restore,omitempty" xml:"restore,omitempty"`
  Trash *TrashDetail `json:"trash,omitempty" xml:"trash,omitempty"`
}

func (s ActionDetail) String() string {
  return tea.Prettify(s)
}

func (s ActionDetail) GoString() string {
  return s.String()
}

func (s *ActionDetail) SetCreate(v *CreateDetail) *ActionDetail {
  s.Create = v
  return s
}

func (s *ActionDetail) SetDelete(v *DeleteDetail) *ActionDetail {
  s.Delete = v
  return s
}

func (s *ActionDetail) SetEdit(v *EditDetail) *ActionDetail {
  s.Edit = v
  return s
}

func (s *ActionDetail) SetMove(v *MoveDetail) *ActionDetail {
  s.Move = v
  return s
}

func (s *ActionDetail) SetRename(v *RenameDetail) *ActionDetail {
  s.Rename = v
  return s
}

func (s *ActionDetail) SetRestore(v *RestoreDetail) *ActionDetail {
  s.Restore = v
  return s
}

func (s *ActionDetail) SetTrash(v *TrashDetail) *ActionDetail {
  s.Trash = v
  return s
}

/**
 * 
 */
type Actor struct {
  AliUser *ActorAliUser `json:"ali_user,omitempty" xml:"ali_user,omitempty"`
  AnonymousUser *ActorAnonymousUser `json:"anonymous_user,omitempty" xml:"anonymous_user,omitempty"`
  System *ActorSystem `json:"system,omitempty" xml:"system,omitempty"`
  User *ActorUser `json:"user,omitempty" xml:"user,omitempty"`
}

func (s Actor) String() string {
  return tea.Prettify(s)
}

func (s Actor) GoString() string {
  return s.String()
}

func (s *Actor) SetAliUser(v *ActorAliUser) *Actor {
  s.AliUser = v
  return s
}

func (s *Actor) SetAnonymousUser(v *ActorAnonymousUser) *Actor {
  s.AnonymousUser = v
  return s
}

func (s *Actor) SetSystem(v *ActorSystem) *Actor {
  s.System = v
  return s
}

func (s *Actor) SetUser(v *ActorUser) *Actor {
  s.User = v
  return s
}

/**
 * 
 */
type ActorAliUser struct {
  // AliUserID
  AliUserId *string `json:"ali_user_id,omitempty" xml:"ali_user_id,omitempty"`
  // AliUserType
  AliUserType *string `json:"ali_user_type,omitempty" xml:"ali_user_type,omitempty"`
}

func (s ActorAliUser) String() string {
  return tea.Prettify(s)
}

func (s ActorAliUser) GoString() string {
  return s.String()
}

func (s *ActorAliUser) SetAliUserId(v string) *ActorAliUser {
  s.AliUserId = &v
  return s
}

func (s *ActorAliUser) SetAliUserType(v string) *ActorAliUser {
  s.AliUserType = &v
  return s
}

/**
 * 
 */
type ActorAnonymousUser struct {
}

func (s ActorAnonymousUser) String() string {
  return tea.Prettify(s)
}

func (s ActorAnonymousUser) GoString() string {
  return s.String()
}

/**
 * 
 */
type ActorSystem struct {
  // EventType
  EventType *string `json:"event_type,omitempty" xml:"event_type,omitempty"`
}

func (s ActorSystem) String() string {
  return tea.Prettify(s)
}

func (s ActorSystem) GoString() string {
  return s.String()
}

func (s *ActorSystem) SetEventType(v string) *ActorSystem {
  s.EventType = &v
  return s
}

/**
 * 
 */
type ActorUser struct {
  // UserID
  UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty"`
  // UserName
  UserName *string `json:"user_name,omitempty" xml:"user_name,omitempty"`
}

func (s ActorUser) String() string {
  return tea.Prettify(s)
}

func (s ActorUser) GoString() string {
  return s.String()
}

func (s *ActorUser) SetUserId(v string) *ActorUser {
  s.UserId = &v
  return s
}

func (s *ActorUser) SetUserName(v string) *ActorUser {
  s.UserName = &v
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
 * 
 */
type BaseAdditionDataRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
}

func (s BaseAdditionDataRequest) String() string {
  return tea.Prettify(s)
}

func (s BaseAdditionDataRequest) GoString() string {
  return s.String()
}

func (s *BaseAdditionDataRequest) SetAdditionData(v map[string]interface{}) *BaseAdditionDataRequest {
  s.AdditionData = v
  return s
}

/**
 * Base file response
 */
type BaseCCPFileResponse struct {
  // category
  Category *string `json:"category,omitempty" xml:"category,omitempty"`
  // CharacteristicHash
  CharacteristicHash *string `json:"characteristic_hash,omitempty" xml:"characteristic_hash,omitempty"`
  // Content Hash
  ContentHash *string `json:"content_hash,omitempty" xml:"content_hash,omitempty"`
  // content_hash_name
  ContentHashName *string `json:"content_hash_name,omitempty" xml:"content_hash_name,omitempty"`
  // content_type
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // crc64_hash
  Crc64Hash *string `json:"crc64_hash,omitempty" xml:"crc64_hash,omitempty"`
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // DomainID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // download_url
  DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // encrypt_mode
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // file_extension
  FileExtension *string `json:"file_extension,omitempty" xml:"file_extension,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // Hidden
  // type: boolean
  Hidden *bool `json:"hidden,omitempty" xml:"hidden,omitempty"`
  ImageMediaMetadata *ImageMediaResponse `json:"image_media_metadata,omitempty" xml:"image_media_metadata,omitempty"`
  // labels
  Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
  Meta *string `json:"meta,omitempty" xml:"meta,omitempty"`
  // name
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
  // parent_file_id
  ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // PunishFlag
  PunishFlag *int64 `json:"punish_flag,omitempty" xml:"punish_flag,omitempty"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // starred
  // type: boolean
  Starred *bool `json:"starred,omitempty" xml:"starred,omitempty"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // @Deprecated streams url info
  StreamsInfo map[string]interface{} `json:"streams_info,omitempty" xml:"streams_info,omitempty"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // trashed_at
  TrashedAt *string `json:"trashed_at,omitempty" xml:"trashed_at,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
  // user_meta
  UserMeta *string `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
  VideoMediaMetadata *VideoMediaResponse `json:"video_media_metadata,omitempty" xml:"video_media_metadata,omitempty"`
  VideoPreviewMetadata *VideoPreviewResponse `json:"video_preview_metadata,omitempty" xml:"video_preview_metadata,omitempty"`
}

func (s BaseCCPFileResponse) String() string {
  return tea.Prettify(s)
}

func (s BaseCCPFileResponse) GoString() string {
  return s.String()
}

func (s *BaseCCPFileResponse) SetCategory(v string) *BaseCCPFileResponse {
  s.Category = &v
  return s
}

func (s *BaseCCPFileResponse) SetCharacteristicHash(v string) *BaseCCPFileResponse {
  s.CharacteristicHash = &v
  return s
}

func (s *BaseCCPFileResponse) SetContentHash(v string) *BaseCCPFileResponse {
  s.ContentHash = &v
  return s
}

func (s *BaseCCPFileResponse) SetContentHashName(v string) *BaseCCPFileResponse {
  s.ContentHashName = &v
  return s
}

func (s *BaseCCPFileResponse) SetContentType(v string) *BaseCCPFileResponse {
  s.ContentType = &v
  return s
}

func (s *BaseCCPFileResponse) SetCrc64Hash(v string) *BaseCCPFileResponse {
  s.Crc64Hash = &v
  return s
}

func (s *BaseCCPFileResponse) SetCreatedAt(v string) *BaseCCPFileResponse {
  s.CreatedAt = &v
  return s
}

func (s *BaseCCPFileResponse) SetDescription(v string) *BaseCCPFileResponse {
  s.Description = &v
  return s
}

func (s *BaseCCPFileResponse) SetDomainId(v string) *BaseCCPFileResponse {
  s.DomainId = &v
  return s
}

func (s *BaseCCPFileResponse) SetDownloadUrl(v string) *BaseCCPFileResponse {
  s.DownloadUrl = &v
  return s
}

func (s *BaseCCPFileResponse) SetDriveId(v string) *BaseCCPFileResponse {
  s.DriveId = &v
  return s
}

func (s *BaseCCPFileResponse) SetEncryptMode(v string) *BaseCCPFileResponse {
  s.EncryptMode = &v
  return s
}

func (s *BaseCCPFileResponse) SetFileExtension(v string) *BaseCCPFileResponse {
  s.FileExtension = &v
  return s
}

func (s *BaseCCPFileResponse) SetFileId(v string) *BaseCCPFileResponse {
  s.FileId = &v
  return s
}

func (s *BaseCCPFileResponse) SetHidden(v bool) *BaseCCPFileResponse {
  s.Hidden = &v
  return s
}

func (s *BaseCCPFileResponse) SetImageMediaMetadata(v *ImageMediaResponse) *BaseCCPFileResponse {
  s.ImageMediaMetadata = v
  return s
}

func (s *BaseCCPFileResponse) SetLabels(v []*string) *BaseCCPFileResponse {
  s.Labels = v
  return s
}

func (s *BaseCCPFileResponse) SetMeta(v string) *BaseCCPFileResponse {
  s.Meta = &v
  return s
}

func (s *BaseCCPFileResponse) SetName(v string) *BaseCCPFileResponse {
  s.Name = &v
  return s
}

func (s *BaseCCPFileResponse) SetParentFileId(v string) *BaseCCPFileResponse {
  s.ParentFileId = &v
  return s
}

func (s *BaseCCPFileResponse) SetPunishFlag(v int64) *BaseCCPFileResponse {
  s.PunishFlag = &v
  return s
}

func (s *BaseCCPFileResponse) SetShareId(v string) *BaseCCPFileResponse {
  s.ShareId = &v
  return s
}

func (s *BaseCCPFileResponse) SetSize(v int64) *BaseCCPFileResponse {
  s.Size = &v
  return s
}

func (s *BaseCCPFileResponse) SetStarred(v bool) *BaseCCPFileResponse {
  s.Starred = &v
  return s
}

func (s *BaseCCPFileResponse) SetStatus(v string) *BaseCCPFileResponse {
  s.Status = &v
  return s
}

func (s *BaseCCPFileResponse) SetStreamsInfo(v map[string]interface{}) *BaseCCPFileResponse {
  s.StreamsInfo = v
  return s
}

func (s *BaseCCPFileResponse) SetThumbnail(v string) *BaseCCPFileResponse {
  s.Thumbnail = &v
  return s
}

func (s *BaseCCPFileResponse) SetTrashedAt(v string) *BaseCCPFileResponse {
  s.TrashedAt = &v
  return s
}

func (s *BaseCCPFileResponse) SetType(v string) *BaseCCPFileResponse {
  s.Type = &v
  return s
}

func (s *BaseCCPFileResponse) SetUpdatedAt(v string) *BaseCCPFileResponse {
  s.UpdatedAt = &v
  return s
}

func (s *BaseCCPFileResponse) SetUploadId(v string) *BaseCCPFileResponse {
  s.UploadId = &v
  return s
}

func (s *BaseCCPFileResponse) SetUrl(v string) *BaseCCPFileResponse {
  s.Url = &v
  return s
}

func (s *BaseCCPFileResponse) SetUserMeta(v string) *BaseCCPFileResponse {
  s.UserMeta = &v
  return s
}

func (s *BaseCCPFileResponse) SetVideoMediaMetadata(v *VideoMediaResponse) *BaseCCPFileResponse {
  s.VideoMediaMetadata = v
  return s
}

func (s *BaseCCPFileResponse) SetVideoPreviewMetadata(v *VideoPreviewResponse) *BaseCCPFileResponse {
  s.VideoPreviewMetadata = v
  return s
}

/**
 * complete file request
 */
type BaseCompleteFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // part_info_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
}

func (s BaseCompleteFileRequest) String() string {
  return tea.Prettify(s)
}

func (s BaseCompleteFileRequest) GoString() string {
  return s.String()
}

func (s *BaseCompleteFileRequest) SetAdditionData(v map[string]interface{}) *BaseCompleteFileRequest {
  s.AdditionData = v
  return s
}

func (s *BaseCompleteFileRequest) SetDriveId(v string) *BaseCompleteFileRequest {
  s.DriveId = &v
  return s
}

func (s *BaseCompleteFileRequest) SetPartInfoList(v []*UploadPartInfo) *BaseCompleteFileRequest {
  s.PartInfoList = v
  return s
}

func (s *BaseCompleteFileRequest) SetShareId(v string) *BaseCompleteFileRequest {
  s.ShareId = &v
  return s
}

func (s *BaseCompleteFileRequest) SetUploadId(v string) *BaseCompleteFileRequest {
  s.UploadId = &v
  return s
}

/**
 * create file request
 */
type BaseCreateFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // ContentMd5
  ContentMd5 *string `json:"content_md5,omitempty" xml:"content_md5,omitempty"`
  // ContentType
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // Name
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" maxLength:"1024" minLength:"1"`
  // part_info_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // Type
  Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
}

func (s BaseCreateFileRequest) String() string {
  return tea.Prettify(s)
}

func (s BaseCreateFileRequest) GoString() string {
  return s.String()
}

func (s *BaseCreateFileRequest) SetAdditionData(v map[string]interface{}) *BaseCreateFileRequest {
  s.AdditionData = v
  return s
}

func (s *BaseCreateFileRequest) SetContentMd5(v string) *BaseCreateFileRequest {
  s.ContentMd5 = &v
  return s
}

func (s *BaseCreateFileRequest) SetContentType(v string) *BaseCreateFileRequest {
  s.ContentType = &v
  return s
}

func (s *BaseCreateFileRequest) SetName(v string) *BaseCreateFileRequest {
  s.Name = &v
  return s
}

func (s *BaseCreateFileRequest) SetPartInfoList(v []*UploadPartInfo) *BaseCreateFileRequest {
  s.PartInfoList = v
  return s
}

func (s *BaseCreateFileRequest) SetSize(v int64) *BaseCreateFileRequest {
  s.Size = &v
  return s
}

func (s *BaseCreateFileRequest) SetType(v string) *BaseCreateFileRequest {
  s.Type = &v
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
  Benefits map[string]interface{} `json:"benefits,omitempty" xml:"benefits,omitempty"`
  // Domain 创建时间
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // 数据 Hash 算法
  DataHashName *string `json:"data_hash_name,omitempty" xml:"data_hash_name,omitempty"`
  DefaultSuperAdminConfig *DomainSuperAdminConfig `json:"default_super_admin_config,omitempty" xml:"default_super_admin_config,omitempty"`
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
  // 预付费domain过期时间
  ExpireTime *int64 `json:"expire_time,omitempty" xml:"expire_time,omitempty"`
  // 是否开启了自动初始化 Drive
  InitDriveEnable *bool `json:"init_drive_enable,omitempty" xml:"init_drive_enable,omitempty"`
  // 自动初始化 Drive 大小
  InitDriveSize *int64 `json:"init_drive_size,omitempty" xml:"init_drive_size,omitempty"`
  // 自动初始化 Drive 所用 Store ID
  InitDriveStoreId *string `json:"init_drive_store_id,omitempty" xml:"init_drive_store_id,omitempty"`
  // Domain 类型
  Mode *string `json:"mode,omitempty" xml:"mode,omitempty"`
  OfficePreviewConfig *OfficePreviewConfig `json:"office_preview_config,omitempty" xml:"office_preview_config,omitempty"`
  // Domain 类型
  PathType *string `json:"path_type,omitempty" xml:"path_type,omitempty"`
  // 预付费套餐
  PrepaidPackage *string `json:"prepaid_package,omitempty" xml:"prepaid_package,omitempty"`
  PublishedAppAccessStrategy *AppAccessStrategy `json:"published_app_access_strategy,omitempty" xml:"published_app_access_strategy,omitempty"`
  // Domain ServiceCode
  ServiceCode *string `json:"service_code,omitempty" xml:"service_code,omitempty"`
  // 是否开启了共享
  Sharable *bool `json:"sharable,omitempty" xml:"sharable,omitempty"`
  // 是否开启了分享
  ShareLinkEnabled *bool `json:"share_link_enabled,omitempty" xml:"share_link_enabled,omitempty"`
  // 容量配额
  SizeQuota *int64 `json:"size_quota,omitempty" xml:"size_quota,omitempty"`
  // SPI 实例 id
  SpiInstanceId *string `json:"spi_instance_id,omitempty" xml:"spi_instance_id,omitempty"`
  // domain状态：创建中，正常，已过期
  Status *int64 `json:"status,omitempty" xml:"status,omitempty"`
  // 存储级别
  StoreLevel *string `json:"store_level,omitempty" xml:"store_level,omitempty"`
  // 存储 Region 列表
  StoreRegionList []*string `json:"store_region_list,omitempty" xml:"store_region_list,omitempty" type:"Repeated"`
  // Domain 更新时间
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // 用户数配额
  UserCountQuota *int64 `json:"user_count_quota,omitempty" xml:"user_count_quota,omitempty"`
  VideoPreviewConfig *VideoPreviewConfig `json:"video_preview_config,omitempty" xml:"video_preview_config,omitempty"`
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

func (s *BaseDomainResponse) SetBenefits(v map[string]interface{}) *BaseDomainResponse {
  s.Benefits = v
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

func (s *BaseDomainResponse) SetDefaultSuperAdminConfig(v *DomainSuperAdminConfig) *BaseDomainResponse {
  s.DefaultSuperAdminConfig = v
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

func (s *BaseDomainResponse) SetExpireTime(v int64) *BaseDomainResponse {
  s.ExpireTime = &v
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

func (s *BaseDomainResponse) SetOfficePreviewConfig(v *OfficePreviewConfig) *BaseDomainResponse {
  s.OfficePreviewConfig = v
  return s
}

func (s *BaseDomainResponse) SetPathType(v string) *BaseDomainResponse {
  s.PathType = &v
  return s
}

func (s *BaseDomainResponse) SetPrepaidPackage(v string) *BaseDomainResponse {
  s.PrepaidPackage = &v
  return s
}

func (s *BaseDomainResponse) SetPublishedAppAccessStrategy(v *AppAccessStrategy) *BaseDomainResponse {
  s.PublishedAppAccessStrategy = v
  return s
}

func (s *BaseDomainResponse) SetServiceCode(v string) *BaseDomainResponse {
  s.ServiceCode = &v
  return s
}

func (s *BaseDomainResponse) SetSharable(v bool) *BaseDomainResponse {
  s.Sharable = &v
  return s
}

func (s *BaseDomainResponse) SetShareLinkEnabled(v bool) *BaseDomainResponse {
  s.ShareLinkEnabled = &v
  return s
}

func (s *BaseDomainResponse) SetSizeQuota(v int64) *BaseDomainResponse {
  s.SizeQuota = &v
  return s
}

func (s *BaseDomainResponse) SetSpiInstanceId(v string) *BaseDomainResponse {
  s.SpiInstanceId = &v
  return s
}

func (s *BaseDomainResponse) SetStatus(v int64) *BaseDomainResponse {
  s.Status = &v
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

func (s *BaseDomainResponse) SetUserCountQuota(v int64) *BaseDomainResponse {
  s.UserCountQuota = &v
  return s
}

func (s *BaseDomainResponse) SetVideoPreviewConfig(v *VideoPreviewConfig) *BaseDomainResponse {
  s.VideoPreviewConfig = v
  return s
}

/**
 * Base drive response
 */
type BaseDriveResponse struct {
  // Drive 创建者
  Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
  // Drive 备注信息
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // Drive ID
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty"`
  // Drive 名称
  DriveName *string `json:"drive_name,omitempty" xml:"drive_name,omitempty"`
  // Drive 类型
  DriveType *string `json:"drive_type,omitempty" xml:"drive_type,omitempty"`
  EncryptDataAccess *bool `json:"encrypt_data_access,omitempty" xml:"encrypt_data_access,omitempty"`
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // Drive 所有者
  Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
  // Drive 所有者类型
  OwnerType *string `json:"owner_type,omitempty" xml:"owner_type,omitempty"`
  // Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
  RelativePath *string `json:"relative_path,omitempty" xml:"relative_path,omitempty"`
  // Drive 状态
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // 存储 ID, domain的PathType为OSSPath时返回
  StoreId *string `json:"store_id,omitempty" xml:"store_id,omitempty"`
  // Drive 空间总量
  TotalSize *int64 `json:"total_size,omitempty" xml:"total_size,omitempty"`
  // Drive 空间已使用量
  UsedSize *int64 `json:"used_size,omitempty" xml:"used_size,omitempty"`
}

func (s BaseDriveResponse) String() string {
  return tea.Prettify(s)
}

func (s BaseDriveResponse) GoString() string {
  return s.String()
}

func (s *BaseDriveResponse) SetCreator(v string) *BaseDriveResponse {
  s.Creator = &v
  return s
}

func (s *BaseDriveResponse) SetDescription(v string) *BaseDriveResponse {
  s.Description = &v
  return s
}

func (s *BaseDriveResponse) SetDomainId(v string) *BaseDriveResponse {
  s.DomainId = &v
  return s
}

func (s *BaseDriveResponse) SetDriveId(v string) *BaseDriveResponse {
  s.DriveId = &v
  return s
}

func (s *BaseDriveResponse) SetDriveName(v string) *BaseDriveResponse {
  s.DriveName = &v
  return s
}

func (s *BaseDriveResponse) SetDriveType(v string) *BaseDriveResponse {
  s.DriveType = &v
  return s
}

func (s *BaseDriveResponse) SetEncryptDataAccess(v bool) *BaseDriveResponse {
  s.EncryptDataAccess = &v
  return s
}

func (s *BaseDriveResponse) SetEncryptMode(v string) *BaseDriveResponse {
  s.EncryptMode = &v
  return s
}

func (s *BaseDriveResponse) SetOwner(v string) *BaseDriveResponse {
  s.Owner = &v
  return s
}

func (s *BaseDriveResponse) SetOwnerType(v string) *BaseDriveResponse {
  s.OwnerType = &v
  return s
}

func (s *BaseDriveResponse) SetRelativePath(v string) *BaseDriveResponse {
  s.RelativePath = &v
  return s
}

func (s *BaseDriveResponse) SetStatus(v string) *BaseDriveResponse {
  s.Status = &v
  return s
}

func (s *BaseDriveResponse) SetStoreId(v string) *BaseDriveResponse {
  s.StoreId = &v
  return s
}

func (s *BaseDriveResponse) SetTotalSize(v int64) *BaseDriveResponse {
  s.TotalSize = &v
  return s
}

func (s *BaseDriveResponse) SetUsedSize(v int64) *BaseDriveResponse {
  s.UsedSize = &v
  return s
}

/**
 * list_file_by_anonymous base response
 */
type BaseFileAnonymousResponse struct {
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // name
  Name *string `json:"name,omitempty" xml:"name,omitempty" pattern:"[a-zA-Z0-9.-]{1,1000}"`
  // size, type=file时才有效
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s BaseFileAnonymousResponse) String() string {
  return tea.Prettify(s)
}

func (s BaseFileAnonymousResponse) GoString() string {
  return s.String()
}

func (s *BaseFileAnonymousResponse) SetFileId(v string) *BaseFileAnonymousResponse {
  s.FileId = &v
  return s
}

func (s *BaseFileAnonymousResponse) SetName(v string) *BaseFileAnonymousResponse {
  s.Name = &v
  return s
}

func (s *BaseFileAnonymousResponse) SetSize(v int64) *BaseFileAnonymousResponse {
  s.Size = &v
  return s
}

func (s *BaseFileAnonymousResponse) SetThumbnail(v string) *BaseFileAnonymousResponse {
  s.Thumbnail = &v
  return s
}

func (s *BaseFileAnonymousResponse) SetType(v string) *BaseFileAnonymousResponse {
  s.Type = &v
  return s
}

func (s *BaseFileAnonymousResponse) SetUpdatedAt(v string) *BaseFileAnonymousResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * 
 */
type BaseFileProcessRequest struct {
  ImageCroppingAspectRatios []*string `json:"image_cropping_aspect_ratios,omitempty" xml:"image_cropping_aspect_ratios,omitempty" type:"Repeated"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s BaseFileProcessRequest) String() string {
  return tea.Prettify(s)
}

func (s BaseFileProcessRequest) GoString() string {
  return s.String()
}

func (s *BaseFileProcessRequest) SetImageCroppingAspectRatios(v []*string) *BaseFileProcessRequest {
  s.ImageCroppingAspectRatios = v
  return s
}

func (s *BaseFileProcessRequest) SetImageThumbnailProcess(v string) *BaseFileProcessRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *BaseFileProcessRequest) SetImageUrlProcess(v string) *BaseFileProcessRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *BaseFileProcessRequest) SetOfficeThumbnailProcess(v string) *BaseFileProcessRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *BaseFileProcessRequest) SetVideoThumbnailProcess(v string) *BaseFileProcessRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * 获取文件上传URL
 */
type BaseGetUploadUrlRequest struct {
  // content_md5
  ContentMd5 *string `json:"content_md5,omitempty" xml:"content_md5,omitempty" maxLength:"32"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // upload_part_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty" require:"true"`
}

func (s BaseGetUploadUrlRequest) String() string {
  return tea.Prettify(s)
}

func (s BaseGetUploadUrlRequest) GoString() string {
  return s.String()
}

func (s *BaseGetUploadUrlRequest) SetContentMd5(v string) *BaseGetUploadUrlRequest {
  s.ContentMd5 = &v
  return s
}

func (s *BaseGetUploadUrlRequest) SetDriveId(v string) *BaseGetUploadUrlRequest {
  s.DriveId = &v
  return s
}

func (s *BaseGetUploadUrlRequest) SetPartInfoList(v []*UploadPartInfo) *BaseGetUploadUrlRequest {
  s.PartInfoList = v
  return s
}

func (s *BaseGetUploadUrlRequest) SetShareId(v string) *BaseGetUploadUrlRequest {
  s.ShareId = &v
  return s
}

func (s *BaseGetUploadUrlRequest) SetUploadId(v string) *BaseGetUploadUrlRequest {
  s.UploadId = &v
  return s
}

/**
 * Base file response
 */
type BaseHostingFileResponse struct {
  // Content Hash
  ContentHash *string `json:"content_hash,omitempty" xml:"content_hash,omitempty"`
  // content_hash_name
  ContentHashName *string `json:"content_hash_name,omitempty" xml:"content_hash_name,omitempty"`
  // content_type
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // crc64_hash
  Crc64Hash *string `json:"crc64_hash,omitempty" xml:"crc64_hash,omitempty"`
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // download_url
  DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_extension
  FileExtension *string `json:"file_extension,omitempty" xml:"file_extension,omitempty"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  // name
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
  // parent_file_id
  ParentFilePath *string `json:"parent_file_path,omitempty" xml:"parent_file_path,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9]+"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // trashed_at
  TrashedAt *string `json:"trashed_at,omitempty" xml:"trashed_at,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s BaseHostingFileResponse) String() string {
  return tea.Prettify(s)
}

func (s BaseHostingFileResponse) GoString() string {
  return s.String()
}

func (s *BaseHostingFileResponse) SetContentHash(v string) *BaseHostingFileResponse {
  s.ContentHash = &v
  return s
}

func (s *BaseHostingFileResponse) SetContentHashName(v string) *BaseHostingFileResponse {
  s.ContentHashName = &v
  return s
}

func (s *BaseHostingFileResponse) SetContentType(v string) *BaseHostingFileResponse {
  s.ContentType = &v
  return s
}

func (s *BaseHostingFileResponse) SetCrc64Hash(v string) *BaseHostingFileResponse {
  s.Crc64Hash = &v
  return s
}

func (s *BaseHostingFileResponse) SetCreatedAt(v string) *BaseHostingFileResponse {
  s.CreatedAt = &v
  return s
}

func (s *BaseHostingFileResponse) SetDescription(v string) *BaseHostingFileResponse {
  s.Description = &v
  return s
}

func (s *BaseHostingFileResponse) SetDomainId(v string) *BaseHostingFileResponse {
  s.DomainId = &v
  return s
}

func (s *BaseHostingFileResponse) SetDownloadUrl(v string) *BaseHostingFileResponse {
  s.DownloadUrl = &v
  return s
}

func (s *BaseHostingFileResponse) SetDriveId(v string) *BaseHostingFileResponse {
  s.DriveId = &v
  return s
}

func (s *BaseHostingFileResponse) SetFileExtension(v string) *BaseHostingFileResponse {
  s.FileExtension = &v
  return s
}

func (s *BaseHostingFileResponse) SetFilePath(v string) *BaseHostingFileResponse {
  s.FilePath = &v
  return s
}

func (s *BaseHostingFileResponse) SetName(v string) *BaseHostingFileResponse {
  s.Name = &v
  return s
}

func (s *BaseHostingFileResponse) SetParentFilePath(v string) *BaseHostingFileResponse {
  s.ParentFilePath = &v
  return s
}

func (s *BaseHostingFileResponse) SetShareId(v string) *BaseHostingFileResponse {
  s.ShareId = &v
  return s
}

func (s *BaseHostingFileResponse) SetSize(v int64) *BaseHostingFileResponse {
  s.Size = &v
  return s
}

func (s *BaseHostingFileResponse) SetStatus(v string) *BaseHostingFileResponse {
  s.Status = &v
  return s
}

func (s *BaseHostingFileResponse) SetThumbnail(v string) *BaseHostingFileResponse {
  s.Thumbnail = &v
  return s
}

func (s *BaseHostingFileResponse) SetTrashedAt(v string) *BaseHostingFileResponse {
  s.TrashedAt = &v
  return s
}

func (s *BaseHostingFileResponse) SetType(v string) *BaseHostingFileResponse {
  s.Type = &v
  return s
}

func (s *BaseHostingFileResponse) SetUpdatedAt(v string) *BaseHostingFileResponse {
  s.UpdatedAt = &v
  return s
}

func (s *BaseHostingFileResponse) SetUploadId(v string) *BaseHostingFileResponse {
  s.UploadId = &v
  return s
}

func (s *BaseHostingFileResponse) SetUrl(v string) *BaseHostingFileResponse {
  s.Url = &v
  return s
}

/**
 * Base image process
 */
type BaseImageProcessRequest struct {
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s BaseImageProcessRequest) String() string {
  return tea.Prettify(s)
}

func (s BaseImageProcessRequest) GoString() string {
  return s.String()
}

func (s *BaseImageProcessRequest) SetImageThumbnailProcess(v string) *BaseImageProcessRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *BaseImageProcessRequest) SetImageUrlProcess(v string) *BaseImageProcessRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *BaseImageProcessRequest) SetOfficeThumbnailProcess(v string) *BaseImageProcessRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *BaseImageProcessRequest) SetVideoThumbnailProcess(v string) *BaseImageProcessRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * list file request
 */
type BaseListFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  ImageCroppingAspectRatios []*string `json:"image_cropping_aspect_ratios,omitempty" xml:"image_cropping_aspect_ratios,omitempty" type:"Repeated"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // limit
  Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"0"`
  // marker
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id, either share_id or drive_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s BaseListFileRequest) String() string {
  return tea.Prettify(s)
}

func (s BaseListFileRequest) GoString() string {
  return s.String()
}

func (s *BaseListFileRequest) SetAdditionData(v map[string]interface{}) *BaseListFileRequest {
  s.AdditionData = v
  return s
}

func (s *BaseListFileRequest) SetDriveId(v string) *BaseListFileRequest {
  s.DriveId = &v
  return s
}

func (s *BaseListFileRequest) SetImageCroppingAspectRatios(v []*string) *BaseListFileRequest {
  s.ImageCroppingAspectRatios = v
  return s
}

func (s *BaseListFileRequest) SetImageThumbnailProcess(v string) *BaseListFileRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *BaseListFileRequest) SetImageUrlProcess(v string) *BaseListFileRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *BaseListFileRequest) SetLimit(v int64) *BaseListFileRequest {
  s.Limit = &v
  return s
}

func (s *BaseListFileRequest) SetMarker(v string) *BaseListFileRequest {
  s.Marker = &v
  return s
}

func (s *BaseListFileRequest) SetOfficeThumbnailProcess(v string) *BaseListFileRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *BaseListFileRequest) SetReferer(v string) *BaseListFileRequest {
  s.Referer = &v
  return s
}

func (s *BaseListFileRequest) SetShareId(v string) *BaseListFileRequest {
  s.ShareId = &v
  return s
}

func (s *BaseListFileRequest) SetSignToken(v string) *BaseListFileRequest {
  s.SignToken = &v
  return s
}

func (s *BaseListFileRequest) SetVideoThumbnailProcess(v string) *BaseListFileRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * 
 */
type BaseMediaResponse struct {
  // address_line
  AddressLine *string `json:"address_line,omitempty" xml:"address_line,omitempty"`
  // city
  City *string `json:"city,omitempty" xml:"city,omitempty"`
  // country
  Country *string `json:"country,omitempty" xml:"country,omitempty"`
  // district
  District *string `json:"district,omitempty" xml:"district,omitempty"`
  // height
  Height *int64 `json:"height,omitempty" xml:"height,omitempty"`
  // system_tags
  ImageTags []*SystemTag `json:"image_tags,omitempty" xml:"image_tags,omitempty" type:"Repeated"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // province
  Province *string `json:"province,omitempty" xml:"province,omitempty"`
  // time
  Time *string `json:"time,omitempty" xml:"time,omitempty"`
  // township
  Township *string `json:"township,omitempty" xml:"township,omitempty"`
  // width
  Width *int64 `json:"width,omitempty" xml:"width,omitempty"`
}

func (s BaseMediaResponse) String() string {
  return tea.Prettify(s)
}

func (s BaseMediaResponse) GoString() string {
  return s.String()
}

func (s *BaseMediaResponse) SetAddressLine(v string) *BaseMediaResponse {
  s.AddressLine = &v
  return s
}

func (s *BaseMediaResponse) SetCity(v string) *BaseMediaResponse {
  s.City = &v
  return s
}

func (s *BaseMediaResponse) SetCountry(v string) *BaseMediaResponse {
  s.Country = &v
  return s
}

func (s *BaseMediaResponse) SetDistrict(v string) *BaseMediaResponse {
  s.District = &v
  return s
}

func (s *BaseMediaResponse) SetHeight(v int64) *BaseMediaResponse {
  s.Height = &v
  return s
}

func (s *BaseMediaResponse) SetImageTags(v []*SystemTag) *BaseMediaResponse {
  s.ImageTags = v
  return s
}

func (s *BaseMediaResponse) SetLocation(v string) *BaseMediaResponse {
  s.Location = &v
  return s
}

func (s *BaseMediaResponse) SetProvince(v string) *BaseMediaResponse {
  s.Province = &v
  return s
}

func (s *BaseMediaResponse) SetTime(v string) *BaseMediaResponse {
  s.Time = &v
  return s
}

func (s *BaseMediaResponse) SetTownship(v string) *BaseMediaResponse {
  s.Township = &v
  return s
}

func (s *BaseMediaResponse) SetWidth(v int64) *BaseMediaResponse {
  s.Width = &v
  return s
}

/**
 * 文件移动请求
 */
type BaseMoveFileRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
  // new_name
  NewName *string `json:"new_name,omitempty" xml:"new_name,omitempty" maxLength:"1024" minLength:"1"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
}

func (s BaseMoveFileRequest) String() string {
  return tea.Prettify(s)
}

func (s BaseMoveFileRequest) GoString() string {
  return s.String()
}

func (s *BaseMoveFileRequest) SetDriveId(v string) *BaseMoveFileRequest {
  s.DriveId = &v
  return s
}

func (s *BaseMoveFileRequest) SetNewName(v string) *BaseMoveFileRequest {
  s.NewName = &v
  return s
}

func (s *BaseMoveFileRequest) SetShareId(v string) *BaseMoveFileRequest {
  s.ShareId = &v
  return s
}

/**
 * list_share_link response
 */
type BaseShareLinkResponse struct {
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // creator
  Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // 下载次数
  DownloadCount *int64 `json:"download_count,omitempty" xml:"download_count,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty"`
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // expired
  Expired *bool `json:"expired,omitempty" xml:"expired,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty"`
  // file_id_list
  FileIdList []*string `json:"file_id_list,omitempty" xml:"file_id_list,omitempty" type:"Repeated"`
  // file_id_list
  FilePathList []*string `json:"file_path_list,omitempty" xml:"file_path_list,omitempty" type:"Repeated"`
  // preview_count
  PreviewCount *int64 `json:"preview_count,omitempty" xml:"preview_count,omitempty"`
  // 转存次数
  SaveCount *int64 `json:"save_count,omitempty" xml:"save_count,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // share_msg
  ShareMsg *string `json:"share_msg,omitempty" xml:"share_msg,omitempty"`
  // share_name
  ShareName *string `json:"share_name,omitempty" xml:"share_name,omitempty"`
  // share_policy
  SharePolicy *string `json:"share_policy,omitempty" xml:"share_policy,omitempty"`
  // share_pwd
  SharePwd *string `json:"share_pwd,omitempty" xml:"share_pwd,omitempty"`
  // share_url
  ShareUrl *string `json:"share_url,omitempty" xml:"share_url,omitempty"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s BaseShareLinkResponse) String() string {
  return tea.Prettify(s)
}

func (s BaseShareLinkResponse) GoString() string {
  return s.String()
}

func (s *BaseShareLinkResponse) SetCreatedAt(v string) *BaseShareLinkResponse {
  s.CreatedAt = &v
  return s
}

func (s *BaseShareLinkResponse) SetCreator(v string) *BaseShareLinkResponse {
  s.Creator = &v
  return s
}

func (s *BaseShareLinkResponse) SetDescription(v string) *BaseShareLinkResponse {
  s.Description = &v
  return s
}

func (s *BaseShareLinkResponse) SetDownloadCount(v int64) *BaseShareLinkResponse {
  s.DownloadCount = &v
  return s
}

func (s *BaseShareLinkResponse) SetDriveId(v string) *BaseShareLinkResponse {
  s.DriveId = &v
  return s
}

func (s *BaseShareLinkResponse) SetExpiration(v string) *BaseShareLinkResponse {
  s.Expiration = &v
  return s
}

func (s *BaseShareLinkResponse) SetExpired(v bool) *BaseShareLinkResponse {
  s.Expired = &v
  return s
}

func (s *BaseShareLinkResponse) SetFileId(v string) *BaseShareLinkResponse {
  s.FileId = &v
  return s
}

func (s *BaseShareLinkResponse) SetFileIdList(v []*string) *BaseShareLinkResponse {
  s.FileIdList = v
  return s
}

func (s *BaseShareLinkResponse) SetFilePathList(v []*string) *BaseShareLinkResponse {
  s.FilePathList = v
  return s
}

func (s *BaseShareLinkResponse) SetPreviewCount(v int64) *BaseShareLinkResponse {
  s.PreviewCount = &v
  return s
}

func (s *BaseShareLinkResponse) SetSaveCount(v int64) *BaseShareLinkResponse {
  s.SaveCount = &v
  return s
}

func (s *BaseShareLinkResponse) SetShareId(v string) *BaseShareLinkResponse {
  s.ShareId = &v
  return s
}

func (s *BaseShareLinkResponse) SetShareMsg(v string) *BaseShareLinkResponse {
  s.ShareMsg = &v
  return s
}

func (s *BaseShareLinkResponse) SetShareName(v string) *BaseShareLinkResponse {
  s.ShareName = &v
  return s
}

func (s *BaseShareLinkResponse) SetSharePolicy(v string) *BaseShareLinkResponse {
  s.SharePolicy = &v
  return s
}

func (s *BaseShareLinkResponse) SetSharePwd(v string) *BaseShareLinkResponse {
  s.SharePwd = &v
  return s
}

func (s *BaseShareLinkResponse) SetShareUrl(v string) *BaseShareLinkResponse {
  s.ShareUrl = &v
  return s
}

func (s *BaseShareLinkResponse) SetStatus(v string) *BaseShareLinkResponse {
  s.Status = &v
  return s
}

func (s *BaseShareLinkResponse) SetUpdatedAt(v string) *BaseShareLinkResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * List share response
 */
type BaseShareResponse struct {
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // creator
  Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty"`
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // expired
  Expired *bool `json:"expired,omitempty" xml:"expired,omitempty"`
  // owner
  Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
  // owner
  OwnerType *string `json:"owner_type,omitempty" xml:"owner_type,omitempty"`
  // permissions
  Permissions []*string `json:"permissions,omitempty" xml:"permissions,omitempty" type:"Repeated"`
  // share_file_id
  ShareFileId *string `json:"share_file_id,omitempty" xml:"share_file_id,omitempty"`
  // share_path
  ShareFilePath *string `json:"share_file_path,omitempty" xml:"share_file_path,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // share_name
  ShareName *string `json:"share_name,omitempty" xml:"share_name,omitempty"`
  SharePolicy []*SharePermissionPolicy `json:"share_policy,omitempty" xml:"share_policy,omitempty" type:"Repeated"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s BaseShareResponse) String() string {
  return tea.Prettify(s)
}

func (s BaseShareResponse) GoString() string {
  return s.String()
}

func (s *BaseShareResponse) SetCreatedAt(v string) *BaseShareResponse {
  s.CreatedAt = &v
  return s
}

func (s *BaseShareResponse) SetCreator(v string) *BaseShareResponse {
  s.Creator = &v
  return s
}

func (s *BaseShareResponse) SetDescription(v string) *BaseShareResponse {
  s.Description = &v
  return s
}

func (s *BaseShareResponse) SetDomainId(v string) *BaseShareResponse {
  s.DomainId = &v
  return s
}

func (s *BaseShareResponse) SetDriveId(v string) *BaseShareResponse {
  s.DriveId = &v
  return s
}

func (s *BaseShareResponse) SetExpiration(v string) *BaseShareResponse {
  s.Expiration = &v
  return s
}

func (s *BaseShareResponse) SetExpired(v bool) *BaseShareResponse {
  s.Expired = &v
  return s
}

func (s *BaseShareResponse) SetOwner(v string) *BaseShareResponse {
  s.Owner = &v
  return s
}

func (s *BaseShareResponse) SetOwnerType(v string) *BaseShareResponse {
  s.OwnerType = &v
  return s
}

func (s *BaseShareResponse) SetPermissions(v []*string) *BaseShareResponse {
  s.Permissions = v
  return s
}

func (s *BaseShareResponse) SetShareFileId(v string) *BaseShareResponse {
  s.ShareFileId = &v
  return s
}

func (s *BaseShareResponse) SetShareFilePath(v string) *BaseShareResponse {
  s.ShareFilePath = &v
  return s
}

func (s *BaseShareResponse) SetShareId(v string) *BaseShareResponse {
  s.ShareId = &v
  return s
}

func (s *BaseShareResponse) SetShareName(v string) *BaseShareResponse {
  s.ShareName = &v
  return s
}

func (s *BaseShareResponse) SetSharePolicy(v []*SharePermissionPolicy) *BaseShareResponse {
  s.SharePolicy = v
  return s
}

func (s *BaseShareResponse) SetStatus(v string) *BaseShareResponse {
  s.Status = &v
  return s
}

func (s *BaseShareResponse) SetUpdatedAt(v string) *BaseShareResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * 批处理
 */
type BatchRequest struct {
  // Requests 请求合集
  Requests []*BatchSubRequest `json:"requests,omitempty" xml:"requests,omitempty" require:"true" type:"Repeated"`
  // 支持的资源类型
  Resource *string `json:"resource,omitempty" xml:"resource,omitempty" require:"true"`
}

func (s BatchRequest) String() string {
  return tea.Prettify(s)
}

func (s BatchRequest) GoString() string {
  return s.String()
}

func (s *BatchRequest) SetRequests(v []*BatchSubRequest) *BatchRequest {
  s.Requests = v
  return s
}

func (s *BatchRequest) SetResource(v string) *BatchRequest {
  s.Resource = &v
  return s
}

/**
 * batch operation response
 */
type BatchResponse struct {
  // responses 返回结果合集
  Responses []*BatchSubResponse `json:"responses,omitempty" xml:"responses,omitempty" type:"Repeated"`
}

func (s BatchResponse) String() string {
  return tea.Prettify(s)
}

func (s BatchResponse) GoString() string {
  return s.String()
}

func (s *BatchResponse) SetResponses(v []*BatchSubResponse) *BatchResponse {
  s.Responses = v
  return s
}

/**
 * 
 */
type BatchSubRequest struct {
  // body 子请求的请求参数 json 字符串，可参考对于子请求文档, 当指定了body 必须传headers ： "Content-Type" 对应的类型，目前子请求入参是"application/json"
  Body map[string]interface{} `json:"body,omitempty" xml:"body,omitempty"`
  // headers 请求头，表示body传入数据的类型
  Headers map[string]interface{} `json:"headers,omitempty" xml:"headers,omitempty"`
  // id 用于request 和 response关联， 不允许重复
  Id *string `json:"id,omitempty" xml:"id,omitempty" require:"true"`
  // method
  Method *string `json:"method,omitempty" xml:"method,omitempty" require:"true"`
  // url 子请求的api path路径， 可参考对于子请求文档
  Url *string `json:"url,omitempty" xml:"url,omitempty" require:"true"`
}

func (s BatchSubRequest) String() string {
  return tea.Prettify(s)
}

func (s BatchSubRequest) GoString() string {
  return s.String()
}

func (s *BatchSubRequest) SetBody(v map[string]interface{}) *BatchSubRequest {
  s.Body = v
  return s
}

func (s *BatchSubRequest) SetHeaders(v map[string]interface{}) *BatchSubRequest {
  s.Headers = v
  return s
}

func (s *BatchSubRequest) SetId(v string) *BatchSubRequest {
  s.Id = &v
  return s
}

func (s *BatchSubRequest) SetMethod(v string) *BatchSubRequest {
  s.Method = &v
  return s
}

func (s *BatchSubRequest) SetUrl(v string) *BatchSubRequest {
  s.Url = &v
  return s
}

/**
 * 
 */
type BatchSubResponse struct {
  // body 子请求的返回结果，可参考对于子请求文档 json 字符串
  Body map[string]interface{} `json:"body,omitempty" xml:"body,omitempty"`
  // id 请求带过来的id, 可以跟 request 进行关联
  Id *string `json:"id,omitempty" xml:"id,omitempty"`
  // status 子请求的返回状态码，可参考对于子请求文档
  Status *int64 `json:"status,omitempty" xml:"status,omitempty"`
}

func (s BatchSubResponse) String() string {
  return tea.Prettify(s)
}

func (s BatchSubResponse) GoString() string {
  return s.String()
}

func (s *BatchSubResponse) SetBody(v map[string]interface{}) *BatchSubResponse {
  s.Body = v
  return s
}

func (s *BatchSubResponse) SetId(v string) *BatchSubResponse {
  s.Id = &v
  return s
}

func (s *BatchSubResponse) SetStatus(v int64) *BatchSubResponse {
  s.Status = &v
  return s
}

/**
 * Benefit base info of benefit package
 */
type BenefitBaseResponse struct {
  // 权益的唯一标识
  BenefitId *string `json:"benefit_id,omitempty" xml:"benefit_id,omitempty"`
  BenefitMeta *BenefitMetaResponse `json:"benefit_meta,omitempty" xml:"benefit_meta,omitempty"`
  // 权益包的唯一标识
  BenefitPkgId *string `json:"benefit_pkg_id,omitempty" xml:"benefit_pkg_id,omitempty"`
  // 权益的名称
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
}

func (s BenefitBaseResponse) String() string {
  return tea.Prettify(s)
}

func (s BenefitBaseResponse) GoString() string {
  return s.String()
}

func (s *BenefitBaseResponse) SetBenefitId(v string) *BenefitBaseResponse {
  s.BenefitId = &v
  return s
}

func (s *BenefitBaseResponse) SetBenefitMeta(v *BenefitMetaResponse) *BenefitBaseResponse {
  s.BenefitMeta = v
  return s
}

func (s *BenefitBaseResponse) SetBenefitPkgId(v string) *BenefitBaseResponse {
  s.BenefitPkgId = &v
  return s
}

func (s *BenefitBaseResponse) SetName(v string) *BenefitBaseResponse {
  s.Name = &v
  return s
}

/**
 * Benefit meta response
 */
type BenefitMetaResponse struct {
  // 权益的配置
  Config *string `json:"config,omitempty" xml:"config,omitempty"`
  // 权益的开关
  Enabled *bool `json:"enabled,omitempty" xml:"enabled,omitempty"`
  // 权益的配额
  Quota *int64 `json:"quota,omitempty" xml:"quota,omitempty"`
}

func (s BenefitMetaResponse) String() string {
  return tea.Prettify(s)
}

func (s BenefitMetaResponse) GoString() string {
  return s.String()
}

func (s *BenefitMetaResponse) SetConfig(v string) *BenefitMetaResponse {
  s.Config = &v
  return s
}

func (s *BenefitMetaResponse) SetEnabled(v bool) *BenefitMetaResponse {
  s.Enabled = &v
  return s
}

func (s *BenefitMetaResponse) SetQuota(v int64) *BenefitMetaResponse {
  s.Quota = &v
  return s
}

/**
 * Benefit package delivery info
 */
type BenefitPkgDeliveryInfoResponse struct {
  // 权益包下发的数量
  Amount *int64 `json:"amount,omitempty" xml:"amount,omitempty"`
  // 权益包下发的创建时间
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // 权益包下发的超期时间，is_permanent为false时，返回有效值
  ExpireTime *string `json:"expire_time,omitempty" xml:"expire_time,omitempty"`
  // 权益包是否永久有效
  IsPermanent *bool `json:"is_permanent,omitempty" xml:"is_permanent,omitempty"`
}

func (s BenefitPkgDeliveryInfoResponse) String() string {
  return tea.Prettify(s)
}

func (s BenefitPkgDeliveryInfoResponse) GoString() string {
  return s.String()
}

func (s *BenefitPkgDeliveryInfoResponse) SetAmount(v int64) *BenefitPkgDeliveryInfoResponse {
  s.Amount = &v
  return s
}

func (s *BenefitPkgDeliveryInfoResponse) SetCreatedAt(v string) *BenefitPkgDeliveryInfoResponse {
  s.CreatedAt = &v
  return s
}

func (s *BenefitPkgDeliveryInfoResponse) SetExpireTime(v string) *BenefitPkgDeliveryInfoResponse {
  s.ExpireTime = &v
  return s
}

func (s *BenefitPkgDeliveryInfoResponse) SetIsPermanent(v bool) *BenefitPkgDeliveryInfoResponse {
  s.IsPermanent = &v
  return s
}

/**
 * 获取文件夹size信息
 */
type CCPGetDirSizeInfoRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  // share_id, either share_id or drive_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
}

func (s CCPGetDirSizeInfoRequest) String() string {
  return tea.Prettify(s)
}

func (s CCPGetDirSizeInfoRequest) GoString() string {
  return s.String()
}

func (s *CCPGetDirSizeInfoRequest) SetDriveId(v string) *CCPGetDirSizeInfoRequest {
  s.DriveId = &v
  return s
}

func (s *CCPGetDirSizeInfoRequest) SetFileId(v string) *CCPGetDirSizeInfoRequest {
  s.FileId = &v
  return s
}

func (s *CCPGetDirSizeInfoRequest) SetShareId(v string) *CCPGetDirSizeInfoRequest {
  s.ShareId = &v
  return s
}

/**
 * 获取分享中文件媒体播放地址的请求body
 */
type CCPGetShareLinkVideoPreviewPlayInfoRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // category
  Category *string `json:"category,omitempty" xml:"category,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  FileIdPath *string `json:"file_id_path,omitempty" xml:"file_id_path,omitempty"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" require:"true"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // template_id
  TemplateId *string `json:"template_id,omitempty" xml:"template_id,omitempty"`
  // url_expire_sec
  UrlExpireSec *int64 `json:"url_expire_sec,omitempty" xml:"url_expire_sec,omitempty" maximum:"600" minimum:"10"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s CCPGetShareLinkVideoPreviewPlayInfoRequest) String() string {
  return tea.Prettify(s)
}

func (s CCPGetShareLinkVideoPreviewPlayInfoRequest) GoString() string {
  return s.String()
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetAdditionData(v map[string]interface{}) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.AdditionData = v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetCategory(v string) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.Category = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetFileId(v string) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.FileId = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetFileIdPath(v string) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.FileIdPath = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetImageThumbnailProcess(v string) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetImageUrlProcess(v string) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetLocation(v string) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.Location = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetOfficeThumbnailProcess(v string) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetReferer(v string) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.Referer = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetShareId(v string) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.ShareId = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetSignToken(v string) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.SignToken = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetTemplateId(v string) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.TemplateId = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetUrlExpireSec(v int64) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.UrlExpireSec = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoRequest) SetVideoThumbnailProcess(v string) *CCPGetShareLinkVideoPreviewPlayInfoRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * 获取分享中媒体播放地址response
 */
type CCPGetShareLinkVideoPreviewPlayInfoResponse struct {
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  VideoPreviewPlayInfo *VideoPreviewPlayInfoResponse `json:"video_preview_play_info,omitempty" xml:"video_preview_play_info,omitempty"`
}

func (s CCPGetShareLinkVideoPreviewPlayInfoResponse) String() string {
  return tea.Prettify(s)
}

func (s CCPGetShareLinkVideoPreviewPlayInfoResponse) GoString() string {
  return s.String()
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoResponse) SetFileId(v string) *CCPGetShareLinkVideoPreviewPlayInfoResponse {
  s.FileId = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoResponse) SetShareId(v string) *CCPGetShareLinkVideoPreviewPlayInfoResponse {
  s.ShareId = &v
  return s
}

func (s *CCPGetShareLinkVideoPreviewPlayInfoResponse) SetVideoPreviewPlayInfo(v *VideoPreviewPlayInfoResponse) *CCPGetShareLinkVideoPreviewPlayInfoResponse {
  s.VideoPreviewPlayInfo = v
  return s
}

/**
 * 获取转码信息请求
 */
type CCPGetVideoPreviewPlayInfoRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // category
  Category *string `json:"category,omitempty" xml:"category,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  FileIdPath *string `json:"file_id_path,omitempty" xml:"file_id_path,omitempty"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id, either share_id or drive_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // template_id
  TemplateId *string `json:"template_id,omitempty" xml:"template_id,omitempty"`
  // url_expire_sec
  UrlExpireSec *int64 `json:"url_expire_sec,omitempty" xml:"url_expire_sec,omitempty" maximum:"14400" minimum:"10"`
}

func (s CCPGetVideoPreviewPlayInfoRequest) String() string {
  return tea.Prettify(s)
}

func (s CCPGetVideoPreviewPlayInfoRequest) GoString() string {
  return s.String()
}

func (s *CCPGetVideoPreviewPlayInfoRequest) SetAdditionData(v map[string]interface{}) *CCPGetVideoPreviewPlayInfoRequest {
  s.AdditionData = v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoRequest) SetCategory(v string) *CCPGetVideoPreviewPlayInfoRequest {
  s.Category = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoRequest) SetDriveId(v string) *CCPGetVideoPreviewPlayInfoRequest {
  s.DriveId = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoRequest) SetFileId(v string) *CCPGetVideoPreviewPlayInfoRequest {
  s.FileId = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoRequest) SetFileIdPath(v string) *CCPGetVideoPreviewPlayInfoRequest {
  s.FileIdPath = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoRequest) SetLocation(v string) *CCPGetVideoPreviewPlayInfoRequest {
  s.Location = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoRequest) SetReferer(v string) *CCPGetVideoPreviewPlayInfoRequest {
  s.Referer = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoRequest) SetShareId(v string) *CCPGetVideoPreviewPlayInfoRequest {
  s.ShareId = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoRequest) SetSignToken(v string) *CCPGetVideoPreviewPlayInfoRequest {
  s.SignToken = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoRequest) SetTemplateId(v string) *CCPGetVideoPreviewPlayInfoRequest {
  s.TemplateId = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoRequest) SetUrlExpireSec(v int64) *CCPGetVideoPreviewPlayInfoRequest {
  s.UrlExpireSec = &v
  return s
}

/**
 * 获取转码信息响应
 */
type CCPGetVideoPreviewPlayInfoResponse struct {
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  VideoPreviewPlayInfo *VideoPreviewPlayInfoResponse `json:"video_preview_play_info,omitempty" xml:"video_preview_play_info,omitempty"`
}

func (s CCPGetVideoPreviewPlayInfoResponse) String() string {
  return tea.Prettify(s)
}

func (s CCPGetVideoPreviewPlayInfoResponse) GoString() string {
  return s.String()
}

func (s *CCPGetVideoPreviewPlayInfoResponse) SetDomainId(v string) *CCPGetVideoPreviewPlayInfoResponse {
  s.DomainId = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoResponse) SetDriveId(v string) *CCPGetVideoPreviewPlayInfoResponse {
  s.DriveId = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoResponse) SetFileId(v string) *CCPGetVideoPreviewPlayInfoResponse {
  s.FileId = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoResponse) SetShareId(v string) *CCPGetVideoPreviewPlayInfoResponse {
  s.ShareId = &v
  return s
}

func (s *CCPGetVideoPreviewPlayInfoResponse) SetVideoPreviewPlayInfo(v *VideoPreviewPlayInfoResponse) *CCPGetVideoPreviewPlayInfoResponse {
  s.VideoPreviewPlayInfo = v
  return s
}

/**
 * 遍历文件
 */
type CCPWalkFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // all
  All *bool `json:"all,omitempty" xml:"all,omitempty"`
  // category
  Category *string `json:"category,omitempty" xml:"category,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // fields
  Fields *string `json:"fields,omitempty" xml:"fields,omitempty"`
  ImageCroppingAspectRatios []*string `json:"image_cropping_aspect_ratios,omitempty" xml:"image_cropping_aspect_ratios,omitempty" type:"Repeated"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // limit
  Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"0"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // marker
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  // order_by
  OrderBy *string `json:"order_by,omitempty" xml:"order_by,omitempty"`
  // order_direction
  OrderDirection *string `json:"order_direction,omitempty" xml:"order_direction,omitempty"`
  // ParentFileID
  ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" require:"true" maxLength:"50" minLength:"4" pattern:"[a-z0-9.-_]{1,50}"`
  ParentFileIdPath *string `json:"parent_file_id_path,omitempty" xml:"parent_file_id_path,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id, either share_id or drive_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // starred
  Starred *bool `json:"starred,omitempty" xml:"starred,omitempty"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // url_expire_sec
  UrlExpireSec *int64 `json:"url_expire_sec,omitempty" xml:"url_expire_sec,omitempty" maximum:"14400" minimum:"10"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s CCPWalkFileRequest) String() string {
  return tea.Prettify(s)
}

func (s CCPWalkFileRequest) GoString() string {
  return s.String()
}

func (s *CCPWalkFileRequest) SetAdditionData(v map[string]interface{}) *CCPWalkFileRequest {
  s.AdditionData = v
  return s
}

func (s *CCPWalkFileRequest) SetAll(v bool) *CCPWalkFileRequest {
  s.All = &v
  return s
}

func (s *CCPWalkFileRequest) SetCategory(v string) *CCPWalkFileRequest {
  s.Category = &v
  return s
}

func (s *CCPWalkFileRequest) SetDriveId(v string) *CCPWalkFileRequest {
  s.DriveId = &v
  return s
}

func (s *CCPWalkFileRequest) SetFields(v string) *CCPWalkFileRequest {
  s.Fields = &v
  return s
}

func (s *CCPWalkFileRequest) SetImageCroppingAspectRatios(v []*string) *CCPWalkFileRequest {
  s.ImageCroppingAspectRatios = v
  return s
}

func (s *CCPWalkFileRequest) SetImageThumbnailProcess(v string) *CCPWalkFileRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *CCPWalkFileRequest) SetImageUrlProcess(v string) *CCPWalkFileRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *CCPWalkFileRequest) SetLimit(v int64) *CCPWalkFileRequest {
  s.Limit = &v
  return s
}

func (s *CCPWalkFileRequest) SetLocation(v string) *CCPWalkFileRequest {
  s.Location = &v
  return s
}

func (s *CCPWalkFileRequest) SetMarker(v string) *CCPWalkFileRequest {
  s.Marker = &v
  return s
}

func (s *CCPWalkFileRequest) SetOfficeThumbnailProcess(v string) *CCPWalkFileRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *CCPWalkFileRequest) SetOrderBy(v string) *CCPWalkFileRequest {
  s.OrderBy = &v
  return s
}

func (s *CCPWalkFileRequest) SetOrderDirection(v string) *CCPWalkFileRequest {
  s.OrderDirection = &v
  return s
}

func (s *CCPWalkFileRequest) SetParentFileId(v string) *CCPWalkFileRequest {
  s.ParentFileId = &v
  return s
}

func (s *CCPWalkFileRequest) SetParentFileIdPath(v string) *CCPWalkFileRequest {
  s.ParentFileIdPath = &v
  return s
}

func (s *CCPWalkFileRequest) SetReferer(v string) *CCPWalkFileRequest {
  s.Referer = &v
  return s
}

func (s *CCPWalkFileRequest) SetShareId(v string) *CCPWalkFileRequest {
  s.ShareId = &v
  return s
}

func (s *CCPWalkFileRequest) SetSignToken(v string) *CCPWalkFileRequest {
  s.SignToken = &v
  return s
}

func (s *CCPWalkFileRequest) SetStarred(v bool) *CCPWalkFileRequest {
  s.Starred = &v
  return s
}

func (s *CCPWalkFileRequest) SetStatus(v string) *CCPWalkFileRequest {
  s.Status = &v
  return s
}

func (s *CCPWalkFileRequest) SetType(v string) *CCPWalkFileRequest {
  s.Type = &v
  return s
}

func (s *CCPWalkFileRequest) SetUrlExpireSec(v int64) *CCPWalkFileRequest {
  s.UrlExpireSec = &v
  return s
}

func (s *CCPWalkFileRequest) SetVideoThumbnailProcess(v string) *CCPWalkFileRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * 列举文件response
 */
type CCPWalkFileResponse struct {
  // items
  Items []*BaseCCPFileResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
  // next_marker
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s CCPWalkFileResponse) String() string {
  return tea.Prettify(s)
}

func (s CCPWalkFileResponse) GoString() string {
  return s.String()
}

func (s *CCPWalkFileResponse) SetItems(v []*BaseCCPFileResponse) *CCPWalkFileResponse {
  s.Items = v
  return s
}

func (s *CCPWalkFileResponse) SetNextMarker(v string) *CCPWalkFileResponse {
  s.NextMarker = &v
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
 * cancel_share_link request
 */
type CancelShareLinkRequest struct {
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
}

func (s CancelShareLinkRequest) String() string {
  return tea.Prettify(s)
}

func (s CancelShareLinkRequest) GoString() string {
  return s.String()
}

func (s *CancelShareLinkRequest) SetShareId(v string) *CancelShareLinkRequest {
  s.ShareId = &v
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
type CertInfo struct {
  CertID *string `json:"CertID,omitempty" xml:"CertID,omitempty"`
  // cert body
  CertBody *string `json:"cert_body,omitempty" xml:"cert_body,omitempty" require:"true"`
  // cert name
  CertName *string `json:"cert_name,omitempty" xml:"cert_name,omitempty" require:"true"`
  // cert privatekey
  CertPrivatekey *string `json:"cert_privatekey,omitempty" xml:"cert_privatekey,omitempty" require:"true"`
}

func (s CertInfo) String() string {
  return tea.Prettify(s)
}

func (s CertInfo) GoString() string {
  return s.String()
}

func (s *CertInfo) SetCertID(v string) *CertInfo {
  s.CertID = &v
  return s
}

func (s *CertInfo) SetCertBody(v string) *CertInfo {
  s.CertBody = &v
  return s
}

func (s *CertInfo) SetCertName(v string) *CertInfo {
  s.CertName = &v
  return s
}

func (s *CertInfo) SetCertPrivatekey(v string) *CertInfo {
  s.CertPrivatekey = &v
  return s
}

/**
 * 合并文件上传任务
 */
type CompleteFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // part_info_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
}

func (s CompleteFileRequest) String() string {
  return tea.Prettify(s)
}

func (s CompleteFileRequest) GoString() string {
  return s.String()
}

func (s *CompleteFileRequest) SetAdditionData(v map[string]interface{}) *CompleteFileRequest {
  s.AdditionData = v
  return s
}

func (s *CompleteFileRequest) SetDriveId(v string) *CompleteFileRequest {
  s.DriveId = &v
  return s
}

func (s *CompleteFileRequest) SetFileId(v string) *CompleteFileRequest {
  s.FileId = &v
  return s
}

func (s *CompleteFileRequest) SetPartInfoList(v []*UploadPartInfo) *CompleteFileRequest {
  s.PartInfoList = v
  return s
}

func (s *CompleteFileRequest) SetShareId(v string) *CompleteFileRequest {
  s.ShareId = &v
  return s
}

func (s *CompleteFileRequest) SetUploadId(v string) *CompleteFileRequest {
  s.UploadId = &v
  return s
}

/**
 * complete file response
 */
type CompleteFileResponse struct {
  // category
  Category *string `json:"category,omitempty" xml:"category,omitempty"`
  // CharacteristicHash
  CharacteristicHash *string `json:"characteristic_hash,omitempty" xml:"characteristic_hash,omitempty"`
  // Content Hash
  ContentHash *string `json:"content_hash,omitempty" xml:"content_hash,omitempty"`
  // content_hash_name
  ContentHashName *string `json:"content_hash_name,omitempty" xml:"content_hash_name,omitempty"`
  // content_type
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // crc64_hash
  Crc64Hash *string `json:"crc64_hash,omitempty" xml:"crc64_hash,omitempty"`
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // DomainID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // download_url
  DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // encrypt_mode
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // file_extension
  FileExtension *string `json:"file_extension,omitempty" xml:"file_extension,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // Hidden
  // type: boolean
  Hidden *bool `json:"hidden,omitempty" xml:"hidden,omitempty"`
  ImageMediaMetadata *ImageMediaResponse `json:"image_media_metadata,omitempty" xml:"image_media_metadata,omitempty"`
  // labels
  Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  Meta *string `json:"meta,omitempty" xml:"meta,omitempty"`
  // name
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
  // parent_file_id
  ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // PunishFlag
  PunishFlag *int64 `json:"punish_flag,omitempty" xml:"punish_flag,omitempty"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // starred
  // type: boolean
  Starred *bool `json:"starred,omitempty" xml:"starred,omitempty"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  StreamLocations map[string]interface{} `json:"stream_locations,omitempty" xml:"stream_locations,omitempty"`
  // @Deprecated streams url info
  StreamsInfo map[string]interface{} `json:"streams_info,omitempty" xml:"streams_info,omitempty"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // trashed_at
  TrashedAt *string `json:"trashed_at,omitempty" xml:"trashed_at,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
  // user_meta
  UserMeta *string `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
  VideoMediaMetadata *VideoMediaResponse `json:"video_media_metadata,omitempty" xml:"video_media_metadata,omitempty"`
  VideoPreviewMetadata *VideoPreviewResponse `json:"video_preview_metadata,omitempty" xml:"video_preview_metadata,omitempty"`
}

func (s CompleteFileResponse) String() string {
  return tea.Prettify(s)
}

func (s CompleteFileResponse) GoString() string {
  return s.String()
}

func (s *CompleteFileResponse) SetCategory(v string) *CompleteFileResponse {
  s.Category = &v
  return s
}

func (s *CompleteFileResponse) SetCharacteristicHash(v string) *CompleteFileResponse {
  s.CharacteristicHash = &v
  return s
}

func (s *CompleteFileResponse) SetContentHash(v string) *CompleteFileResponse {
  s.ContentHash = &v
  return s
}

func (s *CompleteFileResponse) SetContentHashName(v string) *CompleteFileResponse {
  s.ContentHashName = &v
  return s
}

func (s *CompleteFileResponse) SetContentType(v string) *CompleteFileResponse {
  s.ContentType = &v
  return s
}

func (s *CompleteFileResponse) SetCrc64Hash(v string) *CompleteFileResponse {
  s.Crc64Hash = &v
  return s
}

func (s *CompleteFileResponse) SetCreatedAt(v string) *CompleteFileResponse {
  s.CreatedAt = &v
  return s
}

func (s *CompleteFileResponse) SetDescription(v string) *CompleteFileResponse {
  s.Description = &v
  return s
}

func (s *CompleteFileResponse) SetDomainId(v string) *CompleteFileResponse {
  s.DomainId = &v
  return s
}

func (s *CompleteFileResponse) SetDownloadUrl(v string) *CompleteFileResponse {
  s.DownloadUrl = &v
  return s
}

func (s *CompleteFileResponse) SetDriveId(v string) *CompleteFileResponse {
  s.DriveId = &v
  return s
}

func (s *CompleteFileResponse) SetEncryptMode(v string) *CompleteFileResponse {
  s.EncryptMode = &v
  return s
}

func (s *CompleteFileResponse) SetFileExtension(v string) *CompleteFileResponse {
  s.FileExtension = &v
  return s
}

func (s *CompleteFileResponse) SetFileId(v string) *CompleteFileResponse {
  s.FileId = &v
  return s
}

func (s *CompleteFileResponse) SetHidden(v bool) *CompleteFileResponse {
  s.Hidden = &v
  return s
}

func (s *CompleteFileResponse) SetImageMediaMetadata(v *ImageMediaResponse) *CompleteFileResponse {
  s.ImageMediaMetadata = v
  return s
}

func (s *CompleteFileResponse) SetLabels(v []*string) *CompleteFileResponse {
  s.Labels = v
  return s
}

func (s *CompleteFileResponse) SetLocation(v string) *CompleteFileResponse {
  s.Location = &v
  return s
}

func (s *CompleteFileResponse) SetMeta(v string) *CompleteFileResponse {
  s.Meta = &v
  return s
}

func (s *CompleteFileResponse) SetName(v string) *CompleteFileResponse {
  s.Name = &v
  return s
}

func (s *CompleteFileResponse) SetParentFileId(v string) *CompleteFileResponse {
  s.ParentFileId = &v
  return s
}

func (s *CompleteFileResponse) SetPunishFlag(v int64) *CompleteFileResponse {
  s.PunishFlag = &v
  return s
}

func (s *CompleteFileResponse) SetShareId(v string) *CompleteFileResponse {
  s.ShareId = &v
  return s
}

func (s *CompleteFileResponse) SetSize(v int64) *CompleteFileResponse {
  s.Size = &v
  return s
}

func (s *CompleteFileResponse) SetStarred(v bool) *CompleteFileResponse {
  s.Starred = &v
  return s
}

func (s *CompleteFileResponse) SetStatus(v string) *CompleteFileResponse {
  s.Status = &v
  return s
}

func (s *CompleteFileResponse) SetStreamLocations(v map[string]interface{}) *CompleteFileResponse {
  s.StreamLocations = v
  return s
}

func (s *CompleteFileResponse) SetStreamsInfo(v map[string]interface{}) *CompleteFileResponse {
  s.StreamsInfo = v
  return s
}

func (s *CompleteFileResponse) SetThumbnail(v string) *CompleteFileResponse {
  s.Thumbnail = &v
  return s
}

func (s *CompleteFileResponse) SetTrashedAt(v string) *CompleteFileResponse {
  s.TrashedAt = &v
  return s
}

func (s *CompleteFileResponse) SetType(v string) *CompleteFileResponse {
  s.Type = &v
  return s
}

func (s *CompleteFileResponse) SetUpdatedAt(v string) *CompleteFileResponse {
  s.UpdatedAt = &v
  return s
}

func (s *CompleteFileResponse) SetUploadId(v string) *CompleteFileResponse {
  s.UploadId = &v
  return s
}

func (s *CompleteFileResponse) SetUrl(v string) *CompleteFileResponse {
  s.Url = &v
  return s
}

func (s *CompleteFileResponse) SetUserMeta(v string) *CompleteFileResponse {
  s.UserMeta = &v
  return s
}

func (s *CompleteFileResponse) SetVideoMediaMetadata(v *VideoMediaResponse) *CompleteFileResponse {
  s.VideoMediaMetadata = v
  return s
}

func (s *CompleteFileResponse) SetVideoPreviewMetadata(v *VideoPreviewResponse) *CompleteFileResponse {
  s.VideoPreviewMetadata = v
  return s
}

/**
 * 文件拷贝
 */
type CopyFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // auto_rename
  // type: boolean
  AutoRename *bool `json:"auto_rename,omitempty" xml:"auto_rename,omitempty"`
  BatchId *string `json:"batch_id,omitempty" xml:"batch_id,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  FileIdPath *string `json:"file_id_path,omitempty" xml:"file_id_path,omitempty"`
  // new_name
  NewName *string `json:"new_name,omitempty" xml:"new_name,omitempty" maxLength:"1024" minLength:"1"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id, either share_id or drive_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // to_drive_id
  ToDriveId *string `json:"to_drive_id,omitempty" xml:"to_drive_id,omitempty" pattern:"[0-9]+"`
  // to_parent_file_id
  ToParentFileId *string `json:"to_parent_file_id,omitempty" xml:"to_parent_file_id,omitempty" require:"true" maxLength:"50" minLength:"4" pattern:"[a-z0-9.-_]{1,50}"`
  // to_drive_id
  ToShareId *string `json:"to_share_id,omitempty" xml:"to_share_id,omitempty" pattern:"[0-9]+"`
}

func (s CopyFileRequest) String() string {
  return tea.Prettify(s)
}

func (s CopyFileRequest) GoString() string {
  return s.String()
}

func (s *CopyFileRequest) SetAdditionData(v map[string]interface{}) *CopyFileRequest {
  s.AdditionData = v
  return s
}

func (s *CopyFileRequest) SetAutoRename(v bool) *CopyFileRequest {
  s.AutoRename = &v
  return s
}

func (s *CopyFileRequest) SetBatchId(v string) *CopyFileRequest {
  s.BatchId = &v
  return s
}

func (s *CopyFileRequest) SetDriveId(v string) *CopyFileRequest {
  s.DriveId = &v
  return s
}

func (s *CopyFileRequest) SetFileId(v string) *CopyFileRequest {
  s.FileId = &v
  return s
}

func (s *CopyFileRequest) SetFileIdPath(v string) *CopyFileRequest {
  s.FileIdPath = &v
  return s
}

func (s *CopyFileRequest) SetNewName(v string) *CopyFileRequest {
  s.NewName = &v
  return s
}

func (s *CopyFileRequest) SetReferer(v string) *CopyFileRequest {
  s.Referer = &v
  return s
}

func (s *CopyFileRequest) SetShareId(v string) *CopyFileRequest {
  s.ShareId = &v
  return s
}

func (s *CopyFileRequest) SetToDriveId(v string) *CopyFileRequest {
  s.ToDriveId = &v
  return s
}

func (s *CopyFileRequest) SetToParentFileId(v string) *CopyFileRequest {
  s.ToParentFileId = &v
  return s
}

func (s *CopyFileRequest) SetToShareId(v string) *CopyFileRequest {
  s.ToShareId = &v
  return s
}

/**
 * 文件拷贝 response
 */
type CopyFileResponse struct {
  // async_task_id
  AsyncTaskId *string `json:"async_task_id,omitempty" xml:"async_task_id,omitempty"`
  // DomainID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
}

func (s CopyFileResponse) String() string {
  return tea.Prettify(s)
}

func (s CopyFileResponse) GoString() string {
  return s.String()
}

func (s *CopyFileResponse) SetAsyncTaskId(v string) *CopyFileResponse {
  s.AsyncTaskId = &v
  return s
}

func (s *CopyFileResponse) SetDomainId(v string) *CopyFileResponse {
  s.DomainId = &v
  return s
}

func (s *CopyFileResponse) SetDriveId(v string) *CopyFileResponse {
  s.DriveId = &v
  return s
}

func (s *CopyFileResponse) SetFileId(v string) *CopyFileResponse {
  s.FileId = &v
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
 * 
 */
type CreateDetail struct {
  // CreateType
  CreateType *string `json:"create_type,omitempty" xml:"create_type,omitempty"`
  // SrcFileID
  SrcFileId *string `json:"src_file_id,omitempty" xml:"src_file_id,omitempty"`
}

func (s CreateDetail) String() string {
  return tea.Prettify(s)
}

func (s CreateDetail) GoString() string {
  return s.String()
}

func (s *CreateDetail) SetCreateType(v string) *CreateDetail {
  s.CreateType = &v
  return s
}

func (s *CreateDetail) SetSrcFileId(v string) *CreateDetail {
  s.SrcFileId = &v
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
  Benefits map[string]interface{} `json:"benefits,omitempty" xml:"benefits,omitempty"`
  // Domain 创建时间
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // 数据 Hash 算法
  DataHashName *string `json:"data_hash_name,omitempty" xml:"data_hash_name,omitempty"`
  DefaultSuperAdminConfig *DomainSuperAdminConfig `json:"default_super_admin_config,omitempty" xml:"default_super_admin_config,omitempty"`
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
  // 预付费domain过期时间
  ExpireTime *int64 `json:"expire_time,omitempty" xml:"expire_time,omitempty"`
  // 是否开启了自动初始化 Drive
  InitDriveEnable *bool `json:"init_drive_enable,omitempty" xml:"init_drive_enable,omitempty"`
  // 自动初始化 Drive 大小
  InitDriveSize *int64 `json:"init_drive_size,omitempty" xml:"init_drive_size,omitempty"`
  // 自动初始化 Drive 所用 Store ID
  InitDriveStoreId *string `json:"init_drive_store_id,omitempty" xml:"init_drive_store_id,omitempty"`
  // Domain 类型
  Mode *string `json:"mode,omitempty" xml:"mode,omitempty"`
  OfficePreviewConfig *OfficePreviewConfig `json:"office_preview_config,omitempty" xml:"office_preview_config,omitempty"`
  // Domain 类型
  PathType *string `json:"path_type,omitempty" xml:"path_type,omitempty"`
  // 预付费套餐
  PrepaidPackage *string `json:"prepaid_package,omitempty" xml:"prepaid_package,omitempty"`
  PublishedAppAccessStrategy *AppAccessStrategy `json:"published_app_access_strategy,omitempty" xml:"published_app_access_strategy,omitempty"`
  // Domain ServiceCode
  ServiceCode *string `json:"service_code,omitempty" xml:"service_code,omitempty"`
  // 是否开启了共享
  Sharable *bool `json:"sharable,omitempty" xml:"sharable,omitempty"`
  // 是否开启了分享
  ShareLinkEnabled *bool `json:"share_link_enabled,omitempty" xml:"share_link_enabled,omitempty"`
  // 容量配额
  SizeQuota *int64 `json:"size_quota,omitempty" xml:"size_quota,omitempty"`
  // SPI 实例 id
  SpiInstanceId *string `json:"spi_instance_id,omitempty" xml:"spi_instance_id,omitempty"`
  // domain状态：创建中，正常，已过期
  Status *int64 `json:"status,omitempty" xml:"status,omitempty"`
  // 存储级别
  StoreLevel *string `json:"store_level,omitempty" xml:"store_level,omitempty"`
  // 存储 Region 列表
  StoreRegionList []*string `json:"store_region_list,omitempty" xml:"store_region_list,omitempty" type:"Repeated"`
  // Domain 更新时间
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // 用户数配额
  UserCountQuota *int64 `json:"user_count_quota,omitempty" xml:"user_count_quota,omitempty"`
  VideoPreviewConfig *VideoPreviewConfig `json:"video_preview_config,omitempty" xml:"video_preview_config,omitempty"`
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

func (s *CreateDomainResponse) SetBenefits(v map[string]interface{}) *CreateDomainResponse {
  s.Benefits = v
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

func (s *CreateDomainResponse) SetDefaultSuperAdminConfig(v *DomainSuperAdminConfig) *CreateDomainResponse {
  s.DefaultSuperAdminConfig = v
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

func (s *CreateDomainResponse) SetExpireTime(v int64) *CreateDomainResponse {
  s.ExpireTime = &v
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

func (s *CreateDomainResponse) SetOfficePreviewConfig(v *OfficePreviewConfig) *CreateDomainResponse {
  s.OfficePreviewConfig = v
  return s
}

func (s *CreateDomainResponse) SetPathType(v string) *CreateDomainResponse {
  s.PathType = &v
  return s
}

func (s *CreateDomainResponse) SetPrepaidPackage(v string) *CreateDomainResponse {
  s.PrepaidPackage = &v
  return s
}

func (s *CreateDomainResponse) SetPublishedAppAccessStrategy(v *AppAccessStrategy) *CreateDomainResponse {
  s.PublishedAppAccessStrategy = v
  return s
}

func (s *CreateDomainResponse) SetServiceCode(v string) *CreateDomainResponse {
  s.ServiceCode = &v
  return s
}

func (s *CreateDomainResponse) SetSharable(v bool) *CreateDomainResponse {
  s.Sharable = &v
  return s
}

func (s *CreateDomainResponse) SetShareLinkEnabled(v bool) *CreateDomainResponse {
  s.ShareLinkEnabled = &v
  return s
}

func (s *CreateDomainResponse) SetSizeQuota(v int64) *CreateDomainResponse {
  s.SizeQuota = &v
  return s
}

func (s *CreateDomainResponse) SetSpiInstanceId(v string) *CreateDomainResponse {
  s.SpiInstanceId = &v
  return s
}

func (s *CreateDomainResponse) SetStatus(v int64) *CreateDomainResponse {
  s.Status = &v
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

func (s *CreateDomainResponse) SetUserCountQuota(v int64) *CreateDomainResponse {
  s.UserCountQuota = &v
  return s
}

func (s *CreateDomainResponse) SetVideoPreviewConfig(v *VideoPreviewConfig) *CreateDomainResponse {
  s.VideoPreviewConfig = v
  return s
}

/**
 * create drive request
 */
type CreateDriveRequest struct {
  // 是否默认drive, 只允许设置一个默认drive
  Default *bool `json:"default,omitempty" xml:"default,omitempty"`
  // 描述信息
  Description *string `json:"description,omitempty" xml:"description,omitempty" maxLength:"1024"`
  // Drive 名称
  DriveName *string `json:"drive_name,omitempty" xml:"drive_name,omitempty" require:"true" maxLength:"1024"`
  // Drive类型
  DriveType *string `json:"drive_type,omitempty" xml:"drive_type,omitempty"`
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // 所属者
  Owner *string `json:"owner,omitempty" xml:"owner,omitempty" require:"true"`
  // 所属者
  OwnerType *string `json:"owner_type,omitempty" xml:"owner_type,omitempty" require:"true"`
  // domain的PathType为OSSPath时必选。 Drive存储基于store的相对路径
  RelativePath *string `json:"relative_path,omitempty" xml:"relative_path,omitempty"`
  // 状态
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // StoreID , domain的PathType为OSSPath时必选
  StoreId *string `json:"store_id,omitempty" xml:"store_id,omitempty"`
  // Subdomain ID
  SubdomainId *string `json:"subdomain_id,omitempty" xml:"subdomain_id,omitempty"`
  // 总大小,单位Byte [如果设置 -1 代表不限制]
  TotalSize *int64 `json:"total_size,omitempty" xml:"total_size,omitempty"`
}

func (s CreateDriveRequest) String() string {
  return tea.Prettify(s)
}

func (s CreateDriveRequest) GoString() string {
  return s.String()
}

func (s *CreateDriveRequest) SetDefault(v bool) *CreateDriveRequest {
  s.Default = &v
  return s
}

func (s *CreateDriveRequest) SetDescription(v string) *CreateDriveRequest {
  s.Description = &v
  return s
}

func (s *CreateDriveRequest) SetDriveName(v string) *CreateDriveRequest {
  s.DriveName = &v
  return s
}

func (s *CreateDriveRequest) SetDriveType(v string) *CreateDriveRequest {
  s.DriveType = &v
  return s
}

func (s *CreateDriveRequest) SetEncryptMode(v string) *CreateDriveRequest {
  s.EncryptMode = &v
  return s
}

func (s *CreateDriveRequest) SetLocation(v string) *CreateDriveRequest {
  s.Location = &v
  return s
}

func (s *CreateDriveRequest) SetOwner(v string) *CreateDriveRequest {
  s.Owner = &v
  return s
}

func (s *CreateDriveRequest) SetOwnerType(v string) *CreateDriveRequest {
  s.OwnerType = &v
  return s
}

func (s *CreateDriveRequest) SetRelativePath(v string) *CreateDriveRequest {
  s.RelativePath = &v
  return s
}

func (s *CreateDriveRequest) SetStatus(v string) *CreateDriveRequest {
  s.Status = &v
  return s
}

func (s *CreateDriveRequest) SetStoreId(v string) *CreateDriveRequest {
  s.StoreId = &v
  return s
}

func (s *CreateDriveRequest) SetSubdomainId(v string) *CreateDriveRequest {
  s.SubdomainId = &v
  return s
}

func (s *CreateDriveRequest) SetTotalSize(v int64) *CreateDriveRequest {
  s.TotalSize = &v
  return s
}

/**
 * Create drive response
 */
type CreateDriveResponse struct {
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // Drive ID
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty"`
}

func (s CreateDriveResponse) String() string {
  return tea.Prettify(s)
}

func (s CreateDriveResponse) GoString() string {
  return s.String()
}

func (s *CreateDriveResponse) SetDomainId(v string) *CreateDriveResponse {
  s.DomainId = &v
  return s
}

func (s *CreateDriveResponse) SetDriveId(v string) *CreateDriveResponse {
  s.DriveId = &v
  return s
}

/**
 * 创建文件
 */
type CreateFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  AutoRename *bool `json:"auto_rename,omitempty" xml:"auto_rename,omitempty"`
  // check_name_mode
  CheckNameMode *string `json:"check_name_mode,omitempty" xml:"check_name_mode,omitempty"`
  // content_hash
  ContentHash *string `json:"content_hash,omitempty" xml:"content_hash,omitempty"`
  // content_hash_name
  ContentHashName *string `json:"content_hash_name,omitempty" xml:"content_hash_name,omitempty"`
  // ContentMd5
  ContentMd5 *string `json:"content_md5,omitempty" xml:"content_md5,omitempty"`
  // ContentType
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty" maxLength:"1024" minLength:"0"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // encrypt_mode
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty"`
  // force_upload_to_location
  ForceUploadToLocation *bool `json:"force_upload_to_location,omitempty" xml:"force_upload_to_location,omitempty"`
  // hidden
  Hidden *bool `json:"hidden,omitempty" xml:"hidden,omitempty"`
  ImageMediaMetadata *ImageMediaMetadata `json:"image_media_metadata,omitempty" xml:"image_media_metadata,omitempty"`
  // labels
  Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
  // last_updated_at
  LastUpdatedAt *string `json:"last_updated_at,omitempty" xml:"last_updated_at,omitempty"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  Meta *string `json:"meta,omitempty" xml:"meta,omitempty"`
  // Name
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" maxLength:"1024" minLength:"1"`
  ParallelUpload *bool `json:"parallel_upload,omitempty" xml:"parallel_upload,omitempty"`
  // parent_file_id
  ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" require:"true" maxLength:"50" minLength:"4" pattern:"[a-z0-9]{1,50}"`
  ParentFileIdPath *string `json:"parent_file_id_path,omitempty" xml:"parent_file_id_path,omitempty"`
  // part_info_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  // pre_hash
  PreHash *string `json:"pre_hash,omitempty" xml:"pre_hash,omitempty"`
  // proof_code
  ProofCode *string `json:"proof_code,omitempty" xml:"proof_code,omitempty"`
  // proof_version
  ProofVersion *string `json:"proof_version,omitempty" xml:"proof_version,omitempty"`
  // share_id
  // example
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // streams_info
  StreamsInfo map[string]interface{} `json:"streams_info,omitempty" xml:"streams_info,omitempty"`
  // Type
  Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
  // user_meta
  UserMeta *string `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
  VideoMediaMetadata *VideoMediaMetadata `json:"video_media_metadata,omitempty" xml:"video_media_metadata,omitempty"`
}

func (s CreateFileRequest) String() string {
  return tea.Prettify(s)
}

func (s CreateFileRequest) GoString() string {
  return s.String()
}

func (s *CreateFileRequest) SetAdditionData(v map[string]interface{}) *CreateFileRequest {
  s.AdditionData = v
  return s
}

func (s *CreateFileRequest) SetAutoRename(v bool) *CreateFileRequest {
  s.AutoRename = &v
  return s
}

func (s *CreateFileRequest) SetCheckNameMode(v string) *CreateFileRequest {
  s.CheckNameMode = &v
  return s
}

func (s *CreateFileRequest) SetContentHash(v string) *CreateFileRequest {
  s.ContentHash = &v
  return s
}

func (s *CreateFileRequest) SetContentHashName(v string) *CreateFileRequest {
  s.ContentHashName = &v
  return s
}

func (s *CreateFileRequest) SetContentMd5(v string) *CreateFileRequest {
  s.ContentMd5 = &v
  return s
}

func (s *CreateFileRequest) SetContentType(v string) *CreateFileRequest {
  s.ContentType = &v
  return s
}

func (s *CreateFileRequest) SetDescription(v string) *CreateFileRequest {
  s.Description = &v
  return s
}

func (s *CreateFileRequest) SetDriveId(v string) *CreateFileRequest {
  s.DriveId = &v
  return s
}

func (s *CreateFileRequest) SetEncryptMode(v string) *CreateFileRequest {
  s.EncryptMode = &v
  return s
}

func (s *CreateFileRequest) SetFileId(v string) *CreateFileRequest {
  s.FileId = &v
  return s
}

func (s *CreateFileRequest) SetForceUploadToLocation(v bool) *CreateFileRequest {
  s.ForceUploadToLocation = &v
  return s
}

func (s *CreateFileRequest) SetHidden(v bool) *CreateFileRequest {
  s.Hidden = &v
  return s
}

func (s *CreateFileRequest) SetImageMediaMetadata(v *ImageMediaMetadata) *CreateFileRequest {
  s.ImageMediaMetadata = v
  return s
}

func (s *CreateFileRequest) SetLabels(v []*string) *CreateFileRequest {
  s.Labels = v
  return s
}

func (s *CreateFileRequest) SetLastUpdatedAt(v string) *CreateFileRequest {
  s.LastUpdatedAt = &v
  return s
}

func (s *CreateFileRequest) SetLocation(v string) *CreateFileRequest {
  s.Location = &v
  return s
}

func (s *CreateFileRequest) SetMeta(v string) *CreateFileRequest {
  s.Meta = &v
  return s
}

func (s *CreateFileRequest) SetName(v string) *CreateFileRequest {
  s.Name = &v
  return s
}

func (s *CreateFileRequest) SetParallelUpload(v bool) *CreateFileRequest {
  s.ParallelUpload = &v
  return s
}

func (s *CreateFileRequest) SetParentFileId(v string) *CreateFileRequest {
  s.ParentFileId = &v
  return s
}

func (s *CreateFileRequest) SetParentFileIdPath(v string) *CreateFileRequest {
  s.ParentFileIdPath = &v
  return s
}

func (s *CreateFileRequest) SetPartInfoList(v []*UploadPartInfo) *CreateFileRequest {
  s.PartInfoList = v
  return s
}

func (s *CreateFileRequest) SetPreHash(v string) *CreateFileRequest {
  s.PreHash = &v
  return s
}

func (s *CreateFileRequest) SetProofCode(v string) *CreateFileRequest {
  s.ProofCode = &v
  return s
}

func (s *CreateFileRequest) SetProofVersion(v string) *CreateFileRequest {
  s.ProofVersion = &v
  return s
}

func (s *CreateFileRequest) SetShareId(v string) *CreateFileRequest {
  s.ShareId = &v
  return s
}

func (s *CreateFileRequest) SetSize(v int64) *CreateFileRequest {
  s.Size = &v
  return s
}

func (s *CreateFileRequest) SetStreamsInfo(v map[string]interface{}) *CreateFileRequest {
  s.StreamsInfo = v
  return s
}

func (s *CreateFileRequest) SetType(v string) *CreateFileRequest {
  s.Type = &v
  return s
}

func (s *CreateFileRequest) SetUserMeta(v string) *CreateFileRequest {
  s.UserMeta = &v
  return s
}

func (s *CreateFileRequest) SetVideoMediaMetadata(v *VideoMediaMetadata) *CreateFileRequest {
  s.VideoMediaMetadata = v
  return s
}

/**
 * Create file response
 */
type CreateFileResponse struct {
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // encrypt_mode
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // exist
  // type: boolean
  Exist *bool `json:"exist,omitempty" xml:"exist,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // file_name
  FileName *string `json:"file_name,omitempty" xml:"file_name,omitempty" maxLength:"255" minLength:"1"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // parent_file_id
  ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // part_info_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  // rapid_upload
  // type: boolean
  RapidUpload *bool `json:"rapid_upload,omitempty" xml:"rapid_upload,omitempty"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // streams_upload_info
  StreamsUploadInfo map[string]interface{} `json:"streams_upload_info,omitempty" xml:"streams_upload_info,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
}

func (s CreateFileResponse) String() string {
  return tea.Prettify(s)
}

func (s CreateFileResponse) GoString() string {
  return s.String()
}

func (s *CreateFileResponse) SetDomainId(v string) *CreateFileResponse {
  s.DomainId = &v
  return s
}

func (s *CreateFileResponse) SetDriveId(v string) *CreateFileResponse {
  s.DriveId = &v
  return s
}

func (s *CreateFileResponse) SetEncryptMode(v string) *CreateFileResponse {
  s.EncryptMode = &v
  return s
}

func (s *CreateFileResponse) SetExist(v bool) *CreateFileResponse {
  s.Exist = &v
  return s
}

func (s *CreateFileResponse) SetFileId(v string) *CreateFileResponse {
  s.FileId = &v
  return s
}

func (s *CreateFileResponse) SetFileName(v string) *CreateFileResponse {
  s.FileName = &v
  return s
}

func (s *CreateFileResponse) SetLocation(v string) *CreateFileResponse {
  s.Location = &v
  return s
}

func (s *CreateFileResponse) SetParentFileId(v string) *CreateFileResponse {
  s.ParentFileId = &v
  return s
}

func (s *CreateFileResponse) SetPartInfoList(v []*UploadPartInfo) *CreateFileResponse {
  s.PartInfoList = v
  return s
}

func (s *CreateFileResponse) SetRapidUpload(v bool) *CreateFileResponse {
  s.RapidUpload = &v
  return s
}

func (s *CreateFileResponse) SetStatus(v string) *CreateFileResponse {
  s.Status = &v
  return s
}

func (s *CreateFileResponse) SetStreamsUploadInfo(v map[string]interface{}) *CreateFileResponse {
  s.StreamsUploadInfo = v
  return s
}

func (s *CreateFileResponse) SetType(v string) *CreateFileResponse {
  s.Type = &v
  return s
}

func (s *CreateFileResponse) SetUploadId(v string) *CreateFileResponse {
  s.UploadId = &v
  return s
}

/**
 * create_share_link request
 */
type CreateShareLinkRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty"`
  // file_id_list
  FileIdList []*string `json:"file_id_list,omitempty" xml:"file_id_list,omitempty" maximum:"100" minimum:"1" type:"Repeated"`
  // file_path_list
  FilePathList []*string `json:"file_path_list,omitempty" xml:"file_path_list,omitempty" maximum:"100" minimum:"1" type:"Repeated"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_name
  ShareName *string `json:"share_name,omitempty" xml:"share_name,omitempty"`
  // share_pwd
  SharePwd *string `json:"share_pwd,omitempty" xml:"share_pwd,omitempty" maximum:"64" minimum:"0"`
}

func (s CreateShareLinkRequest) String() string {
  return tea.Prettify(s)
}

func (s CreateShareLinkRequest) GoString() string {
  return s.String()
}

func (s *CreateShareLinkRequest) SetAdditionData(v map[string]interface{}) *CreateShareLinkRequest {
  s.AdditionData = v
  return s
}

func (s *CreateShareLinkRequest) SetDescription(v string) *CreateShareLinkRequest {
  s.Description = &v
  return s
}

func (s *CreateShareLinkRequest) SetDriveId(v string) *CreateShareLinkRequest {
  s.DriveId = &v
  return s
}

func (s *CreateShareLinkRequest) SetExpiration(v string) *CreateShareLinkRequest {
  s.Expiration = &v
  return s
}

func (s *CreateShareLinkRequest) SetFileId(v string) *CreateShareLinkRequest {
  s.FileId = &v
  return s
}

func (s *CreateShareLinkRequest) SetFileIdList(v []*string) *CreateShareLinkRequest {
  s.FileIdList = v
  return s
}

func (s *CreateShareLinkRequest) SetFilePathList(v []*string) *CreateShareLinkRequest {
  s.FilePathList = v
  return s
}

func (s *CreateShareLinkRequest) SetReferer(v string) *CreateShareLinkRequest {
  s.Referer = &v
  return s
}

func (s *CreateShareLinkRequest) SetShareName(v string) *CreateShareLinkRequest {
  s.ShareName = &v
  return s
}

func (s *CreateShareLinkRequest) SetSharePwd(v string) *CreateShareLinkRequest {
  s.SharePwd = &v
  return s
}

/**
 * create_share_link response
 */
type CreateShareLinkResponse struct {
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // creator
  Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // 下载次数
  DownloadCount *int64 `json:"download_count,omitempty" xml:"download_count,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty"`
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // expired
  Expired *bool `json:"expired,omitempty" xml:"expired,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty"`
  // file_id_list
  FileIdList []*string `json:"file_id_list,omitempty" xml:"file_id_list,omitempty" type:"Repeated"`
  // file_id_list
  FilePathList []*string `json:"file_path_list,omitempty" xml:"file_path_list,omitempty" type:"Repeated"`
  // preview_count
  PreviewCount *int64 `json:"preview_count,omitempty" xml:"preview_count,omitempty"`
  // 转存次数
  SaveCount *int64 `json:"save_count,omitempty" xml:"save_count,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // share_msg
  ShareMsg *string `json:"share_msg,omitempty" xml:"share_msg,omitempty"`
  // share_name
  ShareName *string `json:"share_name,omitempty" xml:"share_name,omitempty"`
  // share_policy
  SharePolicy *string `json:"share_policy,omitempty" xml:"share_policy,omitempty"`
  // share_pwd
  SharePwd *string `json:"share_pwd,omitempty" xml:"share_pwd,omitempty"`
  // share_url
  ShareUrl *string `json:"share_url,omitempty" xml:"share_url,omitempty"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s CreateShareLinkResponse) String() string {
  return tea.Prettify(s)
}

func (s CreateShareLinkResponse) GoString() string {
  return s.String()
}

func (s *CreateShareLinkResponse) SetCreatedAt(v string) *CreateShareLinkResponse {
  s.CreatedAt = &v
  return s
}

func (s *CreateShareLinkResponse) SetCreator(v string) *CreateShareLinkResponse {
  s.Creator = &v
  return s
}

func (s *CreateShareLinkResponse) SetDescription(v string) *CreateShareLinkResponse {
  s.Description = &v
  return s
}

func (s *CreateShareLinkResponse) SetDownloadCount(v int64) *CreateShareLinkResponse {
  s.DownloadCount = &v
  return s
}

func (s *CreateShareLinkResponse) SetDriveId(v string) *CreateShareLinkResponse {
  s.DriveId = &v
  return s
}

func (s *CreateShareLinkResponse) SetExpiration(v string) *CreateShareLinkResponse {
  s.Expiration = &v
  return s
}

func (s *CreateShareLinkResponse) SetExpired(v bool) *CreateShareLinkResponse {
  s.Expired = &v
  return s
}

func (s *CreateShareLinkResponse) SetFileId(v string) *CreateShareLinkResponse {
  s.FileId = &v
  return s
}

func (s *CreateShareLinkResponse) SetFileIdList(v []*string) *CreateShareLinkResponse {
  s.FileIdList = v
  return s
}

func (s *CreateShareLinkResponse) SetFilePathList(v []*string) *CreateShareLinkResponse {
  s.FilePathList = v
  return s
}

func (s *CreateShareLinkResponse) SetPreviewCount(v int64) *CreateShareLinkResponse {
  s.PreviewCount = &v
  return s
}

func (s *CreateShareLinkResponse) SetSaveCount(v int64) *CreateShareLinkResponse {
  s.SaveCount = &v
  return s
}

func (s *CreateShareLinkResponse) SetShareId(v string) *CreateShareLinkResponse {
  s.ShareId = &v
  return s
}

func (s *CreateShareLinkResponse) SetShareMsg(v string) *CreateShareLinkResponse {
  s.ShareMsg = &v
  return s
}

func (s *CreateShareLinkResponse) SetShareName(v string) *CreateShareLinkResponse {
  s.ShareName = &v
  return s
}

func (s *CreateShareLinkResponse) SetSharePolicy(v string) *CreateShareLinkResponse {
  s.SharePolicy = &v
  return s
}

func (s *CreateShareLinkResponse) SetSharePwd(v string) *CreateShareLinkResponse {
  s.SharePwd = &v
  return s
}

func (s *CreateShareLinkResponse) SetShareUrl(v string) *CreateShareLinkResponse {
  s.ShareUrl = &v
  return s
}

func (s *CreateShareLinkResponse) SetStatus(v string) *CreateShareLinkResponse {
  s.Status = &v
  return s
}

func (s *CreateShareLinkResponse) SetUpdatedAt(v string) *CreateShareLinkResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * create share request
 */
type CreateShareRequest struct {
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // owner
  Owner *string `json:"owner,omitempty" xml:"owner,omitempty" require:"true"`
  // owner_type
  OwnerType *string `json:"owner_type,omitempty" xml:"owner_type,omitempty"`
  // permissions
  Permissions []*string `json:"permissions,omitempty" xml:"permissions,omitempty" type:"Repeated"`
  // share_file_id
  ShareFileId *string `json:"share_file_id,omitempty" xml:"share_file_id,omitempty"`
  // share_file_path
  ShareFilePath *string `json:"share_file_path,omitempty" xml:"share_file_path,omitempty"`
  // share_name
  ShareName *string `json:"share_name,omitempty" xml:"share_name,omitempty"`
  // share create policy
  // 
  // share_policy
  SharePolicy []*SharePermissionPolicy `json:"share_policy,omitempty" xml:"share_policy,omitempty" type:"Repeated"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
}

func (s CreateShareRequest) String() string {
  return tea.Prettify(s)
}

func (s CreateShareRequest) GoString() string {
  return s.String()
}

func (s *CreateShareRequest) SetDescription(v string) *CreateShareRequest {
  s.Description = &v
  return s
}

func (s *CreateShareRequest) SetDriveId(v string) *CreateShareRequest {
  s.DriveId = &v
  return s
}

func (s *CreateShareRequest) SetExpiration(v string) *CreateShareRequest {
  s.Expiration = &v
  return s
}

func (s *CreateShareRequest) SetOwner(v string) *CreateShareRequest {
  s.Owner = &v
  return s
}

func (s *CreateShareRequest) SetOwnerType(v string) *CreateShareRequest {
  s.OwnerType = &v
  return s
}

func (s *CreateShareRequest) SetPermissions(v []*string) *CreateShareRequest {
  s.Permissions = v
  return s
}

func (s *CreateShareRequest) SetShareFileId(v string) *CreateShareRequest {
  s.ShareFileId = &v
  return s
}

func (s *CreateShareRequest) SetShareFilePath(v string) *CreateShareRequest {
  s.ShareFilePath = &v
  return s
}

func (s *CreateShareRequest) SetShareName(v string) *CreateShareRequest {
  s.ShareName = &v
  return s
}

func (s *CreateShareRequest) SetSharePolicy(v []*SharePermissionPolicy) *CreateShareRequest {
  s.SharePolicy = v
  return s
}

func (s *CreateShareRequest) SetStatus(v string) *CreateShareRequest {
  s.Status = &v
  return s
}

/**
 * Create share response
 */
type CreateShareResponse struct {
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
}

func (s CreateShareResponse) String() string {
  return tea.Prettify(s)
}

func (s CreateShareResponse) GoString() string {
  return s.String()
}

func (s *CreateShareResponse) SetDomainId(v string) *CreateShareResponse {
  s.DomainId = &v
  return s
}

func (s *CreateShareResponse) SetShareId(v string) *CreateShareResponse {
  s.ShareId = &v
  return s
}

/**
 * 
 */
type CroppingBoundary struct {
  Height *int64 `json:"height,omitempty" xml:"height,omitempty"`
  Left *int64 `json:"left,omitempty" xml:"left,omitempty"`
  Top *int64 `json:"top,omitempty" xml:"top,omitempty"`
  Width *int64 `json:"width,omitempty" xml:"width,omitempty"`
}

func (s CroppingBoundary) String() string {
  return tea.Prettify(s)
}

func (s CroppingBoundary) GoString() string {
  return s.String()
}

func (s *CroppingBoundary) SetHeight(v int64) *CroppingBoundary {
  s.Height = &v
  return s
}

func (s *CroppingBoundary) SetLeft(v int64) *CroppingBoundary {
  s.Left = &v
  return s
}

func (s *CroppingBoundary) SetTop(v int64) *CroppingBoundary {
  s.Top = &v
  return s
}

func (s *CroppingBoundary) SetWidth(v int64) *CroppingBoundary {
  s.Width = &v
  return s
}

/**
 * 
 */
type CroppingSuggestionItem struct {
  AspectRatio *string `json:"aspect_ratio,omitempty" xml:"aspect_ratio,omitempty"`
  CroppingBoundary *CroppingBoundary `json:"cropping_boundary,omitempty" xml:"cropping_boundary,omitempty"`
  Score *float64 `json:"score,omitempty" xml:"score,omitempty"`
}

func (s CroppingSuggestionItem) String() string {
  return tea.Prettify(s)
}

func (s CroppingSuggestionItem) GoString() string {
  return s.String()
}

func (s *CroppingSuggestionItem) SetAspectRatio(v string) *CroppingSuggestionItem {
  s.AspectRatio = &v
  return s
}

func (s *CroppingSuggestionItem) SetCroppingBoundary(v *CroppingBoundary) *CroppingSuggestionItem {
  s.CroppingBoundary = v
  return s
}

func (s *CroppingSuggestionItem) SetScore(v float64) *CroppingSuggestionItem {
  s.Score = &v
  return s
}

/**
 * 
 */
type CustomBenefitMetaRequest struct {
  Enabled *bool `json:"enabled,omitempty" xml:"enabled,omitempty"`
}

func (s CustomBenefitMetaRequest) String() string {
  return tea.Prettify(s)
}

func (s CustomBenefitMetaRequest) GoString() string {
  return s.String()
}

func (s *CustomBenefitMetaRequest) SetEnabled(v bool) *CustomBenefitMetaRequest {
  s.Enabled = &v
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
 * 
 */
type DeleteDetail struct {
}

func (s DeleteDetail) String() string {
  return tea.Prettify(s)
}

func (s DeleteDetail) GoString() string {
  return s.String()
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
 * Delete drive request
 */
type DeleteDriveRequest struct {
  // Drive ID
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true"`
  // Subdomain ID
  SubdomainId *string `json:"subdomain_id,omitempty" xml:"subdomain_id,omitempty"`
}

func (s DeleteDriveRequest) String() string {
  return tea.Prettify(s)
}

func (s DeleteDriveRequest) GoString() string {
  return s.String()
}

func (s *DeleteDriveRequest) SetDriveId(v string) *DeleteDriveRequest {
  s.DriveId = &v
  return s
}

func (s *DeleteDriveRequest) SetSubdomainId(v string) *DeleteDriveRequest {
  s.SubdomainId = &v
  return s
}

/**
 * delete drive response
 */
type DeleteDriveResponse struct {
}

func (s DeleteDriveResponse) String() string {
  return tea.Prettify(s)
}

func (s DeleteDriveResponse) GoString() string {
  return s.String()
}

/**
 * 删除文件请求
 */
type DeleteFileRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty"`
  FileIdPath *string `json:"file_id_path,omitempty" xml:"file_id_path,omitempty"`
  // permanently
  // type: false
  Permanently *bool `json:"permanently,omitempty" xml:"permanently,omitempty"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
}

func (s DeleteFileRequest) String() string {
  return tea.Prettify(s)
}

func (s DeleteFileRequest) GoString() string {
  return s.String()
}

func (s *DeleteFileRequest) SetDriveId(v string) *DeleteFileRequest {
  s.DriveId = &v
  return s
}

func (s *DeleteFileRequest) SetFileId(v string) *DeleteFileRequest {
  s.FileId = &v
  return s
}

func (s *DeleteFileRequest) SetFileIdPath(v string) *DeleteFileRequest {
  s.FileIdPath = &v
  return s
}

func (s *DeleteFileRequest) SetPermanently(v bool) *DeleteFileRequest {
  s.Permanently = &v
  return s
}

func (s *DeleteFileRequest) SetShareId(v string) *DeleteFileRequest {
  s.ShareId = &v
  return s
}

/**
 * 删除文件 response
 */
type DeleteFileResponse struct {
  // async_task_id
  AsyncTaskId *string `json:"async_task_id,omitempty" xml:"async_task_id,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
}

func (s DeleteFileResponse) String() string {
  return tea.Prettify(s)
}

func (s DeleteFileResponse) GoString() string {
  return s.String()
}

func (s *DeleteFileResponse) SetAsyncTaskId(v string) *DeleteFileResponse {
  s.AsyncTaskId = &v
  return s
}

func (s *DeleteFileResponse) SetDomainId(v string) *DeleteFileResponse {
  s.DomainId = &v
  return s
}

func (s *DeleteFileResponse) SetDriveId(v string) *DeleteFileResponse {
  s.DriveId = &v
  return s
}

func (s *DeleteFileResponse) SetFileId(v string) *DeleteFileResponse {
  s.FileId = &v
  return s
}

/**
 * 批量删除文件请求
 */
type DeleteFilesRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id_list
  FileIdList []*string `json:"file_id_list,omitempty" xml:"file_id_list,omitempty" require:"true" type:"Repeated"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
}

func (s DeleteFilesRequest) String() string {
  return tea.Prettify(s)
}

func (s DeleteFilesRequest) GoString() string {
  return s.String()
}

func (s *DeleteFilesRequest) SetDriveId(v string) *DeleteFilesRequest {
  s.DriveId = &v
  return s
}

func (s *DeleteFilesRequest) SetFileIdList(v []*string) *DeleteFilesRequest {
  s.FileIdList = v
  return s
}

func (s *DeleteFilesRequest) SetShareId(v string) *DeleteFilesRequest {
  s.ShareId = &v
  return s
}

/**
 * 批量删除文件 response
 */
type DeleteFilesResponse struct {
  // deleted_file_id_list
  DeletedFileIdList []*string `json:"deleted_file_id_list,omitempty" xml:"deleted_file_id_list,omitempty" type:"Repeated"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
}

func (s DeleteFilesResponse) String() string {
  return tea.Prettify(s)
}

func (s DeleteFilesResponse) GoString() string {
  return s.String()
}

func (s *DeleteFilesResponse) SetDeletedFileIdList(v []*string) *DeleteFilesResponse {
  s.DeletedFileIdList = v
  return s
}

func (s *DeleteFilesResponse) SetDomainId(v string) *DeleteFilesResponse {
  s.DomainId = &v
  return s
}

func (s *DeleteFilesResponse) SetDriveId(v string) *DeleteFilesResponse {
  s.DriveId = &v
  return s
}

/**
 * delete share request
 */
type DeleteShareRequest struct {
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" require:"true"`
}

func (s DeleteShareRequest) String() string {
  return tea.Prettify(s)
}

func (s DeleteShareRequest) GoString() string {
  return s.String()
}

func (s *DeleteShareRequest) SetShareId(v string) *DeleteShareRequest {
  s.ShareId = &v
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
type DomainSuperAdminConfig struct {
  PhoneNumber *string `json:"phone_number,omitempty" xml:"phone_number,omitempty"`
  PhoneRegion *string `json:"phone_region,omitempty" xml:"phone_region,omitempty"`
  UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty"`
}

func (s DomainSuperAdminConfig) String() string {
  return tea.Prettify(s)
}

func (s DomainSuperAdminConfig) GoString() string {
  return s.String()
}

func (s *DomainSuperAdminConfig) SetPhoneNumber(v string) *DomainSuperAdminConfig {
  s.PhoneNumber = &v
  return s
}

func (s *DomainSuperAdminConfig) SetPhoneRegion(v string) *DomainSuperAdminConfig {
  s.PhoneRegion = &v
  return s
}

func (s *DomainSuperAdminConfig) SetUserId(v string) *DomainSuperAdminConfig {
  s.UserId = &v
  return s
}

/**
 * domain update name request
 */
type DomainUpdateNameRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // Domain 名称
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true"`
}

func (s DomainUpdateNameRequest) String() string {
  return tea.Prettify(s)
}

func (s DomainUpdateNameRequest) GoString() string {
  return s.String()
}

func (s *DomainUpdateNameRequest) SetHeaders(v map[string]*string) *DomainUpdateNameRequest {
  s.Headers = v
  return s
}

func (s *DomainUpdateNameRequest) SetDomainId(v string) *DomainUpdateNameRequest {
  s.DomainId = &v
  return s
}

func (s *DomainUpdateNameRequest) SetName(v string) *DomainUpdateNameRequest {
  s.Name = &v
  return s
}

/**
 * 下载文件请求body
 */
type DownloadRequest struct {
  // drive id
  DriveID *string `json:"DriveID,omitempty" xml:"DriveID,omitempty"`
  // file id
  FileID *string `json:"FileID,omitempty" xml:"FileID,omitempty" require:"true"`
  // in: query
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"ImageThumbnailProcess,omitempty" xml:"ImageThumbnailProcess,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"OfficeThumbnailProcess,omitempty" xml:"OfficeThumbnailProcess,omitempty"`
  // share_id, either share_id or drive_id is required
  ShareID *string `json:"ShareID,omitempty" xml:"ShareID,omitempty"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"VideoThumbnailProcess,omitempty" xml:"VideoThumbnailProcess,omitempty"`
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  FileIdPath *string `json:"file_id_path,omitempty" xml:"file_id_path,omitempty"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
}

func (s DownloadRequest) String() string {
  return tea.Prettify(s)
}

func (s DownloadRequest) GoString() string {
  return s.String()
}

func (s *DownloadRequest) SetDriveID(v string) *DownloadRequest {
  s.DriveID = &v
  return s
}

func (s *DownloadRequest) SetFileID(v string) *DownloadRequest {
  s.FileID = &v
  return s
}

func (s *DownloadRequest) SetImageThumbnailProcess(v string) *DownloadRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *DownloadRequest) SetOfficeThumbnailProcess(v string) *DownloadRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *DownloadRequest) SetShareID(v string) *DownloadRequest {
  s.ShareID = &v
  return s
}

func (s *DownloadRequest) SetVideoThumbnailProcess(v string) *DownloadRequest {
  s.VideoThumbnailProcess = &v
  return s
}

func (s *DownloadRequest) SetAdditionData(v map[string]interface{}) *DownloadRequest {
  s.AdditionData = v
  return s
}

func (s *DownloadRequest) SetFileIdPath(v string) *DownloadRequest {
  s.FileIdPath = &v
  return s
}

func (s *DownloadRequest) SetLocation(v string) *DownloadRequest {
  s.Location = &v
  return s
}

func (s *DownloadRequest) SetReferer(v string) *DownloadRequest {
  s.Referer = &v
  return s
}

func (s *DownloadRequest) SetSignToken(v string) *DownloadRequest {
  s.SignToken = &v
  return s
}

/**
 * 
 */
type EditDetail struct {
}

func (s EditDetail) String() string {
  return tea.Prettify(s)
}

func (s EditDetail) GoString() string {
  return s.String()
}

/**
 * 
 */
type FaceThumbnail struct {
  FaceGroupId *string `json:"face_group_id,omitempty" xml:"face_group_id,omitempty"`
  FaceId *string `json:"face_id,omitempty" xml:"face_id,omitempty"`
  FaceThumbnail *string `json:"face_thumbnail,omitempty" xml:"face_thumbnail,omitempty"`
}

func (s FaceThumbnail) String() string {
  return tea.Prettify(s)
}

func (s FaceThumbnail) GoString() string {
  return s.String()
}

func (s *FaceThumbnail) SetFaceGroupId(v string) *FaceThumbnail {
  s.FaceGroupId = &v
  return s
}

func (s *FaceThumbnail) SetFaceId(v string) *FaceThumbnail {
  s.FaceId = &v
  return s
}

func (s *FaceThumbnail) SetFaceThumbnail(v string) *FaceThumbnail {
  s.FaceThumbnail = &v
  return s
}

/**
 * 
 */
type FileActivity struct {
  // Actors
  Actors []*Actor `json:"actors,omitempty" xml:"actors,omitempty" type:"Repeated"`
  PrimaryActionDetail *ActionDetail `json:"primary_action_detail,omitempty" xml:"primary_action_detail,omitempty"`
  // Targets
  Targets []*Target `json:"targets,omitempty" xml:"targets,omitempty" type:"Repeated"`
  TimeRange *TimeRange `json:"time_range,omitempty" xml:"time_range,omitempty"`
  // Timestamp
  Timestamp *string `json:"timestamp,omitempty" xml:"timestamp,omitempty"`
}

func (s FileActivity) String() string {
  return tea.Prettify(s)
}

func (s FileActivity) GoString() string {
  return s.String()
}

func (s *FileActivity) SetActors(v []*Actor) *FileActivity {
  s.Actors = v
  return s
}

func (s *FileActivity) SetPrimaryActionDetail(v *ActionDetail) *FileActivity {
  s.PrimaryActionDetail = v
  return s
}

func (s *FileActivity) SetTargets(v []*Target) *FileActivity {
  s.Targets = v
  return s
}

func (s *FileActivity) SetTimeRange(v *TimeRange) *FileActivity {
  s.TimeRange = v
  return s
}

func (s *FileActivity) SetTimestamp(v string) *FileActivity {
  s.Timestamp = &v
  return s
}

/**
 * the file op info
 */
type FileDeltaResponse struct {
  CurrentCategory *string `json:"current_category,omitempty" xml:"current_category,omitempty"`
  File *BaseCCPFileResponse `json:"file,omitempty" xml:"file,omitempty"`
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty"`
  Op *string `json:"op,omitempty" xml:"op,omitempty"`
}

func (s FileDeltaResponse) String() string {
  return tea.Prettify(s)
}

func (s FileDeltaResponse) GoString() string {
  return s.String()
}

func (s *FileDeltaResponse) SetCurrentCategory(v string) *FileDeltaResponse {
  s.CurrentCategory = &v
  return s
}

func (s *FileDeltaResponse) SetFile(v *BaseCCPFileResponse) *FileDeltaResponse {
  s.File = v
  return s
}

func (s *FileDeltaResponse) SetFileId(v string) *FileDeltaResponse {
  s.FileId = &v
  return s
}

func (s *FileDeltaResponse) SetOp(v string) *FileDeltaResponse {
  s.Op = &v
  return s
}

/**
 * 
 */
type FileStreamInfo struct {
  // content_hash
  ContentHash *string `json:"content_hash,omitempty" xml:"content_hash,omitempty"`
  // content_hash_name
  ContentHashName *string `json:"content_hash_name,omitempty" xml:"content_hash_name,omitempty"`
  // ContentMd5
  ContentMd5 *string `json:"content_md5,omitempty" xml:"content_md5,omitempty" require:"true"`
  // part_info_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  // pre_hash
  PreHash *string `json:"pre_hash,omitempty" xml:"pre_hash,omitempty"`
  // proof_code
  ProofCode *string `json:"proof_code,omitempty" xml:"proof_code,omitempty"`
  // proof_version
  ProofVersion *string `json:"proof_version,omitempty" xml:"proof_version,omitempty"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" require:"true" maximum:"53687091200" minimum:"0"`
}

func (s FileStreamInfo) String() string {
  return tea.Prettify(s)
}

func (s FileStreamInfo) GoString() string {
  return s.String()
}

func (s *FileStreamInfo) SetContentHash(v string) *FileStreamInfo {
  s.ContentHash = &v
  return s
}

func (s *FileStreamInfo) SetContentHashName(v string) *FileStreamInfo {
  s.ContentHashName = &v
  return s
}

func (s *FileStreamInfo) SetContentMd5(v string) *FileStreamInfo {
  s.ContentMd5 = &v
  return s
}

func (s *FileStreamInfo) SetPartInfoList(v []*UploadPartInfo) *FileStreamInfo {
  s.PartInfoList = v
  return s
}

func (s *FileStreamInfo) SetPreHash(v string) *FileStreamInfo {
  s.PreHash = &v
  return s
}

func (s *FileStreamInfo) SetProofCode(v string) *FileStreamInfo {
  s.ProofCode = &v
  return s
}

func (s *FileStreamInfo) SetProofVersion(v string) *FileStreamInfo {
  s.ProofVersion = &v
  return s
}

func (s *FileStreamInfo) SetSize(v int64) *FileStreamInfo {
  s.Size = &v
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
 * 获取异步人去信息
 */
type GetAsyncTaskRequest struct {
  // async_task_id
  // type:string
  AsyncTaskId *string `json:"async_task_id,omitempty" xml:"async_task_id,omitempty"`
}

func (s GetAsyncTaskRequest) String() string {
  return tea.Prettify(s)
}

func (s GetAsyncTaskRequest) GoString() string {
  return s.String()
}

func (s *GetAsyncTaskRequest) SetAsyncTaskId(v string) *GetAsyncTaskRequest {
  s.AsyncTaskId = &v
  return s
}

/**
 * Get AsyncTask Response
 */
type GetAsyncTaskResponse struct {
  // async_task_id
  // type:string
  AsyncTaskId *string `json:"async_task_id,omitempty" xml:"async_task_id,omitempty"`
  // consumed_process
  ConsumedProcess *int64 `json:"consumed_process,omitempty" xml:"consumed_process,omitempty"`
  // err_code
  ErrCode *int64 `json:"err_code,omitempty" xml:"err_code,omitempty"`
  // message
  Message *string `json:"message,omitempty" xml:"message,omitempty"`
  // state
  State *string `json:"state,omitempty" xml:"state,omitempty"`
  // total_process
  TotalProcess *int64 `json:"total_process,omitempty" xml:"total_process,omitempty"`
  // download_url
  // example
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s GetAsyncTaskResponse) String() string {
  return tea.Prettify(s)
}

func (s GetAsyncTaskResponse) GoString() string {
  return s.String()
}

func (s *GetAsyncTaskResponse) SetAsyncTaskId(v string) *GetAsyncTaskResponse {
  s.AsyncTaskId = &v
  return s
}

func (s *GetAsyncTaskResponse) SetConsumedProcess(v int64) *GetAsyncTaskResponse {
  s.ConsumedProcess = &v
  return s
}

func (s *GetAsyncTaskResponse) SetErrCode(v int64) *GetAsyncTaskResponse {
  s.ErrCode = &v
  return s
}

func (s *GetAsyncTaskResponse) SetMessage(v string) *GetAsyncTaskResponse {
  s.Message = &v
  return s
}

func (s *GetAsyncTaskResponse) SetState(v string) *GetAsyncTaskResponse {
  s.State = &v
  return s
}

func (s *GetAsyncTaskResponse) SetTotalProcess(v int64) *GetAsyncTaskResponse {
  s.TotalProcess = &v
  return s
}

func (s *GetAsyncTaskResponse) SetUrl(v string) *GetAsyncTaskResponse {
  s.Url = &v
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
 * Get default drive request
 */
type GetDefaultDriveRequest struct {
  // Subdomain ID
  SubdomainId *string `json:"subdomain_id,omitempty" xml:"subdomain_id,omitempty"`
  // 用户ID
  UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty"`
}

func (s GetDefaultDriveRequest) String() string {
  return tea.Prettify(s)
}

func (s GetDefaultDriveRequest) GoString() string {
  return s.String()
}

func (s *GetDefaultDriveRequest) SetSubdomainId(v string) *GetDefaultDriveRequest {
  s.SubdomainId = &v
  return s
}

func (s *GetDefaultDriveRequest) SetUserId(v string) *GetDefaultDriveRequest {
  s.UserId = &v
  return s
}

/**
 * 获取文件夹size信息
 */
type GetDirSizeInfoResponse struct {
  // dir_count
  DirCount *int64 `json:"dir_count,omitempty" xml:"dir_count,omitempty"`
  // file_count
  FileCount *int64 `json:"file_count,omitempty" xml:"file_count,omitempty"`
  // size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty"`
}

func (s GetDirSizeInfoResponse) String() string {
  return tea.Prettify(s)
}

func (s GetDirSizeInfoResponse) GoString() string {
  return s.String()
}

func (s *GetDirSizeInfoResponse) SetDirCount(v int64) *GetDirSizeInfoResponse {
  s.DirCount = &v
  return s
}

func (s *GetDirSizeInfoResponse) SetFileCount(v int64) *GetDirSizeInfoResponse {
  s.FileCount = &v
  return s
}

func (s *GetDirSizeInfoResponse) SetSize(v int64) *GetDirSizeInfoResponse {
  s.Size = &v
  return s
}

/**
 * get domain request
 */
type GetDomainRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  GetBenefit *bool `json:"get_benefit,omitempty" xml:"get_benefit,omitempty"`
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

func (s *GetDomainRequest) SetGetBenefit(v bool) *GetDomainRequest {
  s.GetBenefit = &v
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
  Benefits map[string]interface{} `json:"benefits,omitempty" xml:"benefits,omitempty"`
  // Domain 创建时间
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // 数据 Hash 算法
  DataHashName *string `json:"data_hash_name,omitempty" xml:"data_hash_name,omitempty"`
  DefaultSuperAdminConfig *DomainSuperAdminConfig `json:"default_super_admin_config,omitempty" xml:"default_super_admin_config,omitempty"`
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
  // 预付费domain过期时间
  ExpireTime *int64 `json:"expire_time,omitempty" xml:"expire_time,omitempty"`
  // 是否开启了自动初始化 Drive
  InitDriveEnable *bool `json:"init_drive_enable,omitempty" xml:"init_drive_enable,omitempty"`
  // 自动初始化 Drive 大小
  InitDriveSize *int64 `json:"init_drive_size,omitempty" xml:"init_drive_size,omitempty"`
  // 自动初始化 Drive 所用 Store ID
  InitDriveStoreId *string `json:"init_drive_store_id,omitempty" xml:"init_drive_store_id,omitempty"`
  // Domain 类型
  Mode *string `json:"mode,omitempty" xml:"mode,omitempty"`
  OfficePreviewConfig *OfficePreviewConfig `json:"office_preview_config,omitempty" xml:"office_preview_config,omitempty"`
  // Domain 类型
  PathType *string `json:"path_type,omitempty" xml:"path_type,omitempty"`
  // 预付费套餐
  PrepaidPackage *string `json:"prepaid_package,omitempty" xml:"prepaid_package,omitempty"`
  PublishedAppAccessStrategy *AppAccessStrategy `json:"published_app_access_strategy,omitempty" xml:"published_app_access_strategy,omitempty"`
  // Domain ServiceCode
  ServiceCode *string `json:"service_code,omitempty" xml:"service_code,omitempty"`
  // 是否开启了共享
  Sharable *bool `json:"sharable,omitempty" xml:"sharable,omitempty"`
  // 是否开启了分享
  ShareLinkEnabled *bool `json:"share_link_enabled,omitempty" xml:"share_link_enabled,omitempty"`
  // 容量配额
  SizeQuota *int64 `json:"size_quota,omitempty" xml:"size_quota,omitempty"`
  // SPI 实例 id
  SpiInstanceId *string `json:"spi_instance_id,omitempty" xml:"spi_instance_id,omitempty"`
  // domain状态：创建中，正常，已过期
  Status *int64 `json:"status,omitempty" xml:"status,omitempty"`
  // 存储级别
  StoreLevel *string `json:"store_level,omitempty" xml:"store_level,omitempty"`
  // 存储 Region 列表
  StoreRegionList []*string `json:"store_region_list,omitempty" xml:"store_region_list,omitempty" type:"Repeated"`
  // Domain 更新时间
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // 用户数配额
  UserCountQuota *int64 `json:"user_count_quota,omitempty" xml:"user_count_quota,omitempty"`
  VideoPreviewConfig *VideoPreviewConfig `json:"video_preview_config,omitempty" xml:"video_preview_config,omitempty"`
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

func (s *GetDomainResponse) SetBenefits(v map[string]interface{}) *GetDomainResponse {
  s.Benefits = v
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

func (s *GetDomainResponse) SetDefaultSuperAdminConfig(v *DomainSuperAdminConfig) *GetDomainResponse {
  s.DefaultSuperAdminConfig = v
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

func (s *GetDomainResponse) SetExpireTime(v int64) *GetDomainResponse {
  s.ExpireTime = &v
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

func (s *GetDomainResponse) SetOfficePreviewConfig(v *OfficePreviewConfig) *GetDomainResponse {
  s.OfficePreviewConfig = v
  return s
}

func (s *GetDomainResponse) SetPathType(v string) *GetDomainResponse {
  s.PathType = &v
  return s
}

func (s *GetDomainResponse) SetPrepaidPackage(v string) *GetDomainResponse {
  s.PrepaidPackage = &v
  return s
}

func (s *GetDomainResponse) SetPublishedAppAccessStrategy(v *AppAccessStrategy) *GetDomainResponse {
  s.PublishedAppAccessStrategy = v
  return s
}

func (s *GetDomainResponse) SetServiceCode(v string) *GetDomainResponse {
  s.ServiceCode = &v
  return s
}

func (s *GetDomainResponse) SetSharable(v bool) *GetDomainResponse {
  s.Sharable = &v
  return s
}

func (s *GetDomainResponse) SetShareLinkEnabled(v bool) *GetDomainResponse {
  s.ShareLinkEnabled = &v
  return s
}

func (s *GetDomainResponse) SetSizeQuota(v int64) *GetDomainResponse {
  s.SizeQuota = &v
  return s
}

func (s *GetDomainResponse) SetSpiInstanceId(v string) *GetDomainResponse {
  s.SpiInstanceId = &v
  return s
}

func (s *GetDomainResponse) SetStatus(v int64) *GetDomainResponse {
  s.Status = &v
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

func (s *GetDomainResponse) SetUserCountQuota(v int64) *GetDomainResponse {
  s.UserCountQuota = &v
  return s
}

func (s *GetDomainResponse) SetVideoPreviewConfig(v *VideoPreviewConfig) *GetDomainResponse {
  s.VideoPreviewConfig = v
  return s
}

/**
 * 获取文件下载地址的请求body
 */
type GetDownloadUrlRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // expire_sec
  ExpireSec *int64 `json:"expire_sec,omitempty" xml:"expire_sec,omitempty" maximum:"115200" minimum:"1"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  FileIdPath *string `json:"file_id_path,omitempty" xml:"file_id_path,omitempty"`
  // file_name
  FileName *string `json:"file_name,omitempty" xml:"file_name,omitempty" maxLength:"1024" minLength:"1"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id, either share_id or drive_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
}

func (s GetDownloadUrlRequest) String() string {
  return tea.Prettify(s)
}

func (s GetDownloadUrlRequest) GoString() string {
  return s.String()
}

func (s *GetDownloadUrlRequest) SetAdditionData(v map[string]interface{}) *GetDownloadUrlRequest {
  s.AdditionData = v
  return s
}

func (s *GetDownloadUrlRequest) SetDriveId(v string) *GetDownloadUrlRequest {
  s.DriveId = &v
  return s
}

func (s *GetDownloadUrlRequest) SetExpireSec(v int64) *GetDownloadUrlRequest {
  s.ExpireSec = &v
  return s
}

func (s *GetDownloadUrlRequest) SetFileId(v string) *GetDownloadUrlRequest {
  s.FileId = &v
  return s
}

func (s *GetDownloadUrlRequest) SetFileIdPath(v string) *GetDownloadUrlRequest {
  s.FileIdPath = &v
  return s
}

func (s *GetDownloadUrlRequest) SetFileName(v string) *GetDownloadUrlRequest {
  s.FileName = &v
  return s
}

func (s *GetDownloadUrlRequest) SetLocation(v string) *GetDownloadUrlRequest {
  s.Location = &v
  return s
}

func (s *GetDownloadUrlRequest) SetReferer(v string) *GetDownloadUrlRequest {
  s.Referer = &v
  return s
}

func (s *GetDownloadUrlRequest) SetShareId(v string) *GetDownloadUrlRequest {
  s.ShareId = &v
  return s
}

func (s *GetDownloadUrlRequest) SetSignToken(v string) *GetDownloadUrlRequest {
  s.SignToken = &v
  return s
}

/**
 * 获取download url response
 */
type GetDownloadUrlResponse struct {
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // method
  Method *string `json:"method,omitempty" xml:"method,omitempty"`
  Ratelimit *RateLimit `json:"ratelimit,omitempty" xml:"ratelimit,omitempty"`
  // size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty"`
  // streams url info
  StreamsUrl map[string]interface{} `json:"streams_url,omitempty" xml:"streams_url,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s GetDownloadUrlResponse) String() string {
  return tea.Prettify(s)
}

func (s GetDownloadUrlResponse) GoString() string {
  return s.String()
}

func (s *GetDownloadUrlResponse) SetExpiration(v string) *GetDownloadUrlResponse {
  s.Expiration = &v
  return s
}

func (s *GetDownloadUrlResponse) SetMethod(v string) *GetDownloadUrlResponse {
  s.Method = &v
  return s
}

func (s *GetDownloadUrlResponse) SetRatelimit(v *RateLimit) *GetDownloadUrlResponse {
  s.Ratelimit = v
  return s
}

func (s *GetDownloadUrlResponse) SetSize(v int64) *GetDownloadUrlResponse {
  s.Size = &v
  return s
}

func (s *GetDownloadUrlResponse) SetStreamsUrl(v map[string]interface{}) *GetDownloadUrlResponse {
  s.StreamsUrl = v
  return s
}

func (s *GetDownloadUrlResponse) SetUrl(v string) *GetDownloadUrlResponse {
  s.Url = &v
  return s
}

/**
 * Get drive request
 */
type GetDriveRequest struct {
  // Drive ID
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true"`
  // Subdomain ID
  SubdomainId *string `json:"subdomain_id,omitempty" xml:"subdomain_id,omitempty"`
}

func (s GetDriveRequest) String() string {
  return tea.Prettify(s)
}

func (s GetDriveRequest) GoString() string {
  return s.String()
}

func (s *GetDriveRequest) SetDriveId(v string) *GetDriveRequest {
  s.DriveId = &v
  return s
}

func (s *GetDriveRequest) SetSubdomainId(v string) *GetDriveRequest {
  s.SubdomainId = &v
  return s
}

/**
 * Get drive response
 */
type GetDriveResponse struct {
  // Drive 创建者
  Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
  // Drive 备注信息
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // Drive ID
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty"`
  // Drive 名称
  DriveName *string `json:"drive_name,omitempty" xml:"drive_name,omitempty"`
  // Drive 类型
  DriveType *string `json:"drive_type,omitempty" xml:"drive_type,omitempty"`
  EncryptDataAccess *bool `json:"encrypt_data_access,omitempty" xml:"encrypt_data_access,omitempty"`
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // Drive 所有者
  Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
  // Drive 所有者类型
  OwnerType *string `json:"owner_type,omitempty" xml:"owner_type,omitempty"`
  // Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
  RelativePath *string `json:"relative_path,omitempty" xml:"relative_path,omitempty"`
  // Drive 状态
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // 存储 ID, domain的PathType为OSSPath时返回
  StoreId *string `json:"store_id,omitempty" xml:"store_id,omitempty"`
  // Drive 空间总量
  TotalSize *int64 `json:"total_size,omitempty" xml:"total_size,omitempty"`
  // Drive 空间已使用量
  UsedSize *int64 `json:"used_size,omitempty" xml:"used_size,omitempty"`
}

func (s GetDriveResponse) String() string {
  return tea.Prettify(s)
}

func (s GetDriveResponse) GoString() string {
  return s.String()
}

func (s *GetDriveResponse) SetCreator(v string) *GetDriveResponse {
  s.Creator = &v
  return s
}

func (s *GetDriveResponse) SetDescription(v string) *GetDriveResponse {
  s.Description = &v
  return s
}

func (s *GetDriveResponse) SetDomainId(v string) *GetDriveResponse {
  s.DomainId = &v
  return s
}

func (s *GetDriveResponse) SetDriveId(v string) *GetDriveResponse {
  s.DriveId = &v
  return s
}

func (s *GetDriveResponse) SetDriveName(v string) *GetDriveResponse {
  s.DriveName = &v
  return s
}

func (s *GetDriveResponse) SetDriveType(v string) *GetDriveResponse {
  s.DriveType = &v
  return s
}

func (s *GetDriveResponse) SetEncryptDataAccess(v bool) *GetDriveResponse {
  s.EncryptDataAccess = &v
  return s
}

func (s *GetDriveResponse) SetEncryptMode(v string) *GetDriveResponse {
  s.EncryptMode = &v
  return s
}

func (s *GetDriveResponse) SetOwner(v string) *GetDriveResponse {
  s.Owner = &v
  return s
}

func (s *GetDriveResponse) SetOwnerType(v string) *GetDriveResponse {
  s.OwnerType = &v
  return s
}

func (s *GetDriveResponse) SetRelativePath(v string) *GetDriveResponse {
  s.RelativePath = &v
  return s
}

func (s *GetDriveResponse) SetStatus(v string) *GetDriveResponse {
  s.Status = &v
  return s
}

func (s *GetDriveResponse) SetStoreId(v string) *GetDriveResponse {
  s.StoreId = &v
  return s
}

func (s *GetDriveResponse) SetTotalSize(v int64) *GetDriveResponse {
  s.TotalSize = &v
  return s
}

func (s *GetDriveResponse) SetUsedSize(v int64) *GetDriveResponse {
  s.UsedSize = &v
  return s
}

/**
 * 根据路径获取 File 接口 body
 */
type GetFileByPathRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  ImageCroppingAspectRatios []*string `json:"image_cropping_aspect_ratios,omitempty" xml:"image_cropping_aspect_ratios,omitempty" type:"Repeated"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // url_expire_sec
  UrlExpireSec *int64 `json:"url_expire_sec,omitempty" xml:"url_expire_sec,omitempty" maximum:"14400" minimum:"10"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s GetFileByPathRequest) String() string {
  return tea.Prettify(s)
}

func (s GetFileByPathRequest) GoString() string {
  return s.String()
}

func (s *GetFileByPathRequest) SetAdditionData(v map[string]interface{}) *GetFileByPathRequest {
  s.AdditionData = v
  return s
}

func (s *GetFileByPathRequest) SetDriveId(v string) *GetFileByPathRequest {
  s.DriveId = &v
  return s
}

func (s *GetFileByPathRequest) SetFilePath(v string) *GetFileByPathRequest {
  s.FilePath = &v
  return s
}

func (s *GetFileByPathRequest) SetImageCroppingAspectRatios(v []*string) *GetFileByPathRequest {
  s.ImageCroppingAspectRatios = v
  return s
}

func (s *GetFileByPathRequest) SetImageThumbnailProcess(v string) *GetFileByPathRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *GetFileByPathRequest) SetImageUrlProcess(v string) *GetFileByPathRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *GetFileByPathRequest) SetOfficeThumbnailProcess(v string) *GetFileByPathRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *GetFileByPathRequest) SetReferer(v string) *GetFileByPathRequest {
  s.Referer = &v
  return s
}

func (s *GetFileByPathRequest) SetSignToken(v string) *GetFileByPathRequest {
  s.SignToken = &v
  return s
}

func (s *GetFileByPathRequest) SetUrlExpireSec(v int64) *GetFileByPathRequest {
  s.UrlExpireSec = &v
  return s
}

func (s *GetFileByPathRequest) SetVideoThumbnailProcess(v string) *GetFileByPathRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * 根据路径获取文件元数据response
 */
type GetFileByPathResponse struct {
  // category
  Category *string `json:"category,omitempty" xml:"category,omitempty"`
  // CharacteristicHash
  CharacteristicHash *string `json:"characteristic_hash,omitempty" xml:"characteristic_hash,omitempty"`
  // Content Hash
  ContentHash *string `json:"content_hash,omitempty" xml:"content_hash,omitempty"`
  // content_hash_name
  ContentHashName *string `json:"content_hash_name,omitempty" xml:"content_hash_name,omitempty"`
  // content_type
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // crc64_hash
  Crc64Hash *string `json:"crc64_hash,omitempty" xml:"crc64_hash,omitempty"`
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // DomainID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // download_url
  DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // encrypt_mode
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // file_extension
  FileExtension *string `json:"file_extension,omitempty" xml:"file_extension,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // Hidden
  // type: boolean
  Hidden *bool `json:"hidden,omitempty" xml:"hidden,omitempty"`
  ImageMediaMetadata *ImageMediaResponse `json:"image_media_metadata,omitempty" xml:"image_media_metadata,omitempty"`
  // labels
  Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
  Meta *string `json:"meta,omitempty" xml:"meta,omitempty"`
  // name
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
  // parent_file_id
  ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // PunishFlag
  PunishFlag *int64 `json:"punish_flag,omitempty" xml:"punish_flag,omitempty"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // starred
  // type: boolean
  Starred *bool `json:"starred,omitempty" xml:"starred,omitempty"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // @Deprecated streams url info
  StreamsInfo map[string]interface{} `json:"streams_info,omitempty" xml:"streams_info,omitempty"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // Trashed
  // type: boolean
  Trashed *bool `json:"trashed,omitempty" xml:"trashed,omitempty"`
  // trashed_at
  TrashedAt *string `json:"trashed_at,omitempty" xml:"trashed_at,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
  // user_meta
  UserMeta *string `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
  VideoMediaMetadata *VideoMediaResponse `json:"video_media_metadata,omitempty" xml:"video_media_metadata,omitempty"`
  VideoPreviewMetadata *VideoPreviewResponse `json:"video_preview_metadata,omitempty" xml:"video_preview_metadata,omitempty"`
}

func (s GetFileByPathResponse) String() string {
  return tea.Prettify(s)
}

func (s GetFileByPathResponse) GoString() string {
  return s.String()
}

func (s *GetFileByPathResponse) SetCategory(v string) *GetFileByPathResponse {
  s.Category = &v
  return s
}

func (s *GetFileByPathResponse) SetCharacteristicHash(v string) *GetFileByPathResponse {
  s.CharacteristicHash = &v
  return s
}

func (s *GetFileByPathResponse) SetContentHash(v string) *GetFileByPathResponse {
  s.ContentHash = &v
  return s
}

func (s *GetFileByPathResponse) SetContentHashName(v string) *GetFileByPathResponse {
  s.ContentHashName = &v
  return s
}

func (s *GetFileByPathResponse) SetContentType(v string) *GetFileByPathResponse {
  s.ContentType = &v
  return s
}

func (s *GetFileByPathResponse) SetCrc64Hash(v string) *GetFileByPathResponse {
  s.Crc64Hash = &v
  return s
}

func (s *GetFileByPathResponse) SetCreatedAt(v string) *GetFileByPathResponse {
  s.CreatedAt = &v
  return s
}

func (s *GetFileByPathResponse) SetDescription(v string) *GetFileByPathResponse {
  s.Description = &v
  return s
}

func (s *GetFileByPathResponse) SetDomainId(v string) *GetFileByPathResponse {
  s.DomainId = &v
  return s
}

func (s *GetFileByPathResponse) SetDownloadUrl(v string) *GetFileByPathResponse {
  s.DownloadUrl = &v
  return s
}

func (s *GetFileByPathResponse) SetDriveId(v string) *GetFileByPathResponse {
  s.DriveId = &v
  return s
}

func (s *GetFileByPathResponse) SetEncryptMode(v string) *GetFileByPathResponse {
  s.EncryptMode = &v
  return s
}

func (s *GetFileByPathResponse) SetFileExtension(v string) *GetFileByPathResponse {
  s.FileExtension = &v
  return s
}

func (s *GetFileByPathResponse) SetFileId(v string) *GetFileByPathResponse {
  s.FileId = &v
  return s
}

func (s *GetFileByPathResponse) SetHidden(v bool) *GetFileByPathResponse {
  s.Hidden = &v
  return s
}

func (s *GetFileByPathResponse) SetImageMediaMetadata(v *ImageMediaResponse) *GetFileByPathResponse {
  s.ImageMediaMetadata = v
  return s
}

func (s *GetFileByPathResponse) SetLabels(v []*string) *GetFileByPathResponse {
  s.Labels = v
  return s
}

func (s *GetFileByPathResponse) SetMeta(v string) *GetFileByPathResponse {
  s.Meta = &v
  return s
}

func (s *GetFileByPathResponse) SetName(v string) *GetFileByPathResponse {
  s.Name = &v
  return s
}

func (s *GetFileByPathResponse) SetParentFileId(v string) *GetFileByPathResponse {
  s.ParentFileId = &v
  return s
}

func (s *GetFileByPathResponse) SetPunishFlag(v int64) *GetFileByPathResponse {
  s.PunishFlag = &v
  return s
}

func (s *GetFileByPathResponse) SetShareId(v string) *GetFileByPathResponse {
  s.ShareId = &v
  return s
}

func (s *GetFileByPathResponse) SetSize(v int64) *GetFileByPathResponse {
  s.Size = &v
  return s
}

func (s *GetFileByPathResponse) SetStarred(v bool) *GetFileByPathResponse {
  s.Starred = &v
  return s
}

func (s *GetFileByPathResponse) SetStatus(v string) *GetFileByPathResponse {
  s.Status = &v
  return s
}

func (s *GetFileByPathResponse) SetStreamsInfo(v map[string]interface{}) *GetFileByPathResponse {
  s.StreamsInfo = v
  return s
}

func (s *GetFileByPathResponse) SetThumbnail(v string) *GetFileByPathResponse {
  s.Thumbnail = &v
  return s
}

func (s *GetFileByPathResponse) SetTrashed(v bool) *GetFileByPathResponse {
  s.Trashed = &v
  return s
}

func (s *GetFileByPathResponse) SetTrashedAt(v string) *GetFileByPathResponse {
  s.TrashedAt = &v
  return s
}

func (s *GetFileByPathResponse) SetType(v string) *GetFileByPathResponse {
  s.Type = &v
  return s
}

func (s *GetFileByPathResponse) SetUpdatedAt(v string) *GetFileByPathResponse {
  s.UpdatedAt = &v
  return s
}

func (s *GetFileByPathResponse) SetUploadId(v string) *GetFileByPathResponse {
  s.UploadId = &v
  return s
}

func (s *GetFileByPathResponse) SetUrl(v string) *GetFileByPathResponse {
  s.Url = &v
  return s
}

func (s *GetFileByPathResponse) SetUserMeta(v string) *GetFileByPathResponse {
  s.UserMeta = &v
  return s
}

func (s *GetFileByPathResponse) SetVideoMediaMetadata(v *VideoMediaResponse) *GetFileByPathResponse {
  s.VideoMediaMetadata = v
  return s
}

func (s *GetFileByPathResponse) SetVideoPreviewMetadata(v *VideoPreviewResponse) *GetFileByPathResponse {
  s.VideoPreviewMetadata = v
  return s
}

/**
 * 获取文件元数据
 */
type GetFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // fields
  Fields *string `json:"fields,omitempty" xml:"fields,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  FileIdPath *string `json:"file_id_path,omitempty" xml:"file_id_path,omitempty"`
  ImageCroppingAspectRatios []*string `json:"image_cropping_aspect_ratios,omitempty" xml:"image_cropping_aspect_ratios,omitempty" type:"Repeated"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id, either share_id or drive_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // url_expire_sec
  UrlExpireSec *int64 `json:"url_expire_sec,omitempty" xml:"url_expire_sec,omitempty" maximum:"14400" minimum:"10"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s GetFileRequest) String() string {
  return tea.Prettify(s)
}

func (s GetFileRequest) GoString() string {
  return s.String()
}

func (s *GetFileRequest) SetAdditionData(v map[string]interface{}) *GetFileRequest {
  s.AdditionData = v
  return s
}

func (s *GetFileRequest) SetDriveId(v string) *GetFileRequest {
  s.DriveId = &v
  return s
}

func (s *GetFileRequest) SetFields(v string) *GetFileRequest {
  s.Fields = &v
  return s
}

func (s *GetFileRequest) SetFileId(v string) *GetFileRequest {
  s.FileId = &v
  return s
}

func (s *GetFileRequest) SetFileIdPath(v string) *GetFileRequest {
  s.FileIdPath = &v
  return s
}

func (s *GetFileRequest) SetImageCroppingAspectRatios(v []*string) *GetFileRequest {
  s.ImageCroppingAspectRatios = v
  return s
}

func (s *GetFileRequest) SetImageThumbnailProcess(v string) *GetFileRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *GetFileRequest) SetImageUrlProcess(v string) *GetFileRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *GetFileRequest) SetLocation(v string) *GetFileRequest {
  s.Location = &v
  return s
}

func (s *GetFileRequest) SetOfficeThumbnailProcess(v string) *GetFileRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *GetFileRequest) SetReferer(v string) *GetFileRequest {
  s.Referer = &v
  return s
}

func (s *GetFileRequest) SetShareId(v string) *GetFileRequest {
  s.ShareId = &v
  return s
}

func (s *GetFileRequest) SetSignToken(v string) *GetFileRequest {
  s.SignToken = &v
  return s
}

func (s *GetFileRequest) SetUrlExpireSec(v int64) *GetFileRequest {
  s.UrlExpireSec = &v
  return s
}

func (s *GetFileRequest) SetVideoThumbnailProcess(v string) *GetFileRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * 获取文件元数据response
 */
type GetFileResponse struct {
  // category
  Category *string `json:"category,omitempty" xml:"category,omitempty"`
  // CharacteristicHash
  CharacteristicHash *string `json:"characteristic_hash,omitempty" xml:"characteristic_hash,omitempty"`
  // Content Hash
  ContentHash *string `json:"content_hash,omitempty" xml:"content_hash,omitempty"`
  // content_hash_name
  ContentHashName *string `json:"content_hash_name,omitempty" xml:"content_hash_name,omitempty"`
  // content_type
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // crc64_hash
  Crc64Hash *string `json:"crc64_hash,omitempty" xml:"crc64_hash,omitempty"`
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // DomainID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // download_url
  DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // encrypt_mode
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // file_extension
  FileExtension *string `json:"file_extension,omitempty" xml:"file_extension,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // Hidden
  // type: boolean
  Hidden *bool `json:"hidden,omitempty" xml:"hidden,omitempty"`
  ImageMediaMetadata *ImageMediaResponse `json:"image_media_metadata,omitempty" xml:"image_media_metadata,omitempty"`
  // labels
  Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
  Meta *string `json:"meta,omitempty" xml:"meta,omitempty"`
  // name
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
  // parent_file_id
  ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // PunishFlag
  PunishFlag *int64 `json:"punish_flag,omitempty" xml:"punish_flag,omitempty"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // starred
  // type: boolean
  Starred *bool `json:"starred,omitempty" xml:"starred,omitempty"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // @Deprecated streams url info
  StreamsInfo map[string]interface{} `json:"streams_info,omitempty" xml:"streams_info,omitempty"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // Trashed
  // type: boolean
  Trashed *bool `json:"trashed,omitempty" xml:"trashed,omitempty"`
  // trashed_at
  TrashedAt *string `json:"trashed_at,omitempty" xml:"trashed_at,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
  // user_meta
  UserMeta *string `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
  VideoMediaMetadata *VideoMediaResponse `json:"video_media_metadata,omitempty" xml:"video_media_metadata,omitempty"`
  VideoPreviewMetadata *VideoPreviewResponse `json:"video_preview_metadata,omitempty" xml:"video_preview_metadata,omitempty"`
}

func (s GetFileResponse) String() string {
  return tea.Prettify(s)
}

func (s GetFileResponse) GoString() string {
  return s.String()
}

func (s *GetFileResponse) SetCategory(v string) *GetFileResponse {
  s.Category = &v
  return s
}

func (s *GetFileResponse) SetCharacteristicHash(v string) *GetFileResponse {
  s.CharacteristicHash = &v
  return s
}

func (s *GetFileResponse) SetContentHash(v string) *GetFileResponse {
  s.ContentHash = &v
  return s
}

func (s *GetFileResponse) SetContentHashName(v string) *GetFileResponse {
  s.ContentHashName = &v
  return s
}

func (s *GetFileResponse) SetContentType(v string) *GetFileResponse {
  s.ContentType = &v
  return s
}

func (s *GetFileResponse) SetCrc64Hash(v string) *GetFileResponse {
  s.Crc64Hash = &v
  return s
}

func (s *GetFileResponse) SetCreatedAt(v string) *GetFileResponse {
  s.CreatedAt = &v
  return s
}

func (s *GetFileResponse) SetDescription(v string) *GetFileResponse {
  s.Description = &v
  return s
}

func (s *GetFileResponse) SetDomainId(v string) *GetFileResponse {
  s.DomainId = &v
  return s
}

func (s *GetFileResponse) SetDownloadUrl(v string) *GetFileResponse {
  s.DownloadUrl = &v
  return s
}

func (s *GetFileResponse) SetDriveId(v string) *GetFileResponse {
  s.DriveId = &v
  return s
}

func (s *GetFileResponse) SetEncryptMode(v string) *GetFileResponse {
  s.EncryptMode = &v
  return s
}

func (s *GetFileResponse) SetFileExtension(v string) *GetFileResponse {
  s.FileExtension = &v
  return s
}

func (s *GetFileResponse) SetFileId(v string) *GetFileResponse {
  s.FileId = &v
  return s
}

func (s *GetFileResponse) SetHidden(v bool) *GetFileResponse {
  s.Hidden = &v
  return s
}

func (s *GetFileResponse) SetImageMediaMetadata(v *ImageMediaResponse) *GetFileResponse {
  s.ImageMediaMetadata = v
  return s
}

func (s *GetFileResponse) SetLabels(v []*string) *GetFileResponse {
  s.Labels = v
  return s
}

func (s *GetFileResponse) SetMeta(v string) *GetFileResponse {
  s.Meta = &v
  return s
}

func (s *GetFileResponse) SetName(v string) *GetFileResponse {
  s.Name = &v
  return s
}

func (s *GetFileResponse) SetParentFileId(v string) *GetFileResponse {
  s.ParentFileId = &v
  return s
}

func (s *GetFileResponse) SetPunishFlag(v int64) *GetFileResponse {
  s.PunishFlag = &v
  return s
}

func (s *GetFileResponse) SetShareId(v string) *GetFileResponse {
  s.ShareId = &v
  return s
}

func (s *GetFileResponse) SetSize(v int64) *GetFileResponse {
  s.Size = &v
  return s
}

func (s *GetFileResponse) SetStarred(v bool) *GetFileResponse {
  s.Starred = &v
  return s
}

func (s *GetFileResponse) SetStatus(v string) *GetFileResponse {
  s.Status = &v
  return s
}

func (s *GetFileResponse) SetStreamsInfo(v map[string]interface{}) *GetFileResponse {
  s.StreamsInfo = v
  return s
}

func (s *GetFileResponse) SetThumbnail(v string) *GetFileResponse {
  s.Thumbnail = &v
  return s
}

func (s *GetFileResponse) SetTrashed(v bool) *GetFileResponse {
  s.Trashed = &v
  return s
}

func (s *GetFileResponse) SetTrashedAt(v string) *GetFileResponse {
  s.TrashedAt = &v
  return s
}

func (s *GetFileResponse) SetType(v string) *GetFileResponse {
  s.Type = &v
  return s
}

func (s *GetFileResponse) SetUpdatedAt(v string) *GetFileResponse {
  s.UpdatedAt = &v
  return s
}

func (s *GetFileResponse) SetUploadId(v string) *GetFileResponse {
  s.UploadId = &v
  return s
}

func (s *GetFileResponse) SetUrl(v string) *GetFileResponse {
  s.Url = &v
  return s
}

func (s *GetFileResponse) SetUserMeta(v string) *GetFileResponse {
  s.UserMeta = &v
  return s
}

func (s *GetFileResponse) SetVideoMediaMetadata(v *VideoMediaResponse) *GetFileResponse {
  s.VideoMediaMetadata = v
  return s
}

func (s *GetFileResponse) SetVideoPreviewMetadata(v *VideoPreviewResponse) *GetFileResponse {
  s.VideoPreviewMetadata = v
  return s
}

/**
 * 获取最新游标
 */
type GetLastCursorRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
}

func (s GetLastCursorRequest) String() string {
  return tea.Prettify(s)
}

func (s GetLastCursorRequest) GoString() string {
  return s.String()
}

func (s *GetLastCursorRequest) SetDriveId(v string) *GetLastCursorRequest {
  s.DriveId = &v
  return s
}

/**
 * get last file op cursor response
 */
type GetLastCursorResponse struct {
  Cursor *string `json:"cursor,omitempty" xml:"cursor,omitempty"`
}

func (s GetLastCursorResponse) String() string {
  return tea.Prettify(s)
}

func (s GetLastCursorResponse) GoString() string {
  return s.String()
}

func (s *GetLastCursorResponse) SetCursor(v string) *GetLastCursorResponse {
  s.Cursor = &v
  return s
}

/**
 * get_media_play_url request
 */
type GetMediaPlayURLRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
}

func (s GetMediaPlayURLRequest) String() string {
  return tea.Prettify(s)
}

func (s GetMediaPlayURLRequest) GoString() string {
  return s.String()
}

func (s *GetMediaPlayURLRequest) SetDriveId(v string) *GetMediaPlayURLRequest {
  s.DriveId = &v
  return s
}

func (s *GetMediaPlayURLRequest) SetFileId(v string) *GetMediaPlayURLRequest {
  s.FileId = &v
  return s
}

/**
 * get_media_play_url response
 */
type GetMediaPlayURLResponse struct {
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s GetMediaPlayURLResponse) String() string {
  return tea.Prettify(s)
}

func (s GetMediaPlayURLResponse) GoString() string {
  return s.String()
}

func (s *GetMediaPlayURLResponse) SetUrl(v string) *GetMediaPlayURLResponse {
  s.Url = &v
  return s
}

/**
 * GetOfficeEditUrlOption 权限控制
 */
type GetOfficeEditUrlOption struct {
  // Copy
  Copy *bool `json:"copy,omitempty" xml:"copy,omitempty"`
  Readonly *bool `json:"readonly,omitempty" xml:"readonly,omitempty"`
}

func (s GetOfficeEditUrlOption) String() string {
  return tea.Prettify(s)
}

func (s GetOfficeEditUrlOption) GoString() string {
  return s.String()
}

func (s *GetOfficeEditUrlOption) SetCopy(v bool) *GetOfficeEditUrlOption {
  s.Copy = &v
  return s
}

func (s *GetOfficeEditUrlOption) SetReadonly(v bool) *GetOfficeEditUrlOption {
  s.Readonly = &v
  return s
}

/**
 * 获取office文档在线编辑地址
 */
type GetOfficeEditUrlRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  Option *GetOfficeEditUrlOption `json:"option,omitempty" xml:"option,omitempty"`
  Watermark *GetOfficeEditUrlWatermark `json:"watermark,omitempty" xml:"watermark,omitempty"`
}

func (s GetOfficeEditUrlRequest) String() string {
  return tea.Prettify(s)
}

func (s GetOfficeEditUrlRequest) GoString() string {
  return s.String()
}

func (s *GetOfficeEditUrlRequest) SetAdditionData(v map[string]interface{}) *GetOfficeEditUrlRequest {
  s.AdditionData = v
  return s
}

func (s *GetOfficeEditUrlRequest) SetDriveId(v string) *GetOfficeEditUrlRequest {
  s.DriveId = &v
  return s
}

func (s *GetOfficeEditUrlRequest) SetFileId(v string) *GetOfficeEditUrlRequest {
  s.FileId = &v
  return s
}

func (s *GetOfficeEditUrlRequest) SetOption(v *GetOfficeEditUrlOption) *GetOfficeEditUrlRequest {
  s.Option = v
  return s
}

func (s *GetOfficeEditUrlRequest) SetWatermark(v *GetOfficeEditUrlWatermark) *GetOfficeEditUrlRequest {
  s.Watermark = v
  return s
}

/**
 * 获取office文档在线编辑地址 response
 */
type GetOfficeEditUrlResponse struct {
  // EditUrl
  EditUrl *string `json:"edit_url,omitempty" xml:"edit_url,omitempty"`
  // AccessToken
  OfficeAccessToken *string `json:"office_access_token,omitempty" xml:"office_access_token,omitempty"`
  // RefreshToken
  OfficeRefreshToken *string `json:"office_refresh_token,omitempty" xml:"office_refresh_token,omitempty"`
}

func (s GetOfficeEditUrlResponse) String() string {
  return tea.Prettify(s)
}

func (s GetOfficeEditUrlResponse) GoString() string {
  return s.String()
}

func (s *GetOfficeEditUrlResponse) SetEditUrl(v string) *GetOfficeEditUrlResponse {
  s.EditUrl = &v
  return s
}

func (s *GetOfficeEditUrlResponse) SetOfficeAccessToken(v string) *GetOfficeEditUrlResponse {
  s.OfficeAccessToken = &v
  return s
}

func (s *GetOfficeEditUrlResponse) SetOfficeRefreshToken(v string) *GetOfficeEditUrlResponse {
  s.OfficeRefreshToken = &v
  return s
}

/**
 * GetOfficeEditUrlWatermark 水印配置
 */
type GetOfficeEditUrlWatermark struct {
  // FillStyle
  Fillstyle *string `json:"fillstyle,omitempty" xml:"fillstyle,omitempty"`
  // Font
  Font *string `json:"font,omitempty" xml:"font,omitempty"`
  // Horizontal
  Horizontal *int64 `json:"horizontal,omitempty" xml:"horizontal,omitempty"`
  // Rotate
  Rotate *float64 `json:"rotate,omitempty" xml:"rotate,omitempty"`
  // Type
  Type *int32 `json:"type,omitempty" xml:"type,omitempty"`
  // Value
  Value *string `json:"value,omitempty" xml:"value,omitempty"`
  // Vertical
  Vertical *int64 `json:"vertical,omitempty" xml:"vertical,omitempty"`
}

func (s GetOfficeEditUrlWatermark) String() string {
  return tea.Prettify(s)
}

func (s GetOfficeEditUrlWatermark) GoString() string {
  return s.String()
}

func (s *GetOfficeEditUrlWatermark) SetFillstyle(v string) *GetOfficeEditUrlWatermark {
  s.Fillstyle = &v
  return s
}

func (s *GetOfficeEditUrlWatermark) SetFont(v string) *GetOfficeEditUrlWatermark {
  s.Font = &v
  return s
}

func (s *GetOfficeEditUrlWatermark) SetHorizontal(v int64) *GetOfficeEditUrlWatermark {
  s.Horizontal = &v
  return s
}

func (s *GetOfficeEditUrlWatermark) SetRotate(v float64) *GetOfficeEditUrlWatermark {
  s.Rotate = &v
  return s
}

func (s *GetOfficeEditUrlWatermark) SetType(v int32) *GetOfficeEditUrlWatermark {
  s.Type = &v
  return s
}

func (s *GetOfficeEditUrlWatermark) SetValue(v string) *GetOfficeEditUrlWatermark {
  s.Value = &v
  return s
}

func (s *GetOfficeEditUrlWatermark) SetVertical(v int64) *GetOfficeEditUrlWatermark {
  s.Vertical = &v
  return s
}

/**
 * 获取office文档预览地址
 */
type GetOfficePreviewUrlRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id, either share_id or drive_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
}

func (s GetOfficePreviewUrlRequest) String() string {
  return tea.Prettify(s)
}

func (s GetOfficePreviewUrlRequest) GoString() string {
  return s.String()
}

func (s *GetOfficePreviewUrlRequest) SetAdditionData(v map[string]interface{}) *GetOfficePreviewUrlRequest {
  s.AdditionData = v
  return s
}

func (s *GetOfficePreviewUrlRequest) SetDriveId(v string) *GetOfficePreviewUrlRequest {
  s.DriveId = &v
  return s
}

func (s *GetOfficePreviewUrlRequest) SetFileId(v string) *GetOfficePreviewUrlRequest {
  s.FileId = &v
  return s
}

func (s *GetOfficePreviewUrlRequest) SetReferer(v string) *GetOfficePreviewUrlRequest {
  s.Referer = &v
  return s
}

func (s *GetOfficePreviewUrlRequest) SetShareId(v string) *GetOfficePreviewUrlRequest {
  s.ShareId = &v
  return s
}

/**
 * 获取文档预览地址 response
 */
type GetOfficePreviewUrlResponse struct {
  // AccessToken
  AccessToken *string `json:"access_token,omitempty" xml:"access_token,omitempty"`
  // preview_url
  PreviewUrl *string `json:"preview_url,omitempty" xml:"preview_url,omitempty"`
}

func (s GetOfficePreviewUrlResponse) String() string {
  return tea.Prettify(s)
}

func (s GetOfficePreviewUrlResponse) GoString() string {
  return s.String()
}

func (s *GetOfficePreviewUrlResponse) SetAccessToken(v string) *GetOfficePreviewUrlResponse {
  s.AccessToken = &v
  return s
}

func (s *GetOfficePreviewUrlResponse) SetPreviewUrl(v string) *GetOfficePreviewUrlResponse {
  s.PreviewUrl = &v
  return s
}

/**
 * 
 */
type GetPublicKeyResponse struct {
  // App ID
  AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
  KeyPairId *string `json:"key_pair_id,omitempty" xml:"key_pair_id,omitempty"`
  // RSA加密算法的公钥, PEM格式
  PublicKey *string `json:"public_key,omitempty" xml:"public_key,omitempty" require:"true"`
}

func (s GetPublicKeyResponse) String() string {
  return tea.Prettify(s)
}

func (s GetPublicKeyResponse) GoString() string {
  return s.String()
}

func (s *GetPublicKeyResponse) SetAppId(v string) *GetPublicKeyResponse {
  s.AppId = &v
  return s
}

func (s *GetPublicKeyResponse) SetKeyPairId(v string) *GetPublicKeyResponse {
  s.KeyPairId = &v
  return s
}

func (s *GetPublicKeyResponse) SetPublicKey(v string) *GetPublicKeyResponse {
  s.PublicKey = &v
  return s
}

/**
 * get_share_link_by_anonymous request
 */
type GetShareLinkByAnonymousRequest struct {
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
}

func (s GetShareLinkByAnonymousRequest) String() string {
  return tea.Prettify(s)
}

func (s GetShareLinkByAnonymousRequest) GoString() string {
  return s.String()
}

func (s *GetShareLinkByAnonymousRequest) SetShareId(v string) *GetShareLinkByAnonymousRequest {
  s.ShareId = &v
  return s
}

/**
 * get_share_link_by_anonymous response
 */
type GetShareLinkByAnonymousResponse struct {
  // avatar
  Avatar *string `json:"avatar,omitempty" xml:"avatar,omitempty"`
  // creator_id
  CreatorId *string `json:"creator_id,omitempty" xml:"creator_id,omitempty"`
  // creator_name
  CreatorName *string `json:"creator_name,omitempty" xml:"creator_name,omitempty"`
  // creator_phone
  CreatorPhone *string `json:"creator_phone,omitempty" xml:"creator_phone,omitempty"`
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // file_count
  FileCount *int64 `json:"file_count,omitempty" xml:"file_count,omitempty"`
  // share_name
  ShareName *string `json:"share_name,omitempty" xml:"share_name,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s GetShareLinkByAnonymousResponse) String() string {
  return tea.Prettify(s)
}

func (s GetShareLinkByAnonymousResponse) GoString() string {
  return s.String()
}

func (s *GetShareLinkByAnonymousResponse) SetAvatar(v string) *GetShareLinkByAnonymousResponse {
  s.Avatar = &v
  return s
}

func (s *GetShareLinkByAnonymousResponse) SetCreatorId(v string) *GetShareLinkByAnonymousResponse {
  s.CreatorId = &v
  return s
}

func (s *GetShareLinkByAnonymousResponse) SetCreatorName(v string) *GetShareLinkByAnonymousResponse {
  s.CreatorName = &v
  return s
}

func (s *GetShareLinkByAnonymousResponse) SetCreatorPhone(v string) *GetShareLinkByAnonymousResponse {
  s.CreatorPhone = &v
  return s
}

func (s *GetShareLinkByAnonymousResponse) SetExpiration(v string) *GetShareLinkByAnonymousResponse {
  s.Expiration = &v
  return s
}

func (s *GetShareLinkByAnonymousResponse) SetFileCount(v int64) *GetShareLinkByAnonymousResponse {
  s.FileCount = &v
  return s
}

func (s *GetShareLinkByAnonymousResponse) SetShareName(v string) *GetShareLinkByAnonymousResponse {
  s.ShareName = &v
  return s
}

func (s *GetShareLinkByAnonymousResponse) SetUpdatedAt(v string) *GetShareLinkByAnonymousResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * 获取分享中文件下载地址的请求body
 */
type GetShareLinkDownloadURLRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // expire_sec
  ExpireSec *int64 `json:"expire_sec,omitempty" xml:"expire_sec,omitempty" maximum:"600" minimum:"1"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  FileIdPath *string `json:"file_id_path,omitempty" xml:"file_id_path,omitempty"`
  // get_audio_play_info
  GetAudioPlayInfo *bool `json:"get_audio_play_info,omitempty" xml:"get_audio_play_info,omitempty"`
  // get_video_play_info
  GetVideoPlayInfo *bool `json:"get_video_play_info,omitempty" xml:"get_video_play_info,omitempty"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" require:"true"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s GetShareLinkDownloadURLRequest) String() string {
  return tea.Prettify(s)
}

func (s GetShareLinkDownloadURLRequest) GoString() string {
  return s.String()
}

func (s *GetShareLinkDownloadURLRequest) SetAdditionData(v map[string]interface{}) *GetShareLinkDownloadURLRequest {
  s.AdditionData = v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetExpireSec(v int64) *GetShareLinkDownloadURLRequest {
  s.ExpireSec = &v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetFileId(v string) *GetShareLinkDownloadURLRequest {
  s.FileId = &v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetFileIdPath(v string) *GetShareLinkDownloadURLRequest {
  s.FileIdPath = &v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetGetAudioPlayInfo(v bool) *GetShareLinkDownloadURLRequest {
  s.GetAudioPlayInfo = &v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetGetVideoPlayInfo(v bool) *GetShareLinkDownloadURLRequest {
  s.GetVideoPlayInfo = &v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetImageThumbnailProcess(v string) *GetShareLinkDownloadURLRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetImageUrlProcess(v string) *GetShareLinkDownloadURLRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetLocation(v string) *GetShareLinkDownloadURLRequest {
  s.Location = &v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetOfficeThumbnailProcess(v string) *GetShareLinkDownloadURLRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetReferer(v string) *GetShareLinkDownloadURLRequest {
  s.Referer = &v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetShareId(v string) *GetShareLinkDownloadURLRequest {
  s.ShareId = &v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetSignToken(v string) *GetShareLinkDownloadURLRequest {
  s.SignToken = &v
  return s
}

func (s *GetShareLinkDownloadURLRequest) SetVideoThumbnailProcess(v string) *GetShareLinkDownloadURLRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * 获取分享中文件数据response
 */
type GetShareLinkDownloadURLResponse struct {
  // audio_template_list
  AudioTemplateList []*MediaPlayInfoTemplate `json:"audio_template_list,omitempty" xml:"audio_template_list,omitempty" type:"Repeated"`
  // download_url
  DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
  // @Deprecated streams url info
  StreamsInfo map[string]interface{} `json:"streams_info,omitempty" xml:"streams_info,omitempty"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
  // video_template_list
  VideoTemplateList []*MediaPlayInfoTemplate `json:"video_template_list,omitempty" xml:"video_template_list,omitempty" type:"Repeated"`
}

func (s GetShareLinkDownloadURLResponse) String() string {
  return tea.Prettify(s)
}

func (s GetShareLinkDownloadURLResponse) GoString() string {
  return s.String()
}

func (s *GetShareLinkDownloadURLResponse) SetAudioTemplateList(v []*MediaPlayInfoTemplate) *GetShareLinkDownloadURLResponse {
  s.AudioTemplateList = v
  return s
}

func (s *GetShareLinkDownloadURLResponse) SetDownloadUrl(v string) *GetShareLinkDownloadURLResponse {
  s.DownloadUrl = &v
  return s
}

func (s *GetShareLinkDownloadURLResponse) SetStreamsInfo(v map[string]interface{}) *GetShareLinkDownloadURLResponse {
  s.StreamsInfo = v
  return s
}

func (s *GetShareLinkDownloadURLResponse) SetThumbnail(v string) *GetShareLinkDownloadURLResponse {
  s.Thumbnail = &v
  return s
}

func (s *GetShareLinkDownloadURLResponse) SetUrl(v string) *GetShareLinkDownloadURLResponse {
  s.Url = &v
  return s
}

func (s *GetShareLinkDownloadURLResponse) SetVideoTemplateList(v []*MediaPlayInfoTemplate) *GetShareLinkDownloadURLResponse {
  s.VideoTemplateList = v
  return s
}

/**
 * get_share_id request
 */
type GetShareLinkIDRequest struct {
  // share_msg
  ShareMsg *string `json:"share_msg,omitempty" xml:"share_msg,omitempty"`
}

func (s GetShareLinkIDRequest) String() string {
  return tea.Prettify(s)
}

func (s GetShareLinkIDRequest) GoString() string {
  return s.String()
}

func (s *GetShareLinkIDRequest) SetShareMsg(v string) *GetShareLinkIDRequest {
  s.ShareMsg = &v
  return s
}

/**
 * get_share_id response
 */
type GetShareLinkIDResponse struct {
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // share_pwd
  SharePwd *string `json:"share_pwd,omitempty" xml:"share_pwd,omitempty"`
}

func (s GetShareLinkIDResponse) String() string {
  return tea.Prettify(s)
}

func (s GetShareLinkIDResponse) GoString() string {
  return s.String()
}

func (s *GetShareLinkIDResponse) SetShareId(v string) *GetShareLinkIDResponse {
  s.ShareId = &v
  return s
}

func (s *GetShareLinkIDResponse) SetSharePwd(v string) *GetShareLinkIDResponse {
  s.SharePwd = &v
  return s
}

/**
 * get_share request
 */
type GetShareLinkRequest struct {
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
}

func (s GetShareLinkRequest) String() string {
  return tea.Prettify(s)
}

func (s GetShareLinkRequest) GoString() string {
  return s.String()
}

func (s *GetShareLinkRequest) SetShareId(v string) *GetShareLinkRequest {
  s.ShareId = &v
  return s
}

/**
 * get_share_token request
 */
type GetShareLinkTokenRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // expire_sec
  ExpireSec *int64 `json:"expire_sec,omitempty" xml:"expire_sec,omitempty" maximum:"7200" minimum:"0"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // share_pwd
  SharePwd *string `json:"share_pwd,omitempty" xml:"share_pwd,omitempty"`
}

func (s GetShareLinkTokenRequest) String() string {
  return tea.Prettify(s)
}

func (s GetShareLinkTokenRequest) GoString() string {
  return s.String()
}

func (s *GetShareLinkTokenRequest) SetAdditionData(v map[string]interface{}) *GetShareLinkTokenRequest {
  s.AdditionData = v
  return s
}

func (s *GetShareLinkTokenRequest) SetExpireSec(v int64) *GetShareLinkTokenRequest {
  s.ExpireSec = &v
  return s
}

func (s *GetShareLinkTokenRequest) SetReferer(v string) *GetShareLinkTokenRequest {
  s.Referer = &v
  return s
}

func (s *GetShareLinkTokenRequest) SetShareId(v string) *GetShareLinkTokenRequest {
  s.ShareId = &v
  return s
}

func (s *GetShareLinkTokenRequest) SetSharePwd(v string) *GetShareLinkTokenRequest {
  s.SharePwd = &v
  return s
}

/**
 * get_share_token response
 */
type GetShareLinkTokenResponse struct {
  // expire_time
  ExpireTime *string `json:"expire_time,omitempty" xml:"expire_time,omitempty" require:"true"`
  // expires_in
  ExpiresIn *int64 `json:"expires_in,omitempty" xml:"expires_in,omitempty" require:"true"`
  // share_token
  ShareToken *string `json:"share_token,omitempty" xml:"share_token,omitempty" require:"true"`
}

func (s GetShareLinkTokenResponse) String() string {
  return tea.Prettify(s)
}

func (s GetShareLinkTokenResponse) GoString() string {
  return s.String()
}

func (s *GetShareLinkTokenResponse) SetExpireTime(v string) *GetShareLinkTokenResponse {
  s.ExpireTime = &v
  return s
}

func (s *GetShareLinkTokenResponse) SetExpiresIn(v int64) *GetShareLinkTokenResponse {
  s.ExpiresIn = &v
  return s
}

func (s *GetShareLinkTokenResponse) SetShareToken(v string) *GetShareLinkTokenResponse {
  s.ShareToken = &v
  return s
}

/**
 * get share request
 */
type GetShareRequest struct {
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
}

func (s GetShareRequest) String() string {
  return tea.Prettify(s)
}

func (s GetShareRequest) GoString() string {
  return s.String()
}

func (s *GetShareRequest) SetShareId(v string) *GetShareRequest {
  s.ShareId = &v
  return s
}

/**
 * Get share response
 */
type GetShareResponse struct {
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // creator
  Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty"`
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // expired
  Expired *bool `json:"expired,omitempty" xml:"expired,omitempty"`
  // owner
  Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
  // owner
  OwnerType *string `json:"owner_type,omitempty" xml:"owner_type,omitempty"`
  // permissions
  Permissions []*string `json:"permissions,omitempty" xml:"permissions,omitempty" type:"Repeated"`
  // share_file_id
  ShareFileId *string `json:"share_file_id,omitempty" xml:"share_file_id,omitempty"`
  // share_path
  ShareFilePath *string `json:"share_file_path,omitempty" xml:"share_file_path,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // share_name
  ShareName *string `json:"share_name,omitempty" xml:"share_name,omitempty"`
  SharePolicy []*SharePermissionPolicy `json:"share_policy,omitempty" xml:"share_policy,omitempty" type:"Repeated"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s GetShareResponse) String() string {
  return tea.Prettify(s)
}

func (s GetShareResponse) GoString() string {
  return s.String()
}

func (s *GetShareResponse) SetCreatedAt(v string) *GetShareResponse {
  s.CreatedAt = &v
  return s
}

func (s *GetShareResponse) SetCreator(v string) *GetShareResponse {
  s.Creator = &v
  return s
}

func (s *GetShareResponse) SetDescription(v string) *GetShareResponse {
  s.Description = &v
  return s
}

func (s *GetShareResponse) SetDomainId(v string) *GetShareResponse {
  s.DomainId = &v
  return s
}

func (s *GetShareResponse) SetDriveId(v string) *GetShareResponse {
  s.DriveId = &v
  return s
}

func (s *GetShareResponse) SetExpiration(v string) *GetShareResponse {
  s.Expiration = &v
  return s
}

func (s *GetShareResponse) SetExpired(v bool) *GetShareResponse {
  s.Expired = &v
  return s
}

func (s *GetShareResponse) SetOwner(v string) *GetShareResponse {
  s.Owner = &v
  return s
}

func (s *GetShareResponse) SetOwnerType(v string) *GetShareResponse {
  s.OwnerType = &v
  return s
}

func (s *GetShareResponse) SetPermissions(v []*string) *GetShareResponse {
  s.Permissions = v
  return s
}

func (s *GetShareResponse) SetShareFileId(v string) *GetShareResponse {
  s.ShareFileId = &v
  return s
}

func (s *GetShareResponse) SetShareFilePath(v string) *GetShareResponse {
  s.ShareFilePath = &v
  return s
}

func (s *GetShareResponse) SetShareId(v string) *GetShareResponse {
  s.ShareId = &v
  return s
}

func (s *GetShareResponse) SetShareName(v string) *GetShareResponse {
  s.ShareName = &v
  return s
}

func (s *GetShareResponse) SetSharePolicy(v []*SharePermissionPolicy) *GetShareResponse {
  s.SharePolicy = v
  return s
}

func (s *GetShareResponse) SetStatus(v string) *GetShareResponse {
  s.Status = &v
  return s
}

func (s *GetShareResponse) SetUpdatedAt(v string) *GetShareResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * 获取文件上传URL
 */
type GetUploadUrlRequest struct {
  // content_md5
  ContentMd5 *string `json:"content_md5,omitempty" xml:"content_md5,omitempty" maxLength:"32"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // upload_part_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty" require:"true"`
}

func (s GetUploadUrlRequest) String() string {
  return tea.Prettify(s)
}

func (s GetUploadUrlRequest) GoString() string {
  return s.String()
}

func (s *GetUploadUrlRequest) SetContentMd5(v string) *GetUploadUrlRequest {
  s.ContentMd5 = &v
  return s
}

func (s *GetUploadUrlRequest) SetDriveId(v string) *GetUploadUrlRequest {
  s.DriveId = &v
  return s
}

func (s *GetUploadUrlRequest) SetFileId(v string) *GetUploadUrlRequest {
  s.FileId = &v
  return s
}

func (s *GetUploadUrlRequest) SetPartInfoList(v []*UploadPartInfo) *GetUploadUrlRequest {
  s.PartInfoList = v
  return s
}

func (s *GetUploadUrlRequest) SetShareId(v string) *GetUploadUrlRequest {
  s.ShareId = &v
  return s
}

func (s *GetUploadUrlRequest) SetUploadId(v string) *GetUploadUrlRequest {
  s.UploadId = &v
  return s
}

/**
 * Get UploadUrl Response
 */
type GetUploadUrlResponse struct {
  // created_at
  CreateAt *string `json:"create_at,omitempty" xml:"create_at,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // part_info_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
}

func (s GetUploadUrlResponse) String() string {
  return tea.Prettify(s)
}

func (s GetUploadUrlResponse) GoString() string {
  return s.String()
}

func (s *GetUploadUrlResponse) SetCreateAt(v string) *GetUploadUrlResponse {
  s.CreateAt = &v
  return s
}

func (s *GetUploadUrlResponse) SetDomainId(v string) *GetUploadUrlResponse {
  s.DomainId = &v
  return s
}

func (s *GetUploadUrlResponse) SetDriveId(v string) *GetUploadUrlResponse {
  s.DriveId = &v
  return s
}

func (s *GetUploadUrlResponse) SetFileId(v string) *GetUploadUrlResponse {
  s.FileId = &v
  return s
}

func (s *GetUploadUrlResponse) SetPartInfoList(v []*UploadPartInfo) *GetUploadUrlResponse {
  s.PartInfoList = v
  return s
}

func (s *GetUploadUrlResponse) SetUploadId(v string) *GetUploadUrlResponse {
  s.UploadId = &v
  return s
}

/**
 * 获取视频雪碧图地址的请求body
 */
type GetVideoPreviewSpriteURLRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // expire_sec
  ExpireSec *int64 `json:"expire_sec,omitempty" xml:"expire_sec,omitempty" maximum:"14400" minimum:"1"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id, either share_id or drive_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
}

func (s GetVideoPreviewSpriteURLRequest) String() string {
  return tea.Prettify(s)
}

func (s GetVideoPreviewSpriteURLRequest) GoString() string {
  return s.String()
}

func (s *GetVideoPreviewSpriteURLRequest) SetAdditionData(v map[string]interface{}) *GetVideoPreviewSpriteURLRequest {
  s.AdditionData = v
  return s
}

func (s *GetVideoPreviewSpriteURLRequest) SetDriveId(v string) *GetVideoPreviewSpriteURLRequest {
  s.DriveId = &v
  return s
}

func (s *GetVideoPreviewSpriteURLRequest) SetExpireSec(v int64) *GetVideoPreviewSpriteURLRequest {
  s.ExpireSec = &v
  return s
}

func (s *GetVideoPreviewSpriteURLRequest) SetFileId(v string) *GetVideoPreviewSpriteURLRequest {
  s.FileId = &v
  return s
}

func (s *GetVideoPreviewSpriteURLRequest) SetReferer(v string) *GetVideoPreviewSpriteURLRequest {
  s.Referer = &v
  return s
}

func (s *GetVideoPreviewSpriteURLRequest) SetShareId(v string) *GetVideoPreviewSpriteURLRequest {
  s.ShareId = &v
  return s
}

func (s *GetVideoPreviewSpriteURLRequest) SetSignToken(v string) *GetVideoPreviewSpriteURLRequest {
  s.SignToken = &v
  return s
}

/**
 * 获取视频雪碧图地址 url response
 */
type GetVideoPreviewSpriteURLResponse struct {
  // col
  Col *int64 `json:"col,omitempty" xml:"col,omitempty"`
  // count
  Count *int64 `json:"count,omitempty" xml:"count,omitempty"`
  // frame_count
  FrameCount *int64 `json:"frame_count,omitempty" xml:"frame_count,omitempty"`
  // frame_height
  FrameHeight *int64 `json:"frame_height,omitempty" xml:"frame_height,omitempty"`
  // frame_width
  FrameWidth *int64 `json:"frame_width,omitempty" xml:"frame_width,omitempty"`
  // row
  Row *int64 `json:"row,omitempty" xml:"row,omitempty"`
  // sprite_url_list
  SpriteUrlList []*string `json:"sprite_url_list,omitempty" xml:"sprite_url_list,omitempty" type:"Repeated"`
}

func (s GetVideoPreviewSpriteURLResponse) String() string {
  return tea.Prettify(s)
}

func (s GetVideoPreviewSpriteURLResponse) GoString() string {
  return s.String()
}

func (s *GetVideoPreviewSpriteURLResponse) SetCol(v int64) *GetVideoPreviewSpriteURLResponse {
  s.Col = &v
  return s
}

func (s *GetVideoPreviewSpriteURLResponse) SetCount(v int64) *GetVideoPreviewSpriteURLResponse {
  s.Count = &v
  return s
}

func (s *GetVideoPreviewSpriteURLResponse) SetFrameCount(v int64) *GetVideoPreviewSpriteURLResponse {
  s.FrameCount = &v
  return s
}

func (s *GetVideoPreviewSpriteURLResponse) SetFrameHeight(v int64) *GetVideoPreviewSpriteURLResponse {
  s.FrameHeight = &v
  return s
}

func (s *GetVideoPreviewSpriteURLResponse) SetFrameWidth(v int64) *GetVideoPreviewSpriteURLResponse {
  s.FrameWidth = &v
  return s
}

func (s *GetVideoPreviewSpriteURLResponse) SetRow(v int64) *GetVideoPreviewSpriteURLResponse {
  s.Row = &v
  return s
}

func (s *GetVideoPreviewSpriteURLResponse) SetSpriteUrlList(v []*string) *GetVideoPreviewSpriteURLResponse {
  s.SpriteUrlList = v
  return s
}

/**
 * 获取视频文件播放地址的请求body
 */
type GetVideoPreviewURLRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // audio_template_id
  AudioTemplateId *string `json:"audio_template_id,omitempty" xml:"audio_template_id,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // expire_sec
  ExpireSec *int64 `json:"expire_sec,omitempty" xml:"expire_sec,omitempty" maximum:"14400" minimum:"1"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id, either share_id or drive_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // template_id
  TemplateId *string `json:"template_id,omitempty" xml:"template_id,omitempty"`
}

func (s GetVideoPreviewURLRequest) String() string {
  return tea.Prettify(s)
}

func (s GetVideoPreviewURLRequest) GoString() string {
  return s.String()
}

func (s *GetVideoPreviewURLRequest) SetAdditionData(v map[string]interface{}) *GetVideoPreviewURLRequest {
  s.AdditionData = v
  return s
}

func (s *GetVideoPreviewURLRequest) SetAudioTemplateId(v string) *GetVideoPreviewURLRequest {
  s.AudioTemplateId = &v
  return s
}

func (s *GetVideoPreviewURLRequest) SetDriveId(v string) *GetVideoPreviewURLRequest {
  s.DriveId = &v
  return s
}

func (s *GetVideoPreviewURLRequest) SetExpireSec(v int64) *GetVideoPreviewURLRequest {
  s.ExpireSec = &v
  return s
}

func (s *GetVideoPreviewURLRequest) SetFileId(v string) *GetVideoPreviewURLRequest {
  s.FileId = &v
  return s
}

func (s *GetVideoPreviewURLRequest) SetReferer(v string) *GetVideoPreviewURLRequest {
  s.Referer = &v
  return s
}

func (s *GetVideoPreviewURLRequest) SetShareId(v string) *GetVideoPreviewURLRequest {
  s.ShareId = &v
  return s
}

func (s *GetVideoPreviewURLRequest) SetSignToken(v string) *GetVideoPreviewURLRequest {
  s.SignToken = &v
  return s
}

func (s *GetVideoPreviewURLRequest) SetTemplateId(v string) *GetVideoPreviewURLRequest {
  s.TemplateId = &v
  return s
}

/**
 * 获取视频文件播放 url response
 */
type GetVideoPreviewURLResponse struct {
  // preview_url
  PreviewUrl *string `json:"preview_url,omitempty" xml:"preview_url,omitempty"`
}

func (s GetVideoPreviewURLResponse) String() string {
  return tea.Prettify(s)
}

func (s GetVideoPreviewURLResponse) GoString() string {
  return s.String()
}

func (s *GetVideoPreviewURLResponse) SetPreviewUrl(v string) *GetVideoPreviewURLResponse {
  s.PreviewUrl = &v
  return s
}

/**
 * complete file request
 */
type HostingCompleteFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  // forbid_overwrite
  // type: boolean
  ForbidOverwrite *bool `json:"forbid_overwrite,omitempty" xml:"forbid_overwrite,omitempty"`
  // part_info_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
}

func (s HostingCompleteFileRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingCompleteFileRequest) GoString() string {
  return s.String()
}

func (s *HostingCompleteFileRequest) SetAdditionData(v map[string]interface{}) *HostingCompleteFileRequest {
  s.AdditionData = v
  return s
}

func (s *HostingCompleteFileRequest) SetDriveId(v string) *HostingCompleteFileRequest {
  s.DriveId = &v
  return s
}

func (s *HostingCompleteFileRequest) SetFilePath(v string) *HostingCompleteFileRequest {
  s.FilePath = &v
  return s
}

func (s *HostingCompleteFileRequest) SetForbidOverwrite(v bool) *HostingCompleteFileRequest {
  s.ForbidOverwrite = &v
  return s
}

func (s *HostingCompleteFileRequest) SetPartInfoList(v []*UploadPartInfo) *HostingCompleteFileRequest {
  s.PartInfoList = v
  return s
}

func (s *HostingCompleteFileRequest) SetShareId(v string) *HostingCompleteFileRequest {
  s.ShareId = &v
  return s
}

func (s *HostingCompleteFileRequest) SetUploadId(v string) *HostingCompleteFileRequest {
  s.UploadId = &v
  return s
}

/**
 * complete file response
 */
type HostingCompleteFileResponse struct {
  // Content Hash
  ContentHash *string `json:"content_hash,omitempty" xml:"content_hash,omitempty"`
  // content_hash_name
  ContentHashName *string `json:"content_hash_name,omitempty" xml:"content_hash_name,omitempty"`
  // content_type
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // crc
  Crc *string `json:"crc,omitempty" xml:"crc,omitempty"`
  // crc64_hash
  Crc64Hash *string `json:"crc64_hash,omitempty" xml:"crc64_hash,omitempty"`
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // download_url
  DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_extension
  FileExtension *string `json:"file_extension,omitempty" xml:"file_extension,omitempty"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  // name
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
  // parent_file_id
  ParentFilePath *string `json:"parent_file_path,omitempty" xml:"parent_file_path,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9]+"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // trashed_at
  TrashedAt *string `json:"trashed_at,omitempty" xml:"trashed_at,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s HostingCompleteFileResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingCompleteFileResponse) GoString() string {
  return s.String()
}

func (s *HostingCompleteFileResponse) SetContentHash(v string) *HostingCompleteFileResponse {
  s.ContentHash = &v
  return s
}

func (s *HostingCompleteFileResponse) SetContentHashName(v string) *HostingCompleteFileResponse {
  s.ContentHashName = &v
  return s
}

func (s *HostingCompleteFileResponse) SetContentType(v string) *HostingCompleteFileResponse {
  s.ContentType = &v
  return s
}

func (s *HostingCompleteFileResponse) SetCrc(v string) *HostingCompleteFileResponse {
  s.Crc = &v
  return s
}

func (s *HostingCompleteFileResponse) SetCrc64Hash(v string) *HostingCompleteFileResponse {
  s.Crc64Hash = &v
  return s
}

func (s *HostingCompleteFileResponse) SetCreatedAt(v string) *HostingCompleteFileResponse {
  s.CreatedAt = &v
  return s
}

func (s *HostingCompleteFileResponse) SetDescription(v string) *HostingCompleteFileResponse {
  s.Description = &v
  return s
}

func (s *HostingCompleteFileResponse) SetDomainId(v string) *HostingCompleteFileResponse {
  s.DomainId = &v
  return s
}

func (s *HostingCompleteFileResponse) SetDownloadUrl(v string) *HostingCompleteFileResponse {
  s.DownloadUrl = &v
  return s
}

func (s *HostingCompleteFileResponse) SetDriveId(v string) *HostingCompleteFileResponse {
  s.DriveId = &v
  return s
}

func (s *HostingCompleteFileResponse) SetFileExtension(v string) *HostingCompleteFileResponse {
  s.FileExtension = &v
  return s
}

func (s *HostingCompleteFileResponse) SetFilePath(v string) *HostingCompleteFileResponse {
  s.FilePath = &v
  return s
}

func (s *HostingCompleteFileResponse) SetName(v string) *HostingCompleteFileResponse {
  s.Name = &v
  return s
}

func (s *HostingCompleteFileResponse) SetParentFilePath(v string) *HostingCompleteFileResponse {
  s.ParentFilePath = &v
  return s
}

func (s *HostingCompleteFileResponse) SetShareId(v string) *HostingCompleteFileResponse {
  s.ShareId = &v
  return s
}

func (s *HostingCompleteFileResponse) SetSize(v int64) *HostingCompleteFileResponse {
  s.Size = &v
  return s
}

func (s *HostingCompleteFileResponse) SetStatus(v string) *HostingCompleteFileResponse {
  s.Status = &v
  return s
}

func (s *HostingCompleteFileResponse) SetThumbnail(v string) *HostingCompleteFileResponse {
  s.Thumbnail = &v
  return s
}

func (s *HostingCompleteFileResponse) SetTrashedAt(v string) *HostingCompleteFileResponse {
  s.TrashedAt = &v
  return s
}

func (s *HostingCompleteFileResponse) SetType(v string) *HostingCompleteFileResponse {
  s.Type = &v
  return s
}

func (s *HostingCompleteFileResponse) SetUpdatedAt(v string) *HostingCompleteFileResponse {
  s.UpdatedAt = &v
  return s
}

func (s *HostingCompleteFileResponse) SetUploadId(v string) *HostingCompleteFileResponse {
  s.UploadId = &v
  return s
}

func (s *HostingCompleteFileResponse) SetUrl(v string) *HostingCompleteFileResponse {
  s.Url = &v
  return s
}

/**
 * copy file request
 */
type HostingCopyFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true"`
  // new_name
  NewName *string `json:"new_name,omitempty" xml:"new_name,omitempty" maxLength:"1024" minLength:"1"`
  // overwrite
  // type: boolean
  Overwrite *bool `json:"overwrite,omitempty" xml:"overwrite,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
  // to_drive_id
  ToDriveId *string `json:"to_drive_id,omitempty" xml:"to_drive_id,omitempty" pattern:"[0-9]+"`
  // to_parent_file_path
  ToParentFilePath *string `json:"to_parent_file_path,omitempty" xml:"to_parent_file_path,omitempty" require:"true"`
  // share_id
  ToShareId *string `json:"to_share_id,omitempty" xml:"to_share_id,omitempty"`
}

func (s HostingCopyFileRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingCopyFileRequest) GoString() string {
  return s.String()
}

func (s *HostingCopyFileRequest) SetAdditionData(v map[string]interface{}) *HostingCopyFileRequest {
  s.AdditionData = v
  return s
}

func (s *HostingCopyFileRequest) SetDriveId(v string) *HostingCopyFileRequest {
  s.DriveId = &v
  return s
}

func (s *HostingCopyFileRequest) SetFilePath(v string) *HostingCopyFileRequest {
  s.FilePath = &v
  return s
}

func (s *HostingCopyFileRequest) SetNewName(v string) *HostingCopyFileRequest {
  s.NewName = &v
  return s
}

func (s *HostingCopyFileRequest) SetOverwrite(v bool) *HostingCopyFileRequest {
  s.Overwrite = &v
  return s
}

func (s *HostingCopyFileRequest) SetReferer(v string) *HostingCopyFileRequest {
  s.Referer = &v
  return s
}

func (s *HostingCopyFileRequest) SetShareId(v string) *HostingCopyFileRequest {
  s.ShareId = &v
  return s
}

func (s *HostingCopyFileRequest) SetToDriveId(v string) *HostingCopyFileRequest {
  s.ToDriveId = &v
  return s
}

func (s *HostingCopyFileRequest) SetToParentFilePath(v string) *HostingCopyFileRequest {
  s.ToParentFilePath = &v
  return s
}

func (s *HostingCopyFileRequest) SetToShareId(v string) *HostingCopyFileRequest {
  s.ToShareId = &v
  return s
}

/**
 * 文件拷贝 response
 */
type HostingCopyFileResponse struct {
  // async_task_id
  AsyncTaskId *string `json:"async_task_id,omitempty" xml:"async_task_id,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z-]+"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  // drive_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[a-z0-9A-Z]+"`
}

func (s HostingCopyFileResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingCopyFileResponse) GoString() string {
  return s.String()
}

func (s *HostingCopyFileResponse) SetAsyncTaskId(v string) *HostingCopyFileResponse {
  s.AsyncTaskId = &v
  return s
}

func (s *HostingCopyFileResponse) SetDomainId(v string) *HostingCopyFileResponse {
  s.DomainId = &v
  return s
}

func (s *HostingCopyFileResponse) SetDriveId(v string) *HostingCopyFileResponse {
  s.DriveId = &v
  return s
}

func (s *HostingCopyFileResponse) SetFilePath(v string) *HostingCopyFileResponse {
  s.FilePath = &v
  return s
}

func (s *HostingCopyFileResponse) SetShareId(v string) *HostingCopyFileResponse {
  s.ShareId = &v
  return s
}

/**
 * create file request
 */
type HostingCreateFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // ContentMd5
  ContentMd5 *string `json:"content_md5,omitempty" xml:"content_md5,omitempty"`
  // ContentType
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // forbid_overwrite
  // type: boolean
  ForbidOverwrite *bool `json:"forbid_overwrite,omitempty" xml:"forbid_overwrite,omitempty"`
  // Name
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" maxLength:"1024" minLength:"1"`
  // parent_file_path
  ParentFilePath *string `json:"parent_file_path,omitempty" xml:"parent_file_path,omitempty" require:"true"`
  // part_info_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // Type
  Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
}

func (s HostingCreateFileRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingCreateFileRequest) GoString() string {
  return s.String()
}

func (s *HostingCreateFileRequest) SetAdditionData(v map[string]interface{}) *HostingCreateFileRequest {
  s.AdditionData = v
  return s
}

func (s *HostingCreateFileRequest) SetContentMd5(v string) *HostingCreateFileRequest {
  s.ContentMd5 = &v
  return s
}

func (s *HostingCreateFileRequest) SetContentType(v string) *HostingCreateFileRequest {
  s.ContentType = &v
  return s
}

func (s *HostingCreateFileRequest) SetDriveId(v string) *HostingCreateFileRequest {
  s.DriveId = &v
  return s
}

func (s *HostingCreateFileRequest) SetForbidOverwrite(v bool) *HostingCreateFileRequest {
  s.ForbidOverwrite = &v
  return s
}

func (s *HostingCreateFileRequest) SetName(v string) *HostingCreateFileRequest {
  s.Name = &v
  return s
}

func (s *HostingCreateFileRequest) SetParentFilePath(v string) *HostingCreateFileRequest {
  s.ParentFilePath = &v
  return s
}

func (s *HostingCreateFileRequest) SetPartInfoList(v []*UploadPartInfo) *HostingCreateFileRequest {
  s.PartInfoList = v
  return s
}

func (s *HostingCreateFileRequest) SetShareId(v string) *HostingCreateFileRequest {
  s.ShareId = &v
  return s
}

func (s *HostingCreateFileRequest) SetSize(v int64) *HostingCreateFileRequest {
  s.Size = &v
  return s
}

func (s *HostingCreateFileRequest) SetType(v string) *HostingCreateFileRequest {
  s.Type = &v
  return s
}

/**
 * Create file response
 */
type HostingCreateFileResponse struct {
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  // part_info_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9]+"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
}

func (s HostingCreateFileResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingCreateFileResponse) GoString() string {
  return s.String()
}

func (s *HostingCreateFileResponse) SetDomainId(v string) *HostingCreateFileResponse {
  s.DomainId = &v
  return s
}

func (s *HostingCreateFileResponse) SetDriveId(v string) *HostingCreateFileResponse {
  s.DriveId = &v
  return s
}

func (s *HostingCreateFileResponse) SetFilePath(v string) *HostingCreateFileResponse {
  s.FilePath = &v
  return s
}

func (s *HostingCreateFileResponse) SetPartInfoList(v []*UploadPartInfo) *HostingCreateFileResponse {
  s.PartInfoList = v
  return s
}

func (s *HostingCreateFileResponse) SetShareId(v string) *HostingCreateFileResponse {
  s.ShareId = &v
  return s
}

func (s *HostingCreateFileResponse) SetType(v string) *HostingCreateFileResponse {
  s.Type = &v
  return s
}

func (s *HostingCreateFileResponse) SetUploadId(v string) *HostingCreateFileResponse {
  s.UploadId = &v
  return s
}

/**
 * 删除文件请求
 */
type HostingDeleteFileRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true" maxLength:"1000" minLength:"1"`
  // permanently
  // type: false
  Permanently *bool `json:"permanently,omitempty" xml:"permanently,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
}

func (s HostingDeleteFileRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingDeleteFileRequest) GoString() string {
  return s.String()
}

func (s *HostingDeleteFileRequest) SetDriveId(v string) *HostingDeleteFileRequest {
  s.DriveId = &v
  return s
}

func (s *HostingDeleteFileRequest) SetFilePath(v string) *HostingDeleteFileRequest {
  s.FilePath = &v
  return s
}

func (s *HostingDeleteFileRequest) SetPermanently(v bool) *HostingDeleteFileRequest {
  s.Permanently = &v
  return s
}

func (s *HostingDeleteFileRequest) SetShareId(v string) *HostingDeleteFileRequest {
  s.ShareId = &v
  return s
}

/**
 * 删除文件 response
 */
type HostingDeleteFileResponse struct {
  // async_task_id
  AsyncTaskId *string `json:"async_task_id,omitempty" xml:"async_task_id,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[a-z0-9A-Z]+"`
}

func (s HostingDeleteFileResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingDeleteFileResponse) GoString() string {
  return s.String()
}

func (s *HostingDeleteFileResponse) SetAsyncTaskId(v string) *HostingDeleteFileResponse {
  s.AsyncTaskId = &v
  return s
}

func (s *HostingDeleteFileResponse) SetDomainId(v string) *HostingDeleteFileResponse {
  s.DomainId = &v
  return s
}

func (s *HostingDeleteFileResponse) SetDriveId(v string) *HostingDeleteFileResponse {
  s.DriveId = &v
  return s
}

func (s *HostingDeleteFileResponse) SetFilePath(v string) *HostingDeleteFileResponse {
  s.FilePath = &v
  return s
}

func (s *HostingDeleteFileResponse) SetShareId(v string) *HostingDeleteFileResponse {
  s.ShareId = &v
  return s
}

/**
 * 批量删除文件 response
 */
type HostingDeleteFilesResponse struct {
  // deleted_file_id_list
  DeletedFileIdList []*string `json:"deleted_file_id_list,omitempty" xml:"deleted_file_id_list,omitempty" type:"Repeated"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9]+"`
}

func (s HostingDeleteFilesResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingDeleteFilesResponse) GoString() string {
  return s.String()
}

func (s *HostingDeleteFilesResponse) SetDeletedFileIdList(v []*string) *HostingDeleteFilesResponse {
  s.DeletedFileIdList = v
  return s
}

func (s *HostingDeleteFilesResponse) SetDomainId(v string) *HostingDeleteFilesResponse {
  s.DomainId = &v
  return s
}

func (s *HostingDeleteFilesResponse) SetDriveId(v string) *HostingDeleteFilesResponse {
  s.DriveId = &v
  return s
}

func (s *HostingDeleteFilesResponse) SetShareId(v string) *HostingDeleteFilesResponse {
  s.ShareId = &v
  return s
}

/**
 * 获取文件下载地址的请求body
 */
type HostingGetDownloadUrlRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // expire_sec
  ExpireSec *int64 `json:"expire_sec,omitempty" xml:"expire_sec,omitempty" maximum:"115200" minimum:"10"`
  // file_name
  FileName *string `json:"file_name,omitempty" xml:"file_name,omitempty"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true" maxLength:"1000" minLength:"1"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
}

func (s HostingGetDownloadUrlRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingGetDownloadUrlRequest) GoString() string {
  return s.String()
}

func (s *HostingGetDownloadUrlRequest) SetAdditionData(v map[string]interface{}) *HostingGetDownloadUrlRequest {
  s.AdditionData = v
  return s
}

func (s *HostingGetDownloadUrlRequest) SetDriveId(v string) *HostingGetDownloadUrlRequest {
  s.DriveId = &v
  return s
}

func (s *HostingGetDownloadUrlRequest) SetExpireSec(v int64) *HostingGetDownloadUrlRequest {
  s.ExpireSec = &v
  return s
}

func (s *HostingGetDownloadUrlRequest) SetFileName(v string) *HostingGetDownloadUrlRequest {
  s.FileName = &v
  return s
}

func (s *HostingGetDownloadUrlRequest) SetFilePath(v string) *HostingGetDownloadUrlRequest {
  s.FilePath = &v
  return s
}

func (s *HostingGetDownloadUrlRequest) SetReferer(v string) *HostingGetDownloadUrlRequest {
  s.Referer = &v
  return s
}

func (s *HostingGetDownloadUrlRequest) SetShareId(v string) *HostingGetDownloadUrlRequest {
  s.ShareId = &v
  return s
}

func (s *HostingGetDownloadUrlRequest) SetSignToken(v string) *HostingGetDownloadUrlRequest {
  s.SignToken = &v
  return s
}

/**
 * 获取download url response
 */
type HostingGetDownloadUrlResponse struct {
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // method
  Method *string `json:"method,omitempty" xml:"method,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s HostingGetDownloadUrlResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingGetDownloadUrlResponse) GoString() string {
  return s.String()
}

func (s *HostingGetDownloadUrlResponse) SetExpiration(v string) *HostingGetDownloadUrlResponse {
  s.Expiration = &v
  return s
}

func (s *HostingGetDownloadUrlResponse) SetMethod(v string) *HostingGetDownloadUrlResponse {
  s.Method = &v
  return s
}

func (s *HostingGetDownloadUrlResponse) SetUrl(v string) *HostingGetDownloadUrlResponse {
  s.Url = &v
  return s
}

/**
 * 获取文件元数据
 */
type HostingGetFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true" maxLength:"1000" minLength:"1"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // url_expire_sec
  UrlExpireSec *int64 `json:"url_expire_sec,omitempty" xml:"url_expire_sec,omitempty" maximum:"14400" minimum:"10"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s HostingGetFileRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingGetFileRequest) GoString() string {
  return s.String()
}

func (s *HostingGetFileRequest) SetAdditionData(v map[string]interface{}) *HostingGetFileRequest {
  s.AdditionData = v
  return s
}

func (s *HostingGetFileRequest) SetDriveId(v string) *HostingGetFileRequest {
  s.DriveId = &v
  return s
}

func (s *HostingGetFileRequest) SetFilePath(v string) *HostingGetFileRequest {
  s.FilePath = &v
  return s
}

func (s *HostingGetFileRequest) SetImageThumbnailProcess(v string) *HostingGetFileRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *HostingGetFileRequest) SetImageUrlProcess(v string) *HostingGetFileRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *HostingGetFileRequest) SetOfficeThumbnailProcess(v string) *HostingGetFileRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *HostingGetFileRequest) SetReferer(v string) *HostingGetFileRequest {
  s.Referer = &v
  return s
}

func (s *HostingGetFileRequest) SetShareId(v string) *HostingGetFileRequest {
  s.ShareId = &v
  return s
}

func (s *HostingGetFileRequest) SetSignToken(v string) *HostingGetFileRequest {
  s.SignToken = &v
  return s
}

func (s *HostingGetFileRequest) SetUrlExpireSec(v int64) *HostingGetFileRequest {
  s.UrlExpireSec = &v
  return s
}

func (s *HostingGetFileRequest) SetVideoThumbnailProcess(v string) *HostingGetFileRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * 获取文件元数据response
 */
type HostingGetFileResponse struct {
  // Content Hash
  ContentHash *string `json:"content_hash,omitempty" xml:"content_hash,omitempty"`
  // content_hash_name
  ContentHashName *string `json:"content_hash_name,omitempty" xml:"content_hash_name,omitempty"`
  // content_type
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // crc64_hash
  Crc64Hash *string `json:"crc64_hash,omitempty" xml:"crc64_hash,omitempty"`
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // download_url
  DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_extension
  FileExtension *string `json:"file_extension,omitempty" xml:"file_extension,omitempty"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  // name
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
  // parent_file_id
  ParentFilePath *string `json:"parent_file_path,omitempty" xml:"parent_file_path,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9]+"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // trashed_at
  TrashedAt *string `json:"trashed_at,omitempty" xml:"trashed_at,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s HostingGetFileResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingGetFileResponse) GoString() string {
  return s.String()
}

func (s *HostingGetFileResponse) SetContentHash(v string) *HostingGetFileResponse {
  s.ContentHash = &v
  return s
}

func (s *HostingGetFileResponse) SetContentHashName(v string) *HostingGetFileResponse {
  s.ContentHashName = &v
  return s
}

func (s *HostingGetFileResponse) SetContentType(v string) *HostingGetFileResponse {
  s.ContentType = &v
  return s
}

func (s *HostingGetFileResponse) SetCrc64Hash(v string) *HostingGetFileResponse {
  s.Crc64Hash = &v
  return s
}

func (s *HostingGetFileResponse) SetCreatedAt(v string) *HostingGetFileResponse {
  s.CreatedAt = &v
  return s
}

func (s *HostingGetFileResponse) SetDescription(v string) *HostingGetFileResponse {
  s.Description = &v
  return s
}

func (s *HostingGetFileResponse) SetDomainId(v string) *HostingGetFileResponse {
  s.DomainId = &v
  return s
}

func (s *HostingGetFileResponse) SetDownloadUrl(v string) *HostingGetFileResponse {
  s.DownloadUrl = &v
  return s
}

func (s *HostingGetFileResponse) SetDriveId(v string) *HostingGetFileResponse {
  s.DriveId = &v
  return s
}

func (s *HostingGetFileResponse) SetFileExtension(v string) *HostingGetFileResponse {
  s.FileExtension = &v
  return s
}

func (s *HostingGetFileResponse) SetFilePath(v string) *HostingGetFileResponse {
  s.FilePath = &v
  return s
}

func (s *HostingGetFileResponse) SetName(v string) *HostingGetFileResponse {
  s.Name = &v
  return s
}

func (s *HostingGetFileResponse) SetParentFilePath(v string) *HostingGetFileResponse {
  s.ParentFilePath = &v
  return s
}

func (s *HostingGetFileResponse) SetShareId(v string) *HostingGetFileResponse {
  s.ShareId = &v
  return s
}

func (s *HostingGetFileResponse) SetSize(v int64) *HostingGetFileResponse {
  s.Size = &v
  return s
}

func (s *HostingGetFileResponse) SetStatus(v string) *HostingGetFileResponse {
  s.Status = &v
  return s
}

func (s *HostingGetFileResponse) SetThumbnail(v string) *HostingGetFileResponse {
  s.Thumbnail = &v
  return s
}

func (s *HostingGetFileResponse) SetTrashedAt(v string) *HostingGetFileResponse {
  s.TrashedAt = &v
  return s
}

func (s *HostingGetFileResponse) SetType(v string) *HostingGetFileResponse {
  s.Type = &v
  return s
}

func (s *HostingGetFileResponse) SetUpdatedAt(v string) *HostingGetFileResponse {
  s.UpdatedAt = &v
  return s
}

func (s *HostingGetFileResponse) SetUploadId(v string) *HostingGetFileResponse {
  s.UploadId = &v
  return s
}

func (s *HostingGetFileResponse) SetUrl(v string) *HostingGetFileResponse {
  s.Url = &v
  return s
}

/**
 * 获取文件安全地址的请求body
 */
type HostingGetSecureUrlRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // expire_sec 单位秒
  ExpireSec *int64 `json:"expire_sec,omitempty" xml:"expire_sec,omitempty"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true" maxLength:"1000" minLength:"1"`
  // secure_ip
  SecureIp *string `json:"secure_ip,omitempty" xml:"secure_ip,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
}

func (s HostingGetSecureUrlRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingGetSecureUrlRequest) GoString() string {
  return s.String()
}

func (s *HostingGetSecureUrlRequest) SetDriveId(v string) *HostingGetSecureUrlRequest {
  s.DriveId = &v
  return s
}

func (s *HostingGetSecureUrlRequest) SetExpireSec(v int64) *HostingGetSecureUrlRequest {
  s.ExpireSec = &v
  return s
}

func (s *HostingGetSecureUrlRequest) SetFilePath(v string) *HostingGetSecureUrlRequest {
  s.FilePath = &v
  return s
}

func (s *HostingGetSecureUrlRequest) SetSecureIp(v string) *HostingGetSecureUrlRequest {
  s.SecureIp = &v
  return s
}

func (s *HostingGetSecureUrlRequest) SetShareId(v string) *HostingGetSecureUrlRequest {
  s.ShareId = &v
  return s
}

/**
 * 获取secure url response
 */
type HostingGetSecureUrlResponse struct {
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s HostingGetSecureUrlResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingGetSecureUrlResponse) GoString() string {
  return s.String()
}

func (s *HostingGetSecureUrlResponse) SetExpiration(v string) *HostingGetSecureUrlResponse {
  s.Expiration = &v
  return s
}

func (s *HostingGetSecureUrlResponse) SetUrl(v string) *HostingGetSecureUrlResponse {
  s.Url = &v
  return s
}

/**
 * 获取文件上传URL
 */
type HostingGetUploadUrlRequest struct {
  // content_md5
  ContentMd5 *string `json:"content_md5,omitempty" xml:"content_md5,omitempty" maxLength:"32"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true"`
  // upload_part_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty" require:"true"`
}

func (s HostingGetUploadUrlRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingGetUploadUrlRequest) GoString() string {
  return s.String()
}

func (s *HostingGetUploadUrlRequest) SetContentMd5(v string) *HostingGetUploadUrlRequest {
  s.ContentMd5 = &v
  return s
}

func (s *HostingGetUploadUrlRequest) SetDriveId(v string) *HostingGetUploadUrlRequest {
  s.DriveId = &v
  return s
}

func (s *HostingGetUploadUrlRequest) SetFilePath(v string) *HostingGetUploadUrlRequest {
  s.FilePath = &v
  return s
}

func (s *HostingGetUploadUrlRequest) SetPartInfoList(v []*UploadPartInfo) *HostingGetUploadUrlRequest {
  s.PartInfoList = v
  return s
}

func (s *HostingGetUploadUrlRequest) SetShareId(v string) *HostingGetUploadUrlRequest {
  s.ShareId = &v
  return s
}

func (s *HostingGetUploadUrlRequest) SetUploadId(v string) *HostingGetUploadUrlRequest {
  s.UploadId = &v
  return s
}

/**
 * Get UploadUrl Response
 */
type HostingGetUploadUrlResponse struct {
  // created_at
  CreateAt *string `json:"create_at,omitempty" xml:"create_at,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  // part_info_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
}

func (s HostingGetUploadUrlResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingGetUploadUrlResponse) GoString() string {
  return s.String()
}

func (s *HostingGetUploadUrlResponse) SetCreateAt(v string) *HostingGetUploadUrlResponse {
  s.CreateAt = &v
  return s
}

func (s *HostingGetUploadUrlResponse) SetDomainId(v string) *HostingGetUploadUrlResponse {
  s.DomainId = &v
  return s
}

func (s *HostingGetUploadUrlResponse) SetDriveId(v string) *HostingGetUploadUrlResponse {
  s.DriveId = &v
  return s
}

func (s *HostingGetUploadUrlResponse) SetFilePath(v string) *HostingGetUploadUrlResponse {
  s.FilePath = &v
  return s
}

func (s *HostingGetUploadUrlResponse) SetPartInfoList(v []*UploadPartInfo) *HostingGetUploadUrlResponse {
  s.PartInfoList = v
  return s
}

func (s *HostingGetUploadUrlResponse) SetUploadId(v string) *HostingGetUploadUrlResponse {
  s.UploadId = &v
  return s
}

/**
 * list file request
 */
type HostingListFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  ImageCroppingAspectRatios []*string `json:"image_cropping_aspect_ratios,omitempty" xml:"image_cropping_aspect_ratios,omitempty" type:"Repeated"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // limit
  Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"0"`
  // marker
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  // ParentFilePath
  ParentFilePath *string `json:"parent_file_path,omitempty" xml:"parent_file_path,omitempty" require:"true"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // url_expire_sec
  UrlExpireSec *int64 `json:"url_expire_sec,omitempty" xml:"url_expire_sec,omitempty" maximum:"14400" minimum:"10"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s HostingListFileRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingListFileRequest) GoString() string {
  return s.String()
}

func (s *HostingListFileRequest) SetAdditionData(v map[string]interface{}) *HostingListFileRequest {
  s.AdditionData = v
  return s
}

func (s *HostingListFileRequest) SetDriveId(v string) *HostingListFileRequest {
  s.DriveId = &v
  return s
}

func (s *HostingListFileRequest) SetImageCroppingAspectRatios(v []*string) *HostingListFileRequest {
  s.ImageCroppingAspectRatios = v
  return s
}

func (s *HostingListFileRequest) SetImageThumbnailProcess(v string) *HostingListFileRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *HostingListFileRequest) SetImageUrlProcess(v string) *HostingListFileRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *HostingListFileRequest) SetLimit(v int64) *HostingListFileRequest {
  s.Limit = &v
  return s
}

func (s *HostingListFileRequest) SetMarker(v string) *HostingListFileRequest {
  s.Marker = &v
  return s
}

func (s *HostingListFileRequest) SetOfficeThumbnailProcess(v string) *HostingListFileRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *HostingListFileRequest) SetParentFilePath(v string) *HostingListFileRequest {
  s.ParentFilePath = &v
  return s
}

func (s *HostingListFileRequest) SetReferer(v string) *HostingListFileRequest {
  s.Referer = &v
  return s
}

func (s *HostingListFileRequest) SetShareId(v string) *HostingListFileRequest {
  s.ShareId = &v
  return s
}

func (s *HostingListFileRequest) SetSignToken(v string) *HostingListFileRequest {
  s.SignToken = &v
  return s
}

func (s *HostingListFileRequest) SetUrlExpireSec(v int64) *HostingListFileRequest {
  s.UrlExpireSec = &v
  return s
}

func (s *HostingListFileRequest) SetVideoThumbnailProcess(v string) *HostingListFileRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * List file response
 */
type HostingListFileResponse struct {
  // items
  Items []*BaseHostingFileResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
  // next_marker
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s HostingListFileResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingListFileResponse) GoString() string {
  return s.String()
}

func (s *HostingListFileResponse) SetItems(v []*BaseHostingFileResponse) *HostingListFileResponse {
  s.Items = v
  return s
}

func (s *HostingListFileResponse) SetNextMarker(v string) *HostingListFileResponse {
  s.NextMarker = &v
  return s
}

/**
 * 列举uploadID对应的已上传分片
 */
type HostingListUploadedPartRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true"`
  // limit
  Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"1000" minimum:"1"`
  // part_number_marker
  PartNumberMarker *int64 `json:"part_number_marker,omitempty" xml:"part_number_marker,omitempty" minimum:"1"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
}

func (s HostingListUploadedPartRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingListUploadedPartRequest) GoString() string {
  return s.String()
}

func (s *HostingListUploadedPartRequest) SetDriveId(v string) *HostingListUploadedPartRequest {
  s.DriveId = &v
  return s
}

func (s *HostingListUploadedPartRequest) SetFilePath(v string) *HostingListUploadedPartRequest {
  s.FilePath = &v
  return s
}

func (s *HostingListUploadedPartRequest) SetLimit(v int64) *HostingListUploadedPartRequest {
  s.Limit = &v
  return s
}

func (s *HostingListUploadedPartRequest) SetPartNumberMarker(v int64) *HostingListUploadedPartRequest {
  s.PartNumberMarker = &v
  return s
}

func (s *HostingListUploadedPartRequest) SetShareId(v string) *HostingListUploadedPartRequest {
  s.ShareId = &v
  return s
}

func (s *HostingListUploadedPartRequest) SetUploadId(v string) *HostingListUploadedPartRequest {
  s.UploadId = &v
  return s
}

/**
 * 获取签名 response
 */
type HostingListUploadedPartResponse struct {
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  // next_part_number_marker
  NextPartNumberMarker *string `json:"next_part_number_marker,omitempty" xml:"next_part_number_marker,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
  // uploaded_parts
  UploadedParts []*UploadPartInfo `json:"uploaded_parts,omitempty" xml:"uploaded_parts,omitempty" type:"Repeated"`
}

func (s HostingListUploadedPartResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingListUploadedPartResponse) GoString() string {
  return s.String()
}

func (s *HostingListUploadedPartResponse) SetFilePath(v string) *HostingListUploadedPartResponse {
  s.FilePath = &v
  return s
}

func (s *HostingListUploadedPartResponse) SetNextPartNumberMarker(v string) *HostingListUploadedPartResponse {
  s.NextPartNumberMarker = &v
  return s
}

func (s *HostingListUploadedPartResponse) SetUploadId(v string) *HostingListUploadedPartResponse {
  s.UploadId = &v
  return s
}

func (s *HostingListUploadedPartResponse) SetUploadedParts(v []*UploadPartInfo) *HostingListUploadedPartResponse {
  s.UploadedParts = v
  return s
}

/**
 * 文件移动请求
 */
type HostingMoveFileRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  // new_name
  NewName *string `json:"new_name,omitempty" xml:"new_name,omitempty"`
  // overwrite
  // type: boolean
  Overwrite *bool `json:"overwrite,omitempty" xml:"overwrite,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
  // file_path
  ToParentFilePath *string `json:"to_parent_file_path,omitempty" xml:"to_parent_file_path,omitempty"`
}

func (s HostingMoveFileRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingMoveFileRequest) GoString() string {
  return s.String()
}

func (s *HostingMoveFileRequest) SetDriveId(v string) *HostingMoveFileRequest {
  s.DriveId = &v
  return s
}

func (s *HostingMoveFileRequest) SetFilePath(v string) *HostingMoveFileRequest {
  s.FilePath = &v
  return s
}

func (s *HostingMoveFileRequest) SetNewName(v string) *HostingMoveFileRequest {
  s.NewName = &v
  return s
}

func (s *HostingMoveFileRequest) SetOverwrite(v bool) *HostingMoveFileRequest {
  s.Overwrite = &v
  return s
}

func (s *HostingMoveFileRequest) SetShareId(v string) *HostingMoveFileRequest {
  s.ShareId = &v
  return s
}

func (s *HostingMoveFileRequest) SetToParentFilePath(v string) *HostingMoveFileRequest {
  s.ToParentFilePath = &v
  return s
}

/**
 * 文件移动 response
 */
type HostingMoveFileResponse struct {
  // async_task_id
  AsyncTaskId *string `json:"async_task_id,omitempty" xml:"async_task_id,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z-]+"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  // drive_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[a-z0-9A-Z]+"`
}

func (s HostingMoveFileResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingMoveFileResponse) GoString() string {
  return s.String()
}

func (s *HostingMoveFileResponse) SetAsyncTaskId(v string) *HostingMoveFileResponse {
  s.AsyncTaskId = &v
  return s
}

func (s *HostingMoveFileResponse) SetDomainId(v string) *HostingMoveFileResponse {
  s.DomainId = &v
  return s
}

func (s *HostingMoveFileResponse) SetDriveId(v string) *HostingMoveFileResponse {
  s.DriveId = &v
  return s
}

func (s *HostingMoveFileResponse) SetFilePath(v string) *HostingMoveFileResponse {
  s.FilePath = &v
  return s
}

func (s *HostingMoveFileResponse) SetShareId(v string) *HostingMoveFileResponse {
  s.ShareId = &v
  return s
}

/**
 * search file response
 */
type HostingSearchFileResponse struct {
  // items
  Items []*BaseHostingFileResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
  // next_marker
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s HostingSearchFileResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingSearchFileResponse) GoString() string {
  return s.String()
}

func (s *HostingSearchFileResponse) SetItems(v []*BaseHostingFileResponse) *HostingSearchFileResponse {
  s.Items = v
  return s
}

func (s *HostingSearchFileResponse) SetNextMarker(v string) *HostingSearchFileResponse {
  s.NextMarker = &v
  return s
}

/**
 * 更新文件元数据 response
 */
type HostingUpdateFileMetaResponse struct {
  // Content Hash
  ContentHash *string `json:"content_hash,omitempty" xml:"content_hash,omitempty"`
  // content_hash_name
  ContentHashName *string `json:"content_hash_name,omitempty" xml:"content_hash_name,omitempty"`
  // content_type
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // crc64_hash
  Crc64Hash *string `json:"crc64_hash,omitempty" xml:"crc64_hash,omitempty"`
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // download_url
  DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_extension
  FileExtension *string `json:"file_extension,omitempty" xml:"file_extension,omitempty"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  // name
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
  // parent_file_id
  ParentFilePath *string `json:"parent_file_path,omitempty" xml:"parent_file_path,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9]+"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // trashed_at
  TrashedAt *string `json:"trashed_at,omitempty" xml:"trashed_at,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s HostingUpdateFileMetaResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingUpdateFileMetaResponse) GoString() string {
  return s.String()
}

func (s *HostingUpdateFileMetaResponse) SetContentHash(v string) *HostingUpdateFileMetaResponse {
  s.ContentHash = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetContentHashName(v string) *HostingUpdateFileMetaResponse {
  s.ContentHashName = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetContentType(v string) *HostingUpdateFileMetaResponse {
  s.ContentType = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetCrc64Hash(v string) *HostingUpdateFileMetaResponse {
  s.Crc64Hash = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetCreatedAt(v string) *HostingUpdateFileMetaResponse {
  s.CreatedAt = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetDescription(v string) *HostingUpdateFileMetaResponse {
  s.Description = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetDomainId(v string) *HostingUpdateFileMetaResponse {
  s.DomainId = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetDownloadUrl(v string) *HostingUpdateFileMetaResponse {
  s.DownloadUrl = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetDriveId(v string) *HostingUpdateFileMetaResponse {
  s.DriveId = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetFileExtension(v string) *HostingUpdateFileMetaResponse {
  s.FileExtension = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetFilePath(v string) *HostingUpdateFileMetaResponse {
  s.FilePath = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetName(v string) *HostingUpdateFileMetaResponse {
  s.Name = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetParentFilePath(v string) *HostingUpdateFileMetaResponse {
  s.ParentFilePath = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetShareId(v string) *HostingUpdateFileMetaResponse {
  s.ShareId = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetSize(v int64) *HostingUpdateFileMetaResponse {
  s.Size = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetStatus(v string) *HostingUpdateFileMetaResponse {
  s.Status = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetThumbnail(v string) *HostingUpdateFileMetaResponse {
  s.Thumbnail = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetTrashedAt(v string) *HostingUpdateFileMetaResponse {
  s.TrashedAt = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetType(v string) *HostingUpdateFileMetaResponse {
  s.Type = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetUpdatedAt(v string) *HostingUpdateFileMetaResponse {
  s.UpdatedAt = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetUploadId(v string) *HostingUpdateFileMetaResponse {
  s.UploadId = &v
  return s
}

func (s *HostingUpdateFileMetaResponse) SetUrl(v string) *HostingUpdateFileMetaResponse {
  s.Url = &v
  return s
}

/**
 * 获取视频DRM License
 */
type HostingVideoDRMLicenseRequest struct {
  // drmType
  DrmType *string `json:"drmType,omitempty" xml:"drmType,omitempty" require:"true"`
  // licenseRequest
  LicenseRequest *string `json:"licenseRequest,omitempty" xml:"licenseRequest,omitempty" require:"true"`
}

func (s HostingVideoDRMLicenseRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingVideoDRMLicenseRequest) GoString() string {
  return s.String()
}

func (s *HostingVideoDRMLicenseRequest) SetDrmType(v string) *HostingVideoDRMLicenseRequest {
  s.DrmType = &v
  return s
}

func (s *HostingVideoDRMLicenseRequest) SetLicenseRequest(v string) *HostingVideoDRMLicenseRequest {
  s.LicenseRequest = &v
  return s
}

/**
 * DRM License response
 */
type HostingVideoDRMLicenseResponse struct {
  // drm_data
  Data *string `json:"data,omitempty" xml:"data,omitempty" require:"true"`
  // device_info
  DeviceInfo *string `json:"device_info,omitempty" xml:"device_info,omitempty" require:"true"`
  // states
  States *int64 `json:"states,omitempty" xml:"states,omitempty" require:"true"`
}

func (s HostingVideoDRMLicenseResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingVideoDRMLicenseResponse) GoString() string {
  return s.String()
}

func (s *HostingVideoDRMLicenseResponse) SetData(v string) *HostingVideoDRMLicenseResponse {
  s.Data = &v
  return s
}

func (s *HostingVideoDRMLicenseResponse) SetDeviceInfo(v string) *HostingVideoDRMLicenseResponse {
  s.DeviceInfo = &v
  return s
}

func (s *HostingVideoDRMLicenseResponse) SetStates(v int64) *HostingVideoDRMLicenseResponse {
  s.States = &v
  return s
}

/**
 * 获取视频分辨率列表
 */
type HostingVideoDefinitionRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true" maxLength:"1000" minLength:"1"`
  // protection_scheme
  ProtectionScheme *string `json:"protection_scheme,omitempty" xml:"protection_scheme,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
}

func (s HostingVideoDefinitionRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingVideoDefinitionRequest) GoString() string {
  return s.String()
}

func (s *HostingVideoDefinitionRequest) SetDriveId(v string) *HostingVideoDefinitionRequest {
  s.DriveId = &v
  return s
}

func (s *HostingVideoDefinitionRequest) SetFilePath(v string) *HostingVideoDefinitionRequest {
  s.FilePath = &v
  return s
}

func (s *HostingVideoDefinitionRequest) SetProtectionScheme(v string) *HostingVideoDefinitionRequest {
  s.ProtectionScheme = &v
  return s
}

func (s *HostingVideoDefinitionRequest) SetShareId(v string) *HostingVideoDefinitionRequest {
  s.ShareId = &v
  return s
}

/**
 * 转码接口response
 */
type HostingVideoDefinitionResponse struct {
  // definition_list
  DefinitionList []*string `json:"definition_list,omitempty" xml:"definition_list,omitempty" type:"Repeated"`
  // frame_rate
  FrameRate *string `json:"frame_rate,omitempty" xml:"frame_rate,omitempty"`
}

func (s HostingVideoDefinitionResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingVideoDefinitionResponse) GoString() string {
  return s.String()
}

func (s *HostingVideoDefinitionResponse) SetDefinitionList(v []*string) *HostingVideoDefinitionResponse {
  s.DefinitionList = v
  return s
}

func (s *HostingVideoDefinitionResponse) SetFrameRate(v string) *HostingVideoDefinitionResponse {
  s.FrameRate = &v
  return s
}

/**
 * 获取视频的m3u8文件
 */
type HostingVideoM3U8Request struct {
  // definition
  Definition *string `json:"definition,omitempty" xml:"definition,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // expire_sec
  ExpireSec *int64 `json:"expire_sec,omitempty" xml:"expire_sec,omitempty" maximum:"86400" minimum:"60"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true" maxLength:"1000" minLength:"1"`
  // protection_scheme
  ProtectionScheme *string `json:"protection_scheme,omitempty" xml:"protection_scheme,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
  // sign_token
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty" require:"true"`
}

func (s HostingVideoM3U8Request) String() string {
  return tea.Prettify(s)
}

func (s HostingVideoM3U8Request) GoString() string {
  return s.String()
}

func (s *HostingVideoM3U8Request) SetDefinition(v string) *HostingVideoM3U8Request {
  s.Definition = &v
  return s
}

func (s *HostingVideoM3U8Request) SetDriveId(v string) *HostingVideoM3U8Request {
  s.DriveId = &v
  return s
}

func (s *HostingVideoM3U8Request) SetExpireSec(v int64) *HostingVideoM3U8Request {
  s.ExpireSec = &v
  return s
}

func (s *HostingVideoM3U8Request) SetFilePath(v string) *HostingVideoM3U8Request {
  s.FilePath = &v
  return s
}

func (s *HostingVideoM3U8Request) SetProtectionScheme(v string) *HostingVideoM3U8Request {
  s.ProtectionScheme = &v
  return s
}

func (s *HostingVideoM3U8Request) SetShareId(v string) *HostingVideoM3U8Request {
  s.ShareId = &v
  return s
}

func (s *HostingVideoM3U8Request) SetSignToken(v string) *HostingVideoM3U8Request {
  s.SignToken = &v
  return s
}

/**
 * 启动视频转码请求
 */
type HostingVideoTranscodeRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_path
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true" maxLength:"1000" minLength:"1"`
  // hls_time
  HlsTime *int64 `json:"hls_time,omitempty" xml:"hls_time,omitempty"`
  // protection_scheme
  ProtectionScheme *string `json:"protection_scheme,omitempty" xml:"protection_scheme,omitempty"`
  // remarks
  Remarks *string `json:"remarks,omitempty" xml:"remarks,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
  // transcode
  Transcode *bool `json:"transcode,omitempty" xml:"transcode,omitempty"`
}

func (s HostingVideoTranscodeRequest) String() string {
  return tea.Prettify(s)
}

func (s HostingVideoTranscodeRequest) GoString() string {
  return s.String()
}

func (s *HostingVideoTranscodeRequest) SetDriveId(v string) *HostingVideoTranscodeRequest {
  s.DriveId = &v
  return s
}

func (s *HostingVideoTranscodeRequest) SetFilePath(v string) *HostingVideoTranscodeRequest {
  s.FilePath = &v
  return s
}

func (s *HostingVideoTranscodeRequest) SetHlsTime(v int64) *HostingVideoTranscodeRequest {
  s.HlsTime = &v
  return s
}

func (s *HostingVideoTranscodeRequest) SetProtectionScheme(v string) *HostingVideoTranscodeRequest {
  s.ProtectionScheme = &v
  return s
}

func (s *HostingVideoTranscodeRequest) SetRemarks(v string) *HostingVideoTranscodeRequest {
  s.Remarks = &v
  return s
}

func (s *HostingVideoTranscodeRequest) SetShareId(v string) *HostingVideoTranscodeRequest {
  s.ShareId = &v
  return s
}

func (s *HostingVideoTranscodeRequest) SetTranscode(v bool) *HostingVideoTranscodeRequest {
  s.Transcode = &v
  return s
}

/**
 * 转码接口response
 */
type HostingVideoTranscodeResponse struct {
  // definition_list
  DefinitionList []*string `json:"definition_list,omitempty" xml:"definition_list,omitempty" type:"Repeated"`
  // duration
  Duration *int64 `json:"duration,omitempty" xml:"duration,omitempty"`
  // hls_time
  HlsTime *int64 `json:"hls_time,omitempty" xml:"hls_time,omitempty"`
}

func (s HostingVideoTranscodeResponse) String() string {
  return tea.Prettify(s)
}

func (s HostingVideoTranscodeResponse) GoString() string {
  return s.String()
}

func (s *HostingVideoTranscodeResponse) SetDefinitionList(v []*string) *HostingVideoTranscodeResponse {
  s.DefinitionList = v
  return s
}

func (s *HostingVideoTranscodeResponse) SetDuration(v int64) *HostingVideoTranscodeResponse {
  s.Duration = &v
  return s
}

func (s *HostingVideoTranscodeResponse) SetHlsTime(v int64) *HostingVideoTranscodeResponse {
  s.HlsTime = &v
  return s
}

/**
 * 
 */
type IMMProject struct {
  CanaryPercent *int64 `json:"canary_percent,omitempty" xml:"canary_percent,omitempty"`
  CanaryProjectName *string `json:"canary_project_name,omitempty" xml:"canary_project_name,omitempty"`
  NotifyEndpoint *string `json:"notify_endpoint,omitempty" xml:"notify_endpoint,omitempty"`
  NotifyTopicName *string `json:"notify_topic_name,omitempty" xml:"notify_topic_name,omitempty"`
  ProjectName *string `json:"project_name,omitempty" xml:"project_name,omitempty"`
  Region *string `json:"region,omitempty" xml:"region,omitempty"`
  // 访问Project的角色ARN
  RoleArn *string `json:"role_arn,omitempty" xml:"role_arn,omitempty"`
}

func (s IMMProject) String() string {
  return tea.Prettify(s)
}

func (s IMMProject) GoString() string {
  return s.String()
}

func (s *IMMProject) SetCanaryPercent(v int64) *IMMProject {
  s.CanaryPercent = &v
  return s
}

func (s *IMMProject) SetCanaryProjectName(v string) *IMMProject {
  s.CanaryProjectName = &v
  return s
}

func (s *IMMProject) SetNotifyEndpoint(v string) *IMMProject {
  s.NotifyEndpoint = &v
  return s
}

func (s *IMMProject) SetNotifyTopicName(v string) *IMMProject {
  s.NotifyTopicName = &v
  return s
}

func (s *IMMProject) SetProjectName(v string) *IMMProject {
  s.ProjectName = &v
  return s
}

func (s *IMMProject) SetRegion(v string) *IMMProject {
  s.Region = &v
  return s
}

func (s *IMMProject) SetRoleArn(v string) *IMMProject {
  s.RoleArn = &v
  return s
}

/**
 * Identity benefit package response
 */
type IdentityBenefitPkgResponse struct {
  // 权益包中的权益列表
  BenefitList []*BenefitBaseResponse `json:"benefit_list,omitempty" xml:"benefit_list,omitempty" type:"Repeated"`
  // 权益包的唯一标识
  BenefitPkgId *string `json:"benefit_pkg_id,omitempty" xml:"benefit_pkg_id,omitempty"`
  // 权益包的下发信息
  DeliveryInfoList []*BenefitPkgDeliveryInfoResponse `json:"delivery_info_list,omitempty" xml:"delivery_info_list,omitempty" type:"Repeated"`
  // 权益包的名称
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
}

func (s IdentityBenefitPkgResponse) String() string {
  return tea.Prettify(s)
}

func (s IdentityBenefitPkgResponse) GoString() string {
  return s.String()
}

func (s *IdentityBenefitPkgResponse) SetBenefitList(v []*BenefitBaseResponse) *IdentityBenefitPkgResponse {
  s.BenefitList = v
  return s
}

func (s *IdentityBenefitPkgResponse) SetBenefitPkgId(v string) *IdentityBenefitPkgResponse {
  s.BenefitPkgId = &v
  return s
}

func (s *IdentityBenefitPkgResponse) SetDeliveryInfoList(v []*BenefitPkgDeliveryInfoResponse) *IdentityBenefitPkgResponse {
  s.DeliveryInfoList = v
  return s
}

func (s *IdentityBenefitPkgResponse) SetName(v string) *IdentityBenefitPkgResponse {
  s.Name = &v
  return s
}

/**
 * 
 */
type ImageMediaMetadata struct {
  // height
  Height *int64 `json:"height,omitempty" xml:"height,omitempty"`
  // width：
  Width *int64 `json:"width,omitempty" xml:"width,omitempty"`
}

func (s ImageMediaMetadata) String() string {
  return tea.Prettify(s)
}

func (s ImageMediaMetadata) GoString() string {
  return s.String()
}

func (s *ImageMediaMetadata) SetHeight(v int64) *ImageMediaMetadata {
  s.Height = &v
  return s
}

func (s *ImageMediaMetadata) SetWidth(v int64) *ImageMediaMetadata {
  s.Width = &v
  return s
}

/**
 * 
 */
type ImageMediaResponse struct {
  // address_line
  AddressLine *string `json:"address_line,omitempty" xml:"address_line,omitempty"`
  // city
  City *string `json:"city,omitempty" xml:"city,omitempty"`
  // country
  Country *string `json:"country,omitempty" xml:"country,omitempty"`
  // cropping_suggestion
  CroppingSuggestion []*CroppingSuggestionItem `json:"cropping_suggestion,omitempty" xml:"cropping_suggestion,omitempty" type:"Repeated"`
  // district
  District *string `json:"district,omitempty" xml:"district,omitempty"`
  // exif json string
  Exif *string `json:"exif,omitempty" xml:"exif,omitempty"`
  // faces json string
  Faces *string `json:"faces,omitempty" xml:"faces,omitempty"`
  // faces_thumbnail_list
  FacesThumbnail []*FaceThumbnail `json:"faces_thumbnail,omitempty" xml:"faces_thumbnail,omitempty" type:"Repeated"`
  // height
  Height *int64 `json:"height,omitempty" xml:"height,omitempty"`
  ImageQuality *ImageQuality `json:"image_quality,omitempty" xml:"image_quality,omitempty"`
  // system_tags
  ImageTags []*SystemTag `json:"image_tags,omitempty" xml:"image_tags,omitempty" type:"Repeated"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // province
  Province *string `json:"province,omitempty" xml:"province,omitempty"`
  // time
  Time *string `json:"time,omitempty" xml:"time,omitempty"`
  // township
  Township *string `json:"township,omitempty" xml:"township,omitempty"`
  // width
  Width *int64 `json:"width,omitempty" xml:"width,omitempty"`
}

func (s ImageMediaResponse) String() string {
  return tea.Prettify(s)
}

func (s ImageMediaResponse) GoString() string {
  return s.String()
}

func (s *ImageMediaResponse) SetAddressLine(v string) *ImageMediaResponse {
  s.AddressLine = &v
  return s
}

func (s *ImageMediaResponse) SetCity(v string) *ImageMediaResponse {
  s.City = &v
  return s
}

func (s *ImageMediaResponse) SetCountry(v string) *ImageMediaResponse {
  s.Country = &v
  return s
}

func (s *ImageMediaResponse) SetCroppingSuggestion(v []*CroppingSuggestionItem) *ImageMediaResponse {
  s.CroppingSuggestion = v
  return s
}

func (s *ImageMediaResponse) SetDistrict(v string) *ImageMediaResponse {
  s.District = &v
  return s
}

func (s *ImageMediaResponse) SetExif(v string) *ImageMediaResponse {
  s.Exif = &v
  return s
}

func (s *ImageMediaResponse) SetFaces(v string) *ImageMediaResponse {
  s.Faces = &v
  return s
}

func (s *ImageMediaResponse) SetFacesThumbnail(v []*FaceThumbnail) *ImageMediaResponse {
  s.FacesThumbnail = v
  return s
}

func (s *ImageMediaResponse) SetHeight(v int64) *ImageMediaResponse {
  s.Height = &v
  return s
}

func (s *ImageMediaResponse) SetImageQuality(v *ImageQuality) *ImageMediaResponse {
  s.ImageQuality = v
  return s
}

func (s *ImageMediaResponse) SetImageTags(v []*SystemTag) *ImageMediaResponse {
  s.ImageTags = v
  return s
}

func (s *ImageMediaResponse) SetLocation(v string) *ImageMediaResponse {
  s.Location = &v
  return s
}

func (s *ImageMediaResponse) SetProvince(v string) *ImageMediaResponse {
  s.Province = &v
  return s
}

func (s *ImageMediaResponse) SetTime(v string) *ImageMediaResponse {
  s.Time = &v
  return s
}

func (s *ImageMediaResponse) SetTownship(v string) *ImageMediaResponse {
  s.Township = &v
  return s
}

func (s *ImageMediaResponse) SetWidth(v int64) *ImageMediaResponse {
  s.Width = &v
  return s
}

/**
 * 
 */
type ImageQuality struct {
  Clarity *float64 `json:"clarity,omitempty" xml:"clarity,omitempty"`
  ClarityScore *float64 `json:"clarity_score,omitempty" xml:"clarity_score,omitempty"`
  Color *float64 `json:"color,omitempty" xml:"color,omitempty"`
  ColorScore *float64 `json:"color_score,omitempty" xml:"color_score,omitempty"`
  CompositionScore *float64 `json:"composition_score,omitempty" xml:"composition_score,omitempty"`
  Contrast *float64 `json:"contrast,omitempty" xml:"contrast,omitempty"`
  ContrastScore *float64 `json:"contrast_score,omitempty" xml:"contrast_score,omitempty"`
  Exposure *float64 `json:"exposure,omitempty" xml:"exposure,omitempty"`
  ExposureScore *float64 `json:"exposure_score,omitempty" xml:"exposure_score,omitempty"`
  OverallScore *float64 `json:"overall_score,omitempty" xml:"overall_score,omitempty"`
}

func (s ImageQuality) String() string {
  return tea.Prettify(s)
}

func (s ImageQuality) GoString() string {
  return s.String()
}

func (s *ImageQuality) SetClarity(v float64) *ImageQuality {
  s.Clarity = &v
  return s
}

func (s *ImageQuality) SetClarityScore(v float64) *ImageQuality {
  s.ClarityScore = &v
  return s
}

func (s *ImageQuality) SetColor(v float64) *ImageQuality {
  s.Color = &v
  return s
}

func (s *ImageQuality) SetColorScore(v float64) *ImageQuality {
  s.ColorScore = &v
  return s
}

func (s *ImageQuality) SetCompositionScore(v float64) *ImageQuality {
  s.CompositionScore = &v
  return s
}

func (s *ImageQuality) SetContrast(v float64) *ImageQuality {
  s.Contrast = &v
  return s
}

func (s *ImageQuality) SetContrastScore(v float64) *ImageQuality {
  s.ContrastScore = &v
  return s
}

func (s *ImageQuality) SetExposure(v float64) *ImageQuality {
  s.Exposure = &v
  return s
}

func (s *ImageQuality) SetExposureScore(v float64) *ImageQuality {
  s.ExposureScore = &v
  return s
}

func (s *ImageQuality) SetOverallScore(v float64) *ImageQuality {
  s.OverallScore = &v
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
type LinkInfo struct {
  // 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
  Extra *string `json:"extra,omitempty" xml:"extra,omitempty"`
  // 当前用户已存在的登录标识
  Identity *string `json:"identity,omitempty" xml:"identity,omitempty"`
  // 当前用户已存在的登录方式
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
}

func (s LinkInfo) String() string {
  return tea.Prettify(s)
}

func (s LinkInfo) GoString() string {
  return s.String()
}

func (s *LinkInfo) SetExtra(v string) *LinkInfo {
  s.Extra = &v
  return s
}

func (s *LinkInfo) SetIdentity(v string) *LinkInfo {
  s.Identity = &v
  return s
}

func (s *LinkInfo) SetType(v string) *LinkInfo {
  s.Type = &v
  return s
}

/**
 * 
 */
type LinkInfoListResponse struct {
  // items
  Items []*LinkInfoResponse `json:"items,omitempty" xml:"items,omitempty" require:"true" type:"Repeated"`
}

func (s LinkInfoListResponse) String() string {
  return tea.Prettify(s)
}

func (s LinkInfoListResponse) GoString() string {
  return s.String()
}

func (s *LinkInfoListResponse) SetItems(v []*LinkInfoResponse) *LinkInfoListResponse {
  s.Items = v
  return s
}

/**
 * 
 */
type LinkInfoResponse struct {
  // 认证类型
  AuthenticationType *string `json:"authentication_type,omitempty" xml:"authentication_type,omitempty" require:"true"`
  // 创建时间
  CreatedAt *int64 `json:"created_at,omitempty" xml:"created_at,omitempty" require:"true"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
  Extra *string `json:"extra,omitempty" xml:"extra,omitempty"`
  // 唯一身份标识
  Identity *string `json:"identity,omitempty" xml:"identity,omitempty" require:"true"`
  // 最后登录时间
  LastLoginTime *int64 `json:"last_login_time,omitempty" xml:"last_login_time,omitempty" require:"true"`
  // 状态
  Status *string `json:"status,omitempty" xml:"status,omitempty" require:"true"`
  // 用户ID
  UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty" require:"true"`
}

func (s LinkInfoResponse) String() string {
  return tea.Prettify(s)
}

func (s LinkInfoResponse) GoString() string {
  return s.String()
}

func (s *LinkInfoResponse) SetAuthenticationType(v string) *LinkInfoResponse {
  s.AuthenticationType = &v
  return s
}

func (s *LinkInfoResponse) SetCreatedAt(v int64) *LinkInfoResponse {
  s.CreatedAt = &v
  return s
}

func (s *LinkInfoResponse) SetDomainId(v string) *LinkInfoResponse {
  s.DomainId = &v
  return s
}

func (s *LinkInfoResponse) SetExtra(v string) *LinkInfoResponse {
  s.Extra = &v
  return s
}

func (s *LinkInfoResponse) SetIdentity(v string) *LinkInfoResponse {
  s.Identity = &v
  return s
}

func (s *LinkInfoResponse) SetLastLoginTime(v int64) *LinkInfoResponse {
  s.LastLoginTime = &v
  return s
}

func (s *LinkInfoResponse) SetStatus(v string) *LinkInfoResponse {
  s.Status = &v
  return s
}

func (s *LinkInfoResponse) SetUserId(v string) *LinkInfoResponse {
  s.UserId = &v
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
 * list_file_by_anonymous request
 */
type ListByAnonymousRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // limit
  Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
  // marker
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  // parent_file_id
  ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" require:"true" maxLength:"50" minLength:"4" pattern:"[a-z0-9]{1,50}"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" require:"true"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s ListByAnonymousRequest) String() string {
  return tea.Prettify(s)
}

func (s ListByAnonymousRequest) GoString() string {
  return s.String()
}

func (s *ListByAnonymousRequest) SetAdditionData(v map[string]interface{}) *ListByAnonymousRequest {
  s.AdditionData = v
  return s
}

func (s *ListByAnonymousRequest) SetImageThumbnailProcess(v string) *ListByAnonymousRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *ListByAnonymousRequest) SetImageUrlProcess(v string) *ListByAnonymousRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *ListByAnonymousRequest) SetLimit(v int64) *ListByAnonymousRequest {
  s.Limit = &v
  return s
}

func (s *ListByAnonymousRequest) SetMarker(v string) *ListByAnonymousRequest {
  s.Marker = &v
  return s
}

func (s *ListByAnonymousRequest) SetOfficeThumbnailProcess(v string) *ListByAnonymousRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *ListByAnonymousRequest) SetParentFileId(v string) *ListByAnonymousRequest {
  s.ParentFileId = &v
  return s
}

func (s *ListByAnonymousRequest) SetReferer(v string) *ListByAnonymousRequest {
  s.Referer = &v
  return s
}

func (s *ListByAnonymousRequest) SetShareId(v string) *ListByAnonymousRequest {
  s.ShareId = &v
  return s
}

func (s *ListByAnonymousRequest) SetSignToken(v string) *ListByAnonymousRequest {
  s.SignToken = &v
  return s
}

func (s *ListByAnonymousRequest) SetVideoThumbnailProcess(v string) *ListByAnonymousRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * list_file_by_anonymous response
 */
type ListByAnonymousResponse struct {
  // items
  Items []*BaseFileAnonymousResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
  // next_marker
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ListByAnonymousResponse) String() string {
  return tea.Prettify(s)
}

func (s ListByAnonymousResponse) GoString() string {
  return s.String()
}

func (s *ListByAnonymousResponse) SetItems(v []*BaseFileAnonymousResponse) *ListByAnonymousResponse {
  s.Items = v
  return s
}

func (s *ListByAnonymousResponse) SetNextMarker(v string) *ListByAnonymousResponse {
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
 * List drive request
 */
type ListDriveRequest struct {
  // 每页大小限制
  Limit *int32 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
  // 翻页标记, 接口返回的标记值
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // 所属者
  Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
  // owner_type
  // 所述者类型
  OwnerType *string `json:"owner_type,omitempty" xml:"owner_type,omitempty"`
  // Subdomain ID
  SubdomainId *string `json:"subdomain_id,omitempty" xml:"subdomain_id,omitempty"`
}

func (s ListDriveRequest) String() string {
  return tea.Prettify(s)
}

func (s ListDriveRequest) GoString() string {
  return s.String()
}

func (s *ListDriveRequest) SetLimit(v int32) *ListDriveRequest {
  s.Limit = &v
  return s
}

func (s *ListDriveRequest) SetMarker(v string) *ListDriveRequest {
  s.Marker = &v
  return s
}

func (s *ListDriveRequest) SetOwner(v string) *ListDriveRequest {
  s.Owner = &v
  return s
}

func (s *ListDriveRequest) SetOwnerType(v string) *ListDriveRequest {
  s.OwnerType = &v
  return s
}

func (s *ListDriveRequest) SetSubdomainId(v string) *ListDriveRequest {
  s.SubdomainId = &v
  return s
}

/**
 * list drive response
 */
type ListDriveResponse struct {
  // Drive 列表
  Items []*BaseDriveResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
  // 翻页标记
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ListDriveResponse) String() string {
  return tea.Prettify(s)
}

func (s ListDriveResponse) GoString() string {
  return s.String()
}

func (s *ListDriveResponse) SetItems(v []*BaseDriveResponse) *ListDriveResponse {
  s.Items = v
  return s
}

func (s *ListDriveResponse) SetNextMarker(v string) *ListDriveResponse {
  s.NextMarker = &v
  return s
}

/**
 * 
 */
type ListFileActivityRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // DriveID
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty"`
  // FileID
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty"`
  // Limit, default
  Limit *int32 `json:"limit,omitempty" xml:"limit,omitempty"`
  // Marker
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
}

func (s ListFileActivityRequest) String() string {
  return tea.Prettify(s)
}

func (s ListFileActivityRequest) GoString() string {
  return s.String()
}

func (s *ListFileActivityRequest) SetAdditionData(v map[string]interface{}) *ListFileActivityRequest {
  s.AdditionData = v
  return s
}

func (s *ListFileActivityRequest) SetDriveId(v string) *ListFileActivityRequest {
  s.DriveId = &v
  return s
}

func (s *ListFileActivityRequest) SetFileId(v string) *ListFileActivityRequest {
  s.FileId = &v
  return s
}

func (s *ListFileActivityRequest) SetLimit(v int32) *ListFileActivityRequest {
  s.Limit = &v
  return s
}

func (s *ListFileActivityRequest) SetMarker(v string) *ListFileActivityRequest {
  s.Marker = &v
  return s
}

/**
 * list file activity response
 */
type ListFileActivityResponse struct {
  // Activities
  Activities []*FileActivity `json:"activities,omitempty" xml:"activities,omitempty" type:"Repeated"`
  // NextMarker
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ListFileActivityResponse) String() string {
  return tea.Prettify(s)
}

func (s ListFileActivityResponse) GoString() string {
  return s.String()
}

func (s *ListFileActivityResponse) SetActivities(v []*FileActivity) *ListFileActivityResponse {
  s.Activities = v
  return s
}

func (s *ListFileActivityResponse) SetNextMarker(v string) *ListFileActivityResponse {
  s.NextMarker = &v
  return s
}

/**
 * 列举文件
 */
type ListFileByCustomIndexKeyRequest struct {
  // starred
  Starred *bool `json:"Starred,omitempty" xml:"Starred,omitempty"`
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // category
  Category *string `json:"category,omitempty" xml:"category,omitempty"`
  // custom_index_key
  CustomIndexKey *string `json:"custom_index_key,omitempty" xml:"custom_index_key,omitempty" require:"true"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // encrypt_mode
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // fields
  Fields *string `json:"fields,omitempty" xml:"fields,omitempty"`
  ImageCroppingAspectRatios []*string `json:"image_cropping_aspect_ratios,omitempty" xml:"image_cropping_aspect_ratios,omitempty" type:"Repeated"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // limit
  Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"0"`
  // marker
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  // order_direction
  OrderDirection *string `json:"order_direction,omitempty" xml:"order_direction,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id, either share_id or drive_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // url_expire_sec
  UrlExpireSec *int64 `json:"url_expire_sec,omitempty" xml:"url_expire_sec,omitempty" maximum:"14400" minimum:"10"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s ListFileByCustomIndexKeyRequest) String() string {
  return tea.Prettify(s)
}

func (s ListFileByCustomIndexKeyRequest) GoString() string {
  return s.String()
}

func (s *ListFileByCustomIndexKeyRequest) SetStarred(v bool) *ListFileByCustomIndexKeyRequest {
  s.Starred = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetAdditionData(v map[string]interface{}) *ListFileByCustomIndexKeyRequest {
  s.AdditionData = v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetCategory(v string) *ListFileByCustomIndexKeyRequest {
  s.Category = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetCustomIndexKey(v string) *ListFileByCustomIndexKeyRequest {
  s.CustomIndexKey = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetDriveId(v string) *ListFileByCustomIndexKeyRequest {
  s.DriveId = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetEncryptMode(v string) *ListFileByCustomIndexKeyRequest {
  s.EncryptMode = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetFields(v string) *ListFileByCustomIndexKeyRequest {
  s.Fields = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetImageCroppingAspectRatios(v []*string) *ListFileByCustomIndexKeyRequest {
  s.ImageCroppingAspectRatios = v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetImageThumbnailProcess(v string) *ListFileByCustomIndexKeyRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetImageUrlProcess(v string) *ListFileByCustomIndexKeyRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetLimit(v int64) *ListFileByCustomIndexKeyRequest {
  s.Limit = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetMarker(v string) *ListFileByCustomIndexKeyRequest {
  s.Marker = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetOfficeThumbnailProcess(v string) *ListFileByCustomIndexKeyRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetOrderDirection(v string) *ListFileByCustomIndexKeyRequest {
  s.OrderDirection = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetReferer(v string) *ListFileByCustomIndexKeyRequest {
  s.Referer = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetShareId(v string) *ListFileByCustomIndexKeyRequest {
  s.ShareId = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetSignToken(v string) *ListFileByCustomIndexKeyRequest {
  s.SignToken = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetStatus(v string) *ListFileByCustomIndexKeyRequest {
  s.Status = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetType(v string) *ListFileByCustomIndexKeyRequest {
  s.Type = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetUrlExpireSec(v int64) *ListFileByCustomIndexKeyRequest {
  s.UrlExpireSec = &v
  return s
}

func (s *ListFileByCustomIndexKeyRequest) SetVideoThumbnailProcess(v string) *ListFileByCustomIndexKeyRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * 获取增量文件操作记录
 */
type ListFileDeltaRequest struct {
  // cursor 游标
  Cursor *string `json:"cursor,omitempty" xml:"cursor,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
  ImageCroppingAspectRatios []*string `json:"image_cropping_aspect_ratios,omitempty" xml:"image_cropping_aspect_ratios,omitempty" type:"Repeated"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // limit
  // default 100
  Limit *int32 `json:"limit,omitempty" xml:"limit,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s ListFileDeltaRequest) String() string {
  return tea.Prettify(s)
}

func (s ListFileDeltaRequest) GoString() string {
  return s.String()
}

func (s *ListFileDeltaRequest) SetCursor(v string) *ListFileDeltaRequest {
  s.Cursor = &v
  return s
}

func (s *ListFileDeltaRequest) SetDriveId(v string) *ListFileDeltaRequest {
  s.DriveId = &v
  return s
}

func (s *ListFileDeltaRequest) SetImageCroppingAspectRatios(v []*string) *ListFileDeltaRequest {
  s.ImageCroppingAspectRatios = v
  return s
}

func (s *ListFileDeltaRequest) SetImageThumbnailProcess(v string) *ListFileDeltaRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *ListFileDeltaRequest) SetImageUrlProcess(v string) *ListFileDeltaRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *ListFileDeltaRequest) SetLimit(v int32) *ListFileDeltaRequest {
  s.Limit = &v
  return s
}

func (s *ListFileDeltaRequest) SetOfficeThumbnailProcess(v string) *ListFileDeltaRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *ListFileDeltaRequest) SetVideoThumbnailProcess(v string) *ListFileDeltaRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * list file op response
 */
type ListFileDeltaResponse struct {
  // cursor
  Cursor *string `json:"cursor,omitempty" xml:"cursor,omitempty"`
  // has_more
  HasMore *bool `json:"has_more,omitempty" xml:"has_more,omitempty"`
  // items
  Items []*FileDeltaResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
}

func (s ListFileDeltaResponse) String() string {
  return tea.Prettify(s)
}

func (s ListFileDeltaResponse) GoString() string {
  return s.String()
}

func (s *ListFileDeltaResponse) SetCursor(v string) *ListFileDeltaResponse {
  s.Cursor = &v
  return s
}

func (s *ListFileDeltaResponse) SetHasMore(v bool) *ListFileDeltaResponse {
  s.HasMore = &v
  return s
}

func (s *ListFileDeltaResponse) SetItems(v []*FileDeltaResponse) *ListFileDeltaResponse {
  s.Items = v
  return s
}

/**
 * 列举文件
 */
type ListFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // all
  All *bool `json:"all,omitempty" xml:"all,omitempty"`
  // category
  Category *string `json:"category,omitempty" xml:"category,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // fields
  Fields *string `json:"fields,omitempty" xml:"fields,omitempty"`
  ImageCroppingAspectRatios []*string `json:"image_cropping_aspect_ratios,omitempty" xml:"image_cropping_aspect_ratios,omitempty" type:"Repeated"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // limit
  Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"0"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // marker
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  // order_by
  OrderBy *string `json:"order_by,omitempty" xml:"order_by,omitempty"`
  // order_direction
  OrderDirection *string `json:"order_direction,omitempty" xml:"order_direction,omitempty"`
  // ParentFileID
  ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" require:"true" maxLength:"50" minLength:"4" pattern:"[a-z0-9.-_]{1,50}"`
  ParentFileIdPath *string `json:"parent_file_id_path,omitempty" xml:"parent_file_id_path,omitempty"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // share_id, either share_id or drive_id is required
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // starred
  Starred *bool `json:"starred,omitempty" xml:"starred,omitempty"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // url_expire_sec
  UrlExpireSec *int64 `json:"url_expire_sec,omitempty" xml:"url_expire_sec,omitempty" maximum:"14400" minimum:"10"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s ListFileRequest) String() string {
  return tea.Prettify(s)
}

func (s ListFileRequest) GoString() string {
  return s.String()
}

func (s *ListFileRequest) SetAdditionData(v map[string]interface{}) *ListFileRequest {
  s.AdditionData = v
  return s
}

func (s *ListFileRequest) SetAll(v bool) *ListFileRequest {
  s.All = &v
  return s
}

func (s *ListFileRequest) SetCategory(v string) *ListFileRequest {
  s.Category = &v
  return s
}

func (s *ListFileRequest) SetDriveId(v string) *ListFileRequest {
  s.DriveId = &v
  return s
}

func (s *ListFileRequest) SetFields(v string) *ListFileRequest {
  s.Fields = &v
  return s
}

func (s *ListFileRequest) SetImageCroppingAspectRatios(v []*string) *ListFileRequest {
  s.ImageCroppingAspectRatios = v
  return s
}

func (s *ListFileRequest) SetImageThumbnailProcess(v string) *ListFileRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *ListFileRequest) SetImageUrlProcess(v string) *ListFileRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *ListFileRequest) SetLimit(v int64) *ListFileRequest {
  s.Limit = &v
  return s
}

func (s *ListFileRequest) SetLocation(v string) *ListFileRequest {
  s.Location = &v
  return s
}

func (s *ListFileRequest) SetMarker(v string) *ListFileRequest {
  s.Marker = &v
  return s
}

func (s *ListFileRequest) SetOfficeThumbnailProcess(v string) *ListFileRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *ListFileRequest) SetOrderBy(v string) *ListFileRequest {
  s.OrderBy = &v
  return s
}

func (s *ListFileRequest) SetOrderDirection(v string) *ListFileRequest {
  s.OrderDirection = &v
  return s
}

func (s *ListFileRequest) SetParentFileId(v string) *ListFileRequest {
  s.ParentFileId = &v
  return s
}

func (s *ListFileRequest) SetParentFileIdPath(v string) *ListFileRequest {
  s.ParentFileIdPath = &v
  return s
}

func (s *ListFileRequest) SetReferer(v string) *ListFileRequest {
  s.Referer = &v
  return s
}

func (s *ListFileRequest) SetShareId(v string) *ListFileRequest {
  s.ShareId = &v
  return s
}

func (s *ListFileRequest) SetSignToken(v string) *ListFileRequest {
  s.SignToken = &v
  return s
}

func (s *ListFileRequest) SetStarred(v bool) *ListFileRequest {
  s.Starred = &v
  return s
}

func (s *ListFileRequest) SetStatus(v string) *ListFileRequest {
  s.Status = &v
  return s
}

func (s *ListFileRequest) SetType(v string) *ListFileRequest {
  s.Type = &v
  return s
}

func (s *ListFileRequest) SetUrlExpireSec(v int64) *ListFileRequest {
  s.UrlExpireSec = &v
  return s
}

func (s *ListFileRequest) SetVideoThumbnailProcess(v string) *ListFileRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * List file response
 */
type ListFileResponse struct {
  // items
  Items []*BaseCCPFileResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
  // next_marker
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ListFileResponse) String() string {
  return tea.Prettify(s)
}

func (s ListFileResponse) GoString() string {
  return s.String()
}

func (s *ListFileResponse) SetItems(v []*BaseCCPFileResponse) *ListFileResponse {
  s.Items = v
  return s
}

func (s *ListFileResponse) SetNextMarker(v string) *ListFileResponse {
  s.NextMarker = &v
  return s
}

/**
 * List identity benefit package request
 */
type ListIdentityBenefitPkgRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // 查询特定的benefit ID，include_benefit为true时有效。 如果为空，不做任何过滤；如果不为空，只返回包含特定benefit ID的权益包；也只返回权益包中特定的权益信息。
  BenefitIdList []*string `json:"benefit_id_list,omitempty" xml:"benefit_id_list,omitempty" type:"Repeated"`
  // domain ID AK方式访问，参数identity_type为user时，该项必传
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // 实体类型，目前只支持查询user类型实体绑定的权益包
  IdentityType *string `json:"identity_type,omitempty" xml:"identity_type,omitempty" require:"true"`
  // 是否返回权益包中的权益，默认为false
  IncludeBenefit *bool `json:"include_benefit,omitempty" xml:"include_benefit,omitempty"`
  // 是否返回已经超期的权益包，默认为false
  IncludeExpired *bool `json:"include_expired,omitempty" xml:"include_expired,omitempty"`
  // 用户 ID, AK方式访问，参数identity_type为user时，该项必传
  UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty"`
}

func (s ListIdentityBenefitPkgRequest) String() string {
  return tea.Prettify(s)
}

func (s ListIdentityBenefitPkgRequest) GoString() string {
  return s.String()
}

func (s *ListIdentityBenefitPkgRequest) SetHeaders(v map[string]*string) *ListIdentityBenefitPkgRequest {
  s.Headers = v
  return s
}

func (s *ListIdentityBenefitPkgRequest) SetBenefitIdList(v []*string) *ListIdentityBenefitPkgRequest {
  s.BenefitIdList = v
  return s
}

func (s *ListIdentityBenefitPkgRequest) SetDomainId(v string) *ListIdentityBenefitPkgRequest {
  s.DomainId = &v
  return s
}

func (s *ListIdentityBenefitPkgRequest) SetIdentityType(v string) *ListIdentityBenefitPkgRequest {
  s.IdentityType = &v
  return s
}

func (s *ListIdentityBenefitPkgRequest) SetIncludeBenefit(v bool) *ListIdentityBenefitPkgRequest {
  s.IncludeBenefit = &v
  return s
}

func (s *ListIdentityBenefitPkgRequest) SetIncludeExpired(v bool) *ListIdentityBenefitPkgRequest {
  s.IncludeExpired = &v
  return s
}

func (s *ListIdentityBenefitPkgRequest) SetUserId(v string) *ListIdentityBenefitPkgRequest {
  s.UserId = &v
  return s
}

/**
 * List identity benefit package response
 */
type ListIdentityBenefitPkgResponse struct {
  Items []*IdentityBenefitPkgResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
}

func (s ListIdentityBenefitPkgResponse) String() string {
  return tea.Prettify(s)
}

func (s ListIdentityBenefitPkgResponse) GoString() string {
  return s.String()
}

func (s *ListIdentityBenefitPkgResponse) SetItems(v []*IdentityBenefitPkgResponse) *ListIdentityBenefitPkgResponse {
  s.Items = v
  return s
}

/**
 * List my drive request
 */
type ListMyDriveRequest struct {
  // 每页大小限制
  Limit *int32 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
  // 翻页标记, 接口返回的标记值
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
}

func (s ListMyDriveRequest) String() string {
  return tea.Prettify(s)
}

func (s ListMyDriveRequest) GoString() string {
  return s.String()
}

func (s *ListMyDriveRequest) SetLimit(v int32) *ListMyDriveRequest {
  s.Limit = &v
  return s
}

func (s *ListMyDriveRequest) SetMarker(v string) *ListMyDriveRequest {
  s.Marker = &v
  return s
}

/**
 * list_share_link request
 */
type ListShareLinkRequest struct {
  // creator
  Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
  // include_cancelled
  IncludeCancelled *bool `json:"include_cancelled,omitempty" xml:"include_cancelled,omitempty"`
  // limit
  Limit *int32 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
  // marker
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // order_by
  OrderBy *string `json:"order_by,omitempty" xml:"order_by,omitempty"`
  // order_direction
  OrderDirection *string `json:"order_direction,omitempty" xml:"order_direction,omitempty"`
}

func (s ListShareLinkRequest) String() string {
  return tea.Prettify(s)
}

func (s ListShareLinkRequest) GoString() string {
  return s.String()
}

func (s *ListShareLinkRequest) SetCreator(v string) *ListShareLinkRequest {
  s.Creator = &v
  return s
}

func (s *ListShareLinkRequest) SetIncludeCancelled(v bool) *ListShareLinkRequest {
  s.IncludeCancelled = &v
  return s
}

func (s *ListShareLinkRequest) SetLimit(v int32) *ListShareLinkRequest {
  s.Limit = &v
  return s
}

func (s *ListShareLinkRequest) SetMarker(v string) *ListShareLinkRequest {
  s.Marker = &v
  return s
}

func (s *ListShareLinkRequest) SetOrderBy(v string) *ListShareLinkRequest {
  s.OrderBy = &v
  return s
}

func (s *ListShareLinkRequest) SetOrderDirection(v string) *ListShareLinkRequest {
  s.OrderDirection = &v
  return s
}

/**
 * list_share_link response
 */
type ListShareLinkResponse struct {
  // items
  Items []*BaseShareLinkResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
  // next_marker
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ListShareLinkResponse) String() string {
  return tea.Prettify(s)
}

func (s ListShareLinkResponse) GoString() string {
  return s.String()
}

func (s *ListShareLinkResponse) SetItems(v []*BaseShareLinkResponse) *ListShareLinkResponse {
  s.Items = v
  return s
}

func (s *ListShareLinkResponse) SetNextMarker(v string) *ListShareLinkResponse {
  s.NextMarker = &v
  return s
}

/**
 * list share request
 */
type ListShareRequest struct {
  // creator
  Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // limit
  Limit *int32 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
  // marker
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // Owner
  Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
  // owner_type
  OwnerType *string `json:"owner_type,omitempty" xml:"owner_type,omitempty"`
  // share_file_path
  ShareFilePath *string `json:"share_file_path,omitempty" xml:"share_file_path,omitempty"`
}

func (s ListShareRequest) String() string {
  return tea.Prettify(s)
}

func (s ListShareRequest) GoString() string {
  return s.String()
}

func (s *ListShareRequest) SetCreator(v string) *ListShareRequest {
  s.Creator = &v
  return s
}

func (s *ListShareRequest) SetDriveId(v string) *ListShareRequest {
  s.DriveId = &v
  return s
}

func (s *ListShareRequest) SetLimit(v int32) *ListShareRequest {
  s.Limit = &v
  return s
}

func (s *ListShareRequest) SetMarker(v string) *ListShareRequest {
  s.Marker = &v
  return s
}

func (s *ListShareRequest) SetOwner(v string) *ListShareRequest {
  s.Owner = &v
  return s
}

func (s *ListShareRequest) SetOwnerType(v string) *ListShareRequest {
  s.OwnerType = &v
  return s
}

func (s *ListShareRequest) SetShareFilePath(v string) *ListShareRequest {
  s.ShareFilePath = &v
  return s
}

/**
 * List share response
 */
type ListShareResponse struct {
  // items
  Items []*BaseShareResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
  // next_marker
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ListShareResponse) String() string {
  return tea.Prettify(s)
}

func (s ListShareResponse) GoString() string {
  return s.String()
}

func (s *ListShareResponse) SetItems(v []*BaseShareResponse) *ListShareResponse {
  s.Items = v
  return s
}

func (s *ListShareResponse) SetNextMarker(v string) *ListShareResponse {
  s.NextMarker = &v
  return s
}

/**
 * list store file
 */
type ListStoreFileRequest struct {
  // limit
  Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"1000" minimum:"1"`
  // marker
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // parent_file_path
  ParentFilePath *string `json:"parent_file_path,omitempty" xml:"parent_file_path,omitempty"`
  // store_id
  StoreId *string `json:"store_id,omitempty" xml:"store_id,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
}

func (s ListStoreFileRequest) String() string {
  return tea.Prettify(s)
}

func (s ListStoreFileRequest) GoString() string {
  return s.String()
}

func (s *ListStoreFileRequest) SetLimit(v int64) *ListStoreFileRequest {
  s.Limit = &v
  return s
}

func (s *ListStoreFileRequest) SetMarker(v string) *ListStoreFileRequest {
  s.Marker = &v
  return s
}

func (s *ListStoreFileRequest) SetParentFilePath(v string) *ListStoreFileRequest {
  s.ParentFilePath = &v
  return s
}

func (s *ListStoreFileRequest) SetStoreId(v string) *ListStoreFileRequest {
  s.StoreId = &v
  return s
}

func (s *ListStoreFileRequest) SetType(v string) *ListStoreFileRequest {
  s.Type = &v
  return s
}

/**
 * List storage file
 */
type ListStoreFileResponse struct {
  // items
  // file list
  Items []*StoreFile `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ListStoreFileResponse) String() string {
  return tea.Prettify(s)
}

func (s ListStoreFileResponse) GoString() string {
  return s.String()
}

func (s *ListStoreFileResponse) SetItems(v []*StoreFile) *ListStoreFileResponse {
  s.Items = v
  return s
}

func (s *ListStoreFileResponse) SetNextMarker(v string) *ListStoreFileResponse {
  s.NextMarker = &v
  return s
}

/**
 * list storage file
 */
type ListStoreRequest struct {
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
}

func (s ListStoreRequest) String() string {
  return tea.Prettify(s)
}

func (s ListStoreRequest) GoString() string {
  return s.String()
}

func (s *ListStoreRequest) SetDomainId(v string) *ListStoreRequest {
  s.DomainId = &v
  return s
}

/**
 * List storage
 */
type ListStoreResponse struct {
  // items
  Items []*StoreItemResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
}

func (s ListStoreResponse) String() string {
  return tea.Prettify(s)
}

func (s ListStoreResponse) GoString() string {
  return s.String()
}

func (s *ListStoreResponse) SetItems(v []*StoreItemResponse) *ListStoreResponse {
  s.Items = v
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
 * 列举uploadID对应的已上传分片
 */
type ListUploadedPartRequest struct {
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  FileIdPath *string `json:"file_id_path,omitempty" xml:"file_id_path,omitempty"`
  // limit
  Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"1000" minimum:"1"`
  // part_number_marker
  PartNumberMarker *int64 `json:"part_number_marker,omitempty" xml:"part_number_marker,omitempty" minimum:"1"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
}

func (s ListUploadedPartRequest) String() string {
  return tea.Prettify(s)
}

func (s ListUploadedPartRequest) GoString() string {
  return s.String()
}

func (s *ListUploadedPartRequest) SetDriveId(v string) *ListUploadedPartRequest {
  s.DriveId = &v
  return s
}

func (s *ListUploadedPartRequest) SetFileId(v string) *ListUploadedPartRequest {
  s.FileId = &v
  return s
}

func (s *ListUploadedPartRequest) SetFileIdPath(v string) *ListUploadedPartRequest {
  s.FileIdPath = &v
  return s
}

func (s *ListUploadedPartRequest) SetLimit(v int64) *ListUploadedPartRequest {
  s.Limit = &v
  return s
}

func (s *ListUploadedPartRequest) SetPartNumberMarker(v int64) *ListUploadedPartRequest {
  s.PartNumberMarker = &v
  return s
}

func (s *ListUploadedPartRequest) SetShareId(v string) *ListUploadedPartRequest {
  s.ShareId = &v
  return s
}

func (s *ListUploadedPartRequest) SetUploadId(v string) *ListUploadedPartRequest {
  s.UploadId = &v
  return s
}

/**
 * 获取签名 response
 */
type ListUploadedPartResponse struct {
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // next_part_number_marker
  NextPartNumberMarker *string `json:"next_part_number_marker,omitempty" xml:"next_part_number_marker,omitempty"`
  ParallelUpload *bool `json:"parallel_upload,omitempty" xml:"parallel_upload,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
  // uploaded_parts
  UploadedParts []*UploadPartInfo `json:"uploaded_parts,omitempty" xml:"uploaded_parts,omitempty" type:"Repeated"`
}

func (s ListUploadedPartResponse) String() string {
  return tea.Prettify(s)
}

func (s ListUploadedPartResponse) GoString() string {
  return s.String()
}

func (s *ListUploadedPartResponse) SetFileId(v string) *ListUploadedPartResponse {
  s.FileId = &v
  return s
}

func (s *ListUploadedPartResponse) SetNextPartNumberMarker(v string) *ListUploadedPartResponse {
  s.NextPartNumberMarker = &v
  return s
}

func (s *ListUploadedPartResponse) SetParallelUpload(v bool) *ListUploadedPartResponse {
  s.ParallelUpload = &v
  return s
}

func (s *ListUploadedPartResponse) SetUploadId(v string) *ListUploadedPartResponse {
  s.UploadId = &v
  return s
}

func (s *ListUploadedPartResponse) SetUploadedParts(v []*UploadPartInfo) *ListUploadedPartResponse {
  s.UploadedParts = v
  return s
}

/**
 * 实时转码信息task响应
 */
type LiveTranscodingTaskResponse struct {
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // template_id
  TemplateId *string `json:"template_id,omitempty" xml:"template_id,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s LiveTranscodingTaskResponse) String() string {
  return tea.Prettify(s)
}

func (s LiveTranscodingTaskResponse) GoString() string {
  return s.String()
}

func (s *LiveTranscodingTaskResponse) SetStatus(v string) *LiveTranscodingTaskResponse {
  s.Status = &v
  return s
}

func (s *LiveTranscodingTaskResponse) SetTemplateId(v string) *LiveTranscodingTaskResponse {
  s.TemplateId = &v
  return s
}

func (s *LiveTranscodingTaskResponse) SetUrl(v string) *LiveTranscodingTaskResponse {
  s.Url = &v
  return s
}

/**
 * 
 */
type MediaPlayInfoTemplate struct {
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // template_id
  TemplateId *string `json:"template_id,omitempty" xml:"template_id,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s MediaPlayInfoTemplate) String() string {
  return tea.Prettify(s)
}

func (s MediaPlayInfoTemplate) GoString() string {
  return s.String()
}

func (s *MediaPlayInfoTemplate) SetStatus(v string) *MediaPlayInfoTemplate {
  s.Status = &v
  return s
}

func (s *MediaPlayInfoTemplate) SetTemplateId(v string) *MediaPlayInfoTemplate {
  s.TemplateId = &v
  return s
}

func (s *MediaPlayInfoTemplate) SetUrl(v string) *MediaPlayInfoTemplate {
  s.Url = &v
  return s
}

/**
 * 
 */
type MobileCheckExistResponse struct {
  // 当前手机号是否存在
  IsExist *bool `json:"is_exist,omitempty" xml:"is_exist,omitempty" require:"true"`
  // 待查询的手机号
  PhoneNumber *string `json:"phone_number,omitempty" xml:"phone_number,omitempty" require:"true"`
  // 国家编号，默认86，不需要填+号，直接填数字
  PhoneRegion *string `json:"phone_region,omitempty" xml:"phone_region,omitempty"`
}

func (s MobileCheckExistResponse) String() string {
  return tea.Prettify(s)
}

func (s MobileCheckExistResponse) GoString() string {
  return s.String()
}

func (s *MobileCheckExistResponse) SetIsExist(v bool) *MobileCheckExistResponse {
  s.IsExist = &v
  return s
}

func (s *MobileCheckExistResponse) SetPhoneNumber(v string) *MobileCheckExistResponse {
  s.PhoneNumber = &v
  return s
}

func (s *MobileCheckExistResponse) SetPhoneRegion(v string) *MobileCheckExistResponse {
  s.PhoneRegion = &v
  return s
}

/**
 * 
 */
type MobileSendSmsCodeResponse struct {
  // 短信验证码ID
  SmsCodeId *string `json:"sms_code_id,omitempty" xml:"sms_code_id,omitempty" require:"true"`
}

func (s MobileSendSmsCodeResponse) String() string {
  return tea.Prettify(s)
}

func (s MobileSendSmsCodeResponse) GoString() string {
  return s.String()
}

func (s *MobileSendSmsCodeResponse) SetSmsCodeId(v string) *MobileSendSmsCodeResponse {
  s.SmsCodeId = &v
  return s
}

/**
 * 
 */
type MoveDetail struct {
  // SrcParentFileID
  SrcParentFileId *string `json:"src_parent_file_id,omitempty" xml:"src_parent_file_id,omitempty"`
  // TgtParentFileID
  TgtParentFileId *string `json:"tgt_parent_file_id,omitempty" xml:"tgt_parent_file_id,omitempty"`
}

func (s MoveDetail) String() string {
  return tea.Prettify(s)
}

func (s MoveDetail) GoString() string {
  return s.String()
}

func (s *MoveDetail) SetSrcParentFileId(v string) *MoveDetail {
  s.SrcParentFileId = &v
  return s
}

func (s *MoveDetail) SetTgtParentFileId(v string) *MoveDetail {
  s.TgtParentFileId = &v
  return s
}

/**
 * 文件移动请求
 */
type MoveFileRequest struct {
  // auto_rename
  AutoRename *bool `json:"auto_rename,omitempty" xml:"auto_rename,omitempty"`
  CategoryList []*string `json:"category_list,omitempty" xml:"category_list,omitempty" type:"Repeated"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  FileIdPath *string `json:"file_id_path,omitempty" xml:"file_id_path,omitempty"`
  // new_name
  NewName *string `json:"new_name,omitempty" xml:"new_name,omitempty" maxLength:"1024" minLength:"1"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // to_drive_id
  ToDriveId *string `json:"to_drive_id,omitempty" xml:"to_drive_id,omitempty" pattern:"[0-9]+"`
  // to_parent_file_id
  ToParentFileId *string `json:"to_parent_file_id,omitempty" xml:"to_parent_file_id,omitempty" require:"true" maxLength:"50" minLength:"4"`
  ToShareId *string `json:"to_share_id,omitempty" xml:"to_share_id,omitempty" pattern:"[0-9]+"`
}

func (s MoveFileRequest) String() string {
  return tea.Prettify(s)
}

func (s MoveFileRequest) GoString() string {
  return s.String()
}

func (s *MoveFileRequest) SetAutoRename(v bool) *MoveFileRequest {
  s.AutoRename = &v
  return s
}

func (s *MoveFileRequest) SetCategoryList(v []*string) *MoveFileRequest {
  s.CategoryList = v
  return s
}

func (s *MoveFileRequest) SetDriveId(v string) *MoveFileRequest {
  s.DriveId = &v
  return s
}

func (s *MoveFileRequest) SetFileId(v string) *MoveFileRequest {
  s.FileId = &v
  return s
}

func (s *MoveFileRequest) SetFileIdPath(v string) *MoveFileRequest {
  s.FileIdPath = &v
  return s
}

func (s *MoveFileRequest) SetNewName(v string) *MoveFileRequest {
  s.NewName = &v
  return s
}

func (s *MoveFileRequest) SetShareId(v string) *MoveFileRequest {
  s.ShareId = &v
  return s
}

func (s *MoveFileRequest) SetToDriveId(v string) *MoveFileRequest {
  s.ToDriveId = &v
  return s
}

func (s *MoveFileRequest) SetToParentFileId(v string) *MoveFileRequest {
  s.ToParentFileId = &v
  return s
}

func (s *MoveFileRequest) SetToShareId(v string) *MoveFileRequest {
  s.ToShareId = &v
  return s
}

/**
 * 文件移动 response
 */
type MoveFileResponse struct {
  // async_task_id
  AsyncTaskId *string `json:"async_task_id,omitempty" xml:"async_task_id,omitempty"`
  // DomainID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
}

func (s MoveFileResponse) String() string {
  return tea.Prettify(s)
}

func (s MoveFileResponse) GoString() string {
  return s.String()
}

func (s *MoveFileResponse) SetAsyncTaskId(v string) *MoveFileResponse {
  s.AsyncTaskId = &v
  return s
}

func (s *MoveFileResponse) SetDomainId(v string) *MoveFileResponse {
  s.DomainId = &v
  return s
}

func (s *MoveFileResponse) SetDriveId(v string) *MoveFileResponse {
  s.DriveId = &v
  return s
}

func (s *MoveFileResponse) SetFileId(v string) *MoveFileResponse {
  s.FileId = &v
  return s
}

/**
 * OfficePreviewConfig 文档预览配置
 */
type OfficePreviewConfig struct {
  Enabled *bool `json:"enabled,omitempty" xml:"enabled,omitempty"`
}

func (s OfficePreviewConfig) String() string {
  return tea.Prettify(s)
}

func (s OfficePreviewConfig) GoString() string {
  return s.String()
}

func (s *OfficePreviewConfig) SetEnabled(v bool) *OfficePreviewConfig {
  s.Enabled = &v
  return s
}

/**
 * play_media request
 */
type PlayMediaRequest struct {
  // auth_key
  AuthKey *string `json:"AuthKey,omitempty" xml:"AuthKey,omitempty" require:"true" pattern:"[a-z0-9]+"`
  // drive_id
  DriveID *string `json:"DriveID,omitempty" xml:"DriveID,omitempty" require:"true" pattern:"[0-9]+"`
  // file_id
  FileID *string `json:"FileID,omitempty" xml:"FileID,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
}

func (s PlayMediaRequest) String() string {
  return tea.Prettify(s)
}

func (s PlayMediaRequest) GoString() string {
  return s.String()
}

func (s *PlayMediaRequest) SetAuthKey(v string) *PlayMediaRequest {
  s.AuthKey = &v
  return s
}

func (s *PlayMediaRequest) SetDriveID(v string) *PlayMediaRequest {
  s.DriveID = &v
  return s
}

func (s *PlayMediaRequest) SetFileID(v string) *PlayMediaRequest {
  s.FileID = &v
  return s
}

/**
 * Pre hash check Response
 */
type PreHashCheckSuccessResponse struct {
  // code
  Code *string `json:"code,omitempty" xml:"code,omitempty"`
  // file_name
  FileName *string `json:"file_name,omitempty" xml:"file_name,omitempty"`
  // message
  Message *string `json:"message,omitempty" xml:"message,omitempty"`
  // parent_file_id
  ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // pre_hash
  PreHash *string `json:"pre_hash,omitempty" xml:"pre_hash,omitempty"`
}

func (s PreHashCheckSuccessResponse) String() string {
  return tea.Prettify(s)
}

func (s PreHashCheckSuccessResponse) GoString() string {
  return s.String()
}

func (s *PreHashCheckSuccessResponse) SetCode(v string) *PreHashCheckSuccessResponse {
  s.Code = &v
  return s
}

func (s *PreHashCheckSuccessResponse) SetFileName(v string) *PreHashCheckSuccessResponse {
  s.FileName = &v
  return s
}

func (s *PreHashCheckSuccessResponse) SetMessage(v string) *PreHashCheckSuccessResponse {
  s.Message = &v
  return s
}

func (s *PreHashCheckSuccessResponse) SetParentFileId(v string) *PreHashCheckSuccessResponse {
  s.ParentFileId = &v
  return s
}

func (s *PreHashCheckSuccessResponse) SetPreHash(v string) *PreHashCheckSuccessResponse {
  s.PreHash = &v
  return s
}

/**
 * 
 */
type RPVerifyTokenResponse struct {
  // 是否需要实人认证，如果用户已通过认证，或者未开启实人认证，返回false
  NeedRpVerify *bool `json:"need_rp_verify,omitempty" xml:"need_rp_verify,omitempty" require:"true"`
  VerifyToken *VerifyTokenResponse `json:"verify_token,omitempty" xml:"verify_token,omitempty" require:"true"`
}

func (s RPVerifyTokenResponse) String() string {
  return tea.Prettify(s)
}

func (s RPVerifyTokenResponse) GoString() string {
  return s.String()
}

func (s *RPVerifyTokenResponse) SetNeedRpVerify(v bool) *RPVerifyTokenResponse {
  s.NeedRpVerify = &v
  return s
}

func (s *RPVerifyTokenResponse) SetVerifyToken(v *VerifyTokenResponse) *RPVerifyTokenResponse {
  s.VerifyToken = v
  return s
}

/**
 * 下载限速配置
 */
type RateLimit struct {
  PartSize *int64 `json:"part_size,omitempty" xml:"part_size,omitempty"`
  PartSpeed *int64 `json:"part_speed,omitempty" xml:"part_speed,omitempty"`
}

func (s RateLimit) String() string {
  return tea.Prettify(s)
}

func (s RateLimit) GoString() string {
  return s.String()
}

func (s *RateLimit) SetPartSize(v int64) *RateLimit {
  s.PartSize = &v
  return s
}

func (s *RateLimit) SetPartSpeed(v int64) *RateLimit {
  s.PartSpeed = &v
  return s
}

/**
 * 刷新office文档在线编辑凭证
 */
type RefreshOfficeEditTokenRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // AccessToken
  OfficeAccessToken *string `json:"office_access_token,omitempty" xml:"office_access_token,omitempty" require:"true"`
  // RefreshToken
  OfficeRefreshToken *string `json:"office_refresh_token,omitempty" xml:"office_refresh_token,omitempty" require:"true"`
}

func (s RefreshOfficeEditTokenRequest) String() string {
  return tea.Prettify(s)
}

func (s RefreshOfficeEditTokenRequest) GoString() string {
  return s.String()
}

func (s *RefreshOfficeEditTokenRequest) SetAdditionData(v map[string]interface{}) *RefreshOfficeEditTokenRequest {
  s.AdditionData = v
  return s
}

func (s *RefreshOfficeEditTokenRequest) SetLocation(v string) *RefreshOfficeEditTokenRequest {
  s.Location = &v
  return s
}

func (s *RefreshOfficeEditTokenRequest) SetOfficeAccessToken(v string) *RefreshOfficeEditTokenRequest {
  s.OfficeAccessToken = &v
  return s
}

func (s *RefreshOfficeEditTokenRequest) SetOfficeRefreshToken(v string) *RefreshOfficeEditTokenRequest {
  s.OfficeRefreshToken = &v
  return s
}

/**
 * 刷新office文档在线编辑凭证 response
 */
type RefreshOfficeEditTokenResponse struct {
  // AccessToken
  OfficeAccessToken *string `json:"office_access_token,omitempty" xml:"office_access_token,omitempty"`
  // RefreshToken
  OfficeRefreshToken *string `json:"office_refresh_token,omitempty" xml:"office_refresh_token,omitempty"`
}

func (s RefreshOfficeEditTokenResponse) String() string {
  return tea.Prettify(s)
}

func (s RefreshOfficeEditTokenResponse) GoString() string {
  return s.String()
}

func (s *RefreshOfficeEditTokenResponse) SetOfficeAccessToken(v string) *RefreshOfficeEditTokenResponse {
  s.OfficeAccessToken = &v
  return s
}

func (s *RefreshOfficeEditTokenResponse) SetOfficeRefreshToken(v string) *RefreshOfficeEditTokenResponse {
  s.OfficeRefreshToken = &v
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
type RenameDetail struct {
  // NewName
  NewName *string `json:"new_name,omitempty" xml:"new_name,omitempty"`
  // OldName
  OldName *string `json:"old_name,omitempty" xml:"old_name,omitempty"`
}

func (s RenameDetail) String() string {
  return tea.Prettify(s)
}

func (s RenameDetail) GoString() string {
  return s.String()
}

func (s *RenameDetail) SetNewName(v string) *RenameDetail {
  s.NewName = &v
  return s
}

func (s *RenameDetail) SetOldName(v string) *RenameDetail {
  s.OldName = &v
  return s
}

/**
 * 
 */
type RestoreDetail struct {
}

func (s RestoreDetail) String() string {
  return tea.Prettify(s)
}

func (s RestoreDetail) GoString() string {
  return s.String()
}

/**
 * 对应OSS Sha1的结构体，定义在 gitlab.alibaba-inc.com/oss/parallel_hash.go OSSSha1Digest
type OSSSha1Digest struct {
h   [5]uint32         // h是计算sha1时存放中间结果的变量，参与每一轮Sha1的计算，必不可少，最后的Sha1值也由这几个数字决定
x   [BlockSize]byte   // 上一轮计算非64字节对齐时，不足64节的内容会保存在这里
nx  int               // 上一轮计算数据长度取模64的结果，64字节对齐时这个值为0
len uint64            // 到上一个数据块为止的总长度，字节，用来计算 OSSRequestSha1Ctx 中的Nl, Nh
}

SHA1CTX 是 OSSSha1Digest 的简化
当每轮计算Sha1的数据长度为64位对齐时，nx固定为0，x长度为0，只需包含h和len；part_offset对应OSSSha1Digest的len
 */
type SHA1CTX struct {
  H []*int `json:"h,omitempty" xml:"h,omitempty" type:"Repeated"`
  PartOffset *int64 `json:"part_offset,omitempty" xml:"part_offset,omitempty"`
}

func (s SHA1CTX) String() string {
  return tea.Prettify(s)
}

func (s SHA1CTX) GoString() string {
  return s.String()
}

func (s *SHA1CTX) SetH(v []*int) *SHA1CTX {
  s.H = v
  return s
}

func (s *SHA1CTX) SetPartOffset(v int64) *SHA1CTX {
  s.PartOffset = &v
  return s
}

/**
 * 全量获取file元信息的请求body
 */
type ScanFileMetaRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // category
  Category *string `json:"category,omitempty" xml:"category,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
  ImageCroppingAspectRatios []*string `json:"image_cropping_aspect_ratios,omitempty" xml:"image_cropping_aspect_ratios,omitempty" type:"Repeated"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // limit
  Limit *int32 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"5000" minimum:"1"`
  // marker
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s ScanFileMetaRequest) String() string {
  return tea.Prettify(s)
}

func (s ScanFileMetaRequest) GoString() string {
  return s.String()
}

func (s *ScanFileMetaRequest) SetAdditionData(v map[string]interface{}) *ScanFileMetaRequest {
  s.AdditionData = v
  return s
}

func (s *ScanFileMetaRequest) SetCategory(v string) *ScanFileMetaRequest {
  s.Category = &v
  return s
}

func (s *ScanFileMetaRequest) SetDriveId(v string) *ScanFileMetaRequest {
  s.DriveId = &v
  return s
}

func (s *ScanFileMetaRequest) SetImageCroppingAspectRatios(v []*string) *ScanFileMetaRequest {
  s.ImageCroppingAspectRatios = v
  return s
}

func (s *ScanFileMetaRequest) SetImageThumbnailProcess(v string) *ScanFileMetaRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *ScanFileMetaRequest) SetImageUrlProcess(v string) *ScanFileMetaRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *ScanFileMetaRequest) SetLimit(v int32) *ScanFileMetaRequest {
  s.Limit = &v
  return s
}

func (s *ScanFileMetaRequest) SetMarker(v string) *ScanFileMetaRequest {
  s.Marker = &v
  return s
}

func (s *ScanFileMetaRequest) SetOfficeThumbnailProcess(v string) *ScanFileMetaRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *ScanFileMetaRequest) SetVideoThumbnailProcess(v string) *ScanFileMetaRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * scan file meta response
 */
type ScanFileMetaResponse struct {
  // items
  Items []*BaseCCPFileResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
  // next_marker
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ScanFileMetaResponse) String() string {
  return tea.Prettify(s)
}

func (s ScanFileMetaResponse) GoString() string {
  return s.String()
}

func (s *ScanFileMetaResponse) SetItems(v []*BaseCCPFileResponse) *ScanFileMetaResponse {
  s.Items = v
  return s
}

func (s *ScanFileMetaResponse) SetNextMarker(v string) *ScanFileMetaResponse {
  s.NextMarker = &v
  return s
}

/**
 * search domain request
 */
type SearchDomainsRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // 分页大小
  Limit *int32 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
  // 查询游标
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // domain名称，模糊匹配
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  // 排序规则
  OrderBy *string `json:"order_by,omitempty" xml:"order_by,omitempty"`
}

func (s SearchDomainsRequest) String() string {
  return tea.Prettify(s)
}

func (s SearchDomainsRequest) GoString() string {
  return s.String()
}

func (s *SearchDomainsRequest) SetHeaders(v map[string]*string) *SearchDomainsRequest {
  s.Headers = v
  return s
}

func (s *SearchDomainsRequest) SetLimit(v int32) *SearchDomainsRequest {
  s.Limit = &v
  return s
}

func (s *SearchDomainsRequest) SetMarker(v string) *SearchDomainsRequest {
  s.Marker = &v
  return s
}

func (s *SearchDomainsRequest) SetName(v string) *SearchDomainsRequest {
  s.Name = &v
  return s
}

func (s *SearchDomainsRequest) SetOrderBy(v string) *SearchDomainsRequest {
  s.OrderBy = &v
  return s
}

/**
 * 搜索文件元数据
 */
type SearchFileRequest struct {
  // addition_data
  AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // drive_ids
  DriveIdList []*string `json:"drive_id_list,omitempty" xml:"drive_id_list,omitempty" type:"Repeated"`
  ImageCroppingAspectRatios []*string `json:"image_cropping_aspect_ratios,omitempty" xml:"image_cropping_aspect_ratios,omitempty" type:"Repeated"`
  // image_thumbnail_process
  ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
  // image_url_process
  ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
  // limit
  Limit *int32 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // Marker
  Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
  // office_thumbnail_process
  OfficeThumbnailProcess *string `json:"office_thumbnail_process,omitempty" xml:"office_thumbnail_process,omitempty"`
  // order_by
  OrderBy *string `json:"order_by,omitempty" xml:"order_by,omitempty"`
  // query
  Query *string `json:"query,omitempty" xml:"query,omitempty" maxLength:"4096"`
  // referer
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  // return_total_count 是否返回查询总数
  ReturnTotalCount *bool `json:"return_total_count,omitempty" xml:"return_total_count,omitempty"`
  // sign_token
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // url_expire_sec
  UrlExpireSec *int64 `json:"url_expire_sec,omitempty" xml:"url_expire_sec,omitempty" maximum:"14400" minimum:"10"`
  // video_thumbnail_process
  // type:string
  VideoThumbnailProcess *string `json:"video_thumbnail_process,omitempty" xml:"video_thumbnail_process,omitempty"`
}

func (s SearchFileRequest) String() string {
  return tea.Prettify(s)
}

func (s SearchFileRequest) GoString() string {
  return s.String()
}

func (s *SearchFileRequest) SetAdditionData(v map[string]interface{}) *SearchFileRequest {
  s.AdditionData = v
  return s
}

func (s *SearchFileRequest) SetDriveId(v string) *SearchFileRequest {
  s.DriveId = &v
  return s
}

func (s *SearchFileRequest) SetDriveIdList(v []*string) *SearchFileRequest {
  s.DriveIdList = v
  return s
}

func (s *SearchFileRequest) SetImageCroppingAspectRatios(v []*string) *SearchFileRequest {
  s.ImageCroppingAspectRatios = v
  return s
}

func (s *SearchFileRequest) SetImageThumbnailProcess(v string) *SearchFileRequest {
  s.ImageThumbnailProcess = &v
  return s
}

func (s *SearchFileRequest) SetImageUrlProcess(v string) *SearchFileRequest {
  s.ImageUrlProcess = &v
  return s
}

func (s *SearchFileRequest) SetLimit(v int32) *SearchFileRequest {
  s.Limit = &v
  return s
}

func (s *SearchFileRequest) SetLocation(v string) *SearchFileRequest {
  s.Location = &v
  return s
}

func (s *SearchFileRequest) SetMarker(v string) *SearchFileRequest {
  s.Marker = &v
  return s
}

func (s *SearchFileRequest) SetOfficeThumbnailProcess(v string) *SearchFileRequest {
  s.OfficeThumbnailProcess = &v
  return s
}

func (s *SearchFileRequest) SetOrderBy(v string) *SearchFileRequest {
  s.OrderBy = &v
  return s
}

func (s *SearchFileRequest) SetQuery(v string) *SearchFileRequest {
  s.Query = &v
  return s
}

func (s *SearchFileRequest) SetReferer(v string) *SearchFileRequest {
  s.Referer = &v
  return s
}

func (s *SearchFileRequest) SetReturnTotalCount(v bool) *SearchFileRequest {
  s.ReturnTotalCount = &v
  return s
}

func (s *SearchFileRequest) SetSignToken(v string) *SearchFileRequest {
  s.SignToken = &v
  return s
}

func (s *SearchFileRequest) SetUrlExpireSec(v int64) *SearchFileRequest {
  s.UrlExpireSec = &v
  return s
}

func (s *SearchFileRequest) SetVideoThumbnailProcess(v string) *SearchFileRequest {
  s.VideoThumbnailProcess = &v
  return s
}

/**
 * search file response
 */
type SearchFileResponse struct {
  // items
  Items []*BaseCCPFileResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
  // next_marker
  NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
  // total_count
  TotalCount *int64 `json:"total_count,omitempty" xml:"total_count,omitempty"`
}

func (s SearchFileResponse) String() string {
  return tea.Prettify(s)
}

func (s SearchFileResponse) GoString() string {
  return s.String()
}

func (s *SearchFileResponse) SetItems(v []*BaseCCPFileResponse) *SearchFileResponse {
  s.Items = v
  return s
}

func (s *SearchFileResponse) SetNextMarker(v string) *SearchFileResponse {
  s.NextMarker = &v
  return s
}

func (s *SearchFileResponse) SetTotalCount(v int64) *SearchFileResponse {
  s.TotalCount = &v
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
type SetShareLinkStatusRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // enabled
  Enabled *bool `json:"enabled,omitempty" xml:"enabled,omitempty" require:"true"`
}

func (s SetShareLinkStatusRequest) String() string {
  return tea.Prettify(s)
}

func (s SetShareLinkStatusRequest) GoString() string {
  return s.String()
}

func (s *SetShareLinkStatusRequest) SetHeaders(v map[string]*string) *SetShareLinkStatusRequest {
  s.Headers = v
  return s
}

func (s *SetShareLinkStatusRequest) SetDomainId(v string) *SetShareLinkStatusRequest {
  s.DomainId = &v
  return s
}

func (s *SetShareLinkStatusRequest) SetEnabled(v bool) *SetShareLinkStatusRequest {
  s.Enabled = &v
  return s
}

/**
 * 
 */
type SetShareStatusRequest struct {
  Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
  // domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" require:"true"`
  // enabled
  Enabled *bool `json:"enabled,omitempty" xml:"enabled,omitempty" require:"true"`
}

func (s SetShareStatusRequest) String() string {
  return tea.Prettify(s)
}

func (s SetShareStatusRequest) GoString() string {
  return s.String()
}

func (s *SetShareStatusRequest) SetHeaders(v map[string]*string) *SetShareStatusRequest {
  s.Headers = v
  return s
}

func (s *SetShareStatusRequest) SetDomainId(v string) *SetShareStatusRequest {
  s.DomainId = &v
  return s
}

func (s *SetShareStatusRequest) SetEnabled(v bool) *SetShareStatusRequest {
  s.Enabled = &v
  return s
}

/**
 * 
 */
type SharePermissionPolicy struct {
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty"`
  FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
  PermissionInheritable *bool `json:"permission_inheritable,omitempty" xml:"permission_inheritable,omitempty"`
  PermissionList []*string `json:"permission_list,omitempty" xml:"permission_list,omitempty" type:"Repeated"`
  PermissionType *string `json:"permission_type,omitempty" xml:"permission_type,omitempty"`
}

func (s SharePermissionPolicy) String() string {
  return tea.Prettify(s)
}

func (s SharePermissionPolicy) GoString() string {
  return s.String()
}

func (s *SharePermissionPolicy) SetFileId(v string) *SharePermissionPolicy {
  s.FileId = &v
  return s
}

func (s *SharePermissionPolicy) SetFilePath(v string) *SharePermissionPolicy {
  s.FilePath = &v
  return s
}

func (s *SharePermissionPolicy) SetPermissionInheritable(v bool) *SharePermissionPolicy {
  s.PermissionInheritable = &v
  return s
}

func (s *SharePermissionPolicy) SetPermissionList(v []*string) *SharePermissionPolicy {
  s.PermissionList = v
  return s
}

func (s *SharePermissionPolicy) SetPermissionType(v string) *SharePermissionPolicy {
  s.PermissionType = &v
  return s
}

/**
 * 
 */
type SimpleStreamInfo struct {
  // crc64_hash
  Crc64Hash *string `json:"crc64_hash,omitempty" xml:"crc64_hash,omitempty"`
  // download_url
  DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
  // size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s SimpleStreamInfo) String() string {
  return tea.Prettify(s)
}

func (s SimpleStreamInfo) GoString() string {
  return s.String()
}

func (s *SimpleStreamInfo) SetCrc64Hash(v string) *SimpleStreamInfo {
  s.Crc64Hash = &v
  return s
}

func (s *SimpleStreamInfo) SetDownloadUrl(v string) *SimpleStreamInfo {
  s.DownloadUrl = &v
  return s
}

func (s *SimpleStreamInfo) SetSize(v int64) *SimpleStreamInfo {
  s.Size = &v
  return s
}

func (s *SimpleStreamInfo) SetThumbnail(v string) *SimpleStreamInfo {
  s.Thumbnail = &v
  return s
}

func (s *SimpleStreamInfo) SetUrl(v string) *SimpleStreamInfo {
  s.Url = &v
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
type StoreFile struct {
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  ParentFilePath *string `json:"parent_file_path,omitempty" xml:"parent_file_path,omitempty"`
  StoreId *string `json:"store_id,omitempty" xml:"store_id,omitempty"`
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
}

func (s StoreFile) String() string {
  return tea.Prettify(s)
}

func (s StoreFile) GoString() string {
  return s.String()
}

func (s *StoreFile) SetDomainId(v string) *StoreFile {
  s.DomainId = &v
  return s
}

func (s *StoreFile) SetName(v string) *StoreFile {
  s.Name = &v
  return s
}

func (s *StoreFile) SetParentFilePath(v string) *StoreFile {
  s.ParentFilePath = &v
  return s
}

func (s *StoreFile) SetStoreId(v string) *StoreFile {
  s.StoreId = &v
  return s
}

func (s *StoreFile) SetType(v string) *StoreFile {
  s.Type = &v
  return s
}

/**
 * 
 */
type StoreItemResponse struct {
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
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
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

func (s StoreItemResponse) String() string {
  return tea.Prettify(s)
}

func (s StoreItemResponse) GoString() string {
  return s.String()
}

func (s *StoreItemResponse) SetAccelerateEndpoint(v string) *StoreItemResponse {
  s.AccelerateEndpoint = &v
  return s
}

func (s *StoreItemResponse) SetBasePath(v string) *StoreItemResponse {
  s.BasePath = &v
  return s
}

func (s *StoreItemResponse) SetBucket(v string) *StoreItemResponse {
  s.Bucket = &v
  return s
}

func (s *StoreItemResponse) SetCdnEndpoint(v string) *StoreItemResponse {
  s.CdnEndpoint = &v
  return s
}

func (s *StoreItemResponse) SetCustomizedAccelerateEndpoint(v string) *StoreItemResponse {
  s.CustomizedAccelerateEndpoint = &v
  return s
}

func (s *StoreItemResponse) SetCustomizedCdnEndpoint(v string) *StoreItemResponse {
  s.CustomizedCdnEndpoint = &v
  return s
}

func (s *StoreItemResponse) SetCustomizedEndpoint(v string) *StoreItemResponse {
  s.CustomizedEndpoint = &v
  return s
}

func (s *StoreItemResponse) SetCustomizedInternalEndpoint(v string) *StoreItemResponse {
  s.CustomizedInternalEndpoint = &v
  return s
}

func (s *StoreItemResponse) SetDomainId(v string) *StoreItemResponse {
  s.DomainId = &v
  return s
}

func (s *StoreItemResponse) SetEndpoint(v string) *StoreItemResponse {
  s.Endpoint = &v
  return s
}

func (s *StoreItemResponse) SetInternalEndpoint(v string) *StoreItemResponse {
  s.InternalEndpoint = &v
  return s
}

func (s *StoreItemResponse) SetLocation(v string) *StoreItemResponse {
  s.Location = &v
  return s
}

func (s *StoreItemResponse) SetOwnership(v string) *StoreItemResponse {
  s.Ownership = &v
  return s
}

func (s *StoreItemResponse) SetPolicy(v string) *StoreItemResponse {
  s.Policy = &v
  return s
}

func (s *StoreItemResponse) SetRoleArn(v string) *StoreItemResponse {
  s.RoleArn = &v
  return s
}

func (s *StoreItemResponse) SetStoreId(v string) *StoreItemResponse {
  s.StoreId = &v
  return s
}

func (s *StoreItemResponse) SetType(v string) *StoreItemResponse {
  s.Type = &v
  return s
}

/**
 * 
 */
type StreamUploadInfo struct {
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // part_info_list
  PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
  // pre_rapid_upload
  // type: boolean
  PreRapidUpload *bool `json:"pre_rapid_upload,omitempty" xml:"pre_rapid_upload,omitempty"`
  // rapid_upload
  // type: boolean
  RapidUpload *bool `json:"rapid_upload,omitempty" xml:"rapid_upload,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
}

func (s StreamUploadInfo) String() string {
  return tea.Prettify(s)
}

func (s StreamUploadInfo) GoString() string {
  return s.String()
}

func (s *StreamUploadInfo) SetLocation(v string) *StreamUploadInfo {
  s.Location = &v
  return s
}

func (s *StreamUploadInfo) SetPartInfoList(v []*UploadPartInfo) *StreamUploadInfo {
  s.PartInfoList = v
  return s
}

func (s *StreamUploadInfo) SetPreRapidUpload(v bool) *StreamUploadInfo {
  s.PreRapidUpload = &v
  return s
}

func (s *StreamUploadInfo) SetRapidUpload(v bool) *StreamUploadInfo {
  s.RapidUpload = &v
  return s
}

func (s *StreamUploadInfo) SetUploadId(v string) *StreamUploadInfo {
  s.UploadId = &v
  return s
}

/**
 * 
 */
type SystemTag struct {
  Confidence *float64 `json:"confidence,omitempty" xml:"confidence,omitempty"`
  EnName *string `json:"en_name,omitempty" xml:"en_name,omitempty"`
  Name *string `json:"name,omitempty" xml:"name,omitempty"`
  ParentEnName *string `json:"parent_en_name,omitempty" xml:"parent_en_name,omitempty"`
  ParentName *string `json:"parent_name,omitempty" xml:"parent_name,omitempty"`
  Source *string `json:"source,omitempty" xml:"source,omitempty"`
  TagLevel *int64 `json:"tag_level,omitempty" xml:"tag_level,omitempty"`
}

func (s SystemTag) String() string {
  return tea.Prettify(s)
}

func (s SystemTag) GoString() string {
  return s.String()
}

func (s *SystemTag) SetConfidence(v float64) *SystemTag {
  s.Confidence = &v
  return s
}

func (s *SystemTag) SetEnName(v string) *SystemTag {
  s.EnName = &v
  return s
}

func (s *SystemTag) SetName(v string) *SystemTag {
  s.Name = &v
  return s
}

func (s *SystemTag) SetParentEnName(v string) *SystemTag {
  s.ParentEnName = &v
  return s
}

func (s *SystemTag) SetParentName(v string) *SystemTag {
  s.ParentName = &v
  return s
}

func (s *SystemTag) SetSource(v string) *SystemTag {
  s.Source = &v
  return s
}

func (s *SystemTag) SetTagLevel(v int64) *SystemTag {
  s.TagLevel = &v
  return s
}

/**
 * 
 */
type Target struct {
  // FileID
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty"`
  // FileName
  FileName *string `json:"file_name,omitempty" xml:"file_name,omitempty"`
  // FileType
  FileType *string `json:"file_type,omitempty" xml:"file_type,omitempty"`
}

func (s Target) String() string {
  return tea.Prettify(s)
}

func (s Target) GoString() string {
  return s.String()
}

func (s *Target) SetFileId(v string) *Target {
  s.FileId = &v
  return s
}

func (s *Target) SetFileName(v string) *Target {
  s.FileName = &v
  return s
}

func (s *Target) SetFileType(v string) *Target {
  s.FileType = &v
  return s
}

/**
 * 
 */
type TimeRange struct {
  // EndTime
  EndTime *string `json:"end_time,omitempty" xml:"end_time,omitempty"`
  // StartTime
  StartTime *string `json:"start_time,omitempty" xml:"start_time,omitempty"`
}

func (s TimeRange) String() string {
  return tea.Prettify(s)
}

func (s TimeRange) GoString() string {
  return s.String()
}

func (s *TimeRange) SetEndTime(v string) *TimeRange {
  s.EndTime = &v
  return s
}

func (s *TimeRange) SetStartTime(v string) *TimeRange {
  s.StartTime = &v
  return s
}

/**
 * 
 */
type TrashDetail struct {
  // ParentFileID
  ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty"`
}

func (s TrashDetail) String() string {
  return tea.Prettify(s)
}

func (s TrashDetail) GoString() string {
  return s.String()
}

func (s *TrashDetail) SetParentFileId(v string) *TrashDetail {
  s.ParentFileId = &v
  return s
}

/**
 * UCGetObjectInfoByObjectKeyRequest
 */
type UCGetObjectInfoByObjectKeyRequest struct {
  ObjectKey *string `json:"object_key,omitempty" xml:"object_key,omitempty"`
}

func (s UCGetObjectInfoByObjectKeyRequest) String() string {
  return tea.Prettify(s)
}

func (s UCGetObjectInfoByObjectKeyRequest) GoString() string {
  return s.String()
}

func (s *UCGetObjectInfoByObjectKeyRequest) SetObjectKey(v string) *UCGetObjectInfoByObjectKeyRequest {
  s.ObjectKey = &v
  return s
}

/**
 * UCGetObjectInfoBySha1Request
 */
type UCGetObjectInfoBySha1Request struct {
  Sha1 *string `json:"sha1,omitempty" xml:"sha1,omitempty"`
}

func (s UCGetObjectInfoBySha1Request) String() string {
  return tea.Prettify(s)
}

func (s UCGetObjectInfoBySha1Request) GoString() string {
  return s.String()
}

func (s *UCGetObjectInfoBySha1Request) SetSha1(v string) *UCGetObjectInfoBySha1Request {
  s.Sha1 = &v
  return s
}

/**
 * 
 */
type UnionAuthentication struct {
  AuthenticationType *string `json:"AuthenticationType,omitempty" xml:"AuthenticationType,omitempty"`
  CreatedAt *int64 `json:"CreatedAt,omitempty" xml:"CreatedAt,omitempty"`
  Extra *string `json:"Extra,omitempty" xml:"Extra,omitempty"`
  Identity *string `json:"Identity,omitempty" xml:"Identity,omitempty"`
  Status *string `json:"Status,omitempty" xml:"Status,omitempty"`
  UnionID *string `json:"UnionID,omitempty" xml:"UnionID,omitempty"`
}

func (s UnionAuthentication) String() string {
  return tea.Prettify(s)
}

func (s UnionAuthentication) GoString() string {
  return s.String()
}

func (s *UnionAuthentication) SetAuthenticationType(v string) *UnionAuthentication {
  s.AuthenticationType = &v
  return s
}

func (s *UnionAuthentication) SetCreatedAt(v int64) *UnionAuthentication {
  s.CreatedAt = &v
  return s
}

func (s *UnionAuthentication) SetExtra(v string) *UnionAuthentication {
  s.Extra = &v
  return s
}

func (s *UnionAuthentication) SetIdentity(v string) *UnionAuthentication {
  s.Identity = &v
  return s
}

func (s *UnionAuthentication) SetStatus(v string) *UnionAuthentication {
  s.Status = &v
  return s
}

func (s *UnionAuthentication) SetUnionID(v string) *UnionAuthentication {
  s.UnionID = &v
  return s
}

/**
 * 
 */
type UnionDomainUserBind struct {
  AuthenticationType *string `json:"AuthenticationType,omitempty" xml:"AuthenticationType,omitempty"`
  DomainID *string `json:"DomainID,omitempty" xml:"DomainID,omitempty"`
  Extra *string `json:"Extra,omitempty" xml:"Extra,omitempty"`
  Identity *string `json:"Identity,omitempty" xml:"Identity,omitempty"`
  UnionID *string `json:"UnionID,omitempty" xml:"UnionID,omitempty"`
  UserID *string `json:"UserID,omitempty" xml:"UserID,omitempty"`
}

func (s UnionDomainUserBind) String() string {
  return tea.Prettify(s)
}

func (s UnionDomainUserBind) GoString() string {
  return s.String()
}

func (s *UnionDomainUserBind) SetAuthenticationType(v string) *UnionDomainUserBind {
  s.AuthenticationType = &v
  return s
}

func (s *UnionDomainUserBind) SetDomainID(v string) *UnionDomainUserBind {
  s.DomainID = &v
  return s
}

func (s *UnionDomainUserBind) SetExtra(v string) *UnionDomainUserBind {
  s.Extra = &v
  return s
}

func (s *UnionDomainUserBind) SetIdentity(v string) *UnionDomainUserBind {
  s.Identity = &v
  return s
}

func (s *UnionDomainUserBind) SetUnionID(v string) *UnionDomainUserBind {
  s.UnionID = &v
  return s
}

func (s *UnionDomainUserBind) SetUserID(v string) *UnionDomainUserBind {
  s.UserID = &v
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
  CustomBenefits map[string]interface{} `json:"custom_benefits,omitempty" xml:"custom_benefits,omitempty"`
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
  GetBenefit *bool `json:"get_benefit,omitempty" xml:"get_benefit,omitempty"`
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

func (s *UpdateDomainRequest) SetCustomBenefits(v map[string]interface{}) *UpdateDomainRequest {
  s.CustomBenefits = v
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

func (s *UpdateDomainRequest) SetGetBenefit(v bool) *UpdateDomainRequest {
  s.GetBenefit = &v
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
  Benefits map[string]interface{} `json:"benefits,omitempty" xml:"benefits,omitempty"`
  // Domain 创建时间
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // 数据 Hash 算法
  DataHashName *string `json:"data_hash_name,omitempty" xml:"data_hash_name,omitempty"`
  DefaultSuperAdminConfig *DomainSuperAdminConfig `json:"default_super_admin_config,omitempty" xml:"default_super_admin_config,omitempty"`
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
  // 预付费domain过期时间
  ExpireTime *int64 `json:"expire_time,omitempty" xml:"expire_time,omitempty"`
  // 是否开启了自动初始化 Drive
  InitDriveEnable *bool `json:"init_drive_enable,omitempty" xml:"init_drive_enable,omitempty"`
  // 自动初始化 Drive 大小
  InitDriveSize *int64 `json:"init_drive_size,omitempty" xml:"init_drive_size,omitempty"`
  // 自动初始化 Drive 所用 Store ID
  InitDriveStoreId *string `json:"init_drive_store_id,omitempty" xml:"init_drive_store_id,omitempty"`
  // Domain 类型
  Mode *string `json:"mode,omitempty" xml:"mode,omitempty"`
  OfficePreviewConfig *OfficePreviewConfig `json:"office_preview_config,omitempty" xml:"office_preview_config,omitempty"`
  // Domain 类型
  PathType *string `json:"path_type,omitempty" xml:"path_type,omitempty"`
  // 预付费套餐
  PrepaidPackage *string `json:"prepaid_package,omitempty" xml:"prepaid_package,omitempty"`
  PublishedAppAccessStrategy *AppAccessStrategy `json:"published_app_access_strategy,omitempty" xml:"published_app_access_strategy,omitempty"`
  // Domain ServiceCode
  ServiceCode *string `json:"service_code,omitempty" xml:"service_code,omitempty"`
  // 是否开启了共享
  Sharable *bool `json:"sharable,omitempty" xml:"sharable,omitempty"`
  // 是否开启了分享
  ShareLinkEnabled *bool `json:"share_link_enabled,omitempty" xml:"share_link_enabled,omitempty"`
  // 容量配额
  SizeQuota *int64 `json:"size_quota,omitempty" xml:"size_quota,omitempty"`
  // SPI 实例 id
  SpiInstanceId *string `json:"spi_instance_id,omitempty" xml:"spi_instance_id,omitempty"`
  // domain状态：创建中，正常，已过期
  Status *int64 `json:"status,omitempty" xml:"status,omitempty"`
  // 存储级别
  StoreLevel *string `json:"store_level,omitempty" xml:"store_level,omitempty"`
  // 存储 Region 列表
  StoreRegionList []*string `json:"store_region_list,omitempty" xml:"store_region_list,omitempty" type:"Repeated"`
  // Domain 更新时间
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // 用户数配额
  UserCountQuota *int64 `json:"user_count_quota,omitempty" xml:"user_count_quota,omitempty"`
  VideoPreviewConfig *VideoPreviewConfig `json:"video_preview_config,omitempty" xml:"video_preview_config,omitempty"`
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

func (s *UpdateDomainResponse) SetBenefits(v map[string]interface{}) *UpdateDomainResponse {
  s.Benefits = v
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

func (s *UpdateDomainResponse) SetDefaultSuperAdminConfig(v *DomainSuperAdminConfig) *UpdateDomainResponse {
  s.DefaultSuperAdminConfig = v
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

func (s *UpdateDomainResponse) SetExpireTime(v int64) *UpdateDomainResponse {
  s.ExpireTime = &v
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

func (s *UpdateDomainResponse) SetOfficePreviewConfig(v *OfficePreviewConfig) *UpdateDomainResponse {
  s.OfficePreviewConfig = v
  return s
}

func (s *UpdateDomainResponse) SetPathType(v string) *UpdateDomainResponse {
  s.PathType = &v
  return s
}

func (s *UpdateDomainResponse) SetPrepaidPackage(v string) *UpdateDomainResponse {
  s.PrepaidPackage = &v
  return s
}

func (s *UpdateDomainResponse) SetPublishedAppAccessStrategy(v *AppAccessStrategy) *UpdateDomainResponse {
  s.PublishedAppAccessStrategy = v
  return s
}

func (s *UpdateDomainResponse) SetServiceCode(v string) *UpdateDomainResponse {
  s.ServiceCode = &v
  return s
}

func (s *UpdateDomainResponse) SetSharable(v bool) *UpdateDomainResponse {
  s.Sharable = &v
  return s
}

func (s *UpdateDomainResponse) SetShareLinkEnabled(v bool) *UpdateDomainResponse {
  s.ShareLinkEnabled = &v
  return s
}

func (s *UpdateDomainResponse) SetSizeQuota(v int64) *UpdateDomainResponse {
  s.SizeQuota = &v
  return s
}

func (s *UpdateDomainResponse) SetSpiInstanceId(v string) *UpdateDomainResponse {
  s.SpiInstanceId = &v
  return s
}

func (s *UpdateDomainResponse) SetStatus(v int64) *UpdateDomainResponse {
  s.Status = &v
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

func (s *UpdateDomainResponse) SetUserCountQuota(v int64) *UpdateDomainResponse {
  s.UserCountQuota = &v
  return s
}

func (s *UpdateDomainResponse) SetVideoPreviewConfig(v *VideoPreviewConfig) *UpdateDomainResponse {
  s.VideoPreviewConfig = v
  return s
}

/**
 * Update drive request
 */
type UpdateDriveRequest struct {
  // 描述信息
  Description *string `json:"description,omitempty" xml:"description,omitempty" maxLength:"1024"`
  // Drive ID
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true"`
  // Drive 名称
  DriveName *string `json:"drive_name,omitempty" xml:"drive_name,omitempty" maxLength:"1024"`
  // 授权访问加密数据
  EncryptDataAccess *bool `json:"encrypt_data_access,omitempty" xml:"encrypt_data_access,omitempty"`
  // 加密模式
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // 状态
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // Subdomain ID
  SubdomainId *string `json:"subdomain_id,omitempty" xml:"subdomain_id,omitempty"`
  // 总大小,单位Byte [如果设置 -1 代表不限制]
  TotalSize *int64 `json:"total_size,omitempty" xml:"total_size,omitempty"`
}

func (s UpdateDriveRequest) String() string {
  return tea.Prettify(s)
}

func (s UpdateDriveRequest) GoString() string {
  return s.String()
}

func (s *UpdateDriveRequest) SetDescription(v string) *UpdateDriveRequest {
  s.Description = &v
  return s
}

func (s *UpdateDriveRequest) SetDriveId(v string) *UpdateDriveRequest {
  s.DriveId = &v
  return s
}

func (s *UpdateDriveRequest) SetDriveName(v string) *UpdateDriveRequest {
  s.DriveName = &v
  return s
}

func (s *UpdateDriveRequest) SetEncryptDataAccess(v bool) *UpdateDriveRequest {
  s.EncryptDataAccess = &v
  return s
}

func (s *UpdateDriveRequest) SetEncryptMode(v string) *UpdateDriveRequest {
  s.EncryptMode = &v
  return s
}

func (s *UpdateDriveRequest) SetStatus(v string) *UpdateDriveRequest {
  s.Status = &v
  return s
}

func (s *UpdateDriveRequest) SetSubdomainId(v string) *UpdateDriveRequest {
  s.SubdomainId = &v
  return s
}

func (s *UpdateDriveRequest) SetTotalSize(v int64) *UpdateDriveRequest {
  s.TotalSize = &v
  return s
}

/**
 * Update drive response
 */
type UpdateDriveResponse struct {
  // Drive 创建者
  Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
  // Drive 备注信息
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // Domain ID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // Drive ID
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty"`
  // Drive 名称
  DriveName *string `json:"drive_name,omitempty" xml:"drive_name,omitempty"`
  // Drive 类型
  DriveType *string `json:"drive_type,omitempty" xml:"drive_type,omitempty"`
  EncryptDataAccess *bool `json:"encrypt_data_access,omitempty" xml:"encrypt_data_access,omitempty"`
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // Drive 所有者
  Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
  // Drive 所有者类型
  OwnerType *string `json:"owner_type,omitempty" xml:"owner_type,omitempty"`
  // Drive存储基于store的相对路径，domain的PathType为OSSPath时返回
  RelativePath *string `json:"relative_path,omitempty" xml:"relative_path,omitempty"`
  // Drive 状态
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // 存储 ID, domain的PathType为OSSPath时返回
  StoreId *string `json:"store_id,omitempty" xml:"store_id,omitempty"`
  // Drive 空间总量
  TotalSize *int64 `json:"total_size,omitempty" xml:"total_size,omitempty"`
  // Drive 空间已使用量
  UsedSize *int64 `json:"used_size,omitempty" xml:"used_size,omitempty"`
}

func (s UpdateDriveResponse) String() string {
  return tea.Prettify(s)
}

func (s UpdateDriveResponse) GoString() string {
  return s.String()
}

func (s *UpdateDriveResponse) SetCreator(v string) *UpdateDriveResponse {
  s.Creator = &v
  return s
}

func (s *UpdateDriveResponse) SetDescription(v string) *UpdateDriveResponse {
  s.Description = &v
  return s
}

func (s *UpdateDriveResponse) SetDomainId(v string) *UpdateDriveResponse {
  s.DomainId = &v
  return s
}

func (s *UpdateDriveResponse) SetDriveId(v string) *UpdateDriveResponse {
  s.DriveId = &v
  return s
}

func (s *UpdateDriveResponse) SetDriveName(v string) *UpdateDriveResponse {
  s.DriveName = &v
  return s
}

func (s *UpdateDriveResponse) SetDriveType(v string) *UpdateDriveResponse {
  s.DriveType = &v
  return s
}

func (s *UpdateDriveResponse) SetEncryptDataAccess(v bool) *UpdateDriveResponse {
  s.EncryptDataAccess = &v
  return s
}

func (s *UpdateDriveResponse) SetEncryptMode(v string) *UpdateDriveResponse {
  s.EncryptMode = &v
  return s
}

func (s *UpdateDriveResponse) SetOwner(v string) *UpdateDriveResponse {
  s.Owner = &v
  return s
}

func (s *UpdateDriveResponse) SetOwnerType(v string) *UpdateDriveResponse {
  s.OwnerType = &v
  return s
}

func (s *UpdateDriveResponse) SetRelativePath(v string) *UpdateDriveResponse {
  s.RelativePath = &v
  return s
}

func (s *UpdateDriveResponse) SetStatus(v string) *UpdateDriveResponse {
  s.Status = &v
  return s
}

func (s *UpdateDriveResponse) SetStoreId(v string) *UpdateDriveResponse {
  s.StoreId = &v
  return s
}

func (s *UpdateDriveResponse) SetTotalSize(v int64) *UpdateDriveResponse {
  s.TotalSize = &v
  return s
}

func (s *UpdateDriveResponse) SetUsedSize(v int64) *UpdateDriveResponse {
  s.UsedSize = &v
  return s
}

/**
 * 更新文件元数据
 */
type UpdateFileMetaRequest struct {
  // check_name_mode
  CheckNameMode *string `json:"check_name_mode,omitempty" xml:"check_name_mode,omitempty"`
  CustomIndexKey *string `json:"custom_index_key,omitempty" xml:"custom_index_key,omitempty"`
  // description
  // type: string
  Description *string `json:"description,omitempty" xml:"description,omitempty" maxLength:"1024"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
  FileIdPath *string `json:"file_id_path,omitempty" xml:"file_id_path,omitempty"`
  // hidden
  // type: boolean
  Hidden *bool `json:"hidden,omitempty" xml:"hidden,omitempty"`
  // labels
  Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
  Meta *string `json:"meta,omitempty" xml:"meta,omitempty"`
  // name
  Name *string `json:"name,omitempty" xml:"name,omitempty" maxLength:"1024" minLength:"1"`
  Referer *string `json:"referer,omitempty" xml:"referer,omitempty"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  SignToken *string `json:"sign_token,omitempty" xml:"sign_token,omitempty"`
  // starred
  // type: boolean
  Starred *bool `json:"starred,omitempty" xml:"starred,omitempty"`
  // user_meta
  UserMeta *string `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
}

func (s UpdateFileMetaRequest) String() string {
  return tea.Prettify(s)
}

func (s UpdateFileMetaRequest) GoString() string {
  return s.String()
}

func (s *UpdateFileMetaRequest) SetCheckNameMode(v string) *UpdateFileMetaRequest {
  s.CheckNameMode = &v
  return s
}

func (s *UpdateFileMetaRequest) SetCustomIndexKey(v string) *UpdateFileMetaRequest {
  s.CustomIndexKey = &v
  return s
}

func (s *UpdateFileMetaRequest) SetDescription(v string) *UpdateFileMetaRequest {
  s.Description = &v
  return s
}

func (s *UpdateFileMetaRequest) SetDriveId(v string) *UpdateFileMetaRequest {
  s.DriveId = &v
  return s
}

func (s *UpdateFileMetaRequest) SetEncryptMode(v string) *UpdateFileMetaRequest {
  s.EncryptMode = &v
  return s
}

func (s *UpdateFileMetaRequest) SetFileId(v string) *UpdateFileMetaRequest {
  s.FileId = &v
  return s
}

func (s *UpdateFileMetaRequest) SetFileIdPath(v string) *UpdateFileMetaRequest {
  s.FileIdPath = &v
  return s
}

func (s *UpdateFileMetaRequest) SetHidden(v bool) *UpdateFileMetaRequest {
  s.Hidden = &v
  return s
}

func (s *UpdateFileMetaRequest) SetLabels(v []*string) *UpdateFileMetaRequest {
  s.Labels = v
  return s
}

func (s *UpdateFileMetaRequest) SetMeta(v string) *UpdateFileMetaRequest {
  s.Meta = &v
  return s
}

func (s *UpdateFileMetaRequest) SetName(v string) *UpdateFileMetaRequest {
  s.Name = &v
  return s
}

func (s *UpdateFileMetaRequest) SetReferer(v string) *UpdateFileMetaRequest {
  s.Referer = &v
  return s
}

func (s *UpdateFileMetaRequest) SetShareId(v string) *UpdateFileMetaRequest {
  s.ShareId = &v
  return s
}

func (s *UpdateFileMetaRequest) SetSignToken(v string) *UpdateFileMetaRequest {
  s.SignToken = &v
  return s
}

func (s *UpdateFileMetaRequest) SetStarred(v bool) *UpdateFileMetaRequest {
  s.Starred = &v
  return s
}

func (s *UpdateFileMetaRequest) SetUserMeta(v string) *UpdateFileMetaRequest {
  s.UserMeta = &v
  return s
}

/**
 * 更新文件元数据 response
 */
type UpdateFileMetaResponse struct {
  // category
  Category *string `json:"category,omitempty" xml:"category,omitempty"`
  // CharacteristicHash
  CharacteristicHash *string `json:"characteristic_hash,omitempty" xml:"characteristic_hash,omitempty"`
  // Content Hash
  ContentHash *string `json:"content_hash,omitempty" xml:"content_hash,omitempty"`
  // content_hash_name
  ContentHashName *string `json:"content_hash_name,omitempty" xml:"content_hash_name,omitempty"`
  // content_type
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // crc64_hash
  Crc64Hash *string `json:"crc64_hash,omitempty" xml:"crc64_hash,omitempty"`
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // DomainID
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
  // download_url
  DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
  // encrypt_mode
  EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
  // file_extension
  FileExtension *string `json:"file_extension,omitempty" xml:"file_extension,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // Hidden
  // type: boolean
  Hidden *bool `json:"hidden,omitempty" xml:"hidden,omitempty"`
  ImageMediaMetadata *ImageMediaResponse `json:"image_media_metadata,omitempty" xml:"image_media_metadata,omitempty"`
  // labels
  Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
  Meta *string `json:"meta,omitempty" xml:"meta,omitempty"`
  // name
  Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
  // parent_file_id
  ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
  // PunishFlag
  PunishFlag *int64 `json:"punish_flag,omitempty" xml:"punish_flag,omitempty"`
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // Size
  Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
  // starred
  // type: boolean
  Starred *bool `json:"starred,omitempty" xml:"starred,omitempty"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // @Deprecated streams url info
  StreamsInfo map[string]interface{} `json:"streams_info,omitempty" xml:"streams_info,omitempty"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // trashed_at
  TrashedAt *string `json:"trashed_at,omitempty" xml:"trashed_at,omitempty"`
  // type
  Type *string `json:"type,omitempty" xml:"type,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
  // upload_id
  UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
  // user_meta
  UserMeta *string `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
  VideoMediaMetadata *VideoMediaResponse `json:"video_media_metadata,omitempty" xml:"video_media_metadata,omitempty"`
  VideoPreviewMetadata *VideoPreviewResponse `json:"video_preview_metadata,omitempty" xml:"video_preview_metadata,omitempty"`
}

func (s UpdateFileMetaResponse) String() string {
  return tea.Prettify(s)
}

func (s UpdateFileMetaResponse) GoString() string {
  return s.String()
}

func (s *UpdateFileMetaResponse) SetCategory(v string) *UpdateFileMetaResponse {
  s.Category = &v
  return s
}

func (s *UpdateFileMetaResponse) SetCharacteristicHash(v string) *UpdateFileMetaResponse {
  s.CharacteristicHash = &v
  return s
}

func (s *UpdateFileMetaResponse) SetContentHash(v string) *UpdateFileMetaResponse {
  s.ContentHash = &v
  return s
}

func (s *UpdateFileMetaResponse) SetContentHashName(v string) *UpdateFileMetaResponse {
  s.ContentHashName = &v
  return s
}

func (s *UpdateFileMetaResponse) SetContentType(v string) *UpdateFileMetaResponse {
  s.ContentType = &v
  return s
}

func (s *UpdateFileMetaResponse) SetCrc64Hash(v string) *UpdateFileMetaResponse {
  s.Crc64Hash = &v
  return s
}

func (s *UpdateFileMetaResponse) SetCreatedAt(v string) *UpdateFileMetaResponse {
  s.CreatedAt = &v
  return s
}

func (s *UpdateFileMetaResponse) SetDescription(v string) *UpdateFileMetaResponse {
  s.Description = &v
  return s
}

func (s *UpdateFileMetaResponse) SetDomainId(v string) *UpdateFileMetaResponse {
  s.DomainId = &v
  return s
}

func (s *UpdateFileMetaResponse) SetDownloadUrl(v string) *UpdateFileMetaResponse {
  s.DownloadUrl = &v
  return s
}

func (s *UpdateFileMetaResponse) SetDriveId(v string) *UpdateFileMetaResponse {
  s.DriveId = &v
  return s
}

func (s *UpdateFileMetaResponse) SetEncryptMode(v string) *UpdateFileMetaResponse {
  s.EncryptMode = &v
  return s
}

func (s *UpdateFileMetaResponse) SetFileExtension(v string) *UpdateFileMetaResponse {
  s.FileExtension = &v
  return s
}

func (s *UpdateFileMetaResponse) SetFileId(v string) *UpdateFileMetaResponse {
  s.FileId = &v
  return s
}

func (s *UpdateFileMetaResponse) SetHidden(v bool) *UpdateFileMetaResponse {
  s.Hidden = &v
  return s
}

func (s *UpdateFileMetaResponse) SetImageMediaMetadata(v *ImageMediaResponse) *UpdateFileMetaResponse {
  s.ImageMediaMetadata = v
  return s
}

func (s *UpdateFileMetaResponse) SetLabels(v []*string) *UpdateFileMetaResponse {
  s.Labels = v
  return s
}

func (s *UpdateFileMetaResponse) SetMeta(v string) *UpdateFileMetaResponse {
  s.Meta = &v
  return s
}

func (s *UpdateFileMetaResponse) SetName(v string) *UpdateFileMetaResponse {
  s.Name = &v
  return s
}

func (s *UpdateFileMetaResponse) SetParentFileId(v string) *UpdateFileMetaResponse {
  s.ParentFileId = &v
  return s
}

func (s *UpdateFileMetaResponse) SetPunishFlag(v int64) *UpdateFileMetaResponse {
  s.PunishFlag = &v
  return s
}

func (s *UpdateFileMetaResponse) SetShareId(v string) *UpdateFileMetaResponse {
  s.ShareId = &v
  return s
}

func (s *UpdateFileMetaResponse) SetSize(v int64) *UpdateFileMetaResponse {
  s.Size = &v
  return s
}

func (s *UpdateFileMetaResponse) SetStarred(v bool) *UpdateFileMetaResponse {
  s.Starred = &v
  return s
}

func (s *UpdateFileMetaResponse) SetStatus(v string) *UpdateFileMetaResponse {
  s.Status = &v
  return s
}

func (s *UpdateFileMetaResponse) SetStreamsInfo(v map[string]interface{}) *UpdateFileMetaResponse {
  s.StreamsInfo = v
  return s
}

func (s *UpdateFileMetaResponse) SetThumbnail(v string) *UpdateFileMetaResponse {
  s.Thumbnail = &v
  return s
}

func (s *UpdateFileMetaResponse) SetTrashedAt(v string) *UpdateFileMetaResponse {
  s.TrashedAt = &v
  return s
}

func (s *UpdateFileMetaResponse) SetType(v string) *UpdateFileMetaResponse {
  s.Type = &v
  return s
}

func (s *UpdateFileMetaResponse) SetUpdatedAt(v string) *UpdateFileMetaResponse {
  s.UpdatedAt = &v
  return s
}

func (s *UpdateFileMetaResponse) SetUploadId(v string) *UpdateFileMetaResponse {
  s.UploadId = &v
  return s
}

func (s *UpdateFileMetaResponse) SetUrl(v string) *UpdateFileMetaResponse {
  s.Url = &v
  return s
}

func (s *UpdateFileMetaResponse) SetUserMeta(v string) *UpdateFileMetaResponse {
  s.UserMeta = &v
  return s
}

func (s *UpdateFileMetaResponse) SetVideoMediaMetadata(v *VideoMediaResponse) *UpdateFileMetaResponse {
  s.VideoMediaMetadata = v
  return s
}

func (s *UpdateFileMetaResponse) SetVideoPreviewMetadata(v *VideoPreviewResponse) *UpdateFileMetaResponse {
  s.VideoPreviewMetadata = v
  return s
}

/**
 * update_share_link request
 */
type UpdateShareLinkRequest struct {
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // share_name
  ShareName *string `json:"share_name,omitempty" xml:"share_name,omitempty"`
  // share_pwd
  SharePwd *string `json:"share_pwd,omitempty" xml:"share_pwd,omitempty" maximum:"64" minimum:"0"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
}

func (s UpdateShareLinkRequest) String() string {
  return tea.Prettify(s)
}

func (s UpdateShareLinkRequest) GoString() string {
  return s.String()
}

func (s *UpdateShareLinkRequest) SetDescription(v string) *UpdateShareLinkRequest {
  s.Description = &v
  return s
}

func (s *UpdateShareLinkRequest) SetExpiration(v string) *UpdateShareLinkRequest {
  s.Expiration = &v
  return s
}

func (s *UpdateShareLinkRequest) SetShareId(v string) *UpdateShareLinkRequest {
  s.ShareId = &v
  return s
}

func (s *UpdateShareLinkRequest) SetShareName(v string) *UpdateShareLinkRequest {
  s.ShareName = &v
  return s
}

func (s *UpdateShareLinkRequest) SetSharePwd(v string) *UpdateShareLinkRequest {
  s.SharePwd = &v
  return s
}

func (s *UpdateShareLinkRequest) SetStatus(v string) *UpdateShareLinkRequest {
  s.Status = &v
  return s
}

/**
 * update_share_link response
 */
type UpdateShareLinkResponse struct {
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // creator
  Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // 下载次数
  DownloadCount *int64 `json:"download_count,omitempty" xml:"download_count,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty"`
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // expired
  Expired *bool `json:"expired,omitempty" xml:"expired,omitempty"`
  // file_id
  FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty"`
  // file_id_list
  FileIdList []*string `json:"file_id_list,omitempty" xml:"file_id_list,omitempty" type:"Repeated"`
  // file_id_list
  FilePathList []*string `json:"file_path_list,omitempty" xml:"file_path_list,omitempty" type:"Repeated"`
  // preview_count
  PreviewCount *int64 `json:"preview_count,omitempty" xml:"preview_count,omitempty"`
  // 转存次数
  SaveCount *int64 `json:"save_count,omitempty" xml:"save_count,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // share_msg
  ShareMsg *string `json:"share_msg,omitempty" xml:"share_msg,omitempty"`
  // share_name
  ShareName *string `json:"share_name,omitempty" xml:"share_name,omitempty"`
  // share_policy
  SharePolicy *string `json:"share_policy,omitempty" xml:"share_policy,omitempty"`
  // share_pwd
  SharePwd *string `json:"share_pwd,omitempty" xml:"share_pwd,omitempty"`
  // share_url
  ShareUrl *string `json:"share_url,omitempty" xml:"share_url,omitempty"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s UpdateShareLinkResponse) String() string {
  return tea.Prettify(s)
}

func (s UpdateShareLinkResponse) GoString() string {
  return s.String()
}

func (s *UpdateShareLinkResponse) SetCreatedAt(v string) *UpdateShareLinkResponse {
  s.CreatedAt = &v
  return s
}

func (s *UpdateShareLinkResponse) SetCreator(v string) *UpdateShareLinkResponse {
  s.Creator = &v
  return s
}

func (s *UpdateShareLinkResponse) SetDescription(v string) *UpdateShareLinkResponse {
  s.Description = &v
  return s
}

func (s *UpdateShareLinkResponse) SetDownloadCount(v int64) *UpdateShareLinkResponse {
  s.DownloadCount = &v
  return s
}

func (s *UpdateShareLinkResponse) SetDriveId(v string) *UpdateShareLinkResponse {
  s.DriveId = &v
  return s
}

func (s *UpdateShareLinkResponse) SetExpiration(v string) *UpdateShareLinkResponse {
  s.Expiration = &v
  return s
}

func (s *UpdateShareLinkResponse) SetExpired(v bool) *UpdateShareLinkResponse {
  s.Expired = &v
  return s
}

func (s *UpdateShareLinkResponse) SetFileId(v string) *UpdateShareLinkResponse {
  s.FileId = &v
  return s
}

func (s *UpdateShareLinkResponse) SetFileIdList(v []*string) *UpdateShareLinkResponse {
  s.FileIdList = v
  return s
}

func (s *UpdateShareLinkResponse) SetFilePathList(v []*string) *UpdateShareLinkResponse {
  s.FilePathList = v
  return s
}

func (s *UpdateShareLinkResponse) SetPreviewCount(v int64) *UpdateShareLinkResponse {
  s.PreviewCount = &v
  return s
}

func (s *UpdateShareLinkResponse) SetSaveCount(v int64) *UpdateShareLinkResponse {
  s.SaveCount = &v
  return s
}

func (s *UpdateShareLinkResponse) SetShareId(v string) *UpdateShareLinkResponse {
  s.ShareId = &v
  return s
}

func (s *UpdateShareLinkResponse) SetShareMsg(v string) *UpdateShareLinkResponse {
  s.ShareMsg = &v
  return s
}

func (s *UpdateShareLinkResponse) SetShareName(v string) *UpdateShareLinkResponse {
  s.ShareName = &v
  return s
}

func (s *UpdateShareLinkResponse) SetSharePolicy(v string) *UpdateShareLinkResponse {
  s.SharePolicy = &v
  return s
}

func (s *UpdateShareLinkResponse) SetSharePwd(v string) *UpdateShareLinkResponse {
  s.SharePwd = &v
  return s
}

func (s *UpdateShareLinkResponse) SetShareUrl(v string) *UpdateShareLinkResponse {
  s.ShareUrl = &v
  return s
}

func (s *UpdateShareLinkResponse) SetStatus(v string) *UpdateShareLinkResponse {
  s.Status = &v
  return s
}

func (s *UpdateShareLinkResponse) SetUpdatedAt(v string) *UpdateShareLinkResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * update share request
 */
type UpdateShareRequest struct {
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty" maxLength:"1024"`
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // permissions
  Permissions []*string `json:"permissions,omitempty" xml:"permissions,omitempty" type:"Repeated"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" require:"true"`
  // share_name
  ShareName *string `json:"share_name,omitempty" xml:"share_name,omitempty"`
  // share_policy
  SharePolicy []*SharePermissionPolicy `json:"share_policy,omitempty" xml:"share_policy,omitempty" type:"Repeated"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
}

func (s UpdateShareRequest) String() string {
  return tea.Prettify(s)
}

func (s UpdateShareRequest) GoString() string {
  return s.String()
}

func (s *UpdateShareRequest) SetDescription(v string) *UpdateShareRequest {
  s.Description = &v
  return s
}

func (s *UpdateShareRequest) SetExpiration(v string) *UpdateShareRequest {
  s.Expiration = &v
  return s
}

func (s *UpdateShareRequest) SetPermissions(v []*string) *UpdateShareRequest {
  s.Permissions = v
  return s
}

func (s *UpdateShareRequest) SetShareId(v string) *UpdateShareRequest {
  s.ShareId = &v
  return s
}

func (s *UpdateShareRequest) SetShareName(v string) *UpdateShareRequest {
  s.ShareName = &v
  return s
}

func (s *UpdateShareRequest) SetSharePolicy(v []*SharePermissionPolicy) *UpdateShareRequest {
  s.SharePolicy = v
  return s
}

func (s *UpdateShareRequest) SetStatus(v string) *UpdateShareRequest {
  s.Status = &v
  return s
}

/**
 * Update share response
 */
type UpdateShareResponse struct {
  // created_at
  CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
  // creator
  Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
  // description
  Description *string `json:"description,omitempty" xml:"description,omitempty"`
  // domain_id
  DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
  // drive_id
  DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty"`
  // expiration
  Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
  // expired
  Expired *bool `json:"expired,omitempty" xml:"expired,omitempty"`
  // owner
  Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
  // owner
  OwnerType *string `json:"owner_type,omitempty" xml:"owner_type,omitempty"`
  // permissions
  Permissions []*string `json:"permissions,omitempty" xml:"permissions,omitempty" type:"Repeated"`
  // share_file_id
  ShareFileId *string `json:"share_file_id,omitempty" xml:"share_file_id,omitempty"`
  // share_path
  ShareFilePath *string `json:"share_file_path,omitempty" xml:"share_file_path,omitempty"`
  // share_id
  ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
  // share_name
  ShareName *string `json:"share_name,omitempty" xml:"share_name,omitempty"`
  SharePolicy []*SharePermissionPolicy `json:"share_policy,omitempty" xml:"share_policy,omitempty" type:"Repeated"`
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // updated_at
  UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s UpdateShareResponse) String() string {
  return tea.Prettify(s)
}

func (s UpdateShareResponse) GoString() string {
  return s.String()
}

func (s *UpdateShareResponse) SetCreatedAt(v string) *UpdateShareResponse {
  s.CreatedAt = &v
  return s
}

func (s *UpdateShareResponse) SetCreator(v string) *UpdateShareResponse {
  s.Creator = &v
  return s
}

func (s *UpdateShareResponse) SetDescription(v string) *UpdateShareResponse {
  s.Description = &v
  return s
}

func (s *UpdateShareResponse) SetDomainId(v string) *UpdateShareResponse {
  s.DomainId = &v
  return s
}

func (s *UpdateShareResponse) SetDriveId(v string) *UpdateShareResponse {
  s.DriveId = &v
  return s
}

func (s *UpdateShareResponse) SetExpiration(v string) *UpdateShareResponse {
  s.Expiration = &v
  return s
}

func (s *UpdateShareResponse) SetExpired(v bool) *UpdateShareResponse {
  s.Expired = &v
  return s
}

func (s *UpdateShareResponse) SetOwner(v string) *UpdateShareResponse {
  s.Owner = &v
  return s
}

func (s *UpdateShareResponse) SetOwnerType(v string) *UpdateShareResponse {
  s.OwnerType = &v
  return s
}

func (s *UpdateShareResponse) SetPermissions(v []*string) *UpdateShareResponse {
  s.Permissions = v
  return s
}

func (s *UpdateShareResponse) SetShareFileId(v string) *UpdateShareResponse {
  s.ShareFileId = &v
  return s
}

func (s *UpdateShareResponse) SetShareFilePath(v string) *UpdateShareResponse {
  s.ShareFilePath = &v
  return s
}

func (s *UpdateShareResponse) SetShareId(v string) *UpdateShareResponse {
  s.ShareId = &v
  return s
}

func (s *UpdateShareResponse) SetShareName(v string) *UpdateShareResponse {
  s.ShareName = &v
  return s
}

func (s *UpdateShareResponse) SetSharePolicy(v []*SharePermissionPolicy) *UpdateShareResponse {
  s.SharePolicy = v
  return s
}

func (s *UpdateShareResponse) SetStatus(v string) *UpdateShareResponse {
  s.Status = &v
  return s
}

func (s *UpdateShareResponse) SetUpdatedAt(v string) *UpdateShareResponse {
  s.UpdatedAt = &v
  return s
}

/**
 * 
 */
type UploadPartInfo struct {
  // content_type
  ContentType *string `json:"content_type,omitempty" xml:"content_type,omitempty"`
  // etag
  Etag *string `json:"etag,omitempty" xml:"etag,omitempty"`
  ParallelSha1Ctx *SHA1CTX `json:"parallel_sha1_ctx,omitempty" xml:"parallel_sha1_ctx,omitempty"`
  // PartNumber
  PartNumber *int64 `json:"part_number,omitempty" xml:"part_number,omitempty" maximum:"10000" minimum:"1"`
  // PartSize：
  PartSize *int64 `json:"part_size,omitempty" xml:"part_size,omitempty" maximum:"5368709120"`
  // upload_url
  UploadUrl *string `json:"upload_url,omitempty" xml:"upload_url,omitempty"`
}

func (s UploadPartInfo) String() string {
  return tea.Prettify(s)
}

func (s UploadPartInfo) GoString() string {
  return s.String()
}

func (s *UploadPartInfo) SetContentType(v string) *UploadPartInfo {
  s.ContentType = &v
  return s
}

func (s *UploadPartInfo) SetEtag(v string) *UploadPartInfo {
  s.Etag = &v
  return s
}

func (s *UploadPartInfo) SetParallelSha1Ctx(v *SHA1CTX) *UploadPartInfo {
  s.ParallelSha1Ctx = v
  return s
}

func (s *UploadPartInfo) SetPartNumber(v int64) *UploadPartInfo {
  s.PartNumber = &v
  return s
}

func (s *UploadPartInfo) SetPartSize(v int64) *UploadPartInfo {
  s.PartSize = &v
  return s
}

func (s *UploadPartInfo) SetUploadUrl(v string) *UploadPartInfo {
  s.UploadUrl = &v
  return s
}

/**
 * 
 */
type UrlInfo struct {
  // download_url
  DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // url
  Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s UrlInfo) String() string {
  return tea.Prettify(s)
}

func (s UrlInfo) GoString() string {
  return s.String()
}

func (s *UrlInfo) SetDownloadUrl(v string) *UrlInfo {
  s.DownloadUrl = &v
  return s
}

func (s *UrlInfo) SetThumbnail(v string) *UrlInfo {
  s.Thumbnail = &v
  return s
}

func (s *UrlInfo) SetUrl(v string) *UrlInfo {
  s.Url = &v
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
  // subdomain id
  SubdomainId *string `json:"subdomain_id,omitempty" xml:"subdomain_id,omitempty"`
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

func (s *UserAuthentication) SetSubdomainId(v string) *UserAuthentication {
  s.SubdomainId = &v
  return s
}

/**
 * 
 */
type VerifyCodeResponse struct {
  // 修改密码的临时授权码
  State *string `json:"state,omitempty" xml:"state,omitempty" require:"true"`
}

func (s VerifyCodeResponse) String() string {
  return tea.Prettify(s)
}

func (s VerifyCodeResponse) GoString() string {
  return s.String()
}

func (s *VerifyCodeResponse) SetState(v string) *VerifyCodeResponse {
  s.State = &v
  return s
}

/**
 * 
 */
type VerifyTokenResponse struct {
  // 实人认证的Token
  Token *string `json:"token,omitempty" xml:"token,omitempty" require:"true"`
  // 实人认证token有效秒数，如1800
  Ttl *int64 `json:"ttl,omitempty" xml:"ttl,omitempty" require:"true"`
  // 实人认证的URL，包含Token
  Url *string `json:"url,omitempty" xml:"url,omitempty" require:"true"`
}

func (s VerifyTokenResponse) String() string {
  return tea.Prettify(s)
}

func (s VerifyTokenResponse) GoString() string {
  return s.String()
}

func (s *VerifyTokenResponse) SetToken(v string) *VerifyTokenResponse {
  s.Token = &v
  return s
}

func (s *VerifyTokenResponse) SetTtl(v int64) *VerifyTokenResponse {
  s.Ttl = &v
  return s
}

func (s *VerifyTokenResponse) SetUrl(v string) *VerifyTokenResponse {
  s.Url = &v
  return s
}

/**
 * 
 */
type VideoMediaAudioStream struct {
  // bit_rate 音频比特率 单位：bps
  BitRate *string `json:"bit_rate,omitempty" xml:"bit_rate,omitempty"`
  // channel_layout 声道布局
  ChannelLayout *string `json:"channel_layout,omitempty" xml:"channel_layout,omitempty"`
  // channels 音频数/声道数
  Channels *int64 `json:"channels,omitempty" xml:"channels,omitempty"`
  // code_name 音频编码模式
  CodeName *string `json:"code_name,omitempty" xml:"code_name,omitempty"`
  // duration 单位 秒
  Duration *string `json:"duration,omitempty" xml:"duration,omitempty"`
  // sample_rate 音频采样率
  SampleRate *string `json:"sample_rate,omitempty" xml:"sample_rate,omitempty"`
}

func (s VideoMediaAudioStream) String() string {
  return tea.Prettify(s)
}

func (s VideoMediaAudioStream) GoString() string {
  return s.String()
}

func (s *VideoMediaAudioStream) SetBitRate(v string) *VideoMediaAudioStream {
  s.BitRate = &v
  return s
}

func (s *VideoMediaAudioStream) SetChannelLayout(v string) *VideoMediaAudioStream {
  s.ChannelLayout = &v
  return s
}

func (s *VideoMediaAudioStream) SetChannels(v int64) *VideoMediaAudioStream {
  s.Channels = &v
  return s
}

func (s *VideoMediaAudioStream) SetCodeName(v string) *VideoMediaAudioStream {
  s.CodeName = &v
  return s
}

func (s *VideoMediaAudioStream) SetDuration(v string) *VideoMediaAudioStream {
  s.Duration = &v
  return s
}

func (s *VideoMediaAudioStream) SetSampleRate(v string) *VideoMediaAudioStream {
  s.SampleRate = &v
  return s
}

/**
 * 
 */
type VideoMediaMetadata struct {
  // Duration
  Duration *string `json:"duration,omitempty" xml:"duration,omitempty"`
}

func (s VideoMediaMetadata) String() string {
  return tea.Prettify(s)
}

func (s VideoMediaMetadata) GoString() string {
  return s.String()
}

func (s *VideoMediaMetadata) SetDuration(v string) *VideoMediaMetadata {
  s.Duration = &v
  return s
}

/**
 * 
 */
type VideoMediaResponse struct {
  // address_line
  AddressLine *string `json:"address_line,omitempty" xml:"address_line,omitempty"`
  // city
  City *string `json:"city,omitempty" xml:"city,omitempty"`
  // country
  Country *string `json:"country,omitempty" xml:"country,omitempty"`
  // district
  District *string `json:"district,omitempty" xml:"district,omitempty"`
  // duration 单位 秒
  Duration *string `json:"duration,omitempty" xml:"duration,omitempty"`
  // height
  Height *int64 `json:"height,omitempty" xml:"height,omitempty"`
  // system_tags
  ImageTags []*SystemTag `json:"image_tags,omitempty" xml:"image_tags,omitempty" type:"Repeated"`
  // location
  Location *string `json:"location,omitempty" xml:"location,omitempty"`
  // province
  Province *string `json:"province,omitempty" xml:"province,omitempty"`
  // time
  Time *string `json:"time,omitempty" xml:"time,omitempty"`
  // township
  Township *string `json:"township,omitempty" xml:"township,omitempty"`
  VideoMediaAudioStream []*VideoMediaAudioStream `json:"video_media_audio_stream,omitempty" xml:"video_media_audio_stream,omitempty" type:"Repeated"`
  VideoMediaVideoStream []*VideoMediaVideoStream `json:"video_media_video_stream,omitempty" xml:"video_media_video_stream,omitempty" type:"Repeated"`
  // width
  Width *int64 `json:"width,omitempty" xml:"width,omitempty"`
}

func (s VideoMediaResponse) String() string {
  return tea.Prettify(s)
}

func (s VideoMediaResponse) GoString() string {
  return s.String()
}

func (s *VideoMediaResponse) SetAddressLine(v string) *VideoMediaResponse {
  s.AddressLine = &v
  return s
}

func (s *VideoMediaResponse) SetCity(v string) *VideoMediaResponse {
  s.City = &v
  return s
}

func (s *VideoMediaResponse) SetCountry(v string) *VideoMediaResponse {
  s.Country = &v
  return s
}

func (s *VideoMediaResponse) SetDistrict(v string) *VideoMediaResponse {
  s.District = &v
  return s
}

func (s *VideoMediaResponse) SetDuration(v string) *VideoMediaResponse {
  s.Duration = &v
  return s
}

func (s *VideoMediaResponse) SetHeight(v int64) *VideoMediaResponse {
  s.Height = &v
  return s
}

func (s *VideoMediaResponse) SetImageTags(v []*SystemTag) *VideoMediaResponse {
  s.ImageTags = v
  return s
}

func (s *VideoMediaResponse) SetLocation(v string) *VideoMediaResponse {
  s.Location = &v
  return s
}

func (s *VideoMediaResponse) SetProvince(v string) *VideoMediaResponse {
  s.Province = &v
  return s
}

func (s *VideoMediaResponse) SetTime(v string) *VideoMediaResponse {
  s.Time = &v
  return s
}

func (s *VideoMediaResponse) SetTownship(v string) *VideoMediaResponse {
  s.Township = &v
  return s
}

func (s *VideoMediaResponse) SetVideoMediaAudioStream(v []*VideoMediaAudioStream) *VideoMediaResponse {
  s.VideoMediaAudioStream = v
  return s
}

func (s *VideoMediaResponse) SetVideoMediaVideoStream(v []*VideoMediaVideoStream) *VideoMediaResponse {
  s.VideoMediaVideoStream = v
  return s
}

func (s *VideoMediaResponse) SetWidth(v int64) *VideoMediaResponse {
  s.Width = &v
  return s
}

/**
 * 
 */
type VideoMediaVideoStream struct {
  // bitrate 视频比特率 单位：bps
  Bitrate *string `json:"bitrate,omitempty" xml:"bitrate,omitempty"`
  // clarity 清晰度（扫描）
  Clarity *string `json:"clarity,omitempty" xml:"clarity,omitempty"`
  // code_name 视频编码模式
  CodeName *string `json:"code_name,omitempty" xml:"code_name,omitempty"`
  // duration 单位 秒
  Duration *string `json:"duration,omitempty" xml:"duration,omitempty"`
  // fps 视频平均帧率
  Fps *string `json:"fps,omitempty" xml:"fps,omitempty"`
  // rotate 视频横屏 竖屏
  Rotate *string `json:"rotate,omitempty" xml:"rotate,omitempty"`
}

func (s VideoMediaVideoStream) String() string {
  return tea.Prettify(s)
}

func (s VideoMediaVideoStream) GoString() string {
  return s.String()
}

func (s *VideoMediaVideoStream) SetBitrate(v string) *VideoMediaVideoStream {
  s.Bitrate = &v
  return s
}

func (s *VideoMediaVideoStream) SetClarity(v string) *VideoMediaVideoStream {
  s.Clarity = &v
  return s
}

func (s *VideoMediaVideoStream) SetCodeName(v string) *VideoMediaVideoStream {
  s.CodeName = &v
  return s
}

func (s *VideoMediaVideoStream) SetDuration(v string) *VideoMediaVideoStream {
  s.Duration = &v
  return s
}

func (s *VideoMediaVideoStream) SetFps(v string) *VideoMediaVideoStream {
  s.Fps = &v
  return s
}

func (s *VideoMediaVideoStream) SetRotate(v string) *VideoMediaVideoStream {
  s.Rotate = &v
  return s
}

/**
 * 
 */
type VideoPreviewAudio struct {
  AudioBitrate *int64 `json:"audio_bitrate,omitempty" xml:"audio_bitrate,omitempty"`
  AudioChannel *int64 `json:"audio_channel,omitempty" xml:"audio_channel,omitempty"`
  AudioCodec *string `json:"audio_codec,omitempty" xml:"audio_codec,omitempty"`
  AudioSampleRate *int64 `json:"audio_sample_rate,omitempty" xml:"audio_sample_rate,omitempty"`
}

func (s VideoPreviewAudio) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewAudio) GoString() string {
  return s.String()
}

func (s *VideoPreviewAudio) SetAudioBitrate(v int64) *VideoPreviewAudio {
  s.AudioBitrate = &v
  return s
}

func (s *VideoPreviewAudio) SetAudioChannel(v int64) *VideoPreviewAudio {
  s.AudioChannel = &v
  return s
}

func (s *VideoPreviewAudio) SetAudioCodec(v string) *VideoPreviewAudio {
  s.AudioCodec = &v
  return s
}

func (s *VideoPreviewAudio) SetAudioSampleRate(v int64) *VideoPreviewAudio {
  s.AudioSampleRate = &v
  return s
}

/**
 * 
 */
type VideoPreviewAudioConfig struct {
  SupportExt []*string `json:"support_ext,omitempty" xml:"support_ext,omitempty" type:"Repeated"`
  Template []*VideoPreviewAudioTemplate `json:"template,omitempty" xml:"template,omitempty" type:"Repeated"`
}

func (s VideoPreviewAudioConfig) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewAudioConfig) GoString() string {
  return s.String()
}

func (s *VideoPreviewAudioConfig) SetSupportExt(v []*string) *VideoPreviewAudioConfig {
  s.SupportExt = v
  return s
}

func (s *VideoPreviewAudioConfig) SetTemplate(v []*VideoPreviewAudioTemplate) *VideoPreviewAudioConfig {
  s.Template = v
  return s
}

/**
 * 
 */
type VideoPreviewAudioMeta struct {
  // bitrate
  Bitrate *float64 `json:"bitrate,omitempty" xml:"bitrate,omitempty"`
  // channels
  Channels *int64 `json:"channels,omitempty" xml:"channels,omitempty"`
  // duration
  Duration *float64 `json:"duration,omitempty" xml:"duration,omitempty"`
  // sample_rate
  SampleRate *float64 `json:"sample_rate,omitempty" xml:"sample_rate,omitempty"`
}

func (s VideoPreviewAudioMeta) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewAudioMeta) GoString() string {
  return s.String()
}

func (s *VideoPreviewAudioMeta) SetBitrate(v float64) *VideoPreviewAudioMeta {
  s.Bitrate = &v
  return s
}

func (s *VideoPreviewAudioMeta) SetChannels(v int64) *VideoPreviewAudioMeta {
  s.Channels = &v
  return s
}

func (s *VideoPreviewAudioMeta) SetDuration(v float64) *VideoPreviewAudioMeta {
  s.Duration = &v
  return s
}

func (s *VideoPreviewAudioMeta) SetSampleRate(v float64) *VideoPreviewAudioMeta {
  s.SampleRate = &v
  return s
}

/**
 * 
 */
type VideoPreviewAudioMusicMeta struct {
  // album
  Album *string `json:"album,omitempty" xml:"album,omitempty"`
  // artist
  Artist *string `json:"artist,omitempty" xml:"artist,omitempty"`
  // cover_url
  CoverUrl *string `json:"cover_url,omitempty" xml:"cover_url,omitempty"`
  // title
  Title *string `json:"title,omitempty" xml:"title,omitempty"`
}

func (s VideoPreviewAudioMusicMeta) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewAudioMusicMeta) GoString() string {
  return s.String()
}

func (s *VideoPreviewAudioMusicMeta) SetAlbum(v string) *VideoPreviewAudioMusicMeta {
  s.Album = &v
  return s
}

func (s *VideoPreviewAudioMusicMeta) SetArtist(v string) *VideoPreviewAudioMusicMeta {
  s.Artist = &v
  return s
}

func (s *VideoPreviewAudioMusicMeta) SetCoverUrl(v string) *VideoPreviewAudioMusicMeta {
  s.CoverUrl = &v
  return s
}

func (s *VideoPreviewAudioMusicMeta) SetTitle(v string) *VideoPreviewAudioMusicMeta {
  s.Title = &v
  return s
}

/**
 * 
 */
type VideoPreviewAudioTemplate struct {
  AudioBitrate *int64 `json:"audio_bitrate,omitempty" xml:"audio_bitrate,omitempty"`
  AudioChannel *int64 `json:"audio_channel,omitempty" xml:"audio_channel,omitempty"`
  AudioCodec *string `json:"audio_codec,omitempty" xml:"audio_codec,omitempty"`
  AudioOutputExt *string `json:"audio_output_ext,omitempty" xml:"audio_output_ext,omitempty"`
  AudioSampleRate *int64 `json:"audio_sample_rate,omitempty" xml:"audio_sample_rate,omitempty"`
  AudioTemplateId *string `json:"audio_template_id,omitempty" xml:"audio_template_id,omitempty"`
}

func (s VideoPreviewAudioTemplate) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewAudioTemplate) GoString() string {
  return s.String()
}

func (s *VideoPreviewAudioTemplate) SetAudioBitrate(v int64) *VideoPreviewAudioTemplate {
  s.AudioBitrate = &v
  return s
}

func (s *VideoPreviewAudioTemplate) SetAudioChannel(v int64) *VideoPreviewAudioTemplate {
  s.AudioChannel = &v
  return s
}

func (s *VideoPreviewAudioTemplate) SetAudioCodec(v string) *VideoPreviewAudioTemplate {
  s.AudioCodec = &v
  return s
}

func (s *VideoPreviewAudioTemplate) SetAudioOutputExt(v string) *VideoPreviewAudioTemplate {
  s.AudioOutputExt = &v
  return s
}

func (s *VideoPreviewAudioTemplate) SetAudioSampleRate(v int64) *VideoPreviewAudioTemplate {
  s.AudioSampleRate = &v
  return s
}

func (s *VideoPreviewAudioTemplate) SetAudioTemplateId(v string) *VideoPreviewAudioTemplate {
  s.AudioTemplateId = &v
  return s
}

/**
 * 
 */
type VideoPreviewAutoScale struct {
  Enabled *bool `json:"enabled,omitempty" xml:"enabled,omitempty"`
  MaxLength *int64 `json:"max_length,omitempty" xml:"max_length,omitempty"`
}

func (s VideoPreviewAutoScale) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewAutoScale) GoString() string {
  return s.String()
}

func (s *VideoPreviewAutoScale) SetEnabled(v bool) *VideoPreviewAutoScale {
  s.Enabled = &v
  return s
}

func (s *VideoPreviewAutoScale) SetMaxLength(v int64) *VideoPreviewAutoScale {
  s.MaxLength = &v
  return s
}

/**
 * 
 */
type VideoPreviewBackupConfig struct {
  CountOnce *int64 `json:"count_once,omitempty" xml:"count_once,omitempty"`
  Store *Store `json:"store,omitempty" xml:"store,omitempty"`
  StoreIdMap map[string]interface{} `json:"store_id_map,omitempty" xml:"store_id_map,omitempty"`
}

func (s VideoPreviewBackupConfig) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewBackupConfig) GoString() string {
  return s.String()
}

func (s *VideoPreviewBackupConfig) SetCountOnce(v int64) *VideoPreviewBackupConfig {
  s.CountOnce = &v
  return s
}

func (s *VideoPreviewBackupConfig) SetStore(v *Store) *VideoPreviewBackupConfig {
  s.Store = v
  return s
}

func (s *VideoPreviewBackupConfig) SetStoreIdMap(v map[string]interface{}) *VideoPreviewBackupConfig {
  s.StoreIdMap = v
  return s
}

/**
 * 
 */
type VideoPreviewConfig struct {
  AudioConfig *VideoPreviewAudioConfig `json:"audio_config,omitempty" xml:"audio_config,omitempty"`
  AudioTemplateList []*string `json:"audio_template_list,omitempty" xml:"audio_template_list,omitempty" type:"Repeated"`
  AudioThumbnail *VideoPreviewThumbnail `json:"audio_thumbnail,omitempty" xml:"audio_thumbnail,omitempty"`
  BackupConfig *VideoPreviewBackupConfig `json:"backup_config,omitempty" xml:"backup_config,omitempty"`
  EnableConfig *VideoPreviewEnableConfig `json:"enable_config,omitempty" xml:"enable_config,omitempty"`
  Enabled *bool `json:"enabled,omitempty" xml:"enabled,omitempty"`
  LiveTranscodingConfig *VideoPreviewLiveTranscodingConfig `json:"live_transcoding_config,omitempty" xml:"live_transcoding_config,omitempty"`
  RateLimitConfig *VideoPreviewRateLimitConfig `json:"rate_limit_config,omitempty" xml:"rate_limit_config,omitempty"`
  Sprite *VideoPreviewSprite `json:"sprite,omitempty" xml:"sprite,omitempty"`
  Store *Store `json:"store,omitempty" xml:"store,omitempty"`
  StoreIdMap map[string]interface{} `json:"store_id_map,omitempty" xml:"store_id_map,omitempty"`
  TemplateList []*string `json:"template_list,omitempty" xml:"template_list,omitempty" type:"Repeated"`
  Thumbnail *VideoPreviewThumbnail `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  VideoConfig *VideoPreviewVideoConfig `json:"video_config,omitempty" xml:"video_config,omitempty"`
  VideoFilterConfig *VideoPreviewVideoFilterConfig `json:"video_filter_config,omitempty" xml:"video_filter_config,omitempty"`
}

func (s VideoPreviewConfig) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewConfig) GoString() string {
  return s.String()
}

func (s *VideoPreviewConfig) SetAudioConfig(v *VideoPreviewAudioConfig) *VideoPreviewConfig {
  s.AudioConfig = v
  return s
}

func (s *VideoPreviewConfig) SetAudioTemplateList(v []*string) *VideoPreviewConfig {
  s.AudioTemplateList = v
  return s
}

func (s *VideoPreviewConfig) SetAudioThumbnail(v *VideoPreviewThumbnail) *VideoPreviewConfig {
  s.AudioThumbnail = v
  return s
}

func (s *VideoPreviewConfig) SetBackupConfig(v *VideoPreviewBackupConfig) *VideoPreviewConfig {
  s.BackupConfig = v
  return s
}

func (s *VideoPreviewConfig) SetEnableConfig(v *VideoPreviewEnableConfig) *VideoPreviewConfig {
  s.EnableConfig = v
  return s
}

func (s *VideoPreviewConfig) SetEnabled(v bool) *VideoPreviewConfig {
  s.Enabled = &v
  return s
}

func (s *VideoPreviewConfig) SetLiveTranscodingConfig(v *VideoPreviewLiveTranscodingConfig) *VideoPreviewConfig {
  s.LiveTranscodingConfig = v
  return s
}

func (s *VideoPreviewConfig) SetRateLimitConfig(v *VideoPreviewRateLimitConfig) *VideoPreviewConfig {
  s.RateLimitConfig = v
  return s
}

func (s *VideoPreviewConfig) SetSprite(v *VideoPreviewSprite) *VideoPreviewConfig {
  s.Sprite = v
  return s
}

func (s *VideoPreviewConfig) SetStore(v *Store) *VideoPreviewConfig {
  s.Store = v
  return s
}

func (s *VideoPreviewConfig) SetStoreIdMap(v map[string]interface{}) *VideoPreviewConfig {
  s.StoreIdMap = v
  return s
}

func (s *VideoPreviewConfig) SetTemplateList(v []*string) *VideoPreviewConfig {
  s.TemplateList = v
  return s
}

func (s *VideoPreviewConfig) SetThumbnail(v *VideoPreviewThumbnail) *VideoPreviewConfig {
  s.Thumbnail = v
  return s
}

func (s *VideoPreviewConfig) SetVideoConfig(v *VideoPreviewVideoConfig) *VideoPreviewConfig {
  s.VideoConfig = v
  return s
}

func (s *VideoPreviewConfig) SetVideoFilterConfig(v *VideoPreviewVideoFilterConfig) *VideoPreviewConfig {
  s.VideoFilterConfig = v
  return s
}

/**
 * 
 */
type VideoPreviewEnableConfig struct {
  EnableTranscodeWhenPlay *bool `json:"enable_transcode_when_play,omitempty" xml:"enable_transcode_when_play,omitempty"`
  EnableTranscodeWhenUploaded *bool `json:"enable_transcode_when_uploaded,omitempty" xml:"enable_transcode_when_uploaded,omitempty"`
}

func (s VideoPreviewEnableConfig) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewEnableConfig) GoString() string {
  return s.String()
}

func (s *VideoPreviewEnableConfig) SetEnableTranscodeWhenPlay(v bool) *VideoPreviewEnableConfig {
  s.EnableTranscodeWhenPlay = &v
  return s
}

func (s *VideoPreviewEnableConfig) SetEnableTranscodeWhenUploaded(v bool) *VideoPreviewEnableConfig {
  s.EnableTranscodeWhenUploaded = &v
  return s
}

/**
 * domain config --------
 */
type VideoPreviewLiveTranscodingConfig struct {
  CurrentVersion *int64 `json:"current_version,omitempty" xml:"current_version,omitempty"`
  DeprecatedVersion *int64 `json:"deprecated_version,omitempty" xml:"deprecated_version,omitempty"`
  DetailCountLimit *int64 `json:"detail_count_limit,omitempty" xml:"detail_count_limit,omitempty"`
  Enabled *bool `json:"enabled,omitempty" xml:"enabled,omitempty"`
  ImmProjectMap map[string]interface{} `json:"imm_project_map,omitempty" xml:"imm_project_map,omitempty"`
  LeadingPrefix *string `json:"leading_prefix,omitempty" xml:"leading_prefix,omitempty"`
  M3u8FilePrefix *string `json:"m3u8_file_prefix,omitempty" xml:"m3u8_file_prefix,omitempty"`
  MediaDurationLimit *float64 `json:"media_duration_limit,omitempty" xml:"media_duration_limit,omitempty"`
  Segment *int64 `json:"segment,omitempty" xml:"segment,omitempty"`
  TemplateList []*string `json:"template_list,omitempty" xml:"template_list,omitempty" type:"Repeated"`
  // Mode              string   `json:"mode"`               // 默认media模式
  // 以下几个count需要根据task的status和stage来判断, 当前实时转码的状态
  TsCountWhenInitM3u8 *int64 `json:"ts_count_when_init_m3u8,omitempty" xml:"ts_count_when_init_m3u8,omitempty"`
  TsCountWhenTs404 *int64 `json:"ts_count_when_ts_404,omitempty" xml:"ts_count_when_ts_404,omitempty"`
  TsFilePrefix *string `json:"ts_file_prefix,omitempty" xml:"ts_file_prefix,omitempty"`
}

func (s VideoPreviewLiveTranscodingConfig) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewLiveTranscodingConfig) GoString() string {
  return s.String()
}

func (s *VideoPreviewLiveTranscodingConfig) SetCurrentVersion(v int64) *VideoPreviewLiveTranscodingConfig {
  s.CurrentVersion = &v
  return s
}

func (s *VideoPreviewLiveTranscodingConfig) SetDeprecatedVersion(v int64) *VideoPreviewLiveTranscodingConfig {
  s.DeprecatedVersion = &v
  return s
}

func (s *VideoPreviewLiveTranscodingConfig) SetDetailCountLimit(v int64) *VideoPreviewLiveTranscodingConfig {
  s.DetailCountLimit = &v
  return s
}

func (s *VideoPreviewLiveTranscodingConfig) SetEnabled(v bool) *VideoPreviewLiveTranscodingConfig {
  s.Enabled = &v
  return s
}

func (s *VideoPreviewLiveTranscodingConfig) SetImmProjectMap(v map[string]interface{}) *VideoPreviewLiveTranscodingConfig {
  s.ImmProjectMap = v
  return s
}

func (s *VideoPreviewLiveTranscodingConfig) SetLeadingPrefix(v string) *VideoPreviewLiveTranscodingConfig {
  s.LeadingPrefix = &v
  return s
}

func (s *VideoPreviewLiveTranscodingConfig) SetM3u8FilePrefix(v string) *VideoPreviewLiveTranscodingConfig {
  s.M3u8FilePrefix = &v
  return s
}

func (s *VideoPreviewLiveTranscodingConfig) SetMediaDurationLimit(v float64) *VideoPreviewLiveTranscodingConfig {
  s.MediaDurationLimit = &v
  return s
}

func (s *VideoPreviewLiveTranscodingConfig) SetSegment(v int64) *VideoPreviewLiveTranscodingConfig {
  s.Segment = &v
  return s
}

func (s *VideoPreviewLiveTranscodingConfig) SetTemplateList(v []*string) *VideoPreviewLiveTranscodingConfig {
  s.TemplateList = v
  return s
}

func (s *VideoPreviewLiveTranscodingConfig) SetTsCountWhenInitM3u8(v int64) *VideoPreviewLiveTranscodingConfig {
  s.TsCountWhenInitM3u8 = &v
  return s
}

func (s *VideoPreviewLiveTranscodingConfig) SetTsCountWhenTs404(v int64) *VideoPreviewLiveTranscodingConfig {
  s.TsCountWhenTs404 = &v
  return s
}

func (s *VideoPreviewLiveTranscodingConfig) SetTsFilePrefix(v string) *VideoPreviewLiveTranscodingConfig {
  s.TsFilePrefix = &v
  return s
}

/**
 * 
 */
type VideoPreviewM3U8Config struct {
  HlsTime *int64 `json:"hls_time,omitempty" xml:"hls_time,omitempty"`
}

func (s VideoPreviewM3U8Config) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewM3U8Config) GoString() string {
  return s.String()
}

func (s *VideoPreviewM3U8Config) SetHlsTime(v int64) *VideoPreviewM3U8Config {
  s.HlsTime = &v
  return s
}

/**
 * 获取转码信息meta响应
 */
type VideoPreviewPlayInfoMetaResponse struct {
  // duration
  Duration *float64 `json:"duration,omitempty" xml:"duration,omitempty"`
  // height
  Height *int64 `json:"height,omitempty" xml:"height,omitempty"`
  // witdh
  Width *int64 `json:"width,omitempty" xml:"width,omitempty"`
}

func (s VideoPreviewPlayInfoMetaResponse) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewPlayInfoMetaResponse) GoString() string {
  return s.String()
}

func (s *VideoPreviewPlayInfoMetaResponse) SetDuration(v float64) *VideoPreviewPlayInfoMetaResponse {
  s.Duration = &v
  return s
}

func (s *VideoPreviewPlayInfoMetaResponse) SetHeight(v int64) *VideoPreviewPlayInfoMetaResponse {
  s.Height = &v
  return s
}

func (s *VideoPreviewPlayInfoMetaResponse) SetWidth(v int64) *VideoPreviewPlayInfoMetaResponse {
  s.Width = &v
  return s
}

/**
 * 转码信息响应
 */
type VideoPreviewPlayInfoResponse struct {
  // category
  Category *string `json:"category,omitempty" xml:"category,omitempty"`
  LiveTranscodingTaskList []*LiveTranscodingTaskResponse `json:"live_transcoding_task_list,omitempty" xml:"live_transcoding_task_list,omitempty" type:"Repeated"`
  Meta *VideoPreviewPlayInfoMetaResponse `json:"meta,omitempty" xml:"meta,omitempty"`
}

func (s VideoPreviewPlayInfoResponse) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewPlayInfoResponse) GoString() string {
  return s.String()
}

func (s *VideoPreviewPlayInfoResponse) SetCategory(v string) *VideoPreviewPlayInfoResponse {
  s.Category = &v
  return s
}

func (s *VideoPreviewPlayInfoResponse) SetLiveTranscodingTaskList(v []*LiveTranscodingTaskResponse) *VideoPreviewPlayInfoResponse {
  s.LiveTranscodingTaskList = v
  return s
}

func (s *VideoPreviewPlayInfoResponse) SetMeta(v *VideoPreviewPlayInfoMetaResponse) *VideoPreviewPlayInfoResponse {
  s.Meta = v
  return s
}

/**
 * 
 */
type VideoPreviewRateLimitConfig struct {
  RateLimit *int64 `json:"rate_limit,omitempty" xml:"rate_limit,omitempty"`
}

func (s VideoPreviewRateLimitConfig) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewRateLimitConfig) GoString() string {
  return s.String()
}

func (s *VideoPreviewRateLimitConfig) SetRateLimit(v int64) *VideoPreviewRateLimitConfig {
  s.RateLimit = &v
  return s
}

/**
 * 
 */
type VideoPreviewResponse struct {
  // audio_channels
  AudioChannels *int64 `json:"audio_channels,omitempty" xml:"audio_channels,omitempty"`
  // audio_format
  AudioFormat *string `json:"audio_format,omitempty" xml:"audio_format,omitempty"`
  AudioMeta *VideoPreviewAudioMeta `json:"audio_meta,omitempty" xml:"audio_meta,omitempty"`
  AudioMusicMeta *VideoPreviewAudioMusicMeta `json:"audio_music_meta,omitempty" xml:"audio_music_meta,omitempty"`
  // audio_sample_rate
  AudioSampleRate *string `json:"audio_sample_rate,omitempty" xml:"audio_sample_rate,omitempty"`
  // audio_template_list
  AudioTemplateList []*VideoPreviewTranscode `json:"audio_template_list,omitempty" xml:"audio_template_list,omitempty" type:"Repeated"`
  // bitrate
  Bitrate *string `json:"bitrate,omitempty" xml:"bitrate,omitempty"`
  // duration
  Duration *string `json:"duration,omitempty" xml:"duration,omitempty"`
  // frame_rate
  FrameRate *string `json:"frame_rate,omitempty" xml:"frame_rate,omitempty"`
  // height
  Height *int64 `json:"height,omitempty" xml:"height,omitempty"`
  SpriteInfo *VideoPreviewSprite `json:"sprite_info,omitempty" xml:"sprite_info,omitempty"`
  // template_list
  TemplateList []*VideoPreviewTranscode `json:"template_list,omitempty" xml:"template_list,omitempty" type:"Repeated"`
  // thumbnail
  Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
  // video_format
  VideoFormat *string `json:"video_format,omitempty" xml:"video_format,omitempty"`
  // width
  Width *int64 `json:"width,omitempty" xml:"width,omitempty"`
}

func (s VideoPreviewResponse) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewResponse) GoString() string {
  return s.String()
}

func (s *VideoPreviewResponse) SetAudioChannels(v int64) *VideoPreviewResponse {
  s.AudioChannels = &v
  return s
}

func (s *VideoPreviewResponse) SetAudioFormat(v string) *VideoPreviewResponse {
  s.AudioFormat = &v
  return s
}

func (s *VideoPreviewResponse) SetAudioMeta(v *VideoPreviewAudioMeta) *VideoPreviewResponse {
  s.AudioMeta = v
  return s
}

func (s *VideoPreviewResponse) SetAudioMusicMeta(v *VideoPreviewAudioMusicMeta) *VideoPreviewResponse {
  s.AudioMusicMeta = v
  return s
}

func (s *VideoPreviewResponse) SetAudioSampleRate(v string) *VideoPreviewResponse {
  s.AudioSampleRate = &v
  return s
}

func (s *VideoPreviewResponse) SetAudioTemplateList(v []*VideoPreviewTranscode) *VideoPreviewResponse {
  s.AudioTemplateList = v
  return s
}

func (s *VideoPreviewResponse) SetBitrate(v string) *VideoPreviewResponse {
  s.Bitrate = &v
  return s
}

func (s *VideoPreviewResponse) SetDuration(v string) *VideoPreviewResponse {
  s.Duration = &v
  return s
}

func (s *VideoPreviewResponse) SetFrameRate(v string) *VideoPreviewResponse {
  s.FrameRate = &v
  return s
}

func (s *VideoPreviewResponse) SetHeight(v int64) *VideoPreviewResponse {
  s.Height = &v
  return s
}

func (s *VideoPreviewResponse) SetSpriteInfo(v *VideoPreviewSprite) *VideoPreviewResponse {
  s.SpriteInfo = v
  return s
}

func (s *VideoPreviewResponse) SetTemplateList(v []*VideoPreviewTranscode) *VideoPreviewResponse {
  s.TemplateList = v
  return s
}

func (s *VideoPreviewResponse) SetThumbnail(v string) *VideoPreviewResponse {
  s.Thumbnail = &v
  return s
}

func (s *VideoPreviewResponse) SetVideoFormat(v string) *VideoPreviewResponse {
  s.VideoFormat = &v
  return s
}

func (s *VideoPreviewResponse) SetWidth(v int64) *VideoPreviewResponse {
  s.Width = &v
  return s
}

/**
 * 
 */
type VideoPreviewSprite struct {
  AutoScale *VideoPreviewAutoScale `json:"auto_scale,omitempty" xml:"auto_scale,omitempty"`
  // col
  Col *int64 `json:"col,omitempty" xml:"col,omitempty"`
  // frame_height
  FrameHeight *int64 `json:"frame_height,omitempty" xml:"frame_height,omitempty"`
  // frame_width
  FrameWidth *int64 `json:"frame_width,omitempty" xml:"frame_width,omitempty"`
  Interval *VideoPreviewSpriteInterval `json:"interval,omitempty" xml:"interval,omitempty"`
  // row
  Row *int64 `json:"row,omitempty" xml:"row,omitempty"`
}

func (s VideoPreviewSprite) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewSprite) GoString() string {
  return s.String()
}

func (s *VideoPreviewSprite) SetAutoScale(v *VideoPreviewAutoScale) *VideoPreviewSprite {
  s.AutoScale = v
  return s
}

func (s *VideoPreviewSprite) SetCol(v int64) *VideoPreviewSprite {
  s.Col = &v
  return s
}

func (s *VideoPreviewSprite) SetFrameHeight(v int64) *VideoPreviewSprite {
  s.FrameHeight = &v
  return s
}

func (s *VideoPreviewSprite) SetFrameWidth(v int64) *VideoPreviewSprite {
  s.FrameWidth = &v
  return s
}

func (s *VideoPreviewSprite) SetInterval(v *VideoPreviewSpriteInterval) *VideoPreviewSprite {
  s.Interval = v
  return s
}

func (s *VideoPreviewSprite) SetRow(v int64) *VideoPreviewSprite {
  s.Row = &v
  return s
}

/**
 * 雪碧图抓图间隔配置。如果配置异常，默认以1%抓图
 */
type VideoPreviewSpriteInterval struct {
  DefaultInterval *string `json:"default_interval,omitempty" xml:"default_interval,omitempty"`
  GrabIntervalList []*string `json:"grab_interval_list,omitempty" xml:"grab_interval_list,omitempty" type:"Repeated"`
  UpperLimitList []*int `json:"upper_limit_list,omitempty" xml:"upper_limit_list,omitempty" type:"Repeated"`
}

func (s VideoPreviewSpriteInterval) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewSpriteInterval) GoString() string {
  return s.String()
}

func (s *VideoPreviewSpriteInterval) SetDefaultInterval(v string) *VideoPreviewSpriteInterval {
  s.DefaultInterval = &v
  return s
}

func (s *VideoPreviewSpriteInterval) SetGrabIntervalList(v []*string) *VideoPreviewSpriteInterval {
  s.GrabIntervalList = v
  return s
}

func (s *VideoPreviewSpriteInterval) SetUpperLimitList(v []*int) *VideoPreviewSpriteInterval {
  s.UpperLimitList = v
  return s
}

/**
 * 
 */
type VideoPreviewThumbnail struct {
  SkipBeginPercent *string `json:"skip_begin_percent,omitempty" xml:"skip_begin_percent,omitempty"`
  SkipBeginSec *float64 `json:"skip_begin_sec,omitempty" xml:"skip_begin_sec,omitempty"`
}

func (s VideoPreviewThumbnail) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewThumbnail) GoString() string {
  return s.String()
}

func (s *VideoPreviewThumbnail) SetSkipBeginPercent(v string) *VideoPreviewThumbnail {
  s.SkipBeginPercent = &v
  return s
}

func (s *VideoPreviewThumbnail) SetSkipBeginSec(v float64) *VideoPreviewThumbnail {
  s.SkipBeginSec = &v
  return s
}

/**
 * 
 */
type VideoPreviewTranscode struct {
  // status
  Status *string `json:"status,omitempty" xml:"status,omitempty"`
  // template_id
  TemplateId *string `json:"template_id,omitempty" xml:"template_id,omitempty"`
}

func (s VideoPreviewTranscode) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewTranscode) GoString() string {
  return s.String()
}

func (s *VideoPreviewTranscode) SetStatus(v string) *VideoPreviewTranscode {
  s.Status = &v
  return s
}

func (s *VideoPreviewTranscode) SetTemplateId(v string) *VideoPreviewTranscode {
  s.TemplateId = &v
  return s
}

/**
 * 
 */
type VideoPreviewVideo struct {
  Height *int64 `json:"height,omitempty" xml:"height,omitempty"`
  KeepOriginal *bool `json:"keep_original,omitempty" xml:"keep_original,omitempty"`
  VideoBitrate *int64 `json:"video_bitrate,omitempty" xml:"video_bitrate,omitempty"`
  VideoCodec *string `json:"video_codec,omitempty" xml:"video_codec,omitempty"`
  VideoFrameRate *int64 `json:"video_frame_rate,omitempty" xml:"video_frame_rate,omitempty"`
  Width *int64 `json:"width,omitempty" xml:"width,omitempty"`
}

func (s VideoPreviewVideo) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewVideo) GoString() string {
  return s.String()
}

func (s *VideoPreviewVideo) SetHeight(v int64) *VideoPreviewVideo {
  s.Height = &v
  return s
}

func (s *VideoPreviewVideo) SetKeepOriginal(v bool) *VideoPreviewVideo {
  s.KeepOriginal = &v
  return s
}

func (s *VideoPreviewVideo) SetVideoBitrate(v int64) *VideoPreviewVideo {
  s.VideoBitrate = &v
  return s
}

func (s *VideoPreviewVideo) SetVideoCodec(v string) *VideoPreviewVideo {
  s.VideoCodec = &v
  return s
}

func (s *VideoPreviewVideo) SetVideoFrameRate(v int64) *VideoPreviewVideo {
  s.VideoFrameRate = &v
  return s
}

func (s *VideoPreviewVideo) SetWidth(v int64) *VideoPreviewVideo {
  s.Width = &v
  return s
}

/**
 * 
 */
type VideoPreviewVideoConfig struct {
  DefaultOutputExt *string `json:"default_output_ext,omitempty" xml:"default_output_ext,omitempty"`
  KeepOriginal *bool `json:"keep_original,omitempty" xml:"keep_original,omitempty"`
  M3u8Config *VideoPreviewM3U8Config `json:"m3u8_config,omitempty" xml:"m3u8_config,omitempty"`
  SupportExt []*string `json:"support_ext,omitempty" xml:"support_ext,omitempty" type:"Repeated"`
  Template []*VideoPreviewVideoTemplate `json:"template,omitempty" xml:"template,omitempty" type:"Repeated"`
}

func (s VideoPreviewVideoConfig) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewVideoConfig) GoString() string {
  return s.String()
}

func (s *VideoPreviewVideoConfig) SetDefaultOutputExt(v string) *VideoPreviewVideoConfig {
  s.DefaultOutputExt = &v
  return s
}

func (s *VideoPreviewVideoConfig) SetKeepOriginal(v bool) *VideoPreviewVideoConfig {
  s.KeepOriginal = &v
  return s
}

func (s *VideoPreviewVideoConfig) SetM3u8Config(v *VideoPreviewM3U8Config) *VideoPreviewVideoConfig {
  s.M3u8Config = v
  return s
}

func (s *VideoPreviewVideoConfig) SetSupportExt(v []*string) *VideoPreviewVideoConfig {
  s.SupportExt = v
  return s
}

func (s *VideoPreviewVideoConfig) SetTemplate(v []*VideoPreviewVideoTemplate) *VideoPreviewVideoConfig {
  s.Template = v
  return s
}

/**
 * 同时满足以下所有null条件，则不触发转码。如果没有配置任何条件，那么不触发过滤
 */
type VideoPreviewVideoFilterConfig struct {
  AudioBitrate *int64 `json:"audio_bitrate,omitempty" xml:"audio_bitrate,omitempty"`
  AudioChannel *int64 `json:"audio_channel,omitempty" xml:"audio_channel,omitempty"`
  // 音频信息过滤
  AudioCodecList []*string `json:"audio_codec_list,omitempty" xml:"audio_codec_list,omitempty" type:"Repeated"`
  AudioSampleRate *int64 `json:"audio_sample_rate,omitempty" xml:"audio_sample_rate,omitempty"`
  Bitrate *int64 `json:"bitrate,omitempty" xml:"bitrate,omitempty"`
  // 综合信息过滤
  Duration *int64 `json:"duration,omitempty" xml:"duration,omitempty"`
  Height *int64 `json:"height,omitempty" xml:"height,omitempty"`
  Pixel *int64 `json:"pixel,omitempty" xml:"pixel,omitempty"`
  Size *int64 `json:"size,omitempty" xml:"size,omitempty"`
  VideoBitrate *int64 `json:"video_bitrate,omitempty" xml:"video_bitrate,omitempty"`
  // 视频信息过滤
  VideoCodecList []*string `json:"video_codec_list,omitempty" xml:"video_codec_list,omitempty" type:"Repeated"`
  VideoFrameRate *int64 `json:"video_frame_rate,omitempty" xml:"video_frame_rate,omitempty"`
  Width *int64 `json:"width,omitempty" xml:"width,omitempty"`
}

func (s VideoPreviewVideoFilterConfig) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewVideoFilterConfig) GoString() string {
  return s.String()
}

func (s *VideoPreviewVideoFilterConfig) SetAudioBitrate(v int64) *VideoPreviewVideoFilterConfig {
  s.AudioBitrate = &v
  return s
}

func (s *VideoPreviewVideoFilterConfig) SetAudioChannel(v int64) *VideoPreviewVideoFilterConfig {
  s.AudioChannel = &v
  return s
}

func (s *VideoPreviewVideoFilterConfig) SetAudioCodecList(v []*string) *VideoPreviewVideoFilterConfig {
  s.AudioCodecList = v
  return s
}

func (s *VideoPreviewVideoFilterConfig) SetAudioSampleRate(v int64) *VideoPreviewVideoFilterConfig {
  s.AudioSampleRate = &v
  return s
}

func (s *VideoPreviewVideoFilterConfig) SetBitrate(v int64) *VideoPreviewVideoFilterConfig {
  s.Bitrate = &v
  return s
}

func (s *VideoPreviewVideoFilterConfig) SetDuration(v int64) *VideoPreviewVideoFilterConfig {
  s.Duration = &v
  return s
}

func (s *VideoPreviewVideoFilterConfig) SetHeight(v int64) *VideoPreviewVideoFilterConfig {
  s.Height = &v
  return s
}

func (s *VideoPreviewVideoFilterConfig) SetPixel(v int64) *VideoPreviewVideoFilterConfig {
  s.Pixel = &v
  return s
}

func (s *VideoPreviewVideoFilterConfig) SetSize(v int64) *VideoPreviewVideoFilterConfig {
  s.Size = &v
  return s
}

func (s *VideoPreviewVideoFilterConfig) SetVideoBitrate(v int64) *VideoPreviewVideoFilterConfig {
  s.VideoBitrate = &v
  return s
}

func (s *VideoPreviewVideoFilterConfig) SetVideoCodecList(v []*string) *VideoPreviewVideoFilterConfig {
  s.VideoCodecList = v
  return s
}

func (s *VideoPreviewVideoFilterConfig) SetVideoFrameRate(v int64) *VideoPreviewVideoFilterConfig {
  s.VideoFrameRate = &v
  return s
}

func (s *VideoPreviewVideoFilterConfig) SetWidth(v int64) *VideoPreviewVideoFilterConfig {
  s.Width = &v
  return s
}

/**
 * 
 */
type VideoPreviewVideoTemplate struct {
  AudioBitrate *int64 `json:"audio_bitrate,omitempty" xml:"audio_bitrate,omitempty"`
  AudioChannel *int64 `json:"audio_channel,omitempty" xml:"audio_channel,omitempty"`
  AudioCodec *string `json:"audio_codec,omitempty" xml:"audio_codec,omitempty"`
  AudioSampleRate *int64 `json:"audio_sample_rate,omitempty" xml:"audio_sample_rate,omitempty"`
  Height *int64 `json:"height,omitempty" xml:"height,omitempty"`
  KeepOriginal *bool `json:"keep_original,omitempty" xml:"keep_original,omitempty"`
  VideoBitrate *int64 `json:"video_bitrate,omitempty" xml:"video_bitrate,omitempty"`
  VideoCodec *string `json:"video_codec,omitempty" xml:"video_codec,omitempty"`
  VideoFrameRate *int64 `json:"video_frame_rate,omitempty" xml:"video_frame_rate,omitempty"`
  VideoOutputExt *string `json:"video_output_ext,omitempty" xml:"video_output_ext,omitempty"`
  VideoTemplateId *string `json:"video_template_id,omitempty" xml:"video_template_id,omitempty"`
  Width *int64 `json:"width,omitempty" xml:"width,omitempty"`
}

func (s VideoPreviewVideoTemplate) String() string {
  return tea.Prettify(s)
}

func (s VideoPreviewVideoTemplate) GoString() string {
  return s.String()
}

func (s *VideoPreviewVideoTemplate) SetAudioBitrate(v int64) *VideoPreviewVideoTemplate {
  s.AudioBitrate = &v
  return s
}

func (s *VideoPreviewVideoTemplate) SetAudioChannel(v int64) *VideoPreviewVideoTemplate {
  s.AudioChannel = &v
  return s
}

func (s *VideoPreviewVideoTemplate) SetAudioCodec(v string) *VideoPreviewVideoTemplate {
  s.AudioCodec = &v
  return s
}

func (s *VideoPreviewVideoTemplate) SetAudioSampleRate(v int64) *VideoPreviewVideoTemplate {
  s.AudioSampleRate = &v
  return s
}

func (s *VideoPreviewVideoTemplate) SetHeight(v int64) *VideoPreviewVideoTemplate {
  s.Height = &v
  return s
}

func (s *VideoPreviewVideoTemplate) SetKeepOriginal(v bool) *VideoPreviewVideoTemplate {
  s.KeepOriginal = &v
  return s
}

func (s *VideoPreviewVideoTemplate) SetVideoBitrate(v int64) *VideoPreviewVideoTemplate {
  s.VideoBitrate = &v
  return s
}

func (s *VideoPreviewVideoTemplate) SetVideoCodec(v string) *VideoPreviewVideoTemplate {
  s.VideoCodec = &v
  return s
}

func (s *VideoPreviewVideoTemplate) SetVideoFrameRate(v int64) *VideoPreviewVideoTemplate {
  s.VideoFrameRate = &v
  return s
}

func (s *VideoPreviewVideoTemplate) SetVideoOutputExt(v string) *VideoPreviewVideoTemplate {
  s.VideoOutputExt = &v
  return s
}

func (s *VideoPreviewVideoTemplate) SetVideoTemplateId(v string) *VideoPreviewVideoTemplate {
  s.VideoTemplateId = &v
  return s
}

func (s *VideoPreviewVideoTemplate) SetWidth(v int64) *VideoPreviewVideoTemplate {
  s.Width = &v
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
 * 列举实体的权益
 * @tags benefit
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListIdentityBenefitPkgEx(request *ListIdentityBenefitPkgRequest, runtime *RuntimeOptions) (_result *ListIdentityBenefitPkgModel, _err error) {
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

  _resp := &ListIdentityBenefitPkgModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*ListIdentityBenefitPkgModel, error){
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
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/benefit/list_identity_benefit_pkg"))
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
        _result = &ListIdentityBenefitPkgModel{}
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
 * 搜索domain
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SearchEx(request *SearchDomainsRequest, runtime *RuntimeOptions) (_result *SearchModel, _err error) {
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

  _resp := &SearchModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*SearchModel, error){
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
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/search"))
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
        _result = &SearchModel{}
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
 * 分享功能开关
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetShareLinkStatusEx(request *SetShareLinkStatusRequest, runtime *RuntimeOptions) (_result *SetShareLinkStatusModel, _err error) {
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

  _resp := &SetShareLinkStatusModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*SetShareLinkStatusModel, error){
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
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/set_share_link_status"))
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
        _result = &SetShareLinkStatusModel{}
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
 * 共享功能开关
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetShareStatusEx(request *SetShareStatusRequest, runtime *RuntimeOptions) (_result *SetShareStatusModel, _err error) {
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

  _resp := &SetShareStatusModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*SetShareStatusModel, error){
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
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/set_share_status"))
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
        _result = &SetShareStatusModel{}
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
 * 修改domain的名称
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) UpdateNameEx(request *DomainUpdateNameRequest, runtime *RuntimeOptions) (_result *UpdateNameModel, _err error) {
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

  _resp := &UpdateNameModel{}
  for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
    if _retryTimes > 0 {
      _backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
      if tea.IntValue(_backoffTime) > 0 {
        tea.Sleep(_backoffTime)
      }
    }

    _resp, _err = func()(*UpdateNameModel, error){
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
      request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/update_name"))
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
        _result = &UpdateNameModel{}
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
 * 列举实体的权益
 * @tags benefit
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListIdentityBenefitPkg (request *ListIdentityBenefitPkgRequest) (_result *ListIdentityBenefitPkgModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &ListIdentityBenefitPkgModel{}
  _body, _err := client.ListIdentityBenefitPkgEx(request, runtime)
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
 * 搜索domain
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) Search (request *SearchDomainsRequest) (_result *SearchModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &SearchModel{}
  _body, _err := client.SearchEx(request, runtime)
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
 * 分享功能开关
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetShareLinkStatus (request *SetShareLinkStatusRequest) (_result *SetShareLinkStatusModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &SetShareLinkStatusModel{}
  _body, _err := client.SetShareLinkStatusEx(request, runtime)
  if _err != nil {
    return _result, _err
  }
  _result = _body
  return _result, _err
}

/**
 * 共享功能开关
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetShareStatus (request *SetShareStatusRequest) (_result *SetShareStatusModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &SetShareStatusModel{}
  _body, _err := client.SetShareStatusEx(request, runtime)
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

/**
 * 修改domain的名称
 * @tags domain
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) UpdateName (request *DomainUpdateNameRequest) (_result *UpdateNameModel, _err error) {
  runtime := &RuntimeOptions{}
  _result = &UpdateNameModel{}
  _body, _err := client.UpdateNameEx(request, runtime)
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

