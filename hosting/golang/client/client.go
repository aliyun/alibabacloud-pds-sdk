// This file is auto-generated, don't edit it. Thanks.
/**
 *
 */
package client

import (
	accesstokencredential "github.com/alibabacloud-go/pds-credentials/service"
	roautil "github.com/alibabacloud-go/tea-roa-utils/service"
	util "github.com/alibabacloud-go/tea-utils/service"
	"github.com/alibabacloud-go/tea/tea"
	credential "github.com/aliyun/credentials-go/credentials"
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
	Endpoint        *string `json:"endpoint,omitempty" xml:"endpoint,omitempty"`
	DomainId        *string `json:"domainId,omitempty" xml:"domainId,omitempty" pattern:"^[a-zA-Z0-9_-]+$"`
	ClientId        *string `json:"clientId,omitempty" xml:"clientId,omitempty"`
	RefreshToken    *string `json:"refreshToken,omitempty" xml:"refreshToken,omitempty"`
	ClientSecret    *string `json:"clientSecret,omitempty" xml:"clientSecret,omitempty"`
	AccessToken     *string `json:"accessToken,omitempty" xml:"accessToken,omitempty"`
	ExpireTime      *string `json:"expireTime,omitempty" xml:"expireTime,omitempty"`
	Protocol        *string `json:"protocol,omitempty" xml:"protocol,omitempty"`
	Type            *string `json:"type,omitempty" xml:"type,omitempty"`
	SecurityToken   *string `json:"securityToken,omitempty" xml:"securityToken,omitempty"`
	AccessKeyId     *string `json:"accessKeyId,omitempty" xml:"accessKeyId,omitempty"`
	AccessKeySecret *string `json:"accessKeySecret,omitempty" xml:"accessKeySecret,omitempty"`
	Nickname        *string `json:"nickname,omitempty" xml:"nickname,omitempty"`
	UserAgent       *string `json:"userAgent,omitempty" xml:"userAgent,omitempty"`
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

func (s *Config) SetDomainId(v string) *Config {
	s.DomainId = &v
	return s
}

func (s *Config) SetClientId(v string) *Config {
	s.ClientId = &v
	return s
}

func (s *Config) SetRefreshToken(v string) *Config {
	s.RefreshToken = &v
	return s
}

func (s *Config) SetClientSecret(v string) *Config {
	s.ClientSecret = &v
	return s
}

func (s *Config) SetAccessToken(v string) *Config {
	s.AccessToken = &v
	return s
}

func (s *Config) SetExpireTime(v string) *Config {
	s.ExpireTime = &v
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

type CancelLinkModel struct {
	Headers map[string]*string          `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *AccountAccessTokenResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s CancelLinkModel) String() string {
	return tea.Prettify(s)
}

func (s CancelLinkModel) GoString() string {
	return s.String()
}

func (s *CancelLinkModel) SetHeaders(v map[string]*string) *CancelLinkModel {
	s.Headers = v
	return s
}

func (s *CancelLinkModel) SetBody(v *AccountAccessTokenResponse) *CancelLinkModel {
	s.Body = v
	return s
}

type ConfirmLinkModel struct {
	Headers map[string]*string          `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *AccountAccessTokenResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ConfirmLinkModel) String() string {
	return tea.Prettify(s)
}

func (s ConfirmLinkModel) GoString() string {
	return s.String()
}

func (s *ConfirmLinkModel) SetHeaders(v map[string]*string) *ConfirmLinkModel {
	s.Headers = v
	return s
}

func (s *ConfirmLinkModel) SetBody(v *AccountAccessTokenResponse) *ConfirmLinkModel {
	s.Body = v
	return s
}

type ChangePasswordModel struct {
	Headers map[string]*string          `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *AccountAccessTokenResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ChangePasswordModel) String() string {
	return tea.Prettify(s)
}

func (s ChangePasswordModel) GoString() string {
	return s.String()
}

func (s *ChangePasswordModel) SetHeaders(v map[string]*string) *ChangePasswordModel {
	s.Headers = v
	return s
}

func (s *ChangePasswordModel) SetBody(v *AccountAccessTokenResponse) *ChangePasswordModel {
	s.Body = v
	return s
}

type SetPasswordModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s SetPasswordModel) String() string {
	return tea.Prettify(s)
}

func (s SetPasswordModel) GoString() string {
	return s.String()
}

func (s *SetPasswordModel) SetHeaders(v map[string]*string) *SetPasswordModel {
	s.Headers = v
	return s
}

type VerifyCodeModel struct {
	Headers map[string]*string  `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *VerifyCodeResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s VerifyCodeModel) String() string {
	return tea.Prettify(s)
}

func (s VerifyCodeModel) GoString() string {
	return s.String()
}

func (s *VerifyCodeModel) SetHeaders(v map[string]*string) *VerifyCodeModel {
	s.Headers = v
	return s
}

func (s *VerifyCodeModel) SetBody(v *VerifyCodeResponse) *VerifyCodeModel {
	s.Body = v
	return s
}

type GetAccessTokenByLinkInfoModel struct {
	Headers map[string]*string          `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *AccountAccessTokenResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetAccessTokenByLinkInfoModel) String() string {
	return tea.Prettify(s)
}

func (s GetAccessTokenByLinkInfoModel) GoString() string {
	return s.String()
}

func (s *GetAccessTokenByLinkInfoModel) SetHeaders(v map[string]*string) *GetAccessTokenByLinkInfoModel {
	s.Headers = v
	return s
}

func (s *GetAccessTokenByLinkInfoModel) SetBody(v *AccountAccessTokenResponse) *GetAccessTokenByLinkInfoModel {
	s.Body = v
	return s
}

type GetCaptchaModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *Captcha           `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetCaptchaModel) String() string {
	return tea.Prettify(s)
}

func (s GetCaptchaModel) GoString() string {
	return s.String()
}

func (s *GetCaptchaModel) SetHeaders(v map[string]*string) *GetCaptchaModel {
	s.Headers = v
	return s
}

func (s *GetCaptchaModel) SetBody(v *Captcha) *GetCaptchaModel {
	s.Body = v
	return s
}

type GetLinkInfoModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *LinkInfoResponse  `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetLinkInfoModel) String() string {
	return tea.Prettify(s)
}

func (s GetLinkInfoModel) GoString() string {
	return s.String()
}

func (s *GetLinkInfoModel) SetHeaders(v map[string]*string) *GetLinkInfoModel {
	s.Headers = v
	return s
}

func (s *GetLinkInfoModel) SetBody(v *LinkInfoResponse) *GetLinkInfoModel {
	s.Body = v
	return s
}

type GetLinkInfoByUserIdModel struct {
	Headers map[string]*string    `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *LinkInfoListResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetLinkInfoByUserIdModel) String() string {
	return tea.Prettify(s)
}

func (s GetLinkInfoByUserIdModel) GoString() string {
	return s.String()
}

func (s *GetLinkInfoByUserIdModel) SetHeaders(v map[string]*string) *GetLinkInfoByUserIdModel {
	s.Headers = v
	return s
}

func (s *GetLinkInfoByUserIdModel) SetBody(v *LinkInfoListResponse) *GetLinkInfoByUserIdModel {
	s.Body = v
	return s
}

type GetPublicKeyModel struct {
	Headers map[string]*string       `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *GetAppPublicKeyResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
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

type LinkModel struct {
	Headers map[string]*string          `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *AccountAccessTokenResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s LinkModel) String() string {
	return tea.Prettify(s)
}

func (s LinkModel) GoString() string {
	return s.String()
}

func (s *LinkModel) SetHeaders(v map[string]*string) *LinkModel {
	s.Headers = v
	return s
}

func (s *LinkModel) SetBody(v *AccountAccessTokenResponse) *LinkModel {
	s.Body = v
	return s
}

type CheckExistModel struct {
	Headers map[string]*string        `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *MobileCheckExistResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s CheckExistModel) String() string {
	return tea.Prettify(s)
}

func (s CheckExistModel) GoString() string {
	return s.String()
}

func (s *CheckExistModel) SetHeaders(v map[string]*string) *CheckExistModel {
	s.Headers = v
	return s
}

func (s *CheckExistModel) SetBody(v *MobileCheckExistResponse) *CheckExistModel {
	s.Body = v
	return s
}

type LoginModel struct {
	Headers map[string]*string          `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *AccountAccessTokenResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s LoginModel) String() string {
	return tea.Prettify(s)
}

func (s LoginModel) GoString() string {
	return s.String()
}

func (s *LoginModel) SetHeaders(v map[string]*string) *LoginModel {
	s.Headers = v
	return s
}

func (s *LoginModel) SetBody(v *AccountAccessTokenResponse) *LoginModel {
	s.Body = v
	return s
}

type RegisterModel struct {
	Headers map[string]*string          `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *AccountAccessTokenResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s RegisterModel) String() string {
	return tea.Prettify(s)
}

func (s RegisterModel) GoString() string {
	return s.String()
}

func (s *RegisterModel) SetHeaders(v map[string]*string) *RegisterModel {
	s.Headers = v
	return s
}

func (s *RegisterModel) SetBody(v *AccountAccessTokenResponse) *RegisterModel {
	s.Body = v
	return s
}

type MobileSendSmsCodeModel struct {
	Headers map[string]*string         `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *MobileSendSmsCodeResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s MobileSendSmsCodeModel) String() string {
	return tea.Prettify(s)
}

func (s MobileSendSmsCodeModel) GoString() string {
	return s.String()
}

func (s *MobileSendSmsCodeModel) SetHeaders(v map[string]*string) *MobileSendSmsCodeModel {
	s.Headers = v
	return s
}

func (s *MobileSendSmsCodeModel) SetBody(v *MobileSendSmsCodeResponse) *MobileSendSmsCodeModel {
	s.Body = v
	return s
}

type AccountRevokeModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s AccountRevokeModel) String() string {
	return tea.Prettify(s)
}

func (s AccountRevokeModel) GoString() string {
	return s.String()
}

func (s *AccountRevokeModel) SetHeaders(v map[string]*string) *AccountRevokeModel {
	s.Headers = v
	return s
}

type AccountTokenModel struct {
	Headers map[string]*string          `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *AccountAccessTokenResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s AccountTokenModel) String() string {
	return tea.Prettify(s)
}

func (s AccountTokenModel) GoString() string {
	return s.String()
}

func (s *AccountTokenModel) SetHeaders(v map[string]*string) *AccountTokenModel {
	s.Headers = v
	return s
}

func (s *AccountTokenModel) SetBody(v *AccountAccessTokenResponse) *AccountTokenModel {
	s.Body = v
	return s
}

/**
 *
 */
type AccessTokenResponse struct {
	// 用于调用业务接口的accessToken
	AccessToken *string `json:"access_token,omitempty" xml:"access_token,omitempty" require:"true"`
	// Default Drive ID
	DefaultDriveId *string `json:"default_drive_id,omitempty" xml:"default_drive_id,omitempty" require:"true"`
	// accessToken过期时间，ISO时间
	ExpireTime *string `json:"expire_time,omitempty" xml:"expire_time,omitempty" require:"true"`
	// accessToken过期时间，单位秒
	ExpiresIn *int64 `json:"expires_in,omitempty" xml:"expires_in,omitempty" require:"true"`
	// 用于刷新accessToken
	RefreshToken *string `json:"refresh_token,omitempty" xml:"refresh_token,omitempty" require:"true"`
	// 当前用户角色
	Role *string `json:"role,omitempty" xml:"role,omitempty" require:"true"`
	// accessToken类型，Bearer
	TokenType *string `json:"token_type,omitempty" xml:"token_type,omitempty" require:"true"`
	// 当前用户ID
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty" require:"true"`
}

func (s AccessTokenResponse) String() string {
	return tea.Prettify(s)
}

func (s AccessTokenResponse) GoString() string {
	return s.String()
}

func (s *AccessTokenResponse) SetAccessToken(v string) *AccessTokenResponse {
	s.AccessToken = &v
	return s
}

func (s *AccessTokenResponse) SetDefaultDriveId(v string) *AccessTokenResponse {
	s.DefaultDriveId = &v
	return s
}

func (s *AccessTokenResponse) SetExpireTime(v string) *AccessTokenResponse {
	s.ExpireTime = &v
	return s
}

func (s *AccessTokenResponse) SetExpiresIn(v int64) *AccessTokenResponse {
	s.ExpiresIn = &v
	return s
}

func (s *AccessTokenResponse) SetRefreshToken(v string) *AccessTokenResponse {
	s.RefreshToken = &v
	return s
}

func (s *AccessTokenResponse) SetRole(v string) *AccessTokenResponse {
	s.Role = &v
	return s
}

func (s *AccessTokenResponse) SetTokenType(v string) *AccessTokenResponse {
	s.TokenType = &v
	return s
}

func (s *AccessTokenResponse) SetUserId(v string) *AccessTokenResponse {
	s.UserId = &v
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
	// 用户的数据密码是否保存服务端
	DataPinSaved *bool `json:"data_pin_saved,omitempty" xml:"data_pin_saved,omitempty"`
	// 用户的数据密码是否设置过
	DataPinSetup *bool `json:"data_pin_setup,omitempty" xml:"data_pin_setup,omitempty"`
	// Default Drive ID
	DefaultDriveId *string `json:"default_drive_id,omitempty" xml:"default_drive_id,omitempty"`
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
	// 当前用户昵称
	NickName *string `json:"nick_name,omitempty" xml:"nick_name,omitempty"`
	// 用于刷新accessToken
	RefreshToken *string `json:"refresh_token,omitempty" xml:"refresh_token,omitempty"`
	// 当前用户角色
	Role *string `json:"role,omitempty" xml:"role,omitempty"`
	// 临时权限，用于登录成功后设置密码
	State *string `json:"state,omitempty" xml:"state,omitempty"`
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

func (s *AccountAccessTokenResponse) SetDataPinSaved(v bool) *AccountAccessTokenResponse {
	s.DataPinSaved = &v
	return s
}

func (s *AccountAccessTokenResponse) SetDataPinSetup(v bool) *AccountAccessTokenResponse {
	s.DataPinSetup = &v
	return s
}

func (s *AccountAccessTokenResponse) SetDefaultDriveId(v string) *AccountAccessTokenResponse {
	s.DefaultDriveId = &v
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

func (s *AccountAccessTokenResponse) SetNickName(v string) *AccountAccessTokenResponse {
	s.NickName = &v
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
type AccountLinkRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 账号信息
	Detail *string `json:"detail,omitempty" xml:"detail,omitempty"`
	// 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
	Extra *string `json:"extra,omitempty" xml:"extra,omitempty"`
	// 唯一身份标识
	Identity *string `json:"identity,omitempty" xml:"identity,omitempty" require:"true"`
	// 状态
	Status *string `json:"status,omitempty" xml:"status,omitempty"`
	// 认证类型
	Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
	// 绑定的user_id
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty" require:"true"`
}

func (s AccountLinkRequest) String() string {
	return tea.Prettify(s)
}

func (s AccountLinkRequest) GoString() string {
	return s.String()
}

func (s *AccountLinkRequest) SetHeaders(v map[string]*string) *AccountLinkRequest {
	s.Headers = v
	return s
}

func (s *AccountLinkRequest) SetDetail(v string) *AccountLinkRequest {
	s.Detail = &v
	return s
}

func (s *AccountLinkRequest) SetExtra(v string) *AccountLinkRequest {
	s.Extra = &v
	return s
}

func (s *AccountLinkRequest) SetIdentity(v string) *AccountLinkRequest {
	s.Identity = &v
	return s
}

func (s *AccountLinkRequest) SetStatus(v string) *AccountLinkRequest {
	s.Status = &v
	return s
}

func (s *AccountLinkRequest) SetType(v string) *AccountLinkRequest {
	s.Type = &v
	return s
}

func (s *AccountLinkRequest) SetUserId(v string) *AccountLinkRequest {
	s.UserId = &v
	return s
}

/**
 *
 */
type AuthorizeRequest struct {
	// Client ID, 此处填写创建App时返回的AppID
	ClientID *string `json:"ClientID,omitempty" xml:"ClientID,omitempty" require:"true"`
	// 鉴权方式，目前支持ding,ram鉴权
	LoginType *string `json:"LoginType,omitempty" xml:"LoginType,omitempty"`
	// 回调地址, 此处填写创建App时填写的回调地址
	RedirectUri *string `json:"RedirectUri,omitempty" xml:"RedirectUri,omitempty" require:"true"`
	// 返回类型, 只能填写code
	ResponseType *string `json:"ResponseType,omitempty" xml:"ResponseType,omitempty" require:"true"`
	// 申请的权限列表, 默认为所有权限
	Scope []*string `json:"Scope,omitempty" xml:"Scope,omitempty" type:"Repeated"`
	// 用户自定义字段，会在鉴权成功后的callback带回
	State *string `json:"State,omitempty" xml:"State,omitempty"`
}

func (s AuthorizeRequest) String() string {
	return tea.Prettify(s)
}

func (s AuthorizeRequest) GoString() string {
	return s.String()
}

func (s *AuthorizeRequest) SetClientID(v string) *AuthorizeRequest {
	s.ClientID = &v
	return s
}

func (s *AuthorizeRequest) SetLoginType(v string) *AuthorizeRequest {
	s.LoginType = &v
	return s
}

func (s *AuthorizeRequest) SetRedirectUri(v string) *AuthorizeRequest {
	s.RedirectUri = &v
	return s
}

func (s *AuthorizeRequest) SetResponseType(v string) *AuthorizeRequest {
	s.ResponseType = &v
	return s
}

func (s *AuthorizeRequest) SetScope(v []*string) *AuthorizeRequest {
	s.Scope = v
	return s
}

func (s *AuthorizeRequest) SetState(v string) *AuthorizeRequest {
	s.State = &v
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
	DriveType         *string `json:"drive_type,omitempty" xml:"drive_type,omitempty"`
	EncryptDataAccess *bool   `json:"encrypt_data_access,omitempty" xml:"encrypt_data_access,omitempty"`
	EncryptMode       *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
	// Drive 所有者
	Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
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
 * Base file response
 */
type BaseFileResponse struct {
	// category
	Category *string `json:"category,omitempty" xml:"category,omitempty"`
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
	Hidden             *bool               `json:"hidden,omitempty" xml:"hidden,omitempty"`
	ImageMediaMetadata *ImageMediaResponse `json:"image_media_metadata,omitempty" xml:"image_media_metadata,omitempty"`
	// labels
	Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
	Meta   *string   `json:"meta,omitempty" xml:"meta,omitempty"`
	// name
	Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
	// parent_file_id
	ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
	PunishFlag   *int    `json:"punish_flag,omitempty" xml:"punish_flag,omitempty"`
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
	UserMeta             *string               `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
	VideoMediaMetadata   *VideoMediaResponse   `json:"video_media_metadata,omitempty" xml:"video_media_metadata,omitempty"`
	VideoPreviewMetadata *VideoPreviewResponse `json:"video_preview_metadata,omitempty" xml:"video_preview_metadata,omitempty"`
}

func (s BaseFileResponse) String() string {
	return tea.Prettify(s)
}

func (s BaseFileResponse) GoString() string {
	return s.String()
}

func (s *BaseFileResponse) SetCategory(v string) *BaseFileResponse {
	s.Category = &v
	return s
}

func (s *BaseFileResponse) SetContentHash(v string) *BaseFileResponse {
	s.ContentHash = &v
	return s
}

func (s *BaseFileResponse) SetContentHashName(v string) *BaseFileResponse {
	s.ContentHashName = &v
	return s
}

func (s *BaseFileResponse) SetContentType(v string) *BaseFileResponse {
	s.ContentType = &v
	return s
}

func (s *BaseFileResponse) SetCrc64Hash(v string) *BaseFileResponse {
	s.Crc64Hash = &v
	return s
}

func (s *BaseFileResponse) SetCreatedAt(v string) *BaseFileResponse {
	s.CreatedAt = &v
	return s
}

func (s *BaseFileResponse) SetDescription(v string) *BaseFileResponse {
	s.Description = &v
	return s
}

func (s *BaseFileResponse) SetDomainId(v string) *BaseFileResponse {
	s.DomainId = &v
	return s
}

func (s *BaseFileResponse) SetDownloadUrl(v string) *BaseFileResponse {
	s.DownloadUrl = &v
	return s
}

func (s *BaseFileResponse) SetDriveId(v string) *BaseFileResponse {
	s.DriveId = &v
	return s
}

func (s *BaseFileResponse) SetEncryptMode(v string) *BaseFileResponse {
	s.EncryptMode = &v
	return s
}

func (s *BaseFileResponse) SetFileExtension(v string) *BaseFileResponse {
	s.FileExtension = &v
	return s
}

func (s *BaseFileResponse) SetFileId(v string) *BaseFileResponse {
	s.FileId = &v
	return s
}

func (s *BaseFileResponse) SetHidden(v bool) *BaseFileResponse {
	s.Hidden = &v
	return s
}

func (s *BaseFileResponse) SetImageMediaMetadata(v *ImageMediaResponse) *BaseFileResponse {
	s.ImageMediaMetadata = v
	return s
}

func (s *BaseFileResponse) SetLabels(v []*string) *BaseFileResponse {
	s.Labels = v
	return s
}

func (s *BaseFileResponse) SetMeta(v string) *BaseFileResponse {
	s.Meta = &v
	return s
}

func (s *BaseFileResponse) SetName(v string) *BaseFileResponse {
	s.Name = &v
	return s
}

func (s *BaseFileResponse) SetParentFileId(v string) *BaseFileResponse {
	s.ParentFileId = &v
	return s
}

func (s *BaseFileResponse) SetPunishFlag(v int) *BaseFileResponse {
	s.PunishFlag = &v
	return s
}

func (s *BaseFileResponse) SetSize(v int64) *BaseFileResponse {
	s.Size = &v
	return s
}

func (s *BaseFileResponse) SetStarred(v bool) *BaseFileResponse {
	s.Starred = &v
	return s
}

func (s *BaseFileResponse) SetStatus(v string) *BaseFileResponse {
	s.Status = &v
	return s
}

func (s *BaseFileResponse) SetStreamsInfo(v map[string]interface{}) *BaseFileResponse {
	s.StreamsInfo = v
	return s
}

func (s *BaseFileResponse) SetThumbnail(v string) *BaseFileResponse {
	s.Thumbnail = &v
	return s
}

func (s *BaseFileResponse) SetTrashedAt(v string) *BaseFileResponse {
	s.TrashedAt = &v
	return s
}

func (s *BaseFileResponse) SetType(v string) *BaseFileResponse {
	s.Type = &v
	return s
}

func (s *BaseFileResponse) SetUpdatedAt(v string) *BaseFileResponse {
	s.UpdatedAt = &v
	return s
}

func (s *BaseFileResponse) SetUploadId(v string) *BaseFileResponse {
	s.UploadId = &v
	return s
}

func (s *BaseFileResponse) SetUrl(v string) *BaseFileResponse {
	s.Url = &v
	return s
}

func (s *BaseFileResponse) SetUserMeta(v string) *BaseFileResponse {
	s.UserMeta = &v
	return s
}

func (s *BaseFileResponse) SetVideoMediaMetadata(v *VideoMediaResponse) *BaseFileResponse {
	s.VideoMediaMetadata = v
	return s
}

func (s *BaseFileResponse) SetVideoPreviewMetadata(v *VideoPreviewResponse) *BaseFileResponse {
	s.VideoPreviewMetadata = v
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
 * Base file response
 */
type BaseOSSFileResponse struct {
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

func (s BaseOSSFileResponse) String() string {
	return tea.Prettify(s)
}

func (s BaseOSSFileResponse) GoString() string {
	return s.String()
}

func (s *BaseOSSFileResponse) SetContentHash(v string) *BaseOSSFileResponse {
	s.ContentHash = &v
	return s
}

func (s *BaseOSSFileResponse) SetContentHashName(v string) *BaseOSSFileResponse {
	s.ContentHashName = &v
	return s
}

func (s *BaseOSSFileResponse) SetContentType(v string) *BaseOSSFileResponse {
	s.ContentType = &v
	return s
}

func (s *BaseOSSFileResponse) SetCrc64Hash(v string) *BaseOSSFileResponse {
	s.Crc64Hash = &v
	return s
}

func (s *BaseOSSFileResponse) SetCreatedAt(v string) *BaseOSSFileResponse {
	s.CreatedAt = &v
	return s
}

func (s *BaseOSSFileResponse) SetDescription(v string) *BaseOSSFileResponse {
	s.Description = &v
	return s
}

func (s *BaseOSSFileResponse) SetDomainId(v string) *BaseOSSFileResponse {
	s.DomainId = &v
	return s
}

func (s *BaseOSSFileResponse) SetDownloadUrl(v string) *BaseOSSFileResponse {
	s.DownloadUrl = &v
	return s
}

func (s *BaseOSSFileResponse) SetDriveId(v string) *BaseOSSFileResponse {
	s.DriveId = &v
	return s
}

func (s *BaseOSSFileResponse) SetFileExtension(v string) *BaseOSSFileResponse {
	s.FileExtension = &v
	return s
}

func (s *BaseOSSFileResponse) SetFilePath(v string) *BaseOSSFileResponse {
	s.FilePath = &v
	return s
}

func (s *BaseOSSFileResponse) SetName(v string) *BaseOSSFileResponse {
	s.Name = &v
	return s
}

func (s *BaseOSSFileResponse) SetParentFilePath(v string) *BaseOSSFileResponse {
	s.ParentFilePath = &v
	return s
}

func (s *BaseOSSFileResponse) SetShareId(v string) *BaseOSSFileResponse {
	s.ShareId = &v
	return s
}

func (s *BaseOSSFileResponse) SetSize(v int64) *BaseOSSFileResponse {
	s.Size = &v
	return s
}

func (s *BaseOSSFileResponse) SetStatus(v string) *BaseOSSFileResponse {
	s.Status = &v
	return s
}

func (s *BaseOSSFileResponse) SetThumbnail(v string) *BaseOSSFileResponse {
	s.Thumbnail = &v
	return s
}

func (s *BaseOSSFileResponse) SetTrashedAt(v string) *BaseOSSFileResponse {
	s.TrashedAt = &v
	return s
}

func (s *BaseOSSFileResponse) SetType(v string) *BaseOSSFileResponse {
	s.Type = &v
	return s
}

func (s *BaseOSSFileResponse) SetUpdatedAt(v string) *BaseOSSFileResponse {
	s.UpdatedAt = &v
	return s
}

func (s *BaseOSSFileResponse) SetUploadId(v string) *BaseOSSFileResponse {
	s.UploadId = &v
	return s
}

func (s *BaseOSSFileResponse) SetUrl(v string) *BaseOSSFileResponse {
	s.Url = &v
	return s
}

/**
 * list_share_link response
 */
type BaseShareLinkResponse struct {
	// created_at
	CreatedAt *string `json:"created_at,omitempty" xml:"created_at,omitempty"`
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
	// preview_count
	PreviewCount *int64 `json:"preview_count,omitempty" xml:"preview_count,omitempty"`
	// 转存次数
	SaveCount *int64 `json:"save_count,omitempty" xml:"save_count,omitempty"`
	// share_id
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
	// share_msg
	ShareMsg *string `json:"share_msg,omitempty" xml:"share_msg,omitempty"`
	// share_policy
	SharePolicy *string `json:"share_policy,omitempty" xml:"share_policy,omitempty"`
	// share_pwd
	SharePwd *string `json:"share_pwd,omitempty" xml:"share_pwd,omitempty"`
	// share_url
	ShareUrl *string `json:"share_url,omitempty" xml:"share_url,omitempty"`
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
	// permissions
	Permissions []*string `json:"permissions,omitempty" xml:"permissions,omitempty" type:"Repeated"`
	// share_path
	ShareFilePath *string `json:"share_file_path,omitempty" xml:"share_file_path,omitempty"`
	// share_id
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
	// share_name
	ShareName   *string                  `json:"share_name,omitempty" xml:"share_name,omitempty"`
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

func (s *BaseShareResponse) SetPermissions(v []*string) *BaseShareResponse {
	s.Permissions = v
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
 *
 */
type CancelLinkRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 待绑定的临时token，此token只能访问绑定、取消绑定接口
	TemporaryToken *string `json:"temporary_token,omitempty" xml:"temporary_token,omitempty" require:"true"`
}

func (s CancelLinkRequest) String() string {
	return tea.Prettify(s)
}

func (s CancelLinkRequest) GoString() string {
	return s.String()
}

func (s *CancelLinkRequest) SetHeaders(v map[string]*string) *CancelLinkRequest {
	s.Headers = v
	return s
}

func (s *CancelLinkRequest) SetTemporaryToken(v string) *CancelLinkRequest {
	s.TemporaryToken = &v
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
 * complete file response
 */
type CompleteFileResponse struct {
	// category
	Category *string `json:"category,omitempty" xml:"category,omitempty"`
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
	Hidden             *bool               `json:"hidden,omitempty" xml:"hidden,omitempty"`
	ImageMediaMetadata *ImageMediaResponse `json:"image_media_metadata,omitempty" xml:"image_media_metadata,omitempty"`
	// labels
	Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
	Meta   *string   `json:"meta,omitempty" xml:"meta,omitempty"`
	// name
	Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
	// parent_file_id
	ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
	PunishFlag   *int    `json:"punish_flag,omitempty" xml:"punish_flag,omitempty"`
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
	UserMeta             *string               `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
	VideoMediaMetadata   *VideoMediaResponse   `json:"video_media_metadata,omitempty" xml:"video_media_metadata,omitempty"`
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

func (s *CompleteFileResponse) SetPunishFlag(v int) *CompleteFileResponse {
	s.PunishFlag = &v
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
 *
 */
type ConfirmLinkRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 待绑定的临时token，此token只能访问绑定、取消绑定接口
	TemporaryToken *string `json:"temporary_token,omitempty" xml:"temporary_token,omitempty" require:"true"`
}

func (s ConfirmLinkRequest) String() string {
	return tea.Prettify(s)
}

func (s ConfirmLinkRequest) GoString() string {
	return s.String()
}

func (s *ConfirmLinkRequest) SetHeaders(v map[string]*string) *ConfirmLinkRequest {
	s.Headers = v
	return s
}

func (s *ConfirmLinkRequest) SetTemporaryToken(v string) *ConfirmLinkRequest {
	s.TemporaryToken = &v
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
 * create_share_link response
 */
type CreateShareLinkResponse struct {
	// share_id
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
	// share_msg
	ShareMsg *string `json:"share_msg,omitempty" xml:"share_msg,omitempty"`
	// share_policy
	SharePolicy *string `json:"share_policy,omitempty" xml:"share_policy,omitempty"`
	// share_pwd
	SharePwd *string `json:"share_pwd,omitempty" xml:"share_pwd,omitempty"`
	// share_url
	ShareUrl *string `json:"share_url,omitempty" xml:"share_url,omitempty"`
}

func (s CreateShareLinkResponse) String() string {
	return tea.Prettify(s)
}

func (s CreateShareLinkResponse) GoString() string {
	return s.String()
}

func (s *CreateShareLinkResponse) SetShareId(v string) *CreateShareLinkResponse {
	s.ShareId = &v
	return s
}

func (s *CreateShareLinkResponse) SetShareMsg(v string) *CreateShareLinkResponse {
	s.ShareMsg = &v
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
	Left   *int64 `json:"left,omitempty" xml:"left,omitempty"`
	Top    *int64 `json:"top,omitempty" xml:"top,omitempty"`
	Width  *int64 `json:"width,omitempty" xml:"width,omitempty"`
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
	AspectRatio      *string           `json:"aspect_ratio,omitempty" xml:"aspect_ratio,omitempty"`
	CroppingBoundary *CroppingBoundary `json:"cropping_boundary,omitempty" xml:"cropping_boundary,omitempty"`
	Score            *int              `json:"score,omitempty" xml:"score,omitempty"`
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

func (s *CroppingSuggestionItem) SetScore(v int) *CroppingSuggestionItem {
	s.Score = &v
	return s
}

/**
 *
 */
type DefaultChangePasswordRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// App ID, 当前访问的App
	AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
	// AES-256对称加密密钥，通过App公钥加密后传输
	EncryptedKey *string `json:"encrypted_key,omitempty" xml:"encrypted_key,omitempty" require:"true"`
	// 新密码，必须包含数字和字母，长度8-20个字符
	NewPassword *string `json:"new_password,omitempty" xml:"new_password,omitempty" require:"true"`
	// 手机号
	PhoneNumber *string `json:"phone_number,omitempty" xml:"phone_number,omitempty" require:"true"`
	// 国家编号，默认86，不需要填+号，直接填数字
	PhoneRegion *string `json:"phone_region,omitempty" xml:"phone_region,omitempty"`
	// 修改密码的临时授权码
	State *string `json:"state,omitempty" xml:"state,omitempty" require:"true"`
}

func (s DefaultChangePasswordRequest) String() string {
	return tea.Prettify(s)
}

func (s DefaultChangePasswordRequest) GoString() string {
	return s.String()
}

func (s *DefaultChangePasswordRequest) SetHeaders(v map[string]*string) *DefaultChangePasswordRequest {
	s.Headers = v
	return s
}

func (s *DefaultChangePasswordRequest) SetAppId(v string) *DefaultChangePasswordRequest {
	s.AppId = &v
	return s
}

func (s *DefaultChangePasswordRequest) SetEncryptedKey(v string) *DefaultChangePasswordRequest {
	s.EncryptedKey = &v
	return s
}

func (s *DefaultChangePasswordRequest) SetNewPassword(v string) *DefaultChangePasswordRequest {
	s.NewPassword = &v
	return s
}

func (s *DefaultChangePasswordRequest) SetPhoneNumber(v string) *DefaultChangePasswordRequest {
	s.PhoneNumber = &v
	return s
}

func (s *DefaultChangePasswordRequest) SetPhoneRegion(v string) *DefaultChangePasswordRequest {
	s.PhoneRegion = &v
	return s
}

func (s *DefaultChangePasswordRequest) SetState(v string) *DefaultChangePasswordRequest {
	s.State = &v
	return s
}

/**
 *
 */
type DefaultSetPasswordRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// App ID, 当前访问的App
	AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
	// AES-256对称加密密钥，通过App公钥加密后传输
	EncryptedKey *string `json:"encrypted_key,omitempty" xml:"encrypted_key,omitempty" require:"true"`
	// 新密码，必须包含数字和字母，长度8-20个字符，使用AES-256对称加密后传输（CBC模式, 填充算法为PKCS7Padding，生成base64字符串）
	NewPassword *string `json:"new_password,omitempty" xml:"new_password,omitempty" require:"true"`
	// 修改密码的临时授权码
	State *string `json:"state,omitempty" xml:"state,omitempty" require:"true"`
}

func (s DefaultSetPasswordRequest) String() string {
	return tea.Prettify(s)
}

func (s DefaultSetPasswordRequest) GoString() string {
	return s.String()
}

func (s *DefaultSetPasswordRequest) SetHeaders(v map[string]*string) *DefaultSetPasswordRequest {
	s.Headers = v
	return s
}

func (s *DefaultSetPasswordRequest) SetAppId(v string) *DefaultSetPasswordRequest {
	s.AppId = &v
	return s
}

func (s *DefaultSetPasswordRequest) SetEncryptedKey(v string) *DefaultSetPasswordRequest {
	s.EncryptedKey = &v
	return s
}

func (s *DefaultSetPasswordRequest) SetNewPassword(v string) *DefaultSetPasswordRequest {
	s.NewPassword = &v
	return s
}

func (s *DefaultSetPasswordRequest) SetState(v string) *DefaultSetPasswordRequest {
	s.State = &v
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
 *
 */
type DeviceAuthorizeRequest struct {
	// Client ID, 此处填写创建App时返回的AppID
	ClientID *string `json:"ClientID,omitempty" xml:"ClientID,omitempty" require:"true"`
	// 设备信息，用于用户识别设备
	DeviceInfo *string `json:"DeviceInfo,omitempty" xml:"DeviceInfo,omitempty"`
	// 设备名，实现方需保证不同设备的设备名不重复（推荐用硬件名称+硬件型号作为设备名）
	DeviceName *string `json:"DeviceName,omitempty" xml:"DeviceName,omitempty" require:"true"`
	// 鉴权方式，目前支持ding,ram鉴权
	LoginType *string `json:"LoginType,omitempty" xml:"LoginType,omitempty"`
	// 申请的权限列表, 默认为所有权限
	Scope []*string `json:"Scope,omitempty" xml:"Scope,omitempty" type:"Repeated"`
}

func (s DeviceAuthorizeRequest) String() string {
	return tea.Prettify(s)
}

func (s DeviceAuthorizeRequest) GoString() string {
	return s.String()
}

func (s *DeviceAuthorizeRequest) SetClientID(v string) *DeviceAuthorizeRequest {
	s.ClientID = &v
	return s
}

func (s *DeviceAuthorizeRequest) SetDeviceInfo(v string) *DeviceAuthorizeRequest {
	s.DeviceInfo = &v
	return s
}

func (s *DeviceAuthorizeRequest) SetDeviceName(v string) *DeviceAuthorizeRequest {
	s.DeviceName = &v
	return s
}

func (s *DeviceAuthorizeRequest) SetLoginType(v string) *DeviceAuthorizeRequest {
	s.LoginType = &v
	return s
}

func (s *DeviceAuthorizeRequest) SetScope(v []*string) *DeviceAuthorizeRequest {
	s.Scope = v
	return s
}

/**
 * the file op info
 */
type FileDeltaResponse struct {
	CurrentCategory *string           `json:"current_category,omitempty" xml:"current_category,omitempty"`
	File            *BaseFileResponse `json:"file,omitempty" xml:"file,omitempty"`
	FileId          *string           `json:"file_id,omitempty" xml:"file_id,omitempty"`
	Op              *string           `json:"op,omitempty" xml:"op,omitempty"`
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

func (s *FileDeltaResponse) SetFile(v *BaseFileResponse) *FileDeltaResponse {
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
type GetAccessTokenByLinkInfoRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
	Extra *string `json:"extra,omitempty" xml:"extra,omitempty"`
	// 唯一身份标识
	Identity *string `json:"identity,omitempty" xml:"identity,omitempty" require:"true"`
	// 认证类型
	Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
}

func (s GetAccessTokenByLinkInfoRequest) String() string {
	return tea.Prettify(s)
}

func (s GetAccessTokenByLinkInfoRequest) GoString() string {
	return s.String()
}

func (s *GetAccessTokenByLinkInfoRequest) SetHeaders(v map[string]*string) *GetAccessTokenByLinkInfoRequest {
	s.Headers = v
	return s
}

func (s *GetAccessTokenByLinkInfoRequest) SetExtra(v string) *GetAccessTokenByLinkInfoRequest {
	s.Extra = &v
	return s
}

func (s *GetAccessTokenByLinkInfoRequest) SetIdentity(v string) *GetAccessTokenByLinkInfoRequest {
	s.Identity = &v
	return s
}

func (s *GetAccessTokenByLinkInfoRequest) SetType(v string) *GetAccessTokenByLinkInfoRequest {
	s.Type = &v
	return s
}

/**
 *
 */
type GetAppPublicKeyRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// App ID
	AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty"`
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
 * Get AsyncTask Response
 */
type GetAsyncTaskResponse struct {
	// async_task_id
	// type:string
	AsyncTaskId *string `json:"async_task_id,omitempty" xml:"async_task_id,omitempty"`
	// message
	Message *string `json:"message,omitempty" xml:"message,omitempty"`
	// state
	State *string `json:"state,omitempty" xml:"state,omitempty"`
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

func (s *GetAsyncTaskResponse) SetMessage(v string) *GetAsyncTaskResponse {
	s.Message = &v
	return s
}

func (s *GetAsyncTaskResponse) SetState(v string) *GetAsyncTaskResponse {
	s.State = &v
	return s
}

/**
 *
 */
type GetByLinkInfoRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
	Extra *string `json:"extra,omitempty" xml:"extra,omitempty"`
	// 唯一身份标识
	Identity *string `json:"identity,omitempty" xml:"identity,omitempty" require:"true"`
	// 认证类型
	Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
}

func (s GetByLinkInfoRequest) String() string {
	return tea.Prettify(s)
}

func (s GetByLinkInfoRequest) GoString() string {
	return s.String()
}

func (s *GetByLinkInfoRequest) SetHeaders(v map[string]*string) *GetByLinkInfoRequest {
	s.Headers = v
	return s
}

func (s *GetByLinkInfoRequest) SetExtra(v string) *GetByLinkInfoRequest {
	s.Extra = &v
	return s
}

func (s *GetByLinkInfoRequest) SetIdentity(v string) *GetByLinkInfoRequest {
	s.Identity = &v
	return s
}

func (s *GetByLinkInfoRequest) SetType(v string) *GetByLinkInfoRequest {
	s.Type = &v
	return s
}

/**
 *
 */
type GetCaptchaRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// App ID, 当前访问的App
	AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
}

func (s GetCaptchaRequest) String() string {
	return tea.Prettify(s)
}

func (s GetCaptchaRequest) GoString() string {
	return s.String()
}

func (s *GetCaptchaRequest) SetHeaders(v map[string]*string) *GetCaptchaRequest {
	s.Headers = v
	return s
}

func (s *GetCaptchaRequest) SetAppId(v string) *GetCaptchaRequest {
	s.AppId = &v
	return s
}

/**
 * 获取download url response
 */
type GetDownloadUrlResponse struct {
	// expiration
	Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
	// method
	Method    *string    `json:"method,omitempty" xml:"method,omitempty"`
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
	DriveType         *string `json:"drive_type,omitempty" xml:"drive_type,omitempty"`
	EncryptDataAccess *bool   `json:"encrypt_data_access,omitempty" xml:"encrypt_data_access,omitempty"`
	EncryptMode       *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
	// Drive 所有者
	Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
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
 * 根据路径获取文件元数据response
 */
type GetFileByPathResponse struct {
	// category
	Category *string `json:"category,omitempty" xml:"category,omitempty"`
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
	Hidden             *bool               `json:"hidden,omitempty" xml:"hidden,omitempty"`
	ImageMediaMetadata *ImageMediaResponse `json:"image_media_metadata,omitempty" xml:"image_media_metadata,omitempty"`
	// labels
	Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
	Meta   *string   `json:"meta,omitempty" xml:"meta,omitempty"`
	// name
	Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
	// parent_file_id
	ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
	PunishFlag   *int    `json:"punish_flag,omitempty" xml:"punish_flag,omitempty"`
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
	UserMeta             *string               `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
	VideoMediaMetadata   *VideoMediaResponse   `json:"video_media_metadata,omitempty" xml:"video_media_metadata,omitempty"`
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

func (s *GetFileByPathResponse) SetPunishFlag(v int) *GetFileByPathResponse {
	s.PunishFlag = &v
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
 * 获取文件元数据response
 */
type GetFileResponse struct {
	// category
	Category *string `json:"category,omitempty" xml:"category,omitempty"`
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
	Hidden             *bool               `json:"hidden,omitempty" xml:"hidden,omitempty"`
	ImageMediaMetadata *ImageMediaResponse `json:"image_media_metadata,omitempty" xml:"image_media_metadata,omitempty"`
	// labels
	Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
	Meta   *string   `json:"meta,omitempty" xml:"meta,omitempty"`
	// name
	Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
	// parent_file_id
	ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
	PunishFlag   *int    `json:"punish_flag,omitempty" xml:"punish_flag,omitempty"`
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
	UserMeta             *string               `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
	VideoMediaMetadata   *VideoMediaResponse   `json:"video_media_metadata,omitempty" xml:"video_media_metadata,omitempty"`
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

func (s *GetFileResponse) SetPunishFlag(v int) *GetFileResponse {
	s.PunishFlag = &v
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
 *
 */
type GetLinkInfoByUserIDRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// user ID
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty" require:"true"`
}

func (s GetLinkInfoByUserIDRequest) String() string {
	return tea.Prettify(s)
}

func (s GetLinkInfoByUserIDRequest) GoString() string {
	return s.String()
}

func (s *GetLinkInfoByUserIDRequest) SetHeaders(v map[string]*string) *GetLinkInfoByUserIDRequest {
	s.Headers = v
	return s
}

func (s *GetLinkInfoByUserIDRequest) SetUserId(v string) *GetLinkInfoByUserIDRequest {
	s.UserId = &v
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
	AppId     *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
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
 * get_share_link_by_anonymous response
 */
type GetShareLinkByAnonymousResponse struct {
	// creator_id
	CreatorId *string `json:"creator_id,omitempty" xml:"creator_id,omitempty"`
	// creator_name
	CreatorName *string `json:"creator_name,omitempty" xml:"creator_name,omitempty"`
	// expiration
	Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
	// updated_at
	UpdatedAt *string `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
}

func (s GetShareLinkByAnonymousResponse) String() string {
	return tea.Prettify(s)
}

func (s GetShareLinkByAnonymousResponse) GoString() string {
	return s.String()
}

func (s *GetShareLinkByAnonymousResponse) SetCreatorId(v string) *GetShareLinkByAnonymousResponse {
	s.CreatorId = &v
	return s
}

func (s *GetShareLinkByAnonymousResponse) SetCreatorName(v string) *GetShareLinkByAnonymousResponse {
	s.CreatorName = &v
	return s
}

func (s *GetShareLinkByAnonymousResponse) SetExpiration(v string) *GetShareLinkByAnonymousResponse {
	s.Expiration = &v
	return s
}

func (s *GetShareLinkByAnonymousResponse) SetUpdatedAt(v string) *GetShareLinkByAnonymousResponse {
	s.UpdatedAt = &v
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
	// permissions
	Permissions []*string `json:"permissions,omitempty" xml:"permissions,omitempty" type:"Repeated"`
	// share_path
	ShareFilePath *string `json:"share_file_path,omitempty" xml:"share_file_path,omitempty"`
	// share_id
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
	// share_name
	ShareName   *string                  `json:"share_name,omitempty" xml:"share_name,omitempty"`
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

func (s *GetShareResponse) SetPermissions(v []*string) *GetShareResponse {
	s.Permissions = v
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
	// height
	Height       *int64        `json:"height,omitempty" xml:"height,omitempty"`
	ImageQuality *ImageQuality `json:"image_quality,omitempty" xml:"image_quality,omitempty"`
	// system_tags
	ImageTags []*SystemTag `json:"image_tags,omitempty" xml:"image_tags,omitempty" type:"Repeated"`
	// location
	Location *string `json:"location,omitempty" xml:"location,omitempty"`
	// province
	Province *string `json:"province,omitempty" xml:"province,omitempty"`
	// story_image_score
	StoryImageScore *int `json:"story_image_score,omitempty" xml:"story_image_score,omitempty"`
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

func (s *ImageMediaResponse) SetStoryImageScore(v int) *ImageMediaResponse {
	s.StoryImageScore = &v
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
	Clarity          *int `json:"clarity,omitempty" xml:"clarity,omitempty"`
	ClarityScore     *int `json:"clarity_score,omitempty" xml:"clarity_score,omitempty"`
	Color            *int `json:"color,omitempty" xml:"color,omitempty"`
	ColorScore       *int `json:"color_score,omitempty" xml:"color_score,omitempty"`
	CompositionScore *int `json:"composition_score,omitempty" xml:"composition_score,omitempty"`
	Contrast         *int `json:"contrast,omitempty" xml:"contrast,omitempty"`
	ContrastScore    *int `json:"contrast_score,omitempty" xml:"contrast_score,omitempty"`
	Exposure         *int `json:"exposure,omitempty" xml:"exposure,omitempty"`
	ExposureScore    *int `json:"exposure_score,omitempty" xml:"exposure_score,omitempty"`
	OverallScore     *int `json:"overall_score,omitempty" xml:"overall_score,omitempty"`
}

func (s ImageQuality) String() string {
	return tea.Prettify(s)
}

func (s ImageQuality) GoString() string {
	return s.String()
}

func (s *ImageQuality) SetClarity(v int) *ImageQuality {
	s.Clarity = &v
	return s
}

func (s *ImageQuality) SetClarityScore(v int) *ImageQuality {
	s.ClarityScore = &v
	return s
}

func (s *ImageQuality) SetColor(v int) *ImageQuality {
	s.Color = &v
	return s
}

func (s *ImageQuality) SetColorScore(v int) *ImageQuality {
	s.ColorScore = &v
	return s
}

func (s *ImageQuality) SetCompositionScore(v int) *ImageQuality {
	s.CompositionScore = &v
	return s
}

func (s *ImageQuality) SetContrast(v int) *ImageQuality {
	s.Contrast = &v
	return s
}

func (s *ImageQuality) SetContrastScore(v int) *ImageQuality {
	s.ContrastScore = &v
	return s
}

func (s *ImageQuality) SetExposure(v int) *ImageQuality {
	s.Exposure = &v
	return s
}

func (s *ImageQuality) SetExposureScore(v int) *ImageQuality {
	s.ExposureScore = &v
	return s
}

func (s *ImageQuality) SetOverallScore(v int) *ImageQuality {
	s.OverallScore = &v
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
 * List file response
 */
type ListFileResponse struct {
	// items
	Items []*BaseFileResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
	// next_marker
	NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ListFileResponse) String() string {
	return tea.Prettify(s)
}

func (s ListFileResponse) GoString() string {
	return s.String()
}

func (s *ListFileResponse) SetItems(v []*BaseFileResponse) *ListFileResponse {
	s.Items = v
	return s
}

func (s *ListFileResponse) SetNextMarker(v string) *ListFileResponse {
	s.NextMarker = &v
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
 * List storage file
 */
type ListStoreFileResponse struct {
	// items
	// file list
	Items      []*StoreFile `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
	NextMarker *string      `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
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
 * 获取签名 response
 */
type ListUploadedPartResponse struct {
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
	// next_part_number_marker
	NextPartNumberMarker *string `json:"next_part_number_marker,omitempty" xml:"next_part_number_marker,omitempty"`
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

func (s *ListUploadedPartResponse) SetUploadId(v string) *ListUploadedPartResponse {
	s.UploadId = &v
	return s
}

func (s *ListUploadedPartResponse) SetUploadedParts(v []*UploadPartInfo) *ListUploadedPartResponse {
	s.UploadedParts = v
	return s
}

/**
 *
 */
type LoginByCodeRequest struct {
	// 鉴权后返回的accessToken，淘宝登录需要此字段
	AccessToken *string `json:"access_token,omitempty" xml:"access_token,omitempty"`
	// App ID, 当前访问的App
	AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
	// 鉴权后返回的AuthCode，支付宝登录需要此字段
	AuthCode *string `json:"auth_code,omitempty" xml:"auth_code,omitempty"`
	// 鉴权类型，淘宝、支付宝
	Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
}

func (s LoginByCodeRequest) String() string {
	return tea.Prettify(s)
}

func (s LoginByCodeRequest) GoString() string {
	return s.String()
}

func (s *LoginByCodeRequest) SetAccessToken(v string) *LoginByCodeRequest {
	s.AccessToken = &v
	return s
}

func (s *LoginByCodeRequest) SetAppId(v string) *LoginByCodeRequest {
	s.AppId = &v
	return s
}

func (s *LoginByCodeRequest) SetAuthCode(v string) *LoginByCodeRequest {
	s.AuthCode = &v
	return s
}

func (s *LoginByCodeRequest) SetType(v string) *LoginByCodeRequest {
	s.Type = &v
	return s
}

/**
 *
 */
type MobileCheckExistRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// App ID, 当前访问的App
	AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
	// 待查询的手机号
	PhoneNumber *string `json:"phone_number,omitempty" xml:"phone_number,omitempty" require:"true"`
	// 国家编号，默认86，不需要填+号，直接填数字
	PhoneRegion *string `json:"phone_region,omitempty" xml:"phone_region,omitempty"`
}

func (s MobileCheckExistRequest) String() string {
	return tea.Prettify(s)
}

func (s MobileCheckExistRequest) GoString() string {
	return s.String()
}

func (s *MobileCheckExistRequest) SetHeaders(v map[string]*string) *MobileCheckExistRequest {
	s.Headers = v
	return s
}

func (s *MobileCheckExistRequest) SetAppId(v string) *MobileCheckExistRequest {
	s.AppId = &v
	return s
}

func (s *MobileCheckExistRequest) SetPhoneNumber(v string) *MobileCheckExistRequest {
	s.PhoneNumber = &v
	return s
}

func (s *MobileCheckExistRequest) SetPhoneRegion(v string) *MobileCheckExistRequest {
	s.PhoneRegion = &v
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
type MobileLoginRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// App ID, 当前访问的App
	AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
	// 是否自动注册用户，使用密码登录此参数不生效
	AutoRegister *bool `json:"auto_register,omitempty" xml:"auto_register,omitempty"`
	// 图片验证码ID, 密码登录需要此参数
	CaptchaId *string `json:"captcha_id,omitempty" xml:"captcha_id,omitempty"`
	// 用户输入的验证码值, 密码登录需要此参数
	CaptchaText *string `json:"captcha_text,omitempty" xml:"captcha_text,omitempty"`
	// AES-256对称加密密钥，通过App公钥加密后传输
	EncryptedKey *string `json:"encrypted_key,omitempty" xml:"encrypted_key,omitempty"`
	// 登录密码, 传入此参数则忽略短信验证码，不传此参数则默认使用短信登录。
	Password *string `json:"password,omitempty" xml:"password,omitempty"`
	// 待查询的手机号
	PhoneNumber *string `json:"phone_number,omitempty" xml:"phone_number,omitempty" require:"true"`
	// 国家编号，默认86，不需要填+号，直接填数字
	PhoneRegion *string `json:"phone_region,omitempty" xml:"phone_region,omitempty"`
	// 短信验证码内容，使用密码登录此参数不生效
	SmsCode *string `json:"sms_code,omitempty" xml:"sms_code,omitempty"`
	// 短信验证码ID，使用密码登录此参数不生效
	SmsCodeId *string `json:"sms_code_id,omitempty" xml:"sms_code_id,omitempty"`
}

func (s MobileLoginRequest) String() string {
	return tea.Prettify(s)
}

func (s MobileLoginRequest) GoString() string {
	return s.String()
}

func (s *MobileLoginRequest) SetHeaders(v map[string]*string) *MobileLoginRequest {
	s.Headers = v
	return s
}

func (s *MobileLoginRequest) SetAppId(v string) *MobileLoginRequest {
	s.AppId = &v
	return s
}

func (s *MobileLoginRequest) SetAutoRegister(v bool) *MobileLoginRequest {
	s.AutoRegister = &v
	return s
}

func (s *MobileLoginRequest) SetCaptchaId(v string) *MobileLoginRequest {
	s.CaptchaId = &v
	return s
}

func (s *MobileLoginRequest) SetCaptchaText(v string) *MobileLoginRequest {
	s.CaptchaText = &v
	return s
}

func (s *MobileLoginRequest) SetEncryptedKey(v string) *MobileLoginRequest {
	s.EncryptedKey = &v
	return s
}

func (s *MobileLoginRequest) SetPassword(v string) *MobileLoginRequest {
	s.Password = &v
	return s
}

func (s *MobileLoginRequest) SetPhoneNumber(v string) *MobileLoginRequest {
	s.PhoneNumber = &v
	return s
}

func (s *MobileLoginRequest) SetPhoneRegion(v string) *MobileLoginRequest {
	s.PhoneRegion = &v
	return s
}

func (s *MobileLoginRequest) SetSmsCode(v string) *MobileLoginRequest {
	s.SmsCode = &v
	return s
}

func (s *MobileLoginRequest) SetSmsCodeId(v string) *MobileLoginRequest {
	s.SmsCodeId = &v
	return s
}

/**
 *
 */
type MobileRegisterRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// App ID, 当前访问的App
	AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
	// 待查询的手机号
	PhoneNumber *string `json:"phone_number,omitempty" xml:"phone_number,omitempty" require:"true"`
	// 国家编号，默认86，不需要填+号，直接填数字
	PhoneRegion *string `json:"phone_region,omitempty" xml:"phone_region,omitempty"`
	// 短信验证码内容
	SmsCode *string `json:"sms_code,omitempty" xml:"sms_code,omitempty" require:"true"`
	// 短信验证码ID
	SmsCodeId *string `json:"sms_code_id,omitempty" xml:"sms_code_id,omitempty" require:"true"`
}

func (s MobileRegisterRequest) String() string {
	return tea.Prettify(s)
}

func (s MobileRegisterRequest) GoString() string {
	return s.String()
}

func (s *MobileRegisterRequest) SetHeaders(v map[string]*string) *MobileRegisterRequest {
	s.Headers = v
	return s
}

func (s *MobileRegisterRequest) SetAppId(v string) *MobileRegisterRequest {
	s.AppId = &v
	return s
}

func (s *MobileRegisterRequest) SetPhoneNumber(v string) *MobileRegisterRequest {
	s.PhoneNumber = &v
	return s
}

func (s *MobileRegisterRequest) SetPhoneRegion(v string) *MobileRegisterRequest {
	s.PhoneRegion = &v
	return s
}

func (s *MobileRegisterRequest) SetSmsCode(v string) *MobileRegisterRequest {
	s.SmsCode = &v
	return s
}

func (s *MobileRegisterRequest) SetSmsCodeId(v string) *MobileRegisterRequest {
	s.SmsCodeId = &v
	return s
}

/**
 *
 */
type MobileSendSmsCodeRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// App ID, 当前访问的App
	AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
	// 图片验证码ID
	CaptchaId *string `json:"captcha_id,omitempty" xml:"captcha_id,omitempty"`
	// 用户输入的验证码值
	CaptchaText *string `json:"captcha_text,omitempty" xml:"captcha_text,omitempty"`
	// 待发送验证短信的手机号
	PhoneNumber *string `json:"phone_number,omitempty" xml:"phone_number,omitempty" require:"true"`
	// 国家编号，默认86，不需要填+号，直接填数字
	PhoneRegion *string `json:"phone_region,omitempty" xml:"phone_region,omitempty"`
	// 验证码用途, 可下发: login、register、change_password
	Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
}

func (s MobileSendSmsCodeRequest) String() string {
	return tea.Prettify(s)
}

func (s MobileSendSmsCodeRequest) GoString() string {
	return s.String()
}

func (s *MobileSendSmsCodeRequest) SetHeaders(v map[string]*string) *MobileSendSmsCodeRequest {
	s.Headers = v
	return s
}

func (s *MobileSendSmsCodeRequest) SetAppId(v string) *MobileSendSmsCodeRequest {
	s.AppId = &v
	return s
}

func (s *MobileSendSmsCodeRequest) SetCaptchaId(v string) *MobileSendSmsCodeRequest {
	s.CaptchaId = &v
	return s
}

func (s *MobileSendSmsCodeRequest) SetCaptchaText(v string) *MobileSendSmsCodeRequest {
	s.CaptchaText = &v
	return s
}

func (s *MobileSendSmsCodeRequest) SetPhoneNumber(v string) *MobileSendSmsCodeRequest {
	s.PhoneNumber = &v
	return s
}

func (s *MobileSendSmsCodeRequest) SetPhoneRegion(v string) *MobileSendSmsCodeRequest {
	s.PhoneRegion = &v
	return s
}

func (s *MobileSendSmsCodeRequest) SetType(v string) *MobileSendSmsCodeRequest {
	s.Type = &v
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
 * complete file response
 */
type OSSCompleteFileResponse struct {
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

func (s OSSCompleteFileResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSCompleteFileResponse) GoString() string {
	return s.String()
}

func (s *OSSCompleteFileResponse) SetContentHash(v string) *OSSCompleteFileResponse {
	s.ContentHash = &v
	return s
}

func (s *OSSCompleteFileResponse) SetContentHashName(v string) *OSSCompleteFileResponse {
	s.ContentHashName = &v
	return s
}

func (s *OSSCompleteFileResponse) SetContentType(v string) *OSSCompleteFileResponse {
	s.ContentType = &v
	return s
}

func (s *OSSCompleteFileResponse) SetCrc(v string) *OSSCompleteFileResponse {
	s.Crc = &v
	return s
}

func (s *OSSCompleteFileResponse) SetCrc64Hash(v string) *OSSCompleteFileResponse {
	s.Crc64Hash = &v
	return s
}

func (s *OSSCompleteFileResponse) SetCreatedAt(v string) *OSSCompleteFileResponse {
	s.CreatedAt = &v
	return s
}

func (s *OSSCompleteFileResponse) SetDescription(v string) *OSSCompleteFileResponse {
	s.Description = &v
	return s
}

func (s *OSSCompleteFileResponse) SetDomainId(v string) *OSSCompleteFileResponse {
	s.DomainId = &v
	return s
}

func (s *OSSCompleteFileResponse) SetDownloadUrl(v string) *OSSCompleteFileResponse {
	s.DownloadUrl = &v
	return s
}

func (s *OSSCompleteFileResponse) SetDriveId(v string) *OSSCompleteFileResponse {
	s.DriveId = &v
	return s
}

func (s *OSSCompleteFileResponse) SetFileExtension(v string) *OSSCompleteFileResponse {
	s.FileExtension = &v
	return s
}

func (s *OSSCompleteFileResponse) SetFilePath(v string) *OSSCompleteFileResponse {
	s.FilePath = &v
	return s
}

func (s *OSSCompleteFileResponse) SetName(v string) *OSSCompleteFileResponse {
	s.Name = &v
	return s
}

func (s *OSSCompleteFileResponse) SetParentFilePath(v string) *OSSCompleteFileResponse {
	s.ParentFilePath = &v
	return s
}

func (s *OSSCompleteFileResponse) SetShareId(v string) *OSSCompleteFileResponse {
	s.ShareId = &v
	return s
}

func (s *OSSCompleteFileResponse) SetSize(v int64) *OSSCompleteFileResponse {
	s.Size = &v
	return s
}

func (s *OSSCompleteFileResponse) SetStatus(v string) *OSSCompleteFileResponse {
	s.Status = &v
	return s
}

func (s *OSSCompleteFileResponse) SetThumbnail(v string) *OSSCompleteFileResponse {
	s.Thumbnail = &v
	return s
}

func (s *OSSCompleteFileResponse) SetTrashedAt(v string) *OSSCompleteFileResponse {
	s.TrashedAt = &v
	return s
}

func (s *OSSCompleteFileResponse) SetType(v string) *OSSCompleteFileResponse {
	s.Type = &v
	return s
}

func (s *OSSCompleteFileResponse) SetUpdatedAt(v string) *OSSCompleteFileResponse {
	s.UpdatedAt = &v
	return s
}

func (s *OSSCompleteFileResponse) SetUploadId(v string) *OSSCompleteFileResponse {
	s.UploadId = &v
	return s
}

func (s *OSSCompleteFileResponse) SetUrl(v string) *OSSCompleteFileResponse {
	s.Url = &v
	return s
}

/**
 * 文件拷贝 response
 */
type OSSCopyFileResponse struct {
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

func (s OSSCopyFileResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSCopyFileResponse) GoString() string {
	return s.String()
}

func (s *OSSCopyFileResponse) SetAsyncTaskId(v string) *OSSCopyFileResponse {
	s.AsyncTaskId = &v
	return s
}

func (s *OSSCopyFileResponse) SetDomainId(v string) *OSSCopyFileResponse {
	s.DomainId = &v
	return s
}

func (s *OSSCopyFileResponse) SetDriveId(v string) *OSSCopyFileResponse {
	s.DriveId = &v
	return s
}

func (s *OSSCopyFileResponse) SetFilePath(v string) *OSSCopyFileResponse {
	s.FilePath = &v
	return s
}

func (s *OSSCopyFileResponse) SetShareId(v string) *OSSCopyFileResponse {
	s.ShareId = &v
	return s
}

/**
 * Create file response
 */
type OSSCreateFileResponse struct {
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

func (s OSSCreateFileResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSCreateFileResponse) GoString() string {
	return s.String()
}

func (s *OSSCreateFileResponse) SetDomainId(v string) *OSSCreateFileResponse {
	s.DomainId = &v
	return s
}

func (s *OSSCreateFileResponse) SetDriveId(v string) *OSSCreateFileResponse {
	s.DriveId = &v
	return s
}

func (s *OSSCreateFileResponse) SetFilePath(v string) *OSSCreateFileResponse {
	s.FilePath = &v
	return s
}

func (s *OSSCreateFileResponse) SetPartInfoList(v []*UploadPartInfo) *OSSCreateFileResponse {
	s.PartInfoList = v
	return s
}

func (s *OSSCreateFileResponse) SetShareId(v string) *OSSCreateFileResponse {
	s.ShareId = &v
	return s
}

func (s *OSSCreateFileResponse) SetType(v string) *OSSCreateFileResponse {
	s.Type = &v
	return s
}

func (s *OSSCreateFileResponse) SetUploadId(v string) *OSSCreateFileResponse {
	s.UploadId = &v
	return s
}

/**
 * 删除文件 response
 */
type OSSDeleteFileResponse struct {
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

func (s OSSDeleteFileResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSDeleteFileResponse) GoString() string {
	return s.String()
}

func (s *OSSDeleteFileResponse) SetAsyncTaskId(v string) *OSSDeleteFileResponse {
	s.AsyncTaskId = &v
	return s
}

func (s *OSSDeleteFileResponse) SetDomainId(v string) *OSSDeleteFileResponse {
	s.DomainId = &v
	return s
}

func (s *OSSDeleteFileResponse) SetDriveId(v string) *OSSDeleteFileResponse {
	s.DriveId = &v
	return s
}

func (s *OSSDeleteFileResponse) SetFilePath(v string) *OSSDeleteFileResponse {
	s.FilePath = &v
	return s
}

func (s *OSSDeleteFileResponse) SetShareId(v string) *OSSDeleteFileResponse {
	s.ShareId = &v
	return s
}

/**
 * 批量删除文件 response
 */
type OSSDeleteFilesResponse struct {
	// deleted_file_id_list
	DeletedFileIdList []*string `json:"deleted_file_id_list,omitempty" xml:"deleted_file_id_list,omitempty" type:"Repeated"`
	// domain_id
	DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty" pattern:"[a-z0-9A-Z]+"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
	// share_id
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9]+"`
}

func (s OSSDeleteFilesResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSDeleteFilesResponse) GoString() string {
	return s.String()
}

func (s *OSSDeleteFilesResponse) SetDeletedFileIdList(v []*string) *OSSDeleteFilesResponse {
	s.DeletedFileIdList = v
	return s
}

func (s *OSSDeleteFilesResponse) SetDomainId(v string) *OSSDeleteFilesResponse {
	s.DomainId = &v
	return s
}

func (s *OSSDeleteFilesResponse) SetDriveId(v string) *OSSDeleteFilesResponse {
	s.DriveId = &v
	return s
}

func (s *OSSDeleteFilesResponse) SetShareId(v string) *OSSDeleteFilesResponse {
	s.ShareId = &v
	return s
}

/**
 * 获取download url response
 */
type OSSGetDownloadUrlResponse struct {
	// expiration
	Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
	// method
	Method *string `json:"method,omitempty" xml:"method,omitempty"`
	// url
	Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s OSSGetDownloadUrlResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSGetDownloadUrlResponse) GoString() string {
	return s.String()
}

func (s *OSSGetDownloadUrlResponse) SetExpiration(v string) *OSSGetDownloadUrlResponse {
	s.Expiration = &v
	return s
}

func (s *OSSGetDownloadUrlResponse) SetMethod(v string) *OSSGetDownloadUrlResponse {
	s.Method = &v
	return s
}

func (s *OSSGetDownloadUrlResponse) SetUrl(v string) *OSSGetDownloadUrlResponse {
	s.Url = &v
	return s
}

/**
 * 获取文件元数据response
 */
type OSSGetFileResponse struct {
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

func (s OSSGetFileResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSGetFileResponse) GoString() string {
	return s.String()
}

func (s *OSSGetFileResponse) SetContentHash(v string) *OSSGetFileResponse {
	s.ContentHash = &v
	return s
}

func (s *OSSGetFileResponse) SetContentHashName(v string) *OSSGetFileResponse {
	s.ContentHashName = &v
	return s
}

func (s *OSSGetFileResponse) SetContentType(v string) *OSSGetFileResponse {
	s.ContentType = &v
	return s
}

func (s *OSSGetFileResponse) SetCrc64Hash(v string) *OSSGetFileResponse {
	s.Crc64Hash = &v
	return s
}

func (s *OSSGetFileResponse) SetCreatedAt(v string) *OSSGetFileResponse {
	s.CreatedAt = &v
	return s
}

func (s *OSSGetFileResponse) SetDescription(v string) *OSSGetFileResponse {
	s.Description = &v
	return s
}

func (s *OSSGetFileResponse) SetDomainId(v string) *OSSGetFileResponse {
	s.DomainId = &v
	return s
}

func (s *OSSGetFileResponse) SetDownloadUrl(v string) *OSSGetFileResponse {
	s.DownloadUrl = &v
	return s
}

func (s *OSSGetFileResponse) SetDriveId(v string) *OSSGetFileResponse {
	s.DriveId = &v
	return s
}

func (s *OSSGetFileResponse) SetFileExtension(v string) *OSSGetFileResponse {
	s.FileExtension = &v
	return s
}

func (s *OSSGetFileResponse) SetFilePath(v string) *OSSGetFileResponse {
	s.FilePath = &v
	return s
}

func (s *OSSGetFileResponse) SetName(v string) *OSSGetFileResponse {
	s.Name = &v
	return s
}

func (s *OSSGetFileResponse) SetParentFilePath(v string) *OSSGetFileResponse {
	s.ParentFilePath = &v
	return s
}

func (s *OSSGetFileResponse) SetShareId(v string) *OSSGetFileResponse {
	s.ShareId = &v
	return s
}

func (s *OSSGetFileResponse) SetSize(v int64) *OSSGetFileResponse {
	s.Size = &v
	return s
}

func (s *OSSGetFileResponse) SetStatus(v string) *OSSGetFileResponse {
	s.Status = &v
	return s
}

func (s *OSSGetFileResponse) SetThumbnail(v string) *OSSGetFileResponse {
	s.Thumbnail = &v
	return s
}

func (s *OSSGetFileResponse) SetTrashedAt(v string) *OSSGetFileResponse {
	s.TrashedAt = &v
	return s
}

func (s *OSSGetFileResponse) SetType(v string) *OSSGetFileResponse {
	s.Type = &v
	return s
}

func (s *OSSGetFileResponse) SetUpdatedAt(v string) *OSSGetFileResponse {
	s.UpdatedAt = &v
	return s
}

func (s *OSSGetFileResponse) SetUploadId(v string) *OSSGetFileResponse {
	s.UploadId = &v
	return s
}

func (s *OSSGetFileResponse) SetUrl(v string) *OSSGetFileResponse {
	s.Url = &v
	return s
}

/**
 * 获取secure url response
 */
type OSSGetSecureUrlResponse struct {
	// expiration
	Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
	// url
	Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s OSSGetSecureUrlResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSGetSecureUrlResponse) GoString() string {
	return s.String()
}

func (s *OSSGetSecureUrlResponse) SetExpiration(v string) *OSSGetSecureUrlResponse {
	s.Expiration = &v
	return s
}

func (s *OSSGetSecureUrlResponse) SetUrl(v string) *OSSGetSecureUrlResponse {
	s.Url = &v
	return s
}

/**
 * Get UploadUrl Response
 */
type OSSGetUploadUrlResponse struct {
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

func (s OSSGetUploadUrlResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSGetUploadUrlResponse) GoString() string {
	return s.String()
}

func (s *OSSGetUploadUrlResponse) SetCreateAt(v string) *OSSGetUploadUrlResponse {
	s.CreateAt = &v
	return s
}

func (s *OSSGetUploadUrlResponse) SetDomainId(v string) *OSSGetUploadUrlResponse {
	s.DomainId = &v
	return s
}

func (s *OSSGetUploadUrlResponse) SetDriveId(v string) *OSSGetUploadUrlResponse {
	s.DriveId = &v
	return s
}

func (s *OSSGetUploadUrlResponse) SetFilePath(v string) *OSSGetUploadUrlResponse {
	s.FilePath = &v
	return s
}

func (s *OSSGetUploadUrlResponse) SetPartInfoList(v []*UploadPartInfo) *OSSGetUploadUrlResponse {
	s.PartInfoList = v
	return s
}

func (s *OSSGetUploadUrlResponse) SetUploadId(v string) *OSSGetUploadUrlResponse {
	s.UploadId = &v
	return s
}

/**
 * List file response
 */
type OSSListFileResponse struct {
	// items
	Items []*BaseOSSFileResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
	// next_marker
	NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s OSSListFileResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSListFileResponse) GoString() string {
	return s.String()
}

func (s *OSSListFileResponse) SetItems(v []*BaseOSSFileResponse) *OSSListFileResponse {
	s.Items = v
	return s
}

func (s *OSSListFileResponse) SetNextMarker(v string) *OSSListFileResponse {
	s.NextMarker = &v
	return s
}

/**
 * 获取签名 response
 */
type OSSListUploadedPartResponse struct {
	// file_path
	FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
	// next_part_number_marker
	NextPartNumberMarker *string `json:"next_part_number_marker,omitempty" xml:"next_part_number_marker,omitempty"`
	// upload_id
	UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
	// uploaded_parts
	UploadedParts []*UploadPartInfo `json:"uploaded_parts,omitempty" xml:"uploaded_parts,omitempty" type:"Repeated"`
}

func (s OSSListUploadedPartResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSListUploadedPartResponse) GoString() string {
	return s.String()
}

func (s *OSSListUploadedPartResponse) SetFilePath(v string) *OSSListUploadedPartResponse {
	s.FilePath = &v
	return s
}

func (s *OSSListUploadedPartResponse) SetNextPartNumberMarker(v string) *OSSListUploadedPartResponse {
	s.NextPartNumberMarker = &v
	return s
}

func (s *OSSListUploadedPartResponse) SetUploadId(v string) *OSSListUploadedPartResponse {
	s.UploadId = &v
	return s
}

func (s *OSSListUploadedPartResponse) SetUploadedParts(v []*UploadPartInfo) *OSSListUploadedPartResponse {
	s.UploadedParts = v
	return s
}

/**
 * 文件移动 response
 */
type OSSMoveFileResponse struct {
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

func (s OSSMoveFileResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSMoveFileResponse) GoString() string {
	return s.String()
}

func (s *OSSMoveFileResponse) SetAsyncTaskId(v string) *OSSMoveFileResponse {
	s.AsyncTaskId = &v
	return s
}

func (s *OSSMoveFileResponse) SetDomainId(v string) *OSSMoveFileResponse {
	s.DomainId = &v
	return s
}

func (s *OSSMoveFileResponse) SetDriveId(v string) *OSSMoveFileResponse {
	s.DriveId = &v
	return s
}

func (s *OSSMoveFileResponse) SetFilePath(v string) *OSSMoveFileResponse {
	s.FilePath = &v
	return s
}

func (s *OSSMoveFileResponse) SetShareId(v string) *OSSMoveFileResponse {
	s.ShareId = &v
	return s
}

/**
 * search file response
 */
type OSSSearchFileResponse struct {
	// items
	Items []*BaseOSSFileResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
	// next_marker
	NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s OSSSearchFileResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSSearchFileResponse) GoString() string {
	return s.String()
}

func (s *OSSSearchFileResponse) SetItems(v []*BaseOSSFileResponse) *OSSSearchFileResponse {
	s.Items = v
	return s
}

func (s *OSSSearchFileResponse) SetNextMarker(v string) *OSSSearchFileResponse {
	s.NextMarker = &v
	return s
}

/**
 * 更新文件元数据 response
 */
type OSSUpdateFileMetaResponse struct {
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

func (s OSSUpdateFileMetaResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSUpdateFileMetaResponse) GoString() string {
	return s.String()
}

func (s *OSSUpdateFileMetaResponse) SetContentHash(v string) *OSSUpdateFileMetaResponse {
	s.ContentHash = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetContentHashName(v string) *OSSUpdateFileMetaResponse {
	s.ContentHashName = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetContentType(v string) *OSSUpdateFileMetaResponse {
	s.ContentType = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetCrc64Hash(v string) *OSSUpdateFileMetaResponse {
	s.Crc64Hash = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetCreatedAt(v string) *OSSUpdateFileMetaResponse {
	s.CreatedAt = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetDescription(v string) *OSSUpdateFileMetaResponse {
	s.Description = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetDomainId(v string) *OSSUpdateFileMetaResponse {
	s.DomainId = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetDownloadUrl(v string) *OSSUpdateFileMetaResponse {
	s.DownloadUrl = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetDriveId(v string) *OSSUpdateFileMetaResponse {
	s.DriveId = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetFileExtension(v string) *OSSUpdateFileMetaResponse {
	s.FileExtension = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetFilePath(v string) *OSSUpdateFileMetaResponse {
	s.FilePath = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetName(v string) *OSSUpdateFileMetaResponse {
	s.Name = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetParentFilePath(v string) *OSSUpdateFileMetaResponse {
	s.ParentFilePath = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetShareId(v string) *OSSUpdateFileMetaResponse {
	s.ShareId = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetSize(v int64) *OSSUpdateFileMetaResponse {
	s.Size = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetStatus(v string) *OSSUpdateFileMetaResponse {
	s.Status = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetThumbnail(v string) *OSSUpdateFileMetaResponse {
	s.Thumbnail = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetTrashedAt(v string) *OSSUpdateFileMetaResponse {
	s.TrashedAt = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetType(v string) *OSSUpdateFileMetaResponse {
	s.Type = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetUpdatedAt(v string) *OSSUpdateFileMetaResponse {
	s.UpdatedAt = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetUploadId(v string) *OSSUpdateFileMetaResponse {
	s.UploadId = &v
	return s
}

func (s *OSSUpdateFileMetaResponse) SetUrl(v string) *OSSUpdateFileMetaResponse {
	s.Url = &v
	return s
}

/**
 * DRM License response
 */
type OSSVideoDRMLicenseResponse struct {
	// drm_data
	Data *string `json:"data,omitempty" xml:"data,omitempty" require:"true"`
	// states
	States *int64 `json:"states,omitempty" xml:"states,omitempty" require:"true"`
}

func (s OSSVideoDRMLicenseResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSVideoDRMLicenseResponse) GoString() string {
	return s.String()
}

func (s *OSSVideoDRMLicenseResponse) SetData(v string) *OSSVideoDRMLicenseResponse {
	s.Data = &v
	return s
}

func (s *OSSVideoDRMLicenseResponse) SetStates(v int64) *OSSVideoDRMLicenseResponse {
	s.States = &v
	return s
}

/**
 * 转码接口response
 */
type OSSVideoDefinitionResponse struct {
	// definition_list
	DefinitionList []*string `json:"definition_list,omitempty" xml:"definition_list,omitempty" type:"Repeated"`
	// frame_rate
	FrameRate *string `json:"frame_rate,omitempty" xml:"frame_rate,omitempty"`
}

func (s OSSVideoDefinitionResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSVideoDefinitionResponse) GoString() string {
	return s.String()
}

func (s *OSSVideoDefinitionResponse) SetDefinitionList(v []*string) *OSSVideoDefinitionResponse {
	s.DefinitionList = v
	return s
}

func (s *OSSVideoDefinitionResponse) SetFrameRate(v string) *OSSVideoDefinitionResponse {
	s.FrameRate = &v
	return s
}

/**
 * 转码接口response
 */
type OSSVideoTranscodeResponse struct {
	// definition_list
	DefinitionList []*string `json:"definition_list,omitempty" xml:"definition_list,omitempty" type:"Repeated"`
	// duration
	Duration *int64 `json:"duration,omitempty" xml:"duration,omitempty"`
	// hls_time
	HlsTime *int64 `json:"hls_time,omitempty" xml:"hls_time,omitempty"`
}

func (s OSSVideoTranscodeResponse) String() string {
	return tea.Prettify(s)
}

func (s OSSVideoTranscodeResponse) GoString() string {
	return s.String()
}

func (s *OSSVideoTranscodeResponse) SetDefinitionList(v []*string) *OSSVideoTranscodeResponse {
	s.DefinitionList = v
	return s
}

func (s *OSSVideoTranscodeResponse) SetDuration(v int64) *OSSVideoTranscodeResponse {
	s.Duration = &v
	return s
}

func (s *OSSVideoTranscodeResponse) SetHlsTime(v int64) *OSSVideoTranscodeResponse {
	s.HlsTime = &v
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
 * 下载限速配置
 */
type RateLimit struct {
	PartSize  *int64 `json:"part_size,omitempty" xml:"part_size,omitempty"`
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
 *
 */
type RevokeRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// App ID, 当前访问的App
	AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
	// refresh token, 登录时返回的
	RefreshToken *string `json:"refresh_token,omitempty" xml:"refresh_token,omitempty" require:"true"`
}

func (s RevokeRequest) String() string {
	return tea.Prettify(s)
}

func (s RevokeRequest) GoString() string {
	return s.String()
}

func (s *RevokeRequest) SetHeaders(v map[string]*string) *RevokeRequest {
	s.Headers = v
	return s
}

func (s *RevokeRequest) SetAppId(v string) *RevokeRequest {
	s.AppId = &v
	return s
}

func (s *RevokeRequest) SetRefreshToken(v string) *RevokeRequest {
	s.RefreshToken = &v
	return s
}

/**
 * scan file meta response
 */
type ScanFileMetaResponse struct {
	// items
	Items []*BaseFileResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
	// next_marker
	NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ScanFileMetaResponse) String() string {
	return tea.Prettify(s)
}

func (s ScanFileMetaResponse) GoString() string {
	return s.String()
}

func (s *ScanFileMetaResponse) SetItems(v []*BaseFileResponse) *ScanFileMetaResponse {
	s.Items = v
	return s
}

func (s *ScanFileMetaResponse) SetNextMarker(v string) *ScanFileMetaResponse {
	s.NextMarker = &v
	return s
}

/**
 * search file response
 */
type SearchFileResponse struct {
	// items
	Items []*BaseFileResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
	// next_marker
	NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s SearchFileResponse) String() string {
	return tea.Prettify(s)
}

func (s SearchFileResponse) GoString() string {
	return s.String()
}

func (s *SearchFileResponse) SetItems(v []*BaseFileResponse) *SearchFileResponse {
	s.Items = v
	return s
}

func (s *SearchFileResponse) SetNextMarker(v string) *SearchFileResponse {
	s.NextMarker = &v
	return s
}

/**
 *
 */
type SharePermissionPolicy struct {
	FilePath              *string   `json:"file_path,omitempty" xml:"file_path,omitempty"`
	PermissionInheritable *bool     `json:"permission_inheritable,omitempty" xml:"permission_inheritable,omitempty"`
	PermissionList        []*string `json:"permission_list,omitempty" xml:"permission_list,omitempty" type:"Repeated"`
	PermissionType        *string   `json:"permission_type,omitempty" xml:"permission_type,omitempty"`
}

func (s SharePermissionPolicy) String() string {
	return tea.Prettify(s)
}

func (s SharePermissionPolicy) GoString() string {
	return s.String()
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
type StoreFile struct {
	DomainId       *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
	Name           *string `json:"name,omitempty" xml:"name,omitempty"`
	ParentFilePath *string `json:"parent_file_path,omitempty" xml:"parent_file_path,omitempty"`
	StoreId        *string `json:"store_id,omitempty" xml:"store_id,omitempty"`
	Type           *string `json:"type,omitempty" xml:"type,omitempty"`
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
	DomainId                   *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
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
type StreamInfo struct {
	// crc64_hash
	Crc64Hash *string `json:"crc64_hash,omitempty" xml:"crc64_hash,omitempty"`
	// download_url
	DownloadUrl *string `json:"download_url,omitempty" xml:"download_url,omitempty"`
	// thumbnail
	Thumbnail *string `json:"thumbnail,omitempty" xml:"thumbnail,omitempty"`
	// url
	Url *string `json:"url,omitempty" xml:"url,omitempty"`
}

func (s StreamInfo) String() string {
	return tea.Prettify(s)
}

func (s StreamInfo) GoString() string {
	return s.String()
}

func (s *StreamInfo) SetCrc64Hash(v string) *StreamInfo {
	s.Crc64Hash = &v
	return s
}

func (s *StreamInfo) SetDownloadUrl(v string) *StreamInfo {
	s.DownloadUrl = &v
	return s
}

func (s *StreamInfo) SetThumbnail(v string) *StreamInfo {
	s.Thumbnail = &v
	return s
}

func (s *StreamInfo) SetUrl(v string) *StreamInfo {
	s.Url = &v
	return s
}

/**
 *
 */
type StreamUploadInfo struct {
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
	Confidence   *int    `json:"confidence,omitempty" xml:"confidence,omitempty"`
	EnName       *string `json:"en_name,omitempty" xml:"en_name,omitempty"`
	Name         *string `json:"name,omitempty" xml:"name,omitempty"`
	ParentEnName *string `json:"parent_en_name,omitempty" xml:"parent_en_name,omitempty"`
	ParentName   *string `json:"parent_name,omitempty" xml:"parent_name,omitempty"`
	Selected     *bool   `json:"selected,omitempty" xml:"selected,omitempty"`
	TagLevel     *int64  `json:"tag_level,omitempty" xml:"tag_level,omitempty"`
}

func (s SystemTag) String() string {
	return tea.Prettify(s)
}

func (s SystemTag) GoString() string {
	return s.String()
}

func (s *SystemTag) SetConfidence(v int) *SystemTag {
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

func (s *SystemTag) SetSelected(v bool) *SystemTag {
	s.Selected = &v
	return s
}

func (s *SystemTag) SetTagLevel(v int64) *SystemTag {
	s.TagLevel = &v
	return s
}

/**
 *
 */
type TokenRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// addition_data
	AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
	// App ID, 当前访问的App
	AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
	// 只能填refresh_token
	GrantType *string `json:"grant_type,omitempty" xml:"grant_type,omitempty" require:"true"`
	// refresh token, 登录时返回的
	RefreshToken *string `json:"refresh_token,omitempty" xml:"refresh_token,omitempty" require:"true"`
}

func (s TokenRequest) String() string {
	return tea.Prettify(s)
}

func (s TokenRequest) GoString() string {
	return s.String()
}

func (s *TokenRequest) SetHeaders(v map[string]*string) *TokenRequest {
	s.Headers = v
	return s
}

func (s *TokenRequest) SetAdditionData(v map[string]interface{}) *TokenRequest {
	s.AdditionData = v
	return s
}

func (s *TokenRequest) SetAppId(v string) *TokenRequest {
	s.AppId = &v
	return s
}

func (s *TokenRequest) SetGrantType(v string) *TokenRequest {
	s.GrantType = &v
	return s
}

func (s *TokenRequest) SetRefreshToken(v string) *TokenRequest {
	s.RefreshToken = &v
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
	DriveType         *string `json:"drive_type,omitempty" xml:"drive_type,omitempty"`
	EncryptDataAccess *bool   `json:"encrypt_data_access,omitempty" xml:"encrypt_data_access,omitempty"`
	EncryptMode       *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
	// Drive 所有者
	Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
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
 * 更新文件元数据 response
 */
type UpdateFileMetaResponse struct {
	// category
	Category *string `json:"category,omitempty" xml:"category,omitempty"`
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
	Hidden             *bool               `json:"hidden,omitempty" xml:"hidden,omitempty"`
	ImageMediaMetadata *ImageMediaResponse `json:"image_media_metadata,omitempty" xml:"image_media_metadata,omitempty"`
	// labels
	Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
	Meta   *string   `json:"meta,omitempty" xml:"meta,omitempty"`
	// name
	Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" pattern:"[a-zA-Z0-9.-]{1,1000}"`
	// parent_file_id
	ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" maxLength:"50" minLength:"40" pattern:"[a-z0-9]{1,50}"`
	PunishFlag   *int    `json:"punish_flag,omitempty" xml:"punish_flag,omitempty"`
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
	UserMeta             *string               `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
	VideoMediaMetadata   *VideoMediaResponse   `json:"video_media_metadata,omitempty" xml:"video_media_metadata,omitempty"`
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

func (s *UpdateFileMetaResponse) SetPunishFlag(v int) *UpdateFileMetaResponse {
	s.PunishFlag = &v
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
	// permissions
	Permissions []*string `json:"permissions,omitempty" xml:"permissions,omitempty" type:"Repeated"`
	// share_path
	ShareFilePath *string `json:"share_file_path,omitempty" xml:"share_file_path,omitempty"`
	// share_id
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
	// share_name
	ShareName   *string                  `json:"share_name,omitempty" xml:"share_name,omitempty"`
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

func (s *UpdateShareResponse) SetPermissions(v []*string) *UpdateShareResponse {
	s.Permissions = v
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
	// etag
	Etag *string `json:"etag,omitempty" xml:"etag,omitempty"`
	// PartNumber
	PartNumber *int64 `json:"part_number,omitempty" xml:"part_number,omitempty" maximum:"10000" minimum:"1" pattern:"[0-9]+"`
	// PartSize：
	PartSize *int64 `json:"part_size,omitempty" xml:"part_size,omitempty" maximum:"5368709120" minimum:"102400"`
	// upload_url
	UploadUrl *string `json:"upload_url,omitempty" xml:"upload_url,omitempty"`
}

func (s UploadPartInfo) String() string {
	return tea.Prettify(s)
}

func (s UploadPartInfo) GoString() string {
	return s.String()
}

func (s *UploadPartInfo) SetEtag(v string) *UploadPartInfo {
	s.Etag = &v
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

/**
 *
 */
type VerifyCodeRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// App ID, 当前访问的App
	AppId *string `json:"app_id,omitempty" xml:"app_id,omitempty" require:"true"`
	// 手机号
	PhoneNumber *string `json:"phone_number,omitempty" xml:"phone_number,omitempty" require:"true"`
	// 国家编号，默认86，不需要填+号，直接填数字
	PhoneRegion *string `json:"phone_region,omitempty" xml:"phone_region,omitempty"`
	// 短信验证码内容
	SmsCode *string `json:"sms_code,omitempty" xml:"sms_code,omitempty" require:"true"`
	// 短信验证码ID
	SmsCodeId *string `json:"sms_code_id,omitempty" xml:"sms_code_id,omitempty" require:"true"`
	// 需要被校验内容的类型
	VerifyType *string `json:"verify_type,omitempty" xml:"verify_type,omitempty"`
}

func (s VerifyCodeRequest) String() string {
	return tea.Prettify(s)
}

func (s VerifyCodeRequest) GoString() string {
	return s.String()
}

func (s *VerifyCodeRequest) SetHeaders(v map[string]*string) *VerifyCodeRequest {
	s.Headers = v
	return s
}

func (s *VerifyCodeRequest) SetAppId(v string) *VerifyCodeRequest {
	s.AppId = &v
	return s
}

func (s *VerifyCodeRequest) SetPhoneNumber(v string) *VerifyCodeRequest {
	s.PhoneNumber = &v
	return s
}

func (s *VerifyCodeRequest) SetPhoneRegion(v string) *VerifyCodeRequest {
	s.PhoneRegion = &v
	return s
}

func (s *VerifyCodeRequest) SetSmsCode(v string) *VerifyCodeRequest {
	s.SmsCode = &v
	return s
}

func (s *VerifyCodeRequest) SetSmsCodeId(v string) *VerifyCodeRequest {
	s.SmsCodeId = &v
	return s
}

func (s *VerifyCodeRequest) SetVerifyType(v string) *VerifyCodeRequest {
	s.VerifyType = &v
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
	// location
	Location *string `json:"location,omitempty" xml:"location,omitempty"`
	// province
	Province *string `json:"province,omitempty" xml:"province,omitempty"`
	// time
	Time *string `json:"time,omitempty" xml:"time,omitempty"`
	// township
	Township              *string                  `json:"township,omitempty" xml:"township,omitempty"`
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

/**
 *
 */
type VideoPreviewResponse struct {
	// audio_format
	AudioFormat *string `json:"audio_format,omitempty" xml:"audio_format,omitempty"`
	// bitrate
	Bitrate *string `json:"bitrate,omitempty" xml:"bitrate,omitempty"`
	// duration
	Duration *string `json:"duration,omitempty" xml:"duration,omitempty"`
	// frame_rate
	FrameRate *string `json:"frame_rate,omitempty" xml:"frame_rate,omitempty"`
	// height
	Height     *int64              `json:"height,omitempty" xml:"height,omitempty"`
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

func (s *VideoPreviewResponse) SetAudioFormat(v string) *VideoPreviewResponse {
	s.AudioFormat = &v
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
	// status
	Status *string `json:"status,omitempty" xml:"status,omitempty"`
}

func (s VideoPreviewSprite) String() string {
	return tea.Prettify(s)
}

func (s VideoPreviewSprite) GoString() string {
	return s.String()
}

func (s *VideoPreviewSprite) SetCol(v int64) *VideoPreviewSprite {
	s.Col = &v
	return s
}

func (s *VideoPreviewSprite) SetCount(v int64) *VideoPreviewSprite {
	s.Count = &v
	return s
}

func (s *VideoPreviewSprite) SetFrameCount(v int64) *VideoPreviewSprite {
	s.FrameCount = &v
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

func (s *VideoPreviewSprite) SetRow(v int64) *VideoPreviewSprite {
	s.Row = &v
	return s
}

func (s *VideoPreviewSprite) SetStatus(v string) *VideoPreviewSprite {
	s.Status = &v
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

type AdminListStoresModel struct {
	Headers map[string]*string  `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *ListStoresResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s AdminListStoresModel) String() string {
	return tea.Prettify(s)
}

func (s AdminListStoresModel) GoString() string {
	return s.String()
}

func (s *AdminListStoresModel) SetHeaders(v map[string]*string) *AdminListStoresModel {
	s.Headers = v
	return s
}

func (s *AdminListStoresModel) SetBody(v *ListStoresResponse) *AdminListStoresModel {
	s.Body = v
	return s
}

type GetUserAccessTokenModel struct {
	Headers map[string]*string   `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *AccessTokenResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetUserAccessTokenModel) String() string {
	return tea.Prettify(s)
}

func (s GetUserAccessTokenModel) GoString() string {
	return s.String()
}

func (s *GetUserAccessTokenModel) SetHeaders(v map[string]*string) *GetUserAccessTokenModel {
	s.Headers = v
	return s
}

func (s *GetUserAccessTokenModel) SetBody(v *AccessTokenResponse) *GetUserAccessTokenModel {
	s.Body = v
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
type AdminListStoresRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s AdminListStoresRequest) String() string {
	return tea.Prettify(s)
}

func (s AdminListStoresRequest) GoString() string {
	return s.String()
}

func (s *AdminListStoresRequest) SetHeaders(v map[string]*string) *AdminListStoresRequest {
	s.Headers = v
	return s
}

/**
 *
 */
type AppAccessStrategy struct {
	Effect          *string   `json:"effect,omitempty" xml:"effect,omitempty"`
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
	AppId             *string                `json:"app_id,omitempty" xml:"app_id,omitempty"`
	AppSecret         *string                `json:"app_secret,omitempty" xml:"app_secret,omitempty"`
	CallbackSecurity  *bool                  `json:"callback_security,omitempty" xml:"callback_security,omitempty"`
	Enable            *bool                  `json:"enable,omitempty" xml:"enable,omitempty"`
	Endpoint          *string                `json:"endpoint,omitempty" xml:"endpoint,omitempty"`
	EnterpriseId      *string                `json:"enterprise_id,omitempty" xml:"enterprise_id,omitempty"`
	LoginPageHeaders  map[string]interface{} `json:"login_page_headers,omitempty" xml:"login_page_headers,omitempty"`
	LoginPageTemplate *string                `json:"login_page_template,omitempty" xml:"login_page_template,omitempty"`
	LoginPageVars     map[string]interface{} `json:"login_page_vars,omitempty" xml:"login_page_vars,omitempty"`
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

/**
 * base domain response
 */
type BaseDomainResponse struct {
	// Domain CName
	ApiCname *string `json:"api_cname,omitempty" xml:"api_cname,omitempty"`
	// 支付宝 App Id
	AuthAlipayAppId *string `json:"auth_alipay_app_id,omitempty" xml:"auth_alipay_app_id,omitempty"`
	// 是否开启了支付宝认证
	AuthAlipayEnable *bool `json:"auth_alipay_enable,omitempty" xml:"auth_alipay_enable,omitempty"`
	// 支付宝 App Secret
	AuthAlipayPrivateKey *string `json:"auth_alipay_private_key,omitempty" xml:"auth_alipay_private_key,omitempty"`
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
	PathType                   *string            `json:"path_type,omitempty" xml:"path_type,omitempty"`
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
 * create domain response
 */
type CreateDomainResponse struct {
	// Domain CName
	ApiCname *string `json:"api_cname,omitempty" xml:"api_cname,omitempty"`
	// 支付宝 App Id
	AuthAlipayAppId *string `json:"auth_alipay_app_id,omitempty" xml:"auth_alipay_app_id,omitempty"`
	// 是否开启了支付宝认证
	AuthAlipayEnable *bool `json:"auth_alipay_enable,omitempty" xml:"auth_alipay_enable,omitempty"`
	// 支付宝 App Secret
	AuthAlipayPrivateKey *string `json:"auth_alipay_private_key,omitempty" xml:"auth_alipay_private_key,omitempty"`
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
	PathType                   *string            `json:"path_type,omitempty" xml:"path_type,omitempty"`
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
type GetBizCNameInfoResponse struct {
	// biz cname
	BizCname *string `json:"biz_cname,omitempty" xml:"biz_cname,omitempty"`
	// cert name
	CertId *string `json:"cert_id,omitempty" xml:"cert_id,omitempty"`
	// cert name
	CertName    *string      `json:"cert_name,omitempty" xml:"cert_name,omitempty"`
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
 * get domain response
 */
type GetDomainResponse struct {
	// Domain CName
	ApiCname *string `json:"api_cname,omitempty" xml:"api_cname,omitempty"`
	// 支付宝 App Id
	AuthAlipayAppId *string `json:"auth_alipay_app_id,omitempty" xml:"auth_alipay_app_id,omitempty"`
	// 是否开启了支付宝认证
	AuthAlipayEnable *bool `json:"auth_alipay_enable,omitempty" xml:"auth_alipay_enable,omitempty"`
	// 支付宝 App Secret
	AuthAlipayPrivateKey *string `json:"auth_alipay_private_key,omitempty" xml:"auth_alipay_private_key,omitempty"`
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
	PathType                   *string            `json:"path_type,omitempty" xml:"path_type,omitempty"`
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
type GetUserAccessTokenRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 角色
	Role *string `json:"role,omitempty" xml:"role,omitempty"`
	// 用户 ID
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty" require:"true"`
}

func (s GetUserAccessTokenRequest) String() string {
	return tea.Prettify(s)
}

func (s GetUserAccessTokenRequest) GoString() string {
	return s.String()
}

func (s *GetUserAccessTokenRequest) SetHeaders(v map[string]*string) *GetUserAccessTokenRequest {
	s.Headers = v
	return s
}

func (s *GetUserAccessTokenRequest) SetRole(v string) *GetUserAccessTokenRequest {
	s.Role = &v
	return s
}

func (s *GetUserAccessTokenRequest) SetUserId(v string) *GetUserAccessTokenRequest {
	s.UserId = &v
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
type SetBizCNameResponse struct {
	// biz cname
	BizCname    *string      `json:"biz_cname,omitempty" xml:"biz_cname,omitempty"`
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
 * create domain response
 */
type UpdateDomainResponse struct {
	// Domain CName
	ApiCname *string `json:"api_cname,omitempty" xml:"api_cname,omitempty"`
	// 支付宝 App Id
	AuthAlipayAppId *string `json:"auth_alipay_app_id,omitempty" xml:"auth_alipay_app_id,omitempty"`
	// 是否开启了支付宝认证
	AuthAlipayEnable *bool `json:"auth_alipay_enable,omitempty" xml:"auth_alipay_enable,omitempty"`
	// 支付宝 App Secret
	AuthAlipayPrivateKey *string `json:"auth_alipay_private_key,omitempty" xml:"auth_alipay_private_key,omitempty"`
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
	PathType                   *string            `json:"path_type,omitempty" xml:"path_type,omitempty"`
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

type CreateDriveModel struct {
	Headers map[string]*string   `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *CreateDriveResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s CreateDriveModel) String() string {
	return tea.Prettify(s)
}

func (s CreateDriveModel) GoString() string {
	return s.String()
}

func (s *CreateDriveModel) SetHeaders(v map[string]*string) *CreateDriveModel {
	s.Headers = v
	return s
}

func (s *CreateDriveModel) SetBody(v *CreateDriveResponse) *CreateDriveModel {
	s.Body = v
	return s
}

type DeleteDriveModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s DeleteDriveModel) String() string {
	return tea.Prettify(s)
}

func (s DeleteDriveModel) GoString() string {
	return s.String()
}

func (s *DeleteDriveModel) SetHeaders(v map[string]*string) *DeleteDriveModel {
	s.Headers = v
	return s
}

type GetDriveModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *GetDriveResponse  `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetDriveModel) String() string {
	return tea.Prettify(s)
}

func (s GetDriveModel) GoString() string {
	return s.String()
}

func (s *GetDriveModel) SetHeaders(v map[string]*string) *GetDriveModel {
	s.Headers = v
	return s
}

func (s *GetDriveModel) SetBody(v *GetDriveResponse) *GetDriveModel {
	s.Body = v
	return s
}

type GetDefaultDriveModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *GetDriveResponse  `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetDefaultDriveModel) String() string {
	return tea.Prettify(s)
}

func (s GetDefaultDriveModel) GoString() string {
	return s.String()
}

func (s *GetDefaultDriveModel) SetHeaders(v map[string]*string) *GetDefaultDriveModel {
	s.Headers = v
	return s
}

func (s *GetDefaultDriveModel) SetBody(v *GetDriveResponse) *GetDefaultDriveModel {
	s.Body = v
	return s
}

type ListDrivesModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *ListDriveResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ListDrivesModel) String() string {
	return tea.Prettify(s)
}

func (s ListDrivesModel) GoString() string {
	return s.String()
}

func (s *ListDrivesModel) SetHeaders(v map[string]*string) *ListDrivesModel {
	s.Headers = v
	return s
}

func (s *ListDrivesModel) SetBody(v *ListDriveResponse) *ListDrivesModel {
	s.Body = v
	return s
}

type ListMyDrivesModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *ListDriveResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ListMyDrivesModel) String() string {
	return tea.Prettify(s)
}

func (s ListMyDrivesModel) GoString() string {
	return s.String()
}

func (s *ListMyDrivesModel) SetHeaders(v map[string]*string) *ListMyDrivesModel {
	s.Headers = v
	return s
}

func (s *ListMyDrivesModel) SetBody(v *ListDriveResponse) *ListMyDrivesModel {
	s.Body = v
	return s
}

type UpdateDriveModel struct {
	Headers map[string]*string   `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *UpdateDriveResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s UpdateDriveModel) String() string {
	return tea.Prettify(s)
}

func (s UpdateDriveModel) GoString() string {
	return s.String()
}

func (s *UpdateDriveModel) SetHeaders(v map[string]*string) *UpdateDriveModel {
	s.Headers = v
	return s
}

func (s *UpdateDriveModel) SetBody(v *UpdateDriveResponse) *UpdateDriveModel {
	s.Body = v
	return s
}

type CompleteFileModel struct {
	Headers map[string]*string           `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingCompleteFileResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s CompleteFileModel) String() string {
	return tea.Prettify(s)
}

func (s CompleteFileModel) GoString() string {
	return s.String()
}

func (s *CompleteFileModel) SetHeaders(v map[string]*string) *CompleteFileModel {
	s.Headers = v
	return s
}

func (s *CompleteFileModel) SetBody(v *HostingCompleteFileResponse) *CompleteFileModel {
	s.Body = v
	return s
}

type CopyFileModel struct {
	Headers map[string]*string       `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingCopyFileResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s CopyFileModel) String() string {
	return tea.Prettify(s)
}

func (s CopyFileModel) GoString() string {
	return s.String()
}

func (s *CopyFileModel) SetHeaders(v map[string]*string) *CopyFileModel {
	s.Headers = v
	return s
}

func (s *CopyFileModel) SetBody(v *HostingCopyFileResponse) *CopyFileModel {
	s.Body = v
	return s
}

type CreateFileModel struct {
	Headers map[string]*string         `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingCreateFileResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s CreateFileModel) String() string {
	return tea.Prettify(s)
}

func (s CreateFileModel) GoString() string {
	return s.String()
}

func (s *CreateFileModel) SetHeaders(v map[string]*string) *CreateFileModel {
	s.Headers = v
	return s
}

func (s *CreateFileModel) SetBody(v *HostingCreateFileResponse) *CreateFileModel {
	s.Body = v
	return s
}

type DeleteFileModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s DeleteFileModel) String() string {
	return tea.Prettify(s)
}

func (s DeleteFileModel) GoString() string {
	return s.String()
}

func (s *DeleteFileModel) SetHeaders(v map[string]*string) *DeleteFileModel {
	s.Headers = v
	return s
}

type GetFileModel struct {
	Headers map[string]*string      `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingGetFileResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetFileModel) String() string {
	return tea.Prettify(s)
}

func (s GetFileModel) GoString() string {
	return s.String()
}

func (s *GetFileModel) SetHeaders(v map[string]*string) *GetFileModel {
	s.Headers = v
	return s
}

func (s *GetFileModel) SetBody(v *HostingGetFileResponse) *GetFileModel {
	s.Body = v
	return s
}

type GetDownloadUrlModel struct {
	Headers map[string]*string             `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingGetDownloadUrlResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetDownloadUrlModel) String() string {
	return tea.Prettify(s)
}

func (s GetDownloadUrlModel) GoString() string {
	return s.String()
}

func (s *GetDownloadUrlModel) SetHeaders(v map[string]*string) *GetDownloadUrlModel {
	s.Headers = v
	return s
}

func (s *GetDownloadUrlModel) SetBody(v *HostingGetDownloadUrlResponse) *GetDownloadUrlModel {
	s.Body = v
	return s
}

type GetSecureUrlModel struct {
	Headers map[string]*string           `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingGetSecureUrlResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetSecureUrlModel) String() string {
	return tea.Prettify(s)
}

func (s GetSecureUrlModel) GoString() string {
	return s.String()
}

func (s *GetSecureUrlModel) SetHeaders(v map[string]*string) *GetSecureUrlModel {
	s.Headers = v
	return s
}

func (s *GetSecureUrlModel) SetBody(v *HostingGetSecureUrlResponse) *GetSecureUrlModel {
	s.Body = v
	return s
}

type GetUploadUrlModel struct {
	Headers map[string]*string           `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingGetUploadUrlResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetUploadUrlModel) String() string {
	return tea.Prettify(s)
}

func (s GetUploadUrlModel) GoString() string {
	return s.String()
}

func (s *GetUploadUrlModel) SetHeaders(v map[string]*string) *GetUploadUrlModel {
	s.Headers = v
	return s
}

func (s *GetUploadUrlModel) SetBody(v *HostingGetUploadUrlResponse) *GetUploadUrlModel {
	s.Body = v
	return s
}

type ListFileModel struct {
	Headers map[string]*string       `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingListFileResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ListFileModel) String() string {
	return tea.Prettify(s)
}

func (s ListFileModel) GoString() string {
	return s.String()
}

func (s *ListFileModel) SetHeaders(v map[string]*string) *ListFileModel {
	s.Headers = v
	return s
}

func (s *ListFileModel) SetBody(v *HostingListFileResponse) *ListFileModel {
	s.Body = v
	return s
}

type ListUploadedPartsModel struct {
	Headers map[string]*string               `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingListUploadedPartResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ListUploadedPartsModel) String() string {
	return tea.Prettify(s)
}

func (s ListUploadedPartsModel) GoString() string {
	return s.String()
}

func (s *ListUploadedPartsModel) SetHeaders(v map[string]*string) *ListUploadedPartsModel {
	s.Headers = v
	return s
}

func (s *ListUploadedPartsModel) SetBody(v *HostingListUploadedPartResponse) *ListUploadedPartsModel {
	s.Body = v
	return s
}

type MoveFileModel struct {
	Headers map[string]*string       `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingMoveFileResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s MoveFileModel) String() string {
	return tea.Prettify(s)
}

func (s MoveFileModel) GoString() string {
	return s.String()
}

func (s *MoveFileModel) SetHeaders(v map[string]*string) *MoveFileModel {
	s.Headers = v
	return s
}

func (s *MoveFileModel) SetBody(v *HostingMoveFileResponse) *MoveFileModel {
	s.Body = v
	return s
}

type VideoDefinitionModel struct {
	Headers map[string]*string              `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingVideoDefinitionResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s VideoDefinitionModel) String() string {
	return tea.Prettify(s)
}

func (s VideoDefinitionModel) GoString() string {
	return s.String()
}

func (s *VideoDefinitionModel) SetHeaders(v map[string]*string) *VideoDefinitionModel {
	s.Headers = v
	return s
}

func (s *VideoDefinitionModel) SetBody(v *HostingVideoDefinitionResponse) *VideoDefinitionModel {
	s.Body = v
	return s
}

type VideoLicenseModel struct {
	Headers map[string]*string              `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingVideoDRMLicenseResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s VideoLicenseModel) String() string {
	return tea.Prettify(s)
}

func (s VideoLicenseModel) GoString() string {
	return s.String()
}

func (s *VideoLicenseModel) SetHeaders(v map[string]*string) *VideoLicenseModel {
	s.Headers = v
	return s
}

func (s *VideoLicenseModel) SetBody(v *HostingVideoDRMLicenseResponse) *VideoLicenseModel {
	s.Body = v
	return s
}

type VideoM3u8Model struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    []byte             `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s VideoM3u8Model) String() string {
	return tea.Prettify(s)
}

func (s VideoM3u8Model) GoString() string {
	return s.String()
}

func (s *VideoM3u8Model) SetHeaders(v map[string]*string) *VideoM3u8Model {
	s.Headers = v
	return s
}

func (s *VideoM3u8Model) SetBody(v []byte) *VideoM3u8Model {
	s.Body = v
	return s
}

type VideoTranscodeModel struct {
	Headers map[string]*string             `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *HostingVideoTranscodeResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s VideoTranscodeModel) String() string {
	return tea.Prettify(s)
}

func (s VideoTranscodeModel) GoString() string {
	return s.String()
}

func (s *VideoTranscodeModel) SetHeaders(v map[string]*string) *VideoTranscodeModel {
	s.Headers = v
	return s
}

func (s *VideoTranscodeModel) SetBody(v *HostingVideoTranscodeResponse) *VideoTranscodeModel {
	s.Body = v
	return s
}

type CreateShareModel struct {
	Headers map[string]*string   `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *CreateShareResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s CreateShareModel) String() string {
	return tea.Prettify(s)
}

func (s CreateShareModel) GoString() string {
	return s.String()
}

func (s *CreateShareModel) SetHeaders(v map[string]*string) *CreateShareModel {
	s.Headers = v
	return s
}

func (s *CreateShareModel) SetBody(v *CreateShareResponse) *CreateShareModel {
	s.Body = v
	return s
}

type DeleteShareModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s DeleteShareModel) String() string {
	return tea.Prettify(s)
}

func (s DeleteShareModel) GoString() string {
	return s.String()
}

func (s *DeleteShareModel) SetHeaders(v map[string]*string) *DeleteShareModel {
	s.Headers = v
	return s
}

type GetShareModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *GetShareResponse  `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetShareModel) String() string {
	return tea.Prettify(s)
}

func (s GetShareModel) GoString() string {
	return s.String()
}

func (s *GetShareModel) SetHeaders(v map[string]*string) *GetShareModel {
	s.Headers = v
	return s
}

func (s *GetShareModel) SetBody(v *GetShareResponse) *GetShareModel {
	s.Body = v
	return s
}

type ListShareModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *ListShareResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ListShareModel) String() string {
	return tea.Prettify(s)
}

func (s ListShareModel) GoString() string {
	return s.String()
}

func (s *ListShareModel) SetHeaders(v map[string]*string) *ListShareModel {
	s.Headers = v
	return s
}

func (s *ListShareModel) SetBody(v *ListShareResponse) *ListShareModel {
	s.Body = v
	return s
}

type UpdateShareModel struct {
	Headers map[string]*string   `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *UpdateShareResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s UpdateShareModel) String() string {
	return tea.Prettify(s)
}

func (s UpdateShareModel) GoString() string {
	return s.String()
}

func (s *UpdateShareModel) SetHeaders(v map[string]*string) *UpdateShareModel {
	s.Headers = v
	return s
}

func (s *UpdateShareModel) SetBody(v *UpdateShareResponse) *UpdateShareModel {
	s.Body = v
	return s
}

type ListStorefileModel struct {
	Headers map[string]*string     `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *ListStoreFileResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ListStorefileModel) String() string {
	return tea.Prettify(s)
}

func (s ListStorefileModel) GoString() string {
	return s.String()
}

func (s *ListStorefileModel) SetHeaders(v map[string]*string) *ListStorefileModel {
	s.Headers = v
	return s
}

func (s *ListStorefileModel) SetBody(v *ListStoreFileResponse) *ListStorefileModel {
	s.Body = v
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
 *
 */
type BaseFileRequest struct {
	// addition_data
	AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
}

func (s BaseFileRequest) String() string {
	return tea.Prettify(s)
}

func (s BaseFileRequest) GoString() string {
	return s.String()
}

func (s *BaseFileRequest) SetAdditionData(v map[string]interface{}) *BaseFileRequest {
	s.AdditionData = v
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
 * list file request
 */
type BaseListFileRequest struct {
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
	// image_thumbnail_process
	ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
	// image_url_process
	ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
	// limit
	Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"0" pattern:"[0-9]{1,3}"`
	// marker
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
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

func (s *BaseListFileRequest) SetDriveId(v string) *BaseListFileRequest {
	s.DriveId = &v
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

func (s *BaseListFileRequest) SetVideoThumbnailProcess(v string) *BaseListFileRequest {
	s.VideoThumbnailProcess = &v
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
	// overwrite
	// type: boolean
	Overwrite *bool `json:"overwrite,omitempty" xml:"overwrite,omitempty"`
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

func (s *BaseMoveFileRequest) SetOverwrite(v bool) *BaseMoveFileRequest {
	s.Overwrite = &v
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

func (s *CompleteFileRequest) SetUploadId(v string) *CompleteFileRequest {
	s.UploadId = &v
	return s
}

/**
 * 文件拷贝
 */
type CopyFileRequest struct {
	// auto_rename
	// type: boolean
	AutoRename *bool `json:"auto_rename,omitempty" xml:"auto_rename,omitempty"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
	// new_name
	NewName *string `json:"new_name,omitempty" xml:"new_name,omitempty" maxLength:"1024" minLength:"1"`
	// share_id, either share_id or drive_id is required
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
	// to_drive_id
	ToDriveId *string `json:"to_drive_id,omitempty" xml:"to_drive_id,omitempty" pattern:"[0-9]+"`
	// to_parent_file_id
	ToParentFileId *string `json:"to_parent_file_id,omitempty" xml:"to_parent_file_id,omitempty" require:"true" maxLength:"50" minLength:"4" pattern:"[a-z0-9.-_]{1,50}"`
}

func (s CopyFileRequest) String() string {
	return tea.Prettify(s)
}

func (s CopyFileRequest) GoString() string {
	return s.String()
}

func (s *CopyFileRequest) SetAutoRename(v bool) *CopyFileRequest {
	s.AutoRename = &v
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

func (s *CopyFileRequest) SetNewName(v string) *CopyFileRequest {
	s.NewName = &v
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

/**
 * create drive request
 */
type CreateDriveRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 是否默认drive, 只允许设置一个默认drive
	Default *bool `json:"default,omitempty" xml:"default,omitempty"`
	// 描述信息
	Description *string `json:"description,omitempty" xml:"description,omitempty" maxLength:"1024"`
	// Drive 名称
	DriveName *string `json:"drive_name,omitempty" xml:"drive_name,omitempty" require:"true" maxLength:"1024"`
	// Drive类型
	DriveType   *string `json:"drive_type,omitempty" xml:"drive_type,omitempty"`
	EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
	// 所属者
	Owner *string `json:"owner,omitempty" xml:"owner,omitempty" require:"true"`
	// domain的PathType为OSSPath时必选。 Drive存储基于store的相对路径
	RelativePath *string `json:"relative_path,omitempty" xml:"relative_path,omitempty"`
	// 状态
	Status *string `json:"status,omitempty" xml:"status,omitempty"`
	// StoreID , domain的PathType为OSSPath时必选
	StoreId *string `json:"store_id,omitempty" xml:"store_id,omitempty"`
	// 总大小,单位Byte [如果设置 -1 代表不限制]
	TotalSize *int64 `json:"total_size,omitempty" xml:"total_size,omitempty"`
}

func (s CreateDriveRequest) String() string {
	return tea.Prettify(s)
}

func (s CreateDriveRequest) GoString() string {
	return s.String()
}

func (s *CreateDriveRequest) SetHeaders(v map[string]*string) *CreateDriveRequest {
	s.Headers = v
	return s
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

func (s *CreateDriveRequest) SetOwner(v string) *CreateDriveRequest {
	s.Owner = &v
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

func (s *CreateDriveRequest) SetTotalSize(v int64) *CreateDriveRequest {
	s.TotalSize = &v
	return s
}

/**
 * 创建文件
 */
type CreateFileRequest struct {
	// addition_data
	AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
	AutoRename   *bool                  `json:"auto_rename,omitempty" xml:"auto_rename,omitempty"`
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
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// encrypt_mode
	EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty"`
	// hidden
	Hidden             *bool               `json:"hidden,omitempty" xml:"hidden,omitempty"`
	ImageMediaMetadata *ImageMediaMetadata `json:"image_media_metadata,omitempty" xml:"image_media_metadata,omitempty"`
	// labels
	Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
	// last_updated_at
	LastUpdatedAt *string `json:"last_updated_at,omitempty" xml:"last_updated_at,omitempty"`
	Meta          *string `json:"meta,omitempty" xml:"meta,omitempty"`
	// Name
	Name *string `json:"name,omitempty" xml:"name,omitempty" require:"true" maxLength:"1024" minLength:"1"`
	// parent_file_id
	ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" require:"true" maxLength:"50" minLength:"4" pattern:"[a-z0-9]{1,50}"`
	// part_info_list
	PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
	// pre_hash
	PreHash *string `json:"pre_hash,omitempty" xml:"pre_hash,omitempty"`
	// Size
	Size *int64 `json:"size,omitempty" xml:"size,omitempty" maximum:"53687091200" minimum:"0"`
	// streams_info
	StreamsInfo map[string]interface{} `json:"streams_info,omitempty" xml:"streams_info,omitempty"`
	// Type
	Type *string `json:"type,omitempty" xml:"type,omitempty" require:"true"`
	// user_meta
	UserMeta           *string             `json:"user_meta,omitempty" xml:"user_meta,omitempty"`
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

func (s *CreateFileRequest) SetMeta(v string) *CreateFileRequest {
	s.Meta = &v
	return s
}

func (s *CreateFileRequest) SetName(v string) *CreateFileRequest {
	s.Name = &v
	return s
}

func (s *CreateFileRequest) SetParentFileId(v string) *CreateFileRequest {
	s.ParentFileId = &v
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
 * create_share_link request
 */
type CreateShareLinkRequest struct {
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// expiration
	Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty" require:"true"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true"`
	// share_pwd
	SharePwd *string `json:"share_pwd,omitempty" xml:"share_pwd,omitempty"`
}

func (s CreateShareLinkRequest) String() string {
	return tea.Prettify(s)
}

func (s CreateShareLinkRequest) GoString() string {
	return s.String()
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

func (s *CreateShareLinkRequest) SetSharePwd(v string) *CreateShareLinkRequest {
	s.SharePwd = &v
	return s
}

/**
 * create share request
 */
type CreateShareRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// description
	Description *string `json:"description,omitempty" xml:"description,omitempty"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// expiration
	Expiration *string `json:"expiration,omitempty" xml:"expiration,omitempty"`
	// creator
	Owner *string `json:"owner,omitempty" xml:"owner,omitempty" require:"true"`
	// permissions
	Permissions []*string `json:"permissions,omitempty" xml:"permissions,omitempty" type:"Repeated"`
	// share_file_path
	ShareFilePath *string `json:"share_file_path,omitempty" xml:"share_file_path,omitempty" require:"true"`
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

func (s *CreateShareRequest) SetHeaders(v map[string]*string) *CreateShareRequest {
	s.Headers = v
	return s
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

func (s *CreateShareRequest) SetPermissions(v []*string) *CreateShareRequest {
	s.Permissions = v
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
 * Delete drive request
 */
type DeleteDriveRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// Drive ID
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true"`
}

func (s DeleteDriveRequest) String() string {
	return tea.Prettify(s)
}

func (s DeleteDriveRequest) GoString() string {
	return s.String()
}

func (s *DeleteDriveRequest) SetHeaders(v map[string]*string) *DeleteDriveRequest {
	s.Headers = v
	return s
}

func (s *DeleteDriveRequest) SetDriveId(v string) *DeleteDriveRequest {
	s.DriveId = &v
	return s
}

/**
 * 删除文件请求
 */
type DeleteFileRequest struct {
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
	// permanently
	// type: false
	Permanently *bool `json:"permanently,omitempty" xml:"permanently,omitempty"`
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

func (s *DeleteFileRequest) SetPermanently(v bool) *DeleteFileRequest {
	s.Permanently = &v
	return s
}

/**
 * 批量删除文件请求
 */
type DeleteFilesRequest struct {
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// file_id_list
	FileIdList []*string `json:"file_id_list,omitempty" xml:"file_id_list,omitempty" require:"true" type:"Repeated"`
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

/**
 * delete share request
 */
type DeleteShareRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// share_id
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" require:"true"`
}

func (s DeleteShareRequest) String() string {
	return tea.Prettify(s)
}

func (s DeleteShareRequest) GoString() string {
	return s.String()
}

func (s *DeleteShareRequest) SetHeaders(v map[string]*string) *DeleteShareRequest {
	s.Headers = v
	return s
}

func (s *DeleteShareRequest) SetShareId(v string) *DeleteShareRequest {
	s.ShareId = &v
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
	// share_id, either share_id or drive_id is required
	ShareID *string `json:"ShareID,omitempty" xml:"ShareID,omitempty"`
	// video_thumbnail_process
	// type:string
	VideoThumbnailProcess *string `json:"VideoThumbnailProcess,omitempty" xml:"VideoThumbnailProcess,omitempty"`
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

func (s *DownloadRequest) SetShareID(v string) *DownloadRequest {
	s.ShareID = &v
	return s
}

func (s *DownloadRequest) SetVideoThumbnailProcess(v string) *DownloadRequest {
	s.VideoThumbnailProcess = &v
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
 * Get default drive request
 */
type GetDefaultDriveRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 用户ID
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty"`
}

func (s GetDefaultDriveRequest) String() string {
	return tea.Prettify(s)
}

func (s GetDefaultDriveRequest) GoString() string {
	return s.String()
}

func (s *GetDefaultDriveRequest) SetHeaders(v map[string]*string) *GetDefaultDriveRequest {
	s.Headers = v
	return s
}

func (s *GetDefaultDriveRequest) SetUserId(v string) *GetDefaultDriveRequest {
	s.UserId = &v
	return s
}

/**
 * 获取文件下载地址的请求body
 */
type GetDownloadUrlRequest struct {
	// addition_data
	AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// expire_sec
	ExpireSec *int64 `json:"expire_sec,omitempty" xml:"expire_sec,omitempty" maximum:"14400" minimum:"0"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
	// file_name
	FileName *string `json:"file_name,omitempty" xml:"file_name,omitempty" maxLength:"1024" minLength:"1"`
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

func (s *GetDownloadUrlRequest) SetFileName(v string) *GetDownloadUrlRequest {
	s.FileName = &v
	return s
}

/**
 * Get drive request
 */
type GetDriveRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// Drive ID
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true"`
}

func (s GetDriveRequest) String() string {
	return tea.Prettify(s)
}

func (s GetDriveRequest) GoString() string {
	return s.String()
}

func (s *GetDriveRequest) SetHeaders(v map[string]*string) *GetDriveRequest {
	s.Headers = v
	return s
}

func (s *GetDriveRequest) SetDriveId(v string) *GetDriveRequest {
	s.DriveId = &v
	return s
}

/**
 * 根据路径获取 File 接口 body
 */
type GetFileByPathRequest struct {
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// fields
	Fields *string `json:"fields,omitempty" xml:"fields,omitempty"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
	// file_path
	FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
	// image_thumbnail_process
	// type:string
	ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
	// image_thumbnail_process
	// type:string
	ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
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

func (s *GetFileByPathRequest) SetDriveId(v string) *GetFileByPathRequest {
	s.DriveId = &v
	return s
}

func (s *GetFileByPathRequest) SetFields(v string) *GetFileByPathRequest {
	s.Fields = &v
	return s
}

func (s *GetFileByPathRequest) SetFileId(v string) *GetFileByPathRequest {
	s.FileId = &v
	return s
}

func (s *GetFileByPathRequest) SetFilePath(v string) *GetFileByPathRequest {
	s.FilePath = &v
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

func (s *GetFileByPathRequest) SetUrlExpireSec(v int64) *GetFileByPathRequest {
	s.UrlExpireSec = &v
	return s
}

func (s *GetFileByPathRequest) SetVideoThumbnailProcess(v string) *GetFileByPathRequest {
	s.VideoThumbnailProcess = &v
	return s
}

/**
 * 获取文件元数据
 */
type GetFileRequest struct {
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// fields
	Fields *string `json:"fields,omitempty" xml:"fields,omitempty"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
	// image_thumbnail_process
	// type:string
	ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
	// image_thumbnail_process
	// type:string
	ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
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

func (s *GetFileRequest) SetImageThumbnailProcess(v string) *GetFileRequest {
	s.ImageThumbnailProcess = &v
	return s
}

func (s *GetFileRequest) SetImageUrlProcess(v string) *GetFileRequest {
	s.ImageUrlProcess = &v
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
 * 获取office文档预览地址
 */
type GetOfficePreviewUrlRequest struct {
	// addition_data
	AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
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
 * get_share_token request
 */
type GetShareLinkTokenRequest struct {
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

func (s *GetShareLinkTokenRequest) SetShareId(v string) *GetShareLinkTokenRequest {
	s.ShareId = &v
	return s
}

func (s *GetShareLinkTokenRequest) SetSharePwd(v string) *GetShareLinkTokenRequest {
	s.SharePwd = &v
	return s
}

/**
 * get share request
 */
type GetShareRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// share_id
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty"`
}

func (s GetShareRequest) String() string {
	return tea.Prettify(s)
}

func (s GetShareRequest) GoString() string {
	return s.String()
}

func (s *GetShareRequest) SetHeaders(v map[string]*string) *GetShareRequest {
	s.Headers = v
	return s
}

func (s *GetShareRequest) SetShareId(v string) *GetShareRequest {
	s.ShareId = &v
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

func (s *GetUploadUrlRequest) SetUploadId(v string) *GetUploadUrlRequest {
	s.UploadId = &v
	return s
}

/**
 * 获取视频雪碧图地址的请求body
 */
type GetVideoPreviewSpriteURLRequest struct {
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// expire_sec
	ExpireSec *int64 `json:"expire_sec,omitempty" xml:"expire_sec,omitempty" maximum:"14400" minimum:"0"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
}

func (s GetVideoPreviewSpriteURLRequest) String() string {
	return tea.Prettify(s)
}

func (s GetVideoPreviewSpriteURLRequest) GoString() string {
	return s.String()
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

/**
 * 获取视频文件播放地址的请求body
 */
type GetVideoPreviewURLRequest struct {
	// addition_data
	AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// expire_sec
	ExpireSec *int64 `json:"expire_sec,omitempty" xml:"expire_sec,omitempty" maximum:"14400" minimum:"0"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
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

func (s *GetVideoPreviewURLRequest) SetTemplateId(v string) *GetVideoPreviewURLRequest {
	s.TemplateId = &v
	return s
}

/**
 * complete file request
 */
type HostingCompleteFileRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// addition_data
	AdditionData map[string]interface{} `json:"addition_data,omitempty" xml:"addition_data,omitempty"`
	// drive_id
	DriveId  *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
	FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty"`
	// forbid_overwrite
	// type: boolean
	ForbidOverwrite *bool `json:"forbid_overwrite,omitempty" xml:"forbid_overwrite,omitempty"`
	// part_info_list
	PartInfoList []*UploadPartInfo `json:"part_info_list,omitempty" xml:"part_info_list,omitempty" type:"Repeated"`
	ShareId      *string           `json:"share_id,omitempty" xml:"share_id,omitempty"`
	// upload_id
	UploadId *string `json:"upload_id,omitempty" xml:"upload_id,omitempty"`
}

func (s HostingCompleteFileRequest) String() string {
	return tea.Prettify(s)
}

func (s HostingCompleteFileRequest) GoString() string {
	return s.String()
}

func (s *HostingCompleteFileRequest) SetHeaders(v map[string]*string) *HostingCompleteFileRequest {
	s.Headers = v
	return s
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
	// file_path
	FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true"`
	// new_name
	NewName *string `json:"new_name,omitempty" xml:"new_name,omitempty" pattern:"[a-zA-Z0-9.-]{1,1000}"`
	// overwrite
	// type: boolean
	Overwrite *bool `json:"overwrite,omitempty" xml:"overwrite,omitempty"`
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

func (s *HostingCopyFileRequest) SetHeaders(v map[string]*string) *HostingCopyFileRequest {
	s.Headers = v
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
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

func (s *HostingCreateFileRequest) SetHeaders(v map[string]*string) *HostingCreateFileRequest {
	s.Headers = v
	return s
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
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

func (s *HostingDeleteFileRequest) SetHeaders(v map[string]*string) *HostingDeleteFileRequest {
	s.Headers = v
	return s
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
	// expire_sec
	ExpireSec *int64 `json:"expire_sec,omitempty" xml:"expire_sec,omitempty" maximum:"14400" minimum:"10"`
	// file_name
	FileName *string `json:"file_name,omitempty" xml:"file_name,omitempty"`
	// file_path
	FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true" maxLength:"1000" minLength:"1"`
	// share_id
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
}

func (s HostingGetDownloadUrlRequest) String() string {
	return tea.Prettify(s)
}

func (s HostingGetDownloadUrlRequest) GoString() string {
	return s.String()
}

func (s *HostingGetDownloadUrlRequest) SetHeaders(v map[string]*string) *HostingGetDownloadUrlRequest {
	s.Headers = v
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

func (s *HostingGetDownloadUrlRequest) SetShareId(v string) *HostingGetDownloadUrlRequest {
	s.ShareId = &v
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
	// file_id
	FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true" maxLength:"1000" minLength:"1"`
	// image_thumbnail_process
	// type:string
	ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
	// image_thumbnail_process
	// type:string
	ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
	// share_id
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
	// url_expire_sec
	UrlExpireSec *int64 `json:"url_expire_sec,omitempty" xml:"url_expire_sec,omitempty" maximum:"14400" minimum:"10"`
}

func (s HostingGetFileRequest) String() string {
	return tea.Prettify(s)
}

func (s HostingGetFileRequest) GoString() string {
	return s.String()
}

func (s *HostingGetFileRequest) SetHeaders(v map[string]*string) *HostingGetFileRequest {
	s.Headers = v
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

func (s *HostingGetFileRequest) SetShareId(v string) *HostingGetFileRequest {
	s.ShareId = &v
	return s
}

func (s *HostingGetFileRequest) SetUrlExpireSec(v int64) *HostingGetFileRequest {
	s.UrlExpireSec = &v
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
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

func (s *HostingGetSecureUrlRequest) SetHeaders(v map[string]*string) *HostingGetSecureUrlRequest {
	s.Headers = v
	return s
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
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

func (s *HostingGetUploadUrlRequest) SetHeaders(v map[string]*string) *HostingGetUploadUrlRequest {
	s.Headers = v
	return s
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
	// image_thumbnail_process
	ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
	// image_url_process
	ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
	// limit
	Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"0" pattern:"[0-9]{1,3}"`
	// marker
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
	// ParentFilePath
	ParentFilePath *string `json:"parent_file_path,omitempty" xml:"parent_file_path,omitempty" require:"true"`
	// share_id
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" pattern:"[0-9a-zA-Z-]+"`
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

func (s *HostingListFileRequest) SetHeaders(v map[string]*string) *HostingListFileRequest {
	s.Headers = v
	return s
}

func (s *HostingListFileRequest) SetDriveId(v string) *HostingListFileRequest {
	s.DriveId = &v
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

func (s *HostingListFileRequest) SetParentFilePath(v string) *HostingListFileRequest {
	s.ParentFilePath = &v
	return s
}

func (s *HostingListFileRequest) SetShareId(v string) *HostingListFileRequest {
	s.ShareId = &v
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
	// file_path
	FilePath *string `json:"file_path,omitempty" xml:"file_path,omitempty" require:"true"`
	// limit
	Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"1000" minimum:"1" pattern:"[0-9]+"`
	// part_number_marker
	PartNumberMarker *int64 `json:"part_number_marker,omitempty" xml:"part_number_marker,omitempty" minimum:"1" pattern:"[0-9]+"`
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

func (s *HostingListUploadedPartRequest) SetHeaders(v map[string]*string) *HostingListUploadedPartRequest {
	s.Headers = v
	return s
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
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

func (s *HostingMoveFileRequest) SetHeaders(v map[string]*string) *HostingMoveFileRequest {
	s.Headers = v
	return s
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
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

func (s *HostingVideoDRMLicenseRequest) SetHeaders(v map[string]*string) *HostingVideoDRMLicenseRequest {
	s.Headers = v
	return s
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

func (s *HostingVideoDRMLicenseResponse) SetStates(v int64) *HostingVideoDRMLicenseResponse {
	s.States = &v
	return s
}

/**
 * 获取视频分辨率列表
 */
type HostingVideoDefinitionRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
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

func (s *HostingVideoDefinitionRequest) SetHeaders(v map[string]*string) *HostingVideoDefinitionRequest {
	s.Headers = v
	return s
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
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

func (s *HostingVideoM3U8Request) SetHeaders(v map[string]*string) *HostingVideoM3U8Request {
	s.Headers = v
	return s
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
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
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

func (s *HostingVideoTranscodeRequest) SetHeaders(v map[string]*string) *HostingVideoTranscodeRequest {
	s.Headers = v
	return s
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
 * list_file_by_anonymous request
 */
type ListByAnonymousRequest struct {
	// limit
	Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
	// marker
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
	// parent_file_id
	ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" require:"true" maxLength:"50" minLength:"4" pattern:"[a-z0-9]{1,50}"`
	// share_id
	ShareId *string `json:"share_id,omitempty" xml:"share_id,omitempty" require:"true"`
}

func (s ListByAnonymousRequest) String() string {
	return tea.Prettify(s)
}

func (s ListByAnonymousRequest) GoString() string {
	return s.String()
}

func (s *ListByAnonymousRequest) SetLimit(v int64) *ListByAnonymousRequest {
	s.Limit = &v
	return s
}

func (s *ListByAnonymousRequest) SetMarker(v string) *ListByAnonymousRequest {
	s.Marker = &v
	return s
}

func (s *ListByAnonymousRequest) SetParentFileId(v string) *ListByAnonymousRequest {
	s.ParentFileId = &v
	return s
}

func (s *ListByAnonymousRequest) SetShareId(v string) *ListByAnonymousRequest {
	s.ShareId = &v
	return s
}

/**
 * List drive request
 */
type ListDriveRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 每页大小限制
	Limit *int `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
	// 翻页标记, 接口返回的标记值
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
	// 所属者
	Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
}

func (s ListDriveRequest) String() string {
	return tea.Prettify(s)
}

func (s ListDriveRequest) GoString() string {
	return s.String()
}

func (s *ListDriveRequest) SetHeaders(v map[string]*string) *ListDriveRequest {
	s.Headers = v
	return s
}

func (s *ListDriveRequest) SetLimit(v int) *ListDriveRequest {
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

/**
 * 列举文件
 */
type ListFileByCustomIndexKeyRequest struct {
	// starred
	Starred *bool `json:"Starred,omitempty" xml:"Starred,omitempty"`
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
	// image_thumbnail_process
	ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
	// image_url_process
	ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
	// limit
	Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"0" pattern:"[0-9]{1,3}"`
	// marker
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
	// order_direction
	OrderDirection *string `json:"order_direction,omitempty" xml:"order_direction,omitempty"`
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

func (s *ListFileByCustomIndexKeyRequest) SetOrderDirection(v string) *ListFileByCustomIndexKeyRequest {
	s.OrderDirection = &v
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
	// limit
	// default 100
	Limit *int `json:"limit,omitempty" xml:"limit,omitempty"`
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

func (s *ListFileDeltaRequest) SetLimit(v int) *ListFileDeltaRequest {
	s.Limit = &v
	return s
}

/**
 * 列举文件
 */
type ListFileRequest struct {
	// starred
	Starred *bool `json:"Starred,omitempty" xml:"Starred,omitempty"`
	// all
	All *bool `json:"all,omitempty" xml:"all,omitempty"`
	// category
	Category *string `json:"category,omitempty" xml:"category,omitempty"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
	// fields
	Fields *string `json:"fields,omitempty" xml:"fields,omitempty"`
	// image_thumbnail_process
	ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
	// image_url_process
	ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
	// limit
	Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"0" pattern:"[0-9]{1,3}"`
	// marker
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
	// order_by
	OrderBy *string `json:"order_by,omitempty" xml:"order_by,omitempty"`
	// order_direction
	OrderDirection *string `json:"order_direction,omitempty" xml:"order_direction,omitempty"`
	// ParentFileID
	ParentFileId *string `json:"parent_file_id,omitempty" xml:"parent_file_id,omitempty" require:"true" maxLength:"50" minLength:"4" pattern:"[a-z0-9.-_]{1,50}"`
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

func (s *ListFileRequest) SetStarred(v bool) *ListFileRequest {
	s.Starred = &v
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

func (s *ListFileRequest) SetMarker(v string) *ListFileRequest {
	s.Marker = &v
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
 * List my drive request
 */
type ListMyDriveRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 每页大小限制
	Limit *int `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
	// 翻页标记, 接口返回的标记值
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
}

func (s ListMyDriveRequest) String() string {
	return tea.Prettify(s)
}

func (s ListMyDriveRequest) GoString() string {
	return s.String()
}

func (s *ListMyDriveRequest) SetHeaders(v map[string]*string) *ListMyDriveRequest {
	s.Headers = v
	return s
}

func (s *ListMyDriveRequest) SetLimit(v int) *ListMyDriveRequest {
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
	// limit
	Limit *int `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
	// marker
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
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

func (s *ListShareLinkRequest) SetLimit(v int) *ListShareLinkRequest {
	s.Limit = &v
	return s
}

func (s *ListShareLinkRequest) SetMarker(v string) *ListShareLinkRequest {
	s.Marker = &v
	return s
}

/**
 * list share request
 */
type ListShareRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// creator
	Creator *string `json:"creator,omitempty" xml:"creator,omitempty"`
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" pattern:"[0-9]+"`
	// limit
	Limit *int `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
	// marker
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
	// Owner
	Owner *string `json:"owner,omitempty" xml:"owner,omitempty"`
	// share_file_path
	ShareFilePath *string `json:"share_file_path,omitempty" xml:"share_file_path,omitempty"`
}

func (s ListShareRequest) String() string {
	return tea.Prettify(s)
}

func (s ListShareRequest) GoString() string {
	return s.String()
}

func (s *ListShareRequest) SetHeaders(v map[string]*string) *ListShareRequest {
	s.Headers = v
	return s
}

func (s *ListShareRequest) SetCreator(v string) *ListShareRequest {
	s.Creator = &v
	return s
}

func (s *ListShareRequest) SetDriveId(v string) *ListShareRequest {
	s.DriveId = &v
	return s
}

func (s *ListShareRequest) SetLimit(v int) *ListShareRequest {
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

func (s *ListShareRequest) SetShareFilePath(v string) *ListShareRequest {
	s.ShareFilePath = &v
	return s
}

/**
 * list store file
 */
type ListStoreFileRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
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

func (s *ListStoreFileRequest) SetHeaders(v map[string]*string) *ListStoreFileRequest {
	s.Headers = v
	return s
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
 * 列举uploadID对应的已上传分片
 */
type ListUploadedPartRequest struct {
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
	// limit
	Limit *int64 `json:"limit,omitempty" xml:"limit,omitempty" maximum:"1000" minimum:"1" pattern:"[0-9]+"`
	// part_number_marker
	PartNumberMarker *int64 `json:"part_number_marker,omitempty" xml:"part_number_marker,omitempty" minimum:"1" pattern:"[0-9]+"`
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

func (s *ListUploadedPartRequest) SetLimit(v int64) *ListUploadedPartRequest {
	s.Limit = &v
	return s
}

func (s *ListUploadedPartRequest) SetPartNumberMarker(v int64) *ListUploadedPartRequest {
	s.PartNumberMarker = &v
	return s
}

func (s *ListUploadedPartRequest) SetUploadId(v string) *ListUploadedPartRequest {
	s.UploadId = &v
	return s
}

/**
 * 文件移动请求
 */
type MoveFileRequest struct {
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
	// new_name
	NewName *string `json:"new_name,omitempty" xml:"new_name,omitempty" maxLength:"1024" minLength:"1"`
	// overwrite
	// type: boolean
	Overwrite *bool `json:"overwrite,omitempty" xml:"overwrite,omitempty"`
	// to_parent_file_id
	ToParentFileId *string `json:"to_parent_file_id,omitempty" xml:"to_parent_file_id,omitempty" require:"true" maxLength:"50" minLength:"4"`
}

func (s MoveFileRequest) String() string {
	return tea.Prettify(s)
}

func (s MoveFileRequest) GoString() string {
	return s.String()
}

func (s *MoveFileRequest) SetDriveId(v string) *MoveFileRequest {
	s.DriveId = &v
	return s
}

func (s *MoveFileRequest) SetFileId(v string) *MoveFileRequest {
	s.FileId = &v
	return s
}

func (s *MoveFileRequest) SetNewName(v string) *MoveFileRequest {
	s.NewName = &v
	return s
}

func (s *MoveFileRequest) SetOverwrite(v bool) *MoveFileRequest {
	s.Overwrite = &v
	return s
}

func (s *MoveFileRequest) SetToParentFileId(v string) *MoveFileRequest {
	s.ToParentFileId = &v
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
 * 全量获取file元信息的请求body
 */
type ScanFileMetaRequest struct {
	// category
	Category *string `json:"category,omitempty" xml:"category,omitempty"`
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// limit
	Limit *int `json:"limit,omitempty" xml:"limit,omitempty" maximum:"5000" minimum:"1"`
	// marker
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
}

func (s ScanFileMetaRequest) String() string {
	return tea.Prettify(s)
}

func (s ScanFileMetaRequest) GoString() string {
	return s.String()
}

func (s *ScanFileMetaRequest) SetCategory(v string) *ScanFileMetaRequest {
	s.Category = &v
	return s
}

func (s *ScanFileMetaRequest) SetDriveId(v string) *ScanFileMetaRequest {
	s.DriveId = &v
	return s
}

func (s *ScanFileMetaRequest) SetLimit(v int) *ScanFileMetaRequest {
	s.Limit = &v
	return s
}

func (s *ScanFileMetaRequest) SetMarker(v string) *ScanFileMetaRequest {
	s.Marker = &v
	return s
}

/**
 * 搜索文件元数据
 */
type SearchFileRequest struct {
	// drive_id
	DriveId *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	// image_thumbnail_process
	ImageThumbnailProcess *string `json:"image_thumbnail_process,omitempty" xml:"image_thumbnail_process,omitempty"`
	// image_url_process
	ImageUrlProcess *string `json:"image_url_process,omitempty" xml:"image_url_process,omitempty"`
	// limit
	Limit *int `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
	// Marker
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
	// order_by
	OrderBy *string `json:"order_by,omitempty" xml:"order_by,omitempty"`
	// query
	Query *string `json:"query,omitempty" xml:"query,omitempty" maxLength:"4096"`
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

func (s *SearchFileRequest) SetDriveId(v string) *SearchFileRequest {
	s.DriveId = &v
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

func (s *SearchFileRequest) SetLimit(v int) *SearchFileRequest {
	s.Limit = &v
	return s
}

func (s *SearchFileRequest) SetMarker(v string) *SearchFileRequest {
	s.Marker = &v
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

func (s *SearchFileRequest) SetUrlExpireSec(v int64) *SearchFileRequest {
	s.UrlExpireSec = &v
	return s
}

func (s *SearchFileRequest) SetVideoThumbnailProcess(v string) *SearchFileRequest {
	s.VideoThumbnailProcess = &v
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
 * Update drive request
 */
type UpdateDriveRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
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
	// 总大小,单位Byte [如果设置 -1 代表不限制]
	TotalSize *int64 `json:"total_size,omitempty" xml:"total_size,omitempty"`
}

func (s UpdateDriveRequest) String() string {
	return tea.Prettify(s)
}

func (s UpdateDriveRequest) GoString() string {
	return s.String()
}

func (s *UpdateDriveRequest) SetHeaders(v map[string]*string) *UpdateDriveRequest {
	s.Headers = v
	return s
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

func (s *UpdateDriveRequest) SetTotalSize(v int64) *UpdateDriveRequest {
	s.TotalSize = &v
	return s
}

/**
 * 更新文件元数据
 */
type UpdateFileMetaRequest struct {
	// check_name_mode
	CheckNameMode  *string `json:"check_name_mode,omitempty" xml:"check_name_mode,omitempty"`
	CustomIndexKey *string `json:"custom_index_key,omitempty" xml:"custom_index_key,omitempty"`
	// description
	// type: string
	Description *string `json:"description,omitempty" xml:"description,omitempty" maxLength:"1024"`
	// drive_id
	DriveId     *string `json:"drive_id,omitempty" xml:"drive_id,omitempty" require:"true" pattern:"[0-9]+"`
	EncryptMode *string `json:"encrypt_mode,omitempty" xml:"encrypt_mode,omitempty"`
	// file_id
	FileId *string `json:"file_id,omitempty" xml:"file_id,omitempty" require:"true" maxLength:"50" minLength:"40" pattern:"[a-z0-9.-_]{1,50}"`
	// hidden
	// type: boolean
	Hidden *bool `json:"hidden,omitempty" xml:"hidden,omitempty"`
	// labels
	Labels []*string `json:"labels,omitempty" xml:"labels,omitempty" type:"Repeated"`
	Meta   *string   `json:"meta,omitempty" xml:"meta,omitempty"`
	// name
	Name *string `json:"name,omitempty" xml:"name,omitempty" maxLength:"1024" minLength:"1"`
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

func (s *UpdateFileMetaRequest) SetStarred(v bool) *UpdateFileMetaRequest {
	s.Starred = &v
	return s
}

func (s *UpdateFileMetaRequest) SetUserMeta(v string) *UpdateFileMetaRequest {
	s.UserMeta = &v
	return s
}

/**
 * update share request
 */
type UpdateShareRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
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

func (s *UpdateShareRequest) SetHeaders(v map[string]*string) *UpdateShareRequest {
	s.Headers = v
	return s
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

type CreateUserModel struct {
	Headers map[string]*string  `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *CreateUserResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s CreateUserModel) String() string {
	return tea.Prettify(s)
}

func (s CreateUserModel) GoString() string {
	return s.String()
}

func (s *CreateUserModel) SetHeaders(v map[string]*string) *CreateUserModel {
	s.Headers = v
	return s
}

func (s *CreateUserModel) SetBody(v *CreateUserResponse) *CreateUserModel {
	s.Body = v
	return s
}

type DeleteUserModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
}

func (s DeleteUserModel) String() string {
	return tea.Prettify(s)
}

func (s DeleteUserModel) GoString() string {
	return s.String()
}

func (s *DeleteUserModel) SetHeaders(v map[string]*string) *DeleteUserModel {
	s.Headers = v
	return s
}

type GetUserModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *GetUserResponse   `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s GetUserModel) String() string {
	return tea.Prettify(s)
}

func (s GetUserModel) GoString() string {
	return s.String()
}

func (s *GetUserModel) SetHeaders(v map[string]*string) *GetUserModel {
	s.Headers = v
	return s
}

func (s *GetUserModel) SetBody(v *GetUserResponse) *GetUserModel {
	s.Body = v
	return s
}

type ListUsersModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *ListUserResponse  `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s ListUsersModel) String() string {
	return tea.Prettify(s)
}

func (s ListUsersModel) GoString() string {
	return s.String()
}

func (s *ListUsersModel) SetHeaders(v map[string]*string) *ListUsersModel {
	s.Headers = v
	return s
}

func (s *ListUsersModel) SetBody(v *ListUserResponse) *ListUsersModel {
	s.Body = v
	return s
}

type SearchUserModel struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *ListUserResponse  `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s SearchUserModel) String() string {
	return tea.Prettify(s)
}

func (s SearchUserModel) GoString() string {
	return s.String()
}

func (s *SearchUserModel) SetHeaders(v map[string]*string) *SearchUserModel {
	s.Headers = v
	return s
}

func (s *SearchUserModel) SetBody(v *ListUserResponse) *SearchUserModel {
	s.Body = v
	return s
}

type UpdateUserModel struct {
	Headers map[string]*string  `json:"headers,omitempty" xml:"headers,omitempty"`
	Body    *UpdateUserResponse `json:"body,omitempty" xml:"body,omitempty" require:"true"`
}

func (s UpdateUserModel) String() string {
	return tea.Prettify(s)
}

func (s UpdateUserModel) GoString() string {
	return s.String()
}

func (s *UpdateUserModel) SetHeaders(v map[string]*string) *UpdateUserModel {
	s.Headers = v
	return s
}

func (s *UpdateUserModel) SetBody(v *UpdateUserResponse) *UpdateUserModel {
	s.Body = v
	return s
}

/**
 * Base user response
 */
type BaseUserResponse struct {
	// 头像
	Avatar *string `json:"avatar,omitempty" xml:"avatar,omitempty"`
	// 用户创建时间
	CreatedAt *int64 `json:"created_at,omitempty" xml:"created_at,omitempty"`
	// 默认 Drive ID
	DefaultDriveId *string `json:"default_drive_id,omitempty" xml:"default_drive_id,omitempty"`
	// 用户备注信息
	Description *string `json:"description,omitempty" xml:"description,omitempty"`
	// Domain ID
	DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
	// 邮箱
	Email *string `json:"email,omitempty" xml:"email,omitempty"`
	// 昵称
	NickName *string `json:"nick_name,omitempty" xml:"nick_name,omitempty"`
	// 电话
	Phone *string `json:"phone,omitempty" xml:"phone,omitempty"`
	// 角色
	Role *string `json:"role,omitempty" xml:"role,omitempty"`
	// 用户状态
	Status *string `json:"status,omitempty" xml:"status,omitempty"`
	// 用户修改时间
	UpdatedAt *int64 `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
	// 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
	UserData map[string]interface{} `json:"user_data,omitempty" xml:"user_data,omitempty"`
	// 用户 ID
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty"`
	// 用户名称
	UserName *string `json:"user_name,omitempty" xml:"user_name,omitempty"`
}

func (s BaseUserResponse) String() string {
	return tea.Prettify(s)
}

func (s BaseUserResponse) GoString() string {
	return s.String()
}

func (s *BaseUserResponse) SetAvatar(v string) *BaseUserResponse {
	s.Avatar = &v
	return s
}

func (s *BaseUserResponse) SetCreatedAt(v int64) *BaseUserResponse {
	s.CreatedAt = &v
	return s
}

func (s *BaseUserResponse) SetDefaultDriveId(v string) *BaseUserResponse {
	s.DefaultDriveId = &v
	return s
}

func (s *BaseUserResponse) SetDescription(v string) *BaseUserResponse {
	s.Description = &v
	return s
}

func (s *BaseUserResponse) SetDomainId(v string) *BaseUserResponse {
	s.DomainId = &v
	return s
}

func (s *BaseUserResponse) SetEmail(v string) *BaseUserResponse {
	s.Email = &v
	return s
}

func (s *BaseUserResponse) SetNickName(v string) *BaseUserResponse {
	s.NickName = &v
	return s
}

func (s *BaseUserResponse) SetPhone(v string) *BaseUserResponse {
	s.Phone = &v
	return s
}

func (s *BaseUserResponse) SetRole(v string) *BaseUserResponse {
	s.Role = &v
	return s
}

func (s *BaseUserResponse) SetStatus(v string) *BaseUserResponse {
	s.Status = &v
	return s
}

func (s *BaseUserResponse) SetUpdatedAt(v int64) *BaseUserResponse {
	s.UpdatedAt = &v
	return s
}

func (s *BaseUserResponse) SetUserData(v map[string]interface{}) *BaseUserResponse {
	s.UserData = v
	return s
}

func (s *BaseUserResponse) SetUserId(v string) *BaseUserResponse {
	s.UserId = &v
	return s
}

func (s *BaseUserResponse) SetUserName(v string) *BaseUserResponse {
	s.UserName = &v
	return s
}

/**
 * Create user request
 */
type CreateUserRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 头像
	Avatar *string `json:"avatar,omitempty" xml:"avatar,omitempty"`
	// 描述信息
	Description *string `json:"description,omitempty" xml:"description,omitempty" maxLength:"1024"`
	// 邮箱
	Email *string `json:"email,omitempty" xml:"email,omitempty"`
	// 昵称
	NickName *string `json:"nick_name,omitempty" xml:"nick_name,omitempty"`
	// 电话号码
	Phone *string `json:"phone,omitempty" xml:"phone,omitempty"`
	// 角色
	Role *string `json:"role,omitempty" xml:"role,omitempty"`
	// 状态
	Status *string `json:"status,omitempty" xml:"status,omitempty"`
	// 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
	UserData map[string]interface{} `json:"user_data,omitempty" xml:"user_data,omitempty"`
	// 用户 ID
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty" require:"true"`
	// 用户名称
	UserName *string `json:"user_name,omitempty" xml:"user_name,omitempty"`
}

func (s CreateUserRequest) String() string {
	return tea.Prettify(s)
}

func (s CreateUserRequest) GoString() string {
	return s.String()
}

func (s *CreateUserRequest) SetHeaders(v map[string]*string) *CreateUserRequest {
	s.Headers = v
	return s
}

func (s *CreateUserRequest) SetAvatar(v string) *CreateUserRequest {
	s.Avatar = &v
	return s
}

func (s *CreateUserRequest) SetDescription(v string) *CreateUserRequest {
	s.Description = &v
	return s
}

func (s *CreateUserRequest) SetEmail(v string) *CreateUserRequest {
	s.Email = &v
	return s
}

func (s *CreateUserRequest) SetNickName(v string) *CreateUserRequest {
	s.NickName = &v
	return s
}

func (s *CreateUserRequest) SetPhone(v string) *CreateUserRequest {
	s.Phone = &v
	return s
}

func (s *CreateUserRequest) SetRole(v string) *CreateUserRequest {
	s.Role = &v
	return s
}

func (s *CreateUserRequest) SetStatus(v string) *CreateUserRequest {
	s.Status = &v
	return s
}

func (s *CreateUserRequest) SetUserData(v map[string]interface{}) *CreateUserRequest {
	s.UserData = v
	return s
}

func (s *CreateUserRequest) SetUserId(v string) *CreateUserRequest {
	s.UserId = &v
	return s
}

func (s *CreateUserRequest) SetUserName(v string) *CreateUserRequest {
	s.UserName = &v
	return s
}

/**
 * Create user response
 */
type CreateUserResponse struct {
	// 头像
	Avatar *string `json:"avatar,omitempty" xml:"avatar,omitempty"`
	// 用户创建时间
	CreatedAt *int64 `json:"created_at,omitempty" xml:"created_at,omitempty"`
	// 默认 Drive ID
	DefaultDriveId *string `json:"default_drive_id,omitempty" xml:"default_drive_id,omitempty"`
	// 用户备注信息
	Description *string `json:"description,omitempty" xml:"description,omitempty"`
	// Domain ID
	DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
	// 邮箱
	Email *string `json:"email,omitempty" xml:"email,omitempty"`
	// 昵称
	NickName *string `json:"nick_name,omitempty" xml:"nick_name,omitempty"`
	// 电话
	Phone *string `json:"phone,omitempty" xml:"phone,omitempty"`
	// 角色
	Role *string `json:"role,omitempty" xml:"role,omitempty"`
	// 用户状态
	Status *string `json:"status,omitempty" xml:"status,omitempty"`
	// 用户修改时间
	UpdatedAt *int64 `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
	// 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
	UserData map[string]interface{} `json:"user_data,omitempty" xml:"user_data,omitempty"`
	// 用户 ID
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty"`
	// 用户名称
	UserName *string `json:"user_name,omitempty" xml:"user_name,omitempty"`
}

func (s CreateUserResponse) String() string {
	return tea.Prettify(s)
}

func (s CreateUserResponse) GoString() string {
	return s.String()
}

func (s *CreateUserResponse) SetAvatar(v string) *CreateUserResponse {
	s.Avatar = &v
	return s
}

func (s *CreateUserResponse) SetCreatedAt(v int64) *CreateUserResponse {
	s.CreatedAt = &v
	return s
}

func (s *CreateUserResponse) SetDefaultDriveId(v string) *CreateUserResponse {
	s.DefaultDriveId = &v
	return s
}

func (s *CreateUserResponse) SetDescription(v string) *CreateUserResponse {
	s.Description = &v
	return s
}

func (s *CreateUserResponse) SetDomainId(v string) *CreateUserResponse {
	s.DomainId = &v
	return s
}

func (s *CreateUserResponse) SetEmail(v string) *CreateUserResponse {
	s.Email = &v
	return s
}

func (s *CreateUserResponse) SetNickName(v string) *CreateUserResponse {
	s.NickName = &v
	return s
}

func (s *CreateUserResponse) SetPhone(v string) *CreateUserResponse {
	s.Phone = &v
	return s
}

func (s *CreateUserResponse) SetRole(v string) *CreateUserResponse {
	s.Role = &v
	return s
}

func (s *CreateUserResponse) SetStatus(v string) *CreateUserResponse {
	s.Status = &v
	return s
}

func (s *CreateUserResponse) SetUpdatedAt(v int64) *CreateUserResponse {
	s.UpdatedAt = &v
	return s
}

func (s *CreateUserResponse) SetUserData(v map[string]interface{}) *CreateUserResponse {
	s.UserData = v
	return s
}

func (s *CreateUserResponse) SetUserId(v string) *CreateUserResponse {
	s.UserId = &v
	return s
}

func (s *CreateUserResponse) SetUserName(v string) *CreateUserResponse {
	s.UserName = &v
	return s
}

/**
 * Delete user request
 */
type DeleteUserRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 用户 ID
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty" require:"true"`
}

func (s DeleteUserRequest) String() string {
	return tea.Prettify(s)
}

func (s DeleteUserRequest) GoString() string {
	return s.String()
}

func (s *DeleteUserRequest) SetHeaders(v map[string]*string) *DeleteUserRequest {
	s.Headers = v
	return s
}

func (s *DeleteUserRequest) SetUserId(v string) *DeleteUserRequest {
	s.UserId = &v
	return s
}

/**
 * Delete user response
 */
type DeleteUserResponse struct {
}

func (s DeleteUserResponse) String() string {
	return tea.Prettify(s)
}

func (s DeleteUserResponse) GoString() string {
	return s.String()
}

/**
 * Get user request
 */
type GetUserRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 用户 ID, 使用ak方式访问，该项必传, access_token访问如果不传，默认取自己的user信息
	// example
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty"`
}

func (s GetUserRequest) String() string {
	return tea.Prettify(s)
}

func (s GetUserRequest) GoString() string {
	return s.String()
}

func (s *GetUserRequest) SetHeaders(v map[string]*string) *GetUserRequest {
	s.Headers = v
	return s
}

func (s *GetUserRequest) SetUserId(v string) *GetUserRequest {
	s.UserId = &v
	return s
}

/**
 * Get user response
 */
type GetUserResponse struct {
	// 头像
	Avatar *string `json:"avatar,omitempty" xml:"avatar,omitempty"`
	// 用户创建时间
	CreatedAt *int64 `json:"created_at,omitempty" xml:"created_at,omitempty"`
	// 默认 Drive ID
	DefaultDriveId *string `json:"default_drive_id,omitempty" xml:"default_drive_id,omitempty"`
	// 用户备注信息
	Description *string `json:"description,omitempty" xml:"description,omitempty"`
	// Domain ID
	DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
	// 邮箱
	Email *string `json:"email,omitempty" xml:"email,omitempty"`
	// 昵称
	NickName *string `json:"nick_name,omitempty" xml:"nick_name,omitempty"`
	// 电话
	Phone *string `json:"phone,omitempty" xml:"phone,omitempty"`
	// 角色
	Role *string `json:"role,omitempty" xml:"role,omitempty"`
	// 用户状态
	Status *string `json:"status,omitempty" xml:"status,omitempty"`
	// 用户修改时间
	UpdatedAt *int64 `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
	// 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
	UserData map[string]interface{} `json:"user_data,omitempty" xml:"user_data,omitempty"`
	// 用户 ID
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty"`
	// 用户名称
	UserName *string `json:"user_name,omitempty" xml:"user_name,omitempty"`
}

func (s GetUserResponse) String() string {
	return tea.Prettify(s)
}

func (s GetUserResponse) GoString() string {
	return s.String()
}

func (s *GetUserResponse) SetAvatar(v string) *GetUserResponse {
	s.Avatar = &v
	return s
}

func (s *GetUserResponse) SetCreatedAt(v int64) *GetUserResponse {
	s.CreatedAt = &v
	return s
}

func (s *GetUserResponse) SetDefaultDriveId(v string) *GetUserResponse {
	s.DefaultDriveId = &v
	return s
}

func (s *GetUserResponse) SetDescription(v string) *GetUserResponse {
	s.Description = &v
	return s
}

func (s *GetUserResponse) SetDomainId(v string) *GetUserResponse {
	s.DomainId = &v
	return s
}

func (s *GetUserResponse) SetEmail(v string) *GetUserResponse {
	s.Email = &v
	return s
}

func (s *GetUserResponse) SetNickName(v string) *GetUserResponse {
	s.NickName = &v
	return s
}

func (s *GetUserResponse) SetPhone(v string) *GetUserResponse {
	s.Phone = &v
	return s
}

func (s *GetUserResponse) SetRole(v string) *GetUserResponse {
	s.Role = &v
	return s
}

func (s *GetUserResponse) SetStatus(v string) *GetUserResponse {
	s.Status = &v
	return s
}

func (s *GetUserResponse) SetUpdatedAt(v int64) *GetUserResponse {
	s.UpdatedAt = &v
	return s
}

func (s *GetUserResponse) SetUserData(v map[string]interface{}) *GetUserResponse {
	s.UserData = v
	return s
}

func (s *GetUserResponse) SetUserId(v string) *GetUserResponse {
	s.UserId = &v
	return s
}

func (s *GetUserResponse) SetUserName(v string) *GetUserResponse {
	s.UserName = &v
	return s
}

/**
 * List user request
 */
type ListUserRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 每页大小限制
	Limit *int `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
	// 翻页标记
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
}

func (s ListUserRequest) String() string {
	return tea.Prettify(s)
}

func (s ListUserRequest) GoString() string {
	return s.String()
}

func (s *ListUserRequest) SetHeaders(v map[string]*string) *ListUserRequest {
	s.Headers = v
	return s
}

func (s *ListUserRequest) SetLimit(v int) *ListUserRequest {
	s.Limit = &v
	return s
}

func (s *ListUserRequest) SetMarker(v string) *ListUserRequest {
	s.Marker = &v
	return s
}

/**
 * List user response
 */
type ListUserResponse struct {
	Items []*BaseUserResponse `json:"items,omitempty" xml:"items,omitempty" type:"Repeated"`
	// 翻页标记
	NextMarker *string `json:"next_marker,omitempty" xml:"next_marker,omitempty"`
}

func (s ListUserResponse) String() string {
	return tea.Prettify(s)
}

func (s ListUserResponse) GoString() string {
	return s.String()
}

func (s *ListUserResponse) SetItems(v []*BaseUserResponse) *ListUserResponse {
	s.Items = v
	return s
}

func (s *ListUserResponse) SetNextMarker(v string) *ListUserResponse {
	s.NextMarker = &v
	return s
}

/**
 * Search user request
 */
type SearchUserRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 邮箱
	Email *string `json:"email,omitempty" xml:"email,omitempty"`
	// 每页大小限制
	Limit *int `json:"limit,omitempty" xml:"limit,omitempty" maximum:"100" minimum:"1"`
	// 翻页标记
	Marker *string `json:"marker,omitempty" xml:"marker,omitempty"`
	// 昵称
	NickName *string `json:"nick_name,omitempty" xml:"nick_name,omitempty"`
	// 电话号码
	Phone *string `json:"phone,omitempty" xml:"phone,omitempty"`
	// 角色
	Role *string `json:"role,omitempty" xml:"role,omitempty"`
	// 状态
	Status *string `json:"status,omitempty" xml:"status,omitempty"`
	// 用户名
	UserName *string `json:"user_name,omitempty" xml:"user_name,omitempty"`
}

func (s SearchUserRequest) String() string {
	return tea.Prettify(s)
}

func (s SearchUserRequest) GoString() string {
	return s.String()
}

func (s *SearchUserRequest) SetHeaders(v map[string]*string) *SearchUserRequest {
	s.Headers = v
	return s
}

func (s *SearchUserRequest) SetEmail(v string) *SearchUserRequest {
	s.Email = &v
	return s
}

func (s *SearchUserRequest) SetLimit(v int) *SearchUserRequest {
	s.Limit = &v
	return s
}

func (s *SearchUserRequest) SetMarker(v string) *SearchUserRequest {
	s.Marker = &v
	return s
}

func (s *SearchUserRequest) SetNickName(v string) *SearchUserRequest {
	s.NickName = &v
	return s
}

func (s *SearchUserRequest) SetPhone(v string) *SearchUserRequest {
	s.Phone = &v
	return s
}

func (s *SearchUserRequest) SetRole(v string) *SearchUserRequest {
	s.Role = &v
	return s
}

func (s *SearchUserRequest) SetStatus(v string) *SearchUserRequest {
	s.Status = &v
	return s
}

func (s *SearchUserRequest) SetUserName(v string) *SearchUserRequest {
	s.UserName = &v
	return s
}

/**
 * Update user request
 */
type UpdateUserRequest struct {
	Headers map[string]*string `json:"headers,omitempty" xml:"headers,omitempty"`
	// 头像
	Avatar *string `json:"avatar,omitempty" xml:"avatar,omitempty"`
	// 描述信息
	Description *string `json:"description,omitempty" xml:"description,omitempty" maxLength:"1024"`
	// 邮箱
	Email *string `json:"email,omitempty" xml:"email,omitempty"`
	// 昵称
	NickName *string `json:"nick_name,omitempty" xml:"nick_name,omitempty"`
	// 电话号码
	Phone *string `json:"phone,omitempty" xml:"phone,omitempty"`
	// 角色
	Role *string `json:"role,omitempty" xml:"role,omitempty"`
	// 状态
	Status *string `json:"status,omitempty" xml:"status,omitempty"`
	// 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
	UserData map[string]interface{} `json:"user_data,omitempty" xml:"user_data,omitempty"`
	// 用户 ID
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty" require:"true"`
}

func (s UpdateUserRequest) String() string {
	return tea.Prettify(s)
}

func (s UpdateUserRequest) GoString() string {
	return s.String()
}

func (s *UpdateUserRequest) SetHeaders(v map[string]*string) *UpdateUserRequest {
	s.Headers = v
	return s
}

func (s *UpdateUserRequest) SetAvatar(v string) *UpdateUserRequest {
	s.Avatar = &v
	return s
}

func (s *UpdateUserRequest) SetDescription(v string) *UpdateUserRequest {
	s.Description = &v
	return s
}

func (s *UpdateUserRequest) SetEmail(v string) *UpdateUserRequest {
	s.Email = &v
	return s
}

func (s *UpdateUserRequest) SetNickName(v string) *UpdateUserRequest {
	s.NickName = &v
	return s
}

func (s *UpdateUserRequest) SetPhone(v string) *UpdateUserRequest {
	s.Phone = &v
	return s
}

func (s *UpdateUserRequest) SetRole(v string) *UpdateUserRequest {
	s.Role = &v
	return s
}

func (s *UpdateUserRequest) SetStatus(v string) *UpdateUserRequest {
	s.Status = &v
	return s
}

func (s *UpdateUserRequest) SetUserData(v map[string]interface{}) *UpdateUserRequest {
	s.UserData = v
	return s
}

func (s *UpdateUserRequest) SetUserId(v string) *UpdateUserRequest {
	s.UserId = &v
	return s
}

/**
 * Update user response
 */
type UpdateUserResponse struct {
	// 头像
	Avatar *string `json:"avatar,omitempty" xml:"avatar,omitempty"`
	// 用户创建时间
	CreatedAt *int64 `json:"created_at,omitempty" xml:"created_at,omitempty"`
	// 默认 Drive ID
	DefaultDriveId *string `json:"default_drive_id,omitempty" xml:"default_drive_id,omitempty"`
	// 用户备注信息
	Description *string `json:"description,omitempty" xml:"description,omitempty"`
	// Domain ID
	DomainId *string `json:"domain_id,omitempty" xml:"domain_id,omitempty"`
	// 邮箱
	Email *string `json:"email,omitempty" xml:"email,omitempty"`
	// 昵称
	NickName *string `json:"nick_name,omitempty" xml:"nick_name,omitempty"`
	// 电话
	Phone *string `json:"phone,omitempty" xml:"phone,omitempty"`
	// 角色
	Role *string `json:"role,omitempty" xml:"role,omitempty"`
	// 用户状态
	Status *string `json:"status,omitempty" xml:"status,omitempty"`
	// 用户修改时间
	UpdatedAt *int64 `json:"updated_at,omitempty" xml:"updated_at,omitempty"`
	// 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
	UserData map[string]interface{} `json:"user_data,omitempty" xml:"user_data,omitempty"`
	// 用户 ID
	UserId *string `json:"user_id,omitempty" xml:"user_id,omitempty"`
	// 用户名称
	UserName *string `json:"user_name,omitempty" xml:"user_name,omitempty"`
}

func (s UpdateUserResponse) String() string {
	return tea.Prettify(s)
}

func (s UpdateUserResponse) GoString() string {
	return s.String()
}

func (s *UpdateUserResponse) SetAvatar(v string) *UpdateUserResponse {
	s.Avatar = &v
	return s
}

func (s *UpdateUserResponse) SetCreatedAt(v int64) *UpdateUserResponse {
	s.CreatedAt = &v
	return s
}

func (s *UpdateUserResponse) SetDefaultDriveId(v string) *UpdateUserResponse {
	s.DefaultDriveId = &v
	return s
}

func (s *UpdateUserResponse) SetDescription(v string) *UpdateUserResponse {
	s.Description = &v
	return s
}

func (s *UpdateUserResponse) SetDomainId(v string) *UpdateUserResponse {
	s.DomainId = &v
	return s
}

func (s *UpdateUserResponse) SetEmail(v string) *UpdateUserResponse {
	s.Email = &v
	return s
}

func (s *UpdateUserResponse) SetNickName(v string) *UpdateUserResponse {
	s.NickName = &v
	return s
}

func (s *UpdateUserResponse) SetPhone(v string) *UpdateUserResponse {
	s.Phone = &v
	return s
}

func (s *UpdateUserResponse) SetRole(v string) *UpdateUserResponse {
	s.Role = &v
	return s
}

func (s *UpdateUserResponse) SetStatus(v string) *UpdateUserResponse {
	s.Status = &v
	return s
}

func (s *UpdateUserResponse) SetUpdatedAt(v int64) *UpdateUserResponse {
	s.UpdatedAt = &v
	return s
}

func (s *UpdateUserResponse) SetUserData(v map[string]interface{}) *UpdateUserResponse {
	s.UserData = v
	return s
}

func (s *UpdateUserResponse) SetUserId(v string) *UpdateUserResponse {
	s.UserId = &v
	return s
}

func (s *UpdateUserResponse) SetUserName(v string) *UpdateUserResponse {
	s.UserName = &v
	return s
}

type Client struct {
	DomainId              *string
	AccessTokenCredential *accesstokencredential.AccessTokenCredential
	Endpoint              *string
	Protocol              *string
	Nickname              *string
	UserAgent             *string
	Credential            credential.Credential
}

func NewClient(config *Config) (*Client, error) {
	client := new(Client)
	err := client.Init(config)
	return client, err
}

func (client *Client) Init(config *Config) (_err error) {
	if tea.BoolValue(util.IsUnset(tea.ToMap(config))) {
		_err = tea.NewSDKError(map[string]interface{}{
			"name":    "ParameterMissing",
			"message": "'config' can not be unset",
		})
		return _err
	}

	_err = util.ValidateModel(config)
	if _err != nil {
		return _err
	}
	if !tea.BoolValue(util.Empty(config.AccessToken)) || !tea.BoolValue(util.Empty(config.RefreshToken)) {
		accessConfig := &accesstokencredential.Config{
			AccessToken:  config.AccessToken,
			Endpoint:     config.Endpoint,
			DomainId:     config.DomainId,
			ClientId:     config.ClientId,
			RefreshToken: config.RefreshToken,
			ClientSecret: config.ClientSecret,
			ExpireTime:   config.ExpireTime,
		}
		client.AccessTokenCredential, _err = accesstokencredential.NewAccessTokenCredential(accessConfig)
		if _err != nil {
			return _err
		}

	}

	if !tea.BoolValue(util.Empty(config.AccessKeyId)) {
		if tea.BoolValue(util.Empty(config.Type)) {
			config.Type = tea.String("access_key")
		}

		credentialConfig := &credential.Config{
			AccessKeyId:     config.AccessKeyId,
			Type:            config.Type,
			AccessKeySecret: config.AccessKeySecret,
			SecurityToken:   config.SecurityToken,
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
	client.DomainId = config.DomainId
	return nil
}

/**
 * 取消绑定关系，生成新用户，返回访问令牌
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) CancelLinkEx(request *CancelLinkRequest, runtime *RuntimeOptions) (_result *CancelLinkModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &CancelLinkModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*CancelLinkModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/cancel_link"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &CancelLinkModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 确认绑定关系, 成功后返回访问令牌
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) ConfirmLinkEx(request *ConfirmLinkRequest, runtime *RuntimeOptions) (_result *ConfirmLinkModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &ConfirmLinkModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*ConfirmLinkModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/confirm_link"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &ConfirmLinkModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 修改手机登录密码，密码必须包含数字和字母，长度8-20个字符
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) ChangePasswordEx(request *DefaultChangePasswordRequest, runtime *RuntimeOptions) (_result *ChangePasswordModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &ChangePasswordModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*ChangePasswordModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/default/change_password"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &ChangePasswordModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 设置手机登录密码，密码必须包含数字和字母，长度8-20个字符
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetPasswordEx(request *DefaultSetPasswordRequest, runtime *RuntimeOptions) (_result *SetPasswordModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &SetPasswordModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*SetPasswordModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/default/set_password"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &SetPasswordModel{}
				_err = tea.Convert(map[string]map[string]*string{
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 校验手机短信验证码，用于重置密码时校验手机，通过校验后返回state，可通过state重新设置密码
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) VerifyCodeEx(request *VerifyCodeRequest, runtime *RuntimeOptions) (_result *VerifyCodeModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &VerifyCodeModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*VerifyCodeModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/default/verify_code"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &VerifyCodeModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 管理员通过账号信息直接获取用户的访问令牌
 * @tags account
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetAccessTokenByLinkInfoEx(request *GetAccessTokenByLinkInfoRequest, runtime *RuntimeOptions) (_result *GetAccessTokenByLinkInfoModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetAccessTokenByLinkInfoModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetAccessTokenByLinkInfoModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/get_access_token_by_link_info"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetAccessTokenByLinkInfoModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 获取图片验证码，用于人机校验，默认不需要
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetCaptchaEx(request *GetCaptchaRequest, runtime *RuntimeOptions) (_result *GetCaptchaModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetCaptchaModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetCaptchaModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/get_captcha"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetCaptchaModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 获取用户认证方式详情
 * @tags account
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetLinkInfoEx(request *GetByLinkInfoRequest, runtime *RuntimeOptions) (_result *GetLinkInfoModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetLinkInfoModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetLinkInfoModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/get_link_info"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetLinkInfoModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 获取用户的所有绑定信息
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetLinkInfoByUserIdEx(request *GetLinkInfoByUserIDRequest, runtime *RuntimeOptions) (_result *GetLinkInfoByUserIdModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetLinkInfoByUserIdModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetLinkInfoByUserIdModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/get_link_info_by_user_id"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetLinkInfoByUserIdModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 获取公钥，用于加密对称密钥
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
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
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
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

		_resp, _err = func() (*GetPublicKeyModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/get_public_key"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 绑定用户认证方式
 * @tags account
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error AlreadyExist {resource} has already exists. {extra_msg}
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) LinkEx(request *AccountLinkRequest, runtime *RuntimeOptions) (_result *LinkModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &LinkModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*LinkModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/link"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &LinkModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 查询手机号是否已被注册
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) CheckExistEx(request *MobileCheckExistRequest, runtime *RuntimeOptions) (_result *CheckExistModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &CheckExistModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*CheckExistModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/mobile/check_exist"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &CheckExistModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 通过手机号+短信或密码登录，返回刷新令牌和访问令牌
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) LoginEx(request *MobileLoginRequest, runtime *RuntimeOptions) (_result *LoginModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &LoginModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*LoginModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/mobile/login"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &LoginModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 通过手机号+短信验证码注册账号
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error AlreadyExist {resource} has already exists. {extra_msg}
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) RegisterEx(request *MobileRegisterRequest, runtime *RuntimeOptions) (_result *RegisterModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &RegisterModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*RegisterModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/mobile/register"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &RegisterModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 发送短信验证码，用于登录、注册、修改密码、绑定等
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) MobileSendSmsCodeEx(request *MobileSendSmsCodeRequest, runtime *RuntimeOptions) (_result *MobileSendSmsCodeModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &MobileSendSmsCodeModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*MobileSendSmsCodeModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/mobile/send_sms_code"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &MobileSendSmsCodeModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 用户退出登录
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) AccountRevokeEx(request *RevokeRequest, runtime *RuntimeOptions) (_result *AccountRevokeModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &AccountRevokeModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*AccountRevokeModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/revoke"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &AccountRevokeModel{}
				_err = tea.Convert(map[string]map[string]*string{
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 用户通过刷新令牌（refresh_token）获取访问令牌（access_token）
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) AccountTokenEx(request *TokenRequest, runtime *RuntimeOptions) (_result *AccountTokenModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &AccountTokenModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*AccountTokenModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/account/token"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".auth.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &AccountTokenModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 列举Store列表
 * @tags admin
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) AdminListStoresEx(request *AdminListStoresRequest, runtime *RuntimeOptions) (_result *AdminListStoresModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &AdminListStoresModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*AdminListStoresModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/domain/list_stores"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &AdminListStoresModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 获取用户的accessToken
 * @tags admin
 * @error undefined undefined
 * @error undefined undefined
 * @error undefined undefined
 * @error undefined undefined
 * @error undefined undefined
 */
func (client *Client) GetUserAccessTokenEx(request *GetUserAccessTokenRequest, runtime *RuntimeOptions) (_result *GetUserAccessTokenModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetUserAccessTokenModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetUserAccessTokenModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/user/get_access_token"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetUserAccessTokenModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 支持normal和large两种drive，
 * large类型的drive用于文件数多的场景，不支持list操作，
 * 当drive的文件数量大于1亿时，建议使用large类型。
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CreateDriveEx(request *CreateDriveRequest, runtime *RuntimeOptions) (_result *CreateDriveModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &CreateDriveModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*CreateDriveModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/drive/create"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &CreateDriveModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 删除指定drive_id对应的Drive
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) DeleteDriveEx(request *DeleteDriveRequest, runtime *RuntimeOptions) (_result *DeleteDriveModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &DeleteDriveModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*DeleteDriveModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/drive/delete"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &DeleteDriveModel{}
				_err = tea.Convert(map[string]map[string]*string{
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 获取指定drive_id对应的Drive详细信息。
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetDriveEx(request *GetDriveRequest, runtime *RuntimeOptions) (_result *GetDriveModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetDriveModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetDriveModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/drive/get"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetDriveModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 一个用户可拥有多个drive，在创建drive时通过参数指定是否为这个用户的默认drive，
 * 每个用户只能设置一个默认drive。
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetDefaultDriveEx(request *GetDefaultDriveRequest, runtime *RuntimeOptions) (_result *GetDefaultDriveModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetDefaultDriveModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetDefaultDriveModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/drive/get_default_drive"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetDefaultDriveModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 管理员列举指定用户的Drive
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListDrivesEx(request *ListDriveRequest, runtime *RuntimeOptions) (_result *ListDrivesModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &ListDrivesModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*ListDrivesModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/drive/list"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &ListDrivesModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 列举当前用户（访问令牌）的Drive
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListMyDrivesEx(request *ListMyDriveRequest, runtime *RuntimeOptions) (_result *ListMyDrivesModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &ListMyDrivesModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*ListMyDrivesModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/drive/list_my_drives"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &ListMyDrivesModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 更新指定drive_id的Drive信息
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) UpdateDriveEx(request *UpdateDriveRequest, runtime *RuntimeOptions) (_result *UpdateDriveModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &UpdateDriveModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*UpdateDriveModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/drive/update"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &UpdateDriveModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 完成文件上传
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CompleteFileEx(request *HostingCompleteFileRequest, runtime *RuntimeOptions) (_result *CompleteFileModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &CompleteFileModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*CompleteFileModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/complete"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &CompleteFileModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 指定源文件或文件夹路径，拷贝到指定的文件夹。
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CopyFileEx(request *HostingCopyFileRequest, runtime *RuntimeOptions) (_result *CopyFileModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &CopyFileModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*CopyFileModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/copy"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &CopyFileModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 创建文件或者文件夹。
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error AlreadyExist {resource} has already exists. {extra_msg}
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CreateFileEx(request *HostingCreateFileRequest, runtime *RuntimeOptions) (_result *CreateFileModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &CreateFileModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*CreateFileModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/create"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &CreateFileModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 指定文件或文件夹路径，删除文件或文件夹
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) DeleteFileEx(request *HostingDeleteFileRequest, runtime *RuntimeOptions) (_result *DeleteFileModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &DeleteFileModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*DeleteFileModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/delete"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &DeleteFileModel{}
				_err = tea.Convert(map[string]map[string]*string{
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 获取指定文件或文件夹路径，获取文件或文件夹信息。
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetFileEx(request *HostingGetFileRequest, runtime *RuntimeOptions) (_result *GetFileModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetFileModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetFileModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/get"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetFileModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 指定文件路径，获取文件下载地址
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetDownloadUrlEx(request *HostingGetDownloadUrlRequest, runtime *RuntimeOptions) (_result *GetDownloadUrlModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetDownloadUrlModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetDownloadUrlModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/get_download_url"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetDownloadUrlModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 指定文件路径，获取文件安全地址
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetSecureUrlEx(request *HostingGetSecureUrlRequest, runtime *RuntimeOptions) (_result *GetSecureUrlModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetSecureUrlModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetSecureUrlModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/get_secure_url"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetSecureUrlModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 可指定分片信息，一次获取多个分片的上传地址。
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetUploadUrlEx(request *HostingGetUploadUrlRequest, runtime *RuntimeOptions) (_result *GetUploadUrlModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetUploadUrlModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetUploadUrlModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/get_upload_url"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetUploadUrlModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 指定父文件夹路径，列举文件夹下的文件或者文件夹
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListFileEx(request *HostingListFileRequest, runtime *RuntimeOptions) (_result *ListFileModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &ListFileModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*ListFileModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/list"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &ListFileModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 列举UploadID对应的已上传分片。
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListUploadedPartsEx(request *HostingListUploadedPartRequest, runtime *RuntimeOptions) (_result *ListUploadedPartsModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &ListUploadedPartsModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*ListUploadedPartsModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/list_uploaded_parts"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &ListUploadedPartsModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 指定源文件或文件夹路径，移动到指定的文件夹。
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) MoveFileEx(request *HostingMoveFileRequest, runtime *RuntimeOptions) (_result *MoveFileModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &MoveFileModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*MoveFileModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/move"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &MoveFileModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 获取视频支持的分辨率
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) VideoDefinitionEx(request *HostingVideoDefinitionRequest, runtime *RuntimeOptions) (_result *VideoDefinitionModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &VideoDefinitionModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*VideoDefinitionModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/video_definition"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &VideoDefinitionModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 获取视频的DRM License
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) VideoLicenseEx(request *HostingVideoDRMLicenseRequest, runtime *RuntimeOptions) (_result *VideoLicenseModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &VideoLicenseModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*VideoLicenseModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/video_license"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &VideoLicenseModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 获取视频转码后的m3u8文件
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) VideoM3u8Ex(request *HostingVideoM3U8Request, runtime *RuntimeOptions) (_result *VideoM3u8Model, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &VideoM3u8Model{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*VideoM3u8Model, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/video_m3u8"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				byt, _err := util.ReadAsBytes(response_.Body)
				if _err != nil {
					return _result, _err
				}

				_result = &VideoM3u8Model{}
				_err = tea.Convert(map[string]interface{}{
					"body":    byt,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 将mp4格式的视频文件，转为m3u8
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) VideoTranscodeEx(request *HostingVideoTranscodeRequest, runtime *RuntimeOptions) (_result *VideoTranscodeModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &VideoTranscodeModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*VideoTranscodeModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/file/video_transcode"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &VideoTranscodeModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if tea.BoolValue(util.EqualNumber(response_.StatusCode, tea.Int(204))) {
				_result = &VideoTranscodeModel{}
				_err = tea.Convert(map[string]map[string]*string{
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 创建共享。
 * @tags share
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CreateShareEx(request *CreateShareRequest, runtime *RuntimeOptions) (_result *CreateShareModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &CreateShareModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*CreateShareModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/share/create"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &CreateShareModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 删除指定共享
 * @tags share
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) DeleteShareEx(request *DeleteShareRequest, runtime *RuntimeOptions) (_result *DeleteShareModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &DeleteShareModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*DeleteShareModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/share/delete"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &DeleteShareModel{}
				_err = tea.Convert(map[string]map[string]*string{
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 获取共享信息。
 * @tags share
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetShareEx(request *GetShareRequest, runtime *RuntimeOptions) (_result *GetShareModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetShareModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetShareModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/share/get"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetShareModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 列举指定用户的共享
 * @tags share
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListShareEx(request *ListShareRequest, runtime *RuntimeOptions) (_result *ListShareModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &ListShareModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*ListShareModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/share/list"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &ListShareModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 修改指定共享
 * @tags share
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) UpdateShareEx(request *UpdateShareRequest, runtime *RuntimeOptions) (_result *UpdateShareModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &UpdateShareModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*UpdateShareModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/share/update"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &UpdateShareModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 列举指定store下的所有文件。
 * @tags store
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListStorefileEx(request *ListStoreFileRequest, runtime *RuntimeOptions) (_result *ListStorefileModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &ListStorefileModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*ListStorefileModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/hosting/store_file/list"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &ListStorefileModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 创建用户，只有管理员可以调用
 * @tags user
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CreateUserEx(request *CreateUserRequest, runtime *RuntimeOptions) (_result *CreateUserModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &CreateUserModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*CreateUserModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/user/create"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &CreateUserModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 只有管理员可以调用
 * @tags user
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) DeleteUserEx(request *DeleteUserRequest, runtime *RuntimeOptions) (_result *DeleteUserModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &DeleteUserModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*DeleteUserModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/user/delete"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &DeleteUserModel{}
				_err = tea.Convert(map[string]map[string]*string{
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 获取用户详细信息，普通用户只能获取自己的信息，管理员可以获取任意用户的信息。
 * @tags user
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetUserEx(request *GetUserRequest, runtime *RuntimeOptions) (_result *GetUserModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &GetUserModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*GetUserModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/user/get"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &GetUserModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 只有管理员可以调用
 * @tags user
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListUsersEx(request *ListUserRequest, runtime *RuntimeOptions) (_result *ListUsersModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &ListUsersModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*ListUsersModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/user/list"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &ListUsersModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 该接口将会根据条件查询用户，只有管理员可以调用
 * @tags user
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) SearchUserEx(request *SearchUserRequest, runtime *RuntimeOptions) (_result *SearchUserModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &SearchUserModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*SearchUserModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/user/search"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &SearchUserModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 用户可以修改自己的description，nick_name，avatar；
 * 管理员在用户基础上还可修改status（可以修改任意用户）；
 * 超级管理员在管理员基础上还可修改role（可以修改任意用户）。
 * @tags user
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) UpdateUserEx(request *UpdateUserRequest, runtime *RuntimeOptions) (_result *UpdateUserModel, _err error) {
	_err = tea.Validate(request)
	if _err != nil {
		return _result, _err
	}
	_err = tea.Validate(runtime)
	if _err != nil {
		return _result, _err
	}
	_runtime := map[string]interface{}{
		"timeouted":      "retry",
		"readTimeout":    tea.IntValue(runtime.ReadTimeout),
		"connectTimeout": tea.IntValue(runtime.ConnectTimeout),
		"localAddr":      tea.StringValue(runtime.LocalAddr),
		"httpProxy":      tea.StringValue(runtime.HttpProxy),
		"httpsProxy":     tea.StringValue(runtime.HttpsProxy),
		"noProxy":        tea.StringValue(runtime.NoProxy),
		"maxIdleConns":   tea.IntValue(runtime.MaxIdleConns),
		"socks5Proxy":    tea.StringValue(runtime.Socks5Proxy),
		"socks5NetWork":  tea.StringValue(runtime.Socks5NetWork),
		"retry": map[string]interface{}{
			"retryable":   tea.BoolValue(runtime.Autoretry),
			"maxAttempts": tea.IntValue(util.DefaultNumber(runtime.MaxAttempts, tea.Int(3))),
		},
		"backoff": map[string]interface{}{
			"policy": tea.StringValue(util.DefaultString(runtime.BackoffPolicy, tea.String("no"))),
			"period": tea.IntValue(util.DefaultNumber(runtime.BackoffPeriod, tea.Int(1))),
		},
		"ignoreSSL": tea.BoolValue(runtime.IgnoreSSL),
	}

	_resp := &UpdateUserModel{}
	for _retryTimes := 0; tea.BoolValue(tea.AllowRetry(_runtime["retry"], tea.Int(_retryTimes))); _retryTimes++ {
		if _retryTimes > 0 {
			_backoffTime := tea.GetBackoffTime(_runtime["backoff"], tea.Int(_retryTimes))
			if tea.IntValue(_backoffTime) > 0 {
				tea.Sleep(_backoffTime)
			}
		}

		_resp, _err = func() (*UpdateUserModel, error) {
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

			accessToken, _err := client.GetAccessToken()
			if _err != nil {
				return _result, _err
			}

			realReq := util.ToMap(request)
			request_.Protocol = util.DefaultString(client.Protocol, tea.String("https"))
			request_.Method = tea.String("POST")
			request_.Pathname = client.GetPathname(client.Nickname, tea.String("/v2/user/update"))
			request_.Headers = tea.Merge(map[string]*string{
				"user-agent":   client.GetUserAgent(),
				"host":         util.DefaultString(client.Endpoint, tea.String(tea.StringValue(client.DomainId)+".api.aliyunpds.com")),
				"content-type": tea.String("application/json; charset=utf-8"),
			}, request.Headers)
			realReq["headers"] = nil
			if !tea.BoolValue(util.Empty(accessToken)) {
				request_.Headers["authorization"] = tea.String("Bearer " + tea.StringValue(accessToken))
			} else if !tea.BoolValue(util.Empty(accesskeyId)) && !tea.BoolValue(util.Empty(accessKeySecret)) {
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
				_result = &UpdateUserModel{}
				_err = tea.Convert(map[string]interface{}{
					"body":    respMap,
					"headers": response_.Headers,
				}, &_result)
				return _result, _err
			}

			if !tea.BoolValue(util.Empty(response_.Headers["x-ca-error-message"])) {
				_err = tea.NewSDKError(map[string]interface{}{
					"data": map[string]interface{}{
						"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
						"statusCode":    tea.IntValue(response_.StatusCode),
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
					"requestId":     tea.StringValue(response_.Headers["x-ca-request-id"]),
					"statusCode":    tea.IntValue(response_.StatusCode),
					"statusMessage": tea.StringValue(response_.StatusMessage),
				},
			}, respMap))
			return _result, _err
		}()
		if !tea.BoolValue(tea.Retryable(_err)) {
			break
		}
	}

	return _resp, _err
}

/**
 * 取消绑定关系，生成新用户，返回访问令牌
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) CancelLink(request *CancelLinkRequest) (_result *CancelLinkModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &CancelLinkModel{}
	_body, _err := client.CancelLinkEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 确认绑定关系, 成功后返回访问令牌
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) ConfirmLink(request *ConfirmLinkRequest) (_result *ConfirmLinkModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &ConfirmLinkModel{}
	_body, _err := client.ConfirmLinkEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 修改手机登录密码，密码必须包含数字和字母，长度8-20个字符
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) ChangePassword(request *DefaultChangePasswordRequest) (_result *ChangePasswordModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &ChangePasswordModel{}
	_body, _err := client.ChangePasswordEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 设置手机登录密码，密码必须包含数字和字母，长度8-20个字符
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) SetPassword(request *DefaultSetPasswordRequest) (_result *SetPasswordModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &SetPasswordModel{}
	_body, _err := client.SetPasswordEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 校验手机短信验证码，用于重置密码时校验手机，通过校验后返回state，可通过state重新设置密码
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) VerifyCode(request *VerifyCodeRequest) (_result *VerifyCodeModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &VerifyCodeModel{}
	_body, _err := client.VerifyCodeEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 管理员通过账号信息直接获取用户的访问令牌
 * @tags account
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetAccessTokenByLinkInfo(request *GetAccessTokenByLinkInfoRequest) (_result *GetAccessTokenByLinkInfoModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetAccessTokenByLinkInfoModel{}
	_body, _err := client.GetAccessTokenByLinkInfoEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 获取图片验证码，用于人机校验，默认不需要
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetCaptcha(request *GetCaptchaRequest) (_result *GetCaptchaModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetCaptchaModel{}
	_body, _err := client.GetCaptchaEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 获取用户认证方式详情
 * @tags account
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetLinkInfo(request *GetByLinkInfoRequest) (_result *GetLinkInfoModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetLinkInfoModel{}
	_body, _err := client.GetLinkInfoEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 获取用户的所有绑定信息
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetLinkInfoByUserId(request *GetLinkInfoByUserIDRequest) (_result *GetLinkInfoByUserIdModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetLinkInfoByUserIdModel{}
	_body, _err := client.GetLinkInfoByUserIdEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 获取公钥，用于加密对称密钥
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) GetPublicKey(request *GetAppPublicKeyRequest) (_result *GetPublicKeyModel, _err error) {
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
 * 绑定用户认证方式
 * @tags account
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error AlreadyExist {resource} has already exists. {extra_msg}
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) Link(request *AccountLinkRequest) (_result *LinkModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &LinkModel{}
	_body, _err := client.LinkEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 查询手机号是否已被注册
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) CheckExist(request *MobileCheckExistRequest) (_result *CheckExistModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &CheckExistModel{}
	_body, _err := client.CheckExistEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 通过手机号+短信或密码登录，返回刷新令牌和访问令牌
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) Login(request *MobileLoginRequest) (_result *LoginModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &LoginModel{}
	_body, _err := client.LoginEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 通过手机号+短信验证码注册账号
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error AlreadyExist {resource} has already exists. {extra_msg}
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) Register(request *MobileRegisterRequest) (_result *RegisterModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &RegisterModel{}
	_body, _err := client.RegisterEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 发送短信验证码，用于登录、注册、修改密码、绑定等
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) MobileSendSmsCode(request *MobileSendSmsCodeRequest) (_result *MobileSendSmsCodeModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &MobileSendSmsCodeModel{}
	_body, _err := client.MobileSendSmsCodeEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 用户退出登录
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) AccountRevoke(request *RevokeRequest) (_result *AccountRevokeModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &AccountRevokeModel{}
	_body, _err := client.AccountRevokeEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 用户通过刷新令牌（refresh_token）获取访问令牌（access_token）
 * @tags account
 * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) AccountToken(request *TokenRequest) (_result *AccountTokenModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &AccountTokenModel{}
	_body, _err := client.AccountTokenEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 列举Store列表
 * @tags admin
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error Forbidden User not authorized to operate on the specified APIs.
 * @error InternalError The request has been failed due to some unknown error.
 */
func (client *Client) AdminListStores(request *AdminListStoresRequest) (_result *AdminListStoresModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &AdminListStoresModel{}
	_body, _err := client.AdminListStoresEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 获取用户的accessToken
 * @tags admin
 * @error undefined undefined
 * @error undefined undefined
 * @error undefined undefined
 * @error undefined undefined
 * @error undefined undefined
 */
func (client *Client) GetUserAccessToken(request *GetUserAccessTokenRequest) (_result *GetUserAccessTokenModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetUserAccessTokenModel{}
	_body, _err := client.GetUserAccessTokenEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 支持normal和large两种drive，
 * large类型的drive用于文件数多的场景，不支持list操作，
 * 当drive的文件数量大于1亿时，建议使用large类型。
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CreateDrive(request *CreateDriveRequest) (_result *CreateDriveModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &CreateDriveModel{}
	_body, _err := client.CreateDriveEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 删除指定drive_id对应的Drive
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) DeleteDrive(request *DeleteDriveRequest) (_result *DeleteDriveModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &DeleteDriveModel{}
	_body, _err := client.DeleteDriveEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 获取指定drive_id对应的Drive详细信息。
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetDrive(request *GetDriveRequest) (_result *GetDriveModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetDriveModel{}
	_body, _err := client.GetDriveEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 一个用户可拥有多个drive，在创建drive时通过参数指定是否为这个用户的默认drive，
 * 每个用户只能设置一个默认drive。
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetDefaultDrive(request *GetDefaultDriveRequest) (_result *GetDefaultDriveModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetDefaultDriveModel{}
	_body, _err := client.GetDefaultDriveEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 管理员列举指定用户的Drive
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListDrives(request *ListDriveRequest) (_result *ListDrivesModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &ListDrivesModel{}
	_body, _err := client.ListDrivesEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 列举当前用户（访问令牌）的Drive
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListMyDrives(request *ListMyDriveRequest) (_result *ListMyDrivesModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &ListMyDrivesModel{}
	_body, _err := client.ListMyDrivesEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 更新指定drive_id的Drive信息
 * @tags drive
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) UpdateDrive(request *UpdateDriveRequest) (_result *UpdateDriveModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &UpdateDriveModel{}
	_body, _err := client.UpdateDriveEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 完成文件上传
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CompleteFile(request *HostingCompleteFileRequest) (_result *CompleteFileModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &CompleteFileModel{}
	_body, _err := client.CompleteFileEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 指定源文件或文件夹路径，拷贝到指定的文件夹。
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CopyFile(request *HostingCopyFileRequest) (_result *CopyFileModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &CopyFileModel{}
	_body, _err := client.CopyFileEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 创建文件或者文件夹。
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error AlreadyExist {resource} has already exists. {extra_msg}
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CreateFile(request *HostingCreateFileRequest) (_result *CreateFileModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &CreateFileModel{}
	_body, _err := client.CreateFileEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 指定文件或文件夹路径，删除文件或文件夹
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) DeleteFile(request *HostingDeleteFileRequest) (_result *DeleteFileModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &DeleteFileModel{}
	_body, _err := client.DeleteFileEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 获取指定文件或文件夹路径，获取文件或文件夹信息。
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetFile(request *HostingGetFileRequest) (_result *GetFileModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetFileModel{}
	_body, _err := client.GetFileEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 指定文件路径，获取文件下载地址
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetDownloadUrl(request *HostingGetDownloadUrlRequest) (_result *GetDownloadUrlModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetDownloadUrlModel{}
	_body, _err := client.GetDownloadUrlEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 指定文件路径，获取文件安全地址
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetSecureUrl(request *HostingGetSecureUrlRequest) (_result *GetSecureUrlModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetSecureUrlModel{}
	_body, _err := client.GetSecureUrlEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 可指定分片信息，一次获取多个分片的上传地址。
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetUploadUrl(request *HostingGetUploadUrlRequest) (_result *GetUploadUrlModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetUploadUrlModel{}
	_body, _err := client.GetUploadUrlEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 指定父文件夹路径，列举文件夹下的文件或者文件夹
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListFile(request *HostingListFileRequest) (_result *ListFileModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &ListFileModel{}
	_body, _err := client.ListFileEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 列举UploadID对应的已上传分片。
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListUploadedParts(request *HostingListUploadedPartRequest) (_result *ListUploadedPartsModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &ListUploadedPartsModel{}
	_body, _err := client.ListUploadedPartsEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 指定源文件或文件夹路径，移动到指定的文件夹。
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) MoveFile(request *HostingMoveFileRequest) (_result *MoveFileModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &MoveFileModel{}
	_body, _err := client.MoveFileEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 获取视频支持的分辨率
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) VideoDefinition(request *HostingVideoDefinitionRequest) (_result *VideoDefinitionModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &VideoDefinitionModel{}
	_body, _err := client.VideoDefinitionEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 获取视频的DRM License
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) VideoLicense(request *HostingVideoDRMLicenseRequest) (_result *VideoLicenseModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &VideoLicenseModel{}
	_body, _err := client.VideoLicenseEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 获取视频转码后的m3u8文件
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) VideoM3u8(request *HostingVideoM3U8Request) (_result *VideoM3u8Model, _err error) {
	runtime := &RuntimeOptions{}
	_result = &VideoM3u8Model{}
	_body, _err := client.VideoM3u8Ex(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 将mp4格式的视频文件，转为m3u8
 * @tags file
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) VideoTranscode(request *HostingVideoTranscodeRequest) (_result *VideoTranscodeModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &VideoTranscodeModel{}
	_body, _err := client.VideoTranscodeEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 创建共享。
 * @tags share
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CreateShare(request *CreateShareRequest) (_result *CreateShareModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &CreateShareModel{}
	_body, _err := client.CreateShareEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 删除指定共享
 * @tags share
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) DeleteShare(request *DeleteShareRequest) (_result *DeleteShareModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &DeleteShareModel{}
	_body, _err := client.DeleteShareEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 获取共享信息。
 * @tags share
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetShare(request *GetShareRequest) (_result *GetShareModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetShareModel{}
	_body, _err := client.GetShareEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 列举指定用户的共享
 * @tags share
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListShare(request *ListShareRequest) (_result *ListShareModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &ListShareModel{}
	_body, _err := client.ListShareEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 修改指定共享
 * @tags share
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) UpdateShare(request *UpdateShareRequest) (_result *UpdateShareModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &UpdateShareModel{}
	_body, _err := client.UpdateShareEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 列举指定store下的所有文件。
 * @tags store
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListStorefile(request *ListStoreFileRequest) (_result *ListStorefileModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &ListStorefileModel{}
	_body, _err := client.ListStorefileEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 创建用户，只有管理员可以调用
 * @tags user
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) CreateUser(request *CreateUserRequest) (_result *CreateUserModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &CreateUserModel{}
	_body, _err := client.CreateUserEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 只有管理员可以调用
 * @tags user
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) DeleteUser(request *DeleteUserRequest) (_result *DeleteUserModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &DeleteUserModel{}
	_body, _err := client.DeleteUserEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 获取用户详细信息，普通用户只能获取自己的信息，管理员可以获取任意用户的信息。
 * @tags user
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) GetUser(request *GetUserRequest) (_result *GetUserModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &GetUserModel{}
	_body, _err := client.GetUserEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 只有管理员可以调用
 * @tags user
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) ListUsers(request *ListUserRequest) (_result *ListUsersModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &ListUsersModel{}
	_body, _err := client.ListUsersEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 该接口将会根据条件查询用户，只有管理员可以调用
 * @tags user
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) SearchUser(request *SearchUserRequest) (_result *SearchUserModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &SearchUserModel{}
	_body, _err := client.SearchUserEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

/**
 * 用户可以修改自己的description，nick_name，avatar；
 * 管理员在用户基础上还可修改status（可以修改任意用户）；
 * 超级管理员在管理员基础上还可修改role（可以修改任意用户）。
 * @tags user
 * @error InvalidParameter The input parameter {parameter_name} is not valid.
 * @error AccessTokenInvalid AccessToken is invalid. {message}
 * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
 * @error NotFound The resource {resource_name} cannot be found. Please check.
 * @error InternalError The request has been failed due to some unknown error.
 * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
 */
func (client *Client) UpdateUser(request *UpdateUserRequest) (_result *UpdateUserModel, _err error) {
	runtime := &RuntimeOptions{}
	_result = &UpdateUserModel{}
	_body, _err := client.UpdateUserEx(request, runtime)
	if _err != nil {
		return _result, _err
	}
	_result = _body
	return _result, _err
}

func (client *Client) GetPathname(nickname *string, path *string) (_result *string) {
	if tea.BoolValue(util.Empty(nickname)) {
		_result = path
		return _result
	}

	_result = tea.String("/" + tea.StringValue(nickname) + tea.StringValue(path))
	return _result
}

func (client *Client) SetExpireTime(expireTime *string) (_err error) {
	if tea.BoolValue(util.IsUnset(client.AccessTokenCredential)) {
		return _err
	}

	client.AccessTokenCredential.SetExpireTime(expireTime)
	return _err
}

func (client *Client) GetExpireTime() (_result *string) {
	if tea.BoolValue(util.IsUnset(client.AccessTokenCredential)) {
		return _result
	}

	expireTime := client.AccessTokenCredential.GetExpireTime()
	_result = expireTime
	return _result
}

func (client *Client) SetRefreshToken(token *string) {
	if tea.BoolValue(util.IsUnset(client.AccessTokenCredential)) {
		return
	}

	client.AccessTokenCredential.SetRefreshToken(token)
}

func (client *Client) GetRefreshToken() (_result *string) {
	if tea.BoolValue(util.IsUnset(client.AccessTokenCredential)) {
		return _result
	}

	token := client.AccessTokenCredential.GetRefreshToken()
	_result = token
	return _result
}

func (client *Client) SetAccessToken(token *string) {
	if tea.BoolValue(util.IsUnset(client.AccessTokenCredential)) {
		return
	}

	client.AccessTokenCredential.SetAccessToken(token)
}

func (client *Client) GetAccessToken() (_result *string, _err error) {
	if tea.BoolValue(util.IsUnset(client.AccessTokenCredential)) {
		return _result, _err
	}

	token, _err := client.AccessTokenCredential.GetAccessToken()
	if _err != nil {
		return _result, _err
	}

	_result = token
	return _result, _err
}

func (client *Client) SetUserAgent(userAgent *string) {
	client.UserAgent = userAgent
}

func (client *Client) AppendUserAgent(userAgent *string) {
	client.UserAgent = tea.String(tea.StringValue(client.UserAgent) + " " + tea.StringValue(userAgent))
}

func (client *Client) GetUserAgent() (_result *string) {
	userAgent := util.GetUserAgent(client.UserAgent)
	_result = userAgent
	return _result
}

func (client *Client) GetAccessKeyId() (_result *string, _err error) {
	if tea.BoolValue(util.IsUnset(client.Credential)) {
		return _result, _err
	}

	accessKeyId, _err := client.Credential.GetAccessKeyId()
	if _err != nil {
		return _result, _err
	}

	_result = accessKeyId
	return _result, _err
}

func (client *Client) GetAccessKeySecret() (_result *string, _err error) {
	if tea.BoolValue(util.IsUnset(client.Credential)) {
		return _result, _err
	}

	secret, _err := client.Credential.GetAccessKeySecret()
	if _err != nil {
		return _result, _err
	}

	_result = secret
	return _result, _err
}

func (client *Client) GetSecurityToken() (_result *string, _err error) {
	if tea.BoolValue(util.IsUnset(client.Credential)) {
		return _result, _err
	}

	token, _err := client.Credential.GetSecurityToken()
	if _err != nil {
		return _result, _err
	}

	_result = token
	return _result, _err
}
