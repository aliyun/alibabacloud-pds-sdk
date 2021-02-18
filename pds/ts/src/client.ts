// This file is auto-generated, don't edit it
/**
 *
 */
import Util from '@alicloud/tea-util';
import ROAUtil from '@alicloud/roa-util';
import Credential, * as $Credential from '@alicloud/credentials';
import AccessTokenCredential, * as $AccessTokenCredential from '@alicloud/pds-credentials';
import * as $tea from '@alicloud/tea-typescript';

export class RuntimeOptions extends $tea.Model {
  autoretry?: boolean;
  ignoreSSL?: boolean;
  maxAttempts?: number;
  backoffPolicy?: string;
  backoffPeriod?: number;
  readTimeout?: number;
  connectTimeout?: number;
  httpProxy?: string;
  httpsProxy?: string;
  noProxy?: string;
  maxIdleConns?: number;
  localAddr?: string;
  socks5Proxy?: string;
  socks5NetWork?: string;
  static names(): { [key: string]: string } {
    return {
      autoretry: 'autoretry',
      ignoreSSL: 'ignoreSSL',
      maxAttempts: 'maxAttempts',
      backoffPolicy: 'backoffPolicy',
      backoffPeriod: 'backoffPeriod',
      readTimeout: 'readTimeout',
      connectTimeout: 'connectTimeout',
      httpProxy: 'httpProxy',
      httpsProxy: 'httpsProxy',
      noProxy: 'noProxy',
      maxIdleConns: 'maxIdleConns',
      localAddr: 'localAddr',
      socks5Proxy: 'socks5Proxy',
      socks5NetWork: 'socks5NetWork',
    };
  }

  static types(): { [key: string]: any } {
    return {
      autoretry: 'boolean',
      ignoreSSL: 'boolean',
      maxAttempts: 'number',
      backoffPolicy: 'string',
      backoffPeriod: 'number',
      readTimeout: 'number',
      connectTimeout: 'number',
      httpProxy: 'string',
      httpsProxy: 'string',
      noProxy: 'string',
      maxIdleConns: 'number',
      localAddr: 'string',
      socks5Proxy: 'string',
      socks5NetWork: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class Config extends $tea.Model {
  endpoint?: string;
  domainId?: string;
  clientId?: string;
  refreshToken?: string;
  clientSecret?: string;
  accessToken?: string;
  expireTime?: string;
  protocol?: string;
  type?: string;
  securityToken?: string;
  accessKeyId?: string;
  accessKeySecret?: string;
  nickname?: string;
  userAgent?: string;
  static names(): { [key: string]: string } {
    return {
      endpoint: 'endpoint',
      domainId: 'domainId',
      clientId: 'clientId',
      refreshToken: 'refreshToken',
      clientSecret: 'clientSecret',
      accessToken: 'accessToken',
      expireTime: 'expireTime',
      protocol: 'protocol',
      type: 'type',
      securityToken: 'securityToken',
      accessKeyId: 'accessKeyId',
      accessKeySecret: 'accessKeySecret',
      nickname: 'nickname',
      userAgent: 'userAgent',
    };
  }

  static types(): { [key: string]: any } {
    return {
      endpoint: 'string',
      domainId: 'string',
      clientId: 'string',
      refreshToken: 'string',
      clientSecret: 'string',
      accessToken: 'string',
      expireTime: 'string',
      protocol: 'string',
      type: 'string',
      securityToken: 'string',
      accessKeyId: 'string',
      accessKeySecret: 'string',
      nickname: 'string',
      userAgent: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class CancelLinkModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: AccountAccessTokenResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: AccountAccessTokenResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ConfirmLinkModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: AccountAccessTokenResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: AccountAccessTokenResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ChangePasswordModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: AccountAccessTokenResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: AccountAccessTokenResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class SetPasswordModel extends $tea.Model {
  headers?: { [key: string]: string };
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class VerifyCodeModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: VerifyCodeResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: VerifyCodeResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetAccessTokenByLinkInfoModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: AccountAccessTokenResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: AccountAccessTokenResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetCaptchaModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: Captcha;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: Captcha,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetLinkInfoModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: LinkInfoResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: LinkInfoResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetLinkInfoByUserIdModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: LinkInfoListResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: LinkInfoListResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetPublicKeyModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetPublicKeyResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetPublicKeyResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class LinkModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: AccountAccessTokenResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: AccountAccessTokenResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class CheckExistModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: MobileCheckExistResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: MobileCheckExistResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class LoginModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: AccountAccessTokenResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: AccountAccessTokenResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class RegisterModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: AccountAccessTokenResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: AccountAccessTokenResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class MobileSendSmsCodeModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: MobileSendSmsCodeResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: MobileSendSmsCodeResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class AccountRevokeModel extends $tea.Model {
  headers?: { [key: string]: string };
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class AccountTokenModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: AccountAccessTokenResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: AccountAccessTokenResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class AccessTokenResponse extends $tea.Model {
  accessToken: string;
  defaultDriveId: string;
  expireTime: string;
  expiresIn: number;
  refreshToken: string;
  role: string;
  tokenType: string;
  userId: string;
  static names(): { [key: string]: string } {
    return {
      accessToken: 'access_token',
      defaultDriveId: 'default_drive_id',
      expireTime: 'expire_time',
      expiresIn: 'expires_in',
      refreshToken: 'refresh_token',
      role: 'role',
      tokenType: 'token_type',
      userId: 'user_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      accessToken: 'string',
      defaultDriveId: 'string',
      expireTime: 'string',
      expiresIn: 'number',
      refreshToken: 'string',
      role: 'string',
      tokenType: 'string',
      userId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class AccountAccessTokenResponse extends $tea.Model {
  accessToken: string;
  avatar?: string;
  defaultDriveId?: string;
  defaultSboxDriveId?: string;
  deviceId?: string;
  deviceName?: string;
  existLink?: LinkInfo[];
  expireTime?: string;
  expiresIn?: number;
  isFirstLogin?: boolean;
  needLink: boolean;
  needRpVerify?: boolean;
  nickName?: string;
  pinSetup?: boolean;
  refreshToken?: string;
  role?: string;
  state?: string;
  tokenType?: string;
  userData?: {[key: string]: any};
  userId?: string;
  userName?: string;
  static names(): { [key: string]: string } {
    return {
      accessToken: 'access_token',
      avatar: 'avatar',
      defaultDriveId: 'default_drive_id',
      defaultSboxDriveId: 'default_sbox_drive_id',
      deviceId: 'device_id',
      deviceName: 'device_name',
      existLink: 'exist_link',
      expireTime: 'expire_time',
      expiresIn: 'expires_in',
      isFirstLogin: 'is_first_login',
      needLink: 'need_link',
      needRpVerify: 'need_rp_verify',
      nickName: 'nick_name',
      pinSetup: 'pin_setup',
      refreshToken: 'refresh_token',
      role: 'role',
      state: 'state',
      tokenType: 'token_type',
      userData: 'user_data',
      userId: 'user_id',
      userName: 'user_name',
    };
  }

  static types(): { [key: string]: any } {
    return {
      accessToken: 'string',
      avatar: 'string',
      defaultDriveId: 'string',
      defaultSboxDriveId: 'string',
      deviceId: 'string',
      deviceName: 'string',
      existLink: { 'type': 'array', 'itemType': LinkInfo },
      expireTime: 'string',
      expiresIn: 'number',
      isFirstLogin: 'boolean',
      needLink: 'boolean',
      needRpVerify: 'boolean',
      nickName: 'string',
      pinSetup: 'boolean',
      refreshToken: 'string',
      role: 'string',
      state: 'string',
      tokenType: 'string',
      userData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      userId: 'string',
      userName: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class AccountLinkRequest extends $tea.Model {
  headers?: { [key: string]: string };
  detail?: string;
  extra?: string;
  identity: string;
  status?: string;
  type: string;
  userId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      detail: 'detail',
      extra: 'extra',
      identity: 'identity',
      status: 'status',
      type: 'type',
      userId: 'user_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      detail: 'string',
      extra: 'string',
      identity: 'string',
      status: 'string',
      type: 'string',
      userId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class AccountTokenRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  appId: string;
  grantType: string;
  refreshToken: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      appId: 'app_id',
      grantType: 'grant_type',
      refreshToken: 'refresh_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      appId: 'string',
      grantType: 'string',
      refreshToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class AddStoreRequest extends $tea.Model {
  basePath?: string;
  bucket?: string;
  domainId: string;
  endpoint: string;
  ownership?: string;
  roleArn?: string;
  type: string;
  static names(): { [key: string]: string } {
    return {
      basePath: 'base_path',
      bucket: 'bucket',
      domainId: 'domain_id',
      endpoint: 'endpoint',
      ownership: 'ownership',
      roleArn: 'role_arn',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      basePath: 'string',
      bucket: 'string',
      domainId: 'string',
      endpoint: 'string',
      ownership: 'string',
      roleArn: 'string',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class AppAccessStrategy extends $tea.Model {
  effect?: string;
  exceptAppIdList?: string[];
  static names(): { [key: string]: string } {
    return {
      effect: 'effect',
      exceptAppIdList: 'except_app_id_list',
    };
  }

  static types(): { [key: string]: any } {
    return {
      effect: 'string',
      exceptAppIdList: { 'type': 'array', 'itemType': 'string' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class AuthConfig extends $tea.Model {
  appId?: string;
  appSecret?: string;
  callbackSecurity?: boolean;
  enable?: boolean;
  endpoint?: string;
  enterpriseId?: string;
  ldapConfig?: LdapConfig;
  loginPageHeaders?: {[key: string]: any};
  loginPageTemplate?: string;
  loginPageVars?: {[key: string]: any};
  whiteListConfig?: {[key: string]: any};
  whiteListEnable?: boolean;
  static names(): { [key: string]: string } {
    return {
      appId: 'app_id',
      appSecret: 'app_secret',
      callbackSecurity: 'callback_security',
      enable: 'enable',
      endpoint: 'endpoint',
      enterpriseId: 'enterprise_id',
      ldapConfig: 'ldap_config',
      loginPageHeaders: 'login_page_headers',
      loginPageTemplate: 'login_page_template',
      loginPageVars: 'login_page_vars',
      whiteListConfig: 'white_list_config',
      whiteListEnable: 'white_list_enable',
    };
  }

  static types(): { [key: string]: any } {
    return {
      appId: 'string',
      appSecret: 'string',
      callbackSecurity: 'boolean',
      enable: 'boolean',
      endpoint: 'string',
      enterpriseId: 'string',
      ldapConfig: LdapConfig,
      loginPageHeaders: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      loginPageTemplate: 'string',
      loginPageVars: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      whiteListConfig: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      whiteListEnable: 'boolean',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class AuthorizeRequest extends $tea.Model {
  ClientID: string;
  LoginType?: string;
  RedirectUri: string;
  ResponseType: string;
  Scope?: string[];
  State?: string;
  UserCode?: string;
  static names(): { [key: string]: string } {
    return {
      ClientID: 'ClientID',
      LoginType: 'LoginType',
      RedirectUri: 'RedirectUri',
      ResponseType: 'ResponseType',
      Scope: 'Scope',
      State: 'State',
      UserCode: 'UserCode',
    };
  }

  static types(): { [key: string]: any } {
    return {
      ClientID: 'string',
      LoginType: 'string',
      RedirectUri: 'string',
      ResponseType: 'string',
      Scope: { 'type': 'array', 'itemType': 'string' },
      State: 'string',
      UserCode: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Base file response
 */
export class BaseCCPFileResponse extends $tea.Model {
  category?: string;
  characteristicHash?: string;
  contentHash?: string;
  contentHashName?: string;
  contentType?: string;
  crc64Hash?: string;
  createdAt?: string;
  description?: string;
  domainId?: string;
  downloadUrl?: string;
  driveId?: string;
  encryptMode?: string;
  fileExtension?: string;
  fileId?: string;
  hidden?: boolean;
  imageMediaMetadata?: ImageMediaResponse;
  labels?: string[];
  meta?: string;
  name: string;
  parentFileId?: string;
  punishFlag?: number;
  shareId?: string;
  size?: number;
  starred?: boolean;
  status?: string;
  streamsInfo?: {[key: string]: any};
  thumbnail?: string;
  trashedAt?: string;
  type?: string;
  updatedAt?: string;
  uploadId?: string;
  url?: string;
  userMeta?: string;
  videoMediaMetadata?: VideoMediaResponse;
  videoPreviewMetadata?: VideoPreviewResponse;
  static names(): { [key: string]: string } {
    return {
      category: 'category',
      characteristicHash: 'characteristic_hash',
      contentHash: 'content_hash',
      contentHashName: 'content_hash_name',
      contentType: 'content_type',
      crc64Hash: 'crc64_hash',
      createdAt: 'created_at',
      description: 'description',
      domainId: 'domain_id',
      downloadUrl: 'download_url',
      driveId: 'drive_id',
      encryptMode: 'encrypt_mode',
      fileExtension: 'file_extension',
      fileId: 'file_id',
      hidden: 'hidden',
      imageMediaMetadata: 'image_media_metadata',
      labels: 'labels',
      meta: 'meta',
      name: 'name',
      parentFileId: 'parent_file_id',
      punishFlag: 'punish_flag',
      shareId: 'share_id',
      size: 'size',
      starred: 'starred',
      status: 'status',
      streamsInfo: 'streams_info',
      thumbnail: 'thumbnail',
      trashedAt: 'trashed_at',
      type: 'type',
      updatedAt: 'updated_at',
      uploadId: 'upload_id',
      url: 'url',
      userMeta: 'user_meta',
      videoMediaMetadata: 'video_media_metadata',
      videoPreviewMetadata: 'video_preview_metadata',
    };
  }

  static types(): { [key: string]: any } {
    return {
      category: 'string',
      characteristicHash: 'string',
      contentHash: 'string',
      contentHashName: 'string',
      contentType: 'string',
      crc64Hash: 'string',
      createdAt: 'string',
      description: 'string',
      domainId: 'string',
      downloadUrl: 'string',
      driveId: 'string',
      encryptMode: 'string',
      fileExtension: 'string',
      fileId: 'string',
      hidden: 'boolean',
      imageMediaMetadata: ImageMediaResponse,
      labels: { 'type': 'array', 'itemType': 'string' },
      meta: 'string',
      name: 'string',
      parentFileId: 'string',
      punishFlag: 'number',
      shareId: 'string',
      size: 'number',
      starred: 'boolean',
      status: 'string',
      streamsInfo: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      thumbnail: 'string',
      trashedAt: 'string',
      type: 'string',
      updatedAt: 'string',
      uploadId: 'string',
      url: 'string',
      userMeta: 'string',
      videoMediaMetadata: VideoMediaResponse,
      videoPreviewMetadata: VideoPreviewResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Base drive response
 */
export class BaseDriveResponse extends $tea.Model {
  creator?: string;
  description?: string;
  domainId?: string;
  driveId?: string;
  driveName?: string;
  driveType?: string;
  encryptDataAccess?: boolean;
  encryptMode?: string;
  owner?: string;
  relativePath?: string;
  status?: string;
  storeId?: string;
  totalSize?: number;
  usedSize?: number;
  static names(): { [key: string]: string } {
    return {
      creator: 'creator',
      description: 'description',
      domainId: 'domain_id',
      driveId: 'drive_id',
      driveName: 'drive_name',
      driveType: 'drive_type',
      encryptDataAccess: 'encrypt_data_access',
      encryptMode: 'encrypt_mode',
      owner: 'owner',
      relativePath: 'relative_path',
      status: 'status',
      storeId: 'store_id',
      totalSize: 'total_size',
      usedSize: 'used_size',
    };
  }

  static types(): { [key: string]: any } {
    return {
      creator: 'string',
      description: 'string',
      domainId: 'string',
      driveId: 'string',
      driveName: 'string',
      driveType: 'string',
      encryptDataAccess: 'boolean',
      encryptMode: 'string',
      owner: 'string',
      relativePath: 'string',
      status: 'string',
      storeId: 'string',
      totalSize: 'number',
      usedSize: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list_file_by_anonymous base response
 */
export class BaseFileAnonymousResponse extends $tea.Model {
  fileId?: string;
  name?: string;
  size?: number;
  thumbnail?: string;
  type?: string;
  updatedAt?: string;
  static names(): { [key: string]: string } {
    return {
      fileId: 'file_id',
      name: 'name',
      size: 'size',
      thumbnail: 'thumbnail',
      type: 'type',
      updatedAt: 'updated_at',
    };
  }

  static types(): { [key: string]: any } {
    return {
      fileId: 'string',
      name: 'string',
      size: 'number',
      thumbnail: 'string',
      type: 'string',
      updatedAt: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Base file response
 */
export class BaseHostingFileResponse extends $tea.Model {
  contentHash?: string;
  contentHashName?: string;
  contentType?: string;
  crc64Hash?: string;
  createdAt?: string;
  description?: string;
  domainId?: string;
  downloadUrl?: string;
  driveId?: string;
  fileExtension?: string;
  filePath?: string;
  name: string;
  parentFilePath?: string;
  shareId?: string;
  size?: number;
  status?: string;
  thumbnail?: string;
  trashedAt?: string;
  type?: string;
  updatedAt?: string;
  uploadId?: string;
  url?: string;
  static names(): { [key: string]: string } {
    return {
      contentHash: 'content_hash',
      contentHashName: 'content_hash_name',
      contentType: 'content_type',
      crc64Hash: 'crc64_hash',
      createdAt: 'created_at',
      description: 'description',
      domainId: 'domain_id',
      downloadUrl: 'download_url',
      driveId: 'drive_id',
      fileExtension: 'file_extension',
      filePath: 'file_path',
      name: 'name',
      parentFilePath: 'parent_file_path',
      shareId: 'share_id',
      size: 'size',
      status: 'status',
      thumbnail: 'thumbnail',
      trashedAt: 'trashed_at',
      type: 'type',
      updatedAt: 'updated_at',
      uploadId: 'upload_id',
      url: 'url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      contentHash: 'string',
      contentHashName: 'string',
      contentType: 'string',
      crc64Hash: 'string',
      createdAt: 'string',
      description: 'string',
      domainId: 'string',
      downloadUrl: 'string',
      driveId: 'string',
      fileExtension: 'string',
      filePath: 'string',
      name: 'string',
      parentFilePath: 'string',
      shareId: 'string',
      size: 'number',
      status: 'string',
      thumbnail: 'string',
      trashedAt: 'string',
      type: 'string',
      updatedAt: 'string',
      uploadId: 'string',
      url: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list_share_link response
 */
export class BaseShareLinkResponse extends $tea.Model {
  createdAt?: string;
  creator?: string;
  description?: string;
  downloadCount?: number;
  driveId?: string;
  expiration?: string;
  expired?: boolean;
  fileId?: string;
  fileIdList?: string[];
  filePathList?: string[];
  previewCount?: number;
  saveCount?: number;
  shareId?: string;
  shareMsg?: string;
  shareName?: string;
  sharePolicy?: string;
  sharePwd?: string;
  shareUrl?: string;
  updatedAt?: string;
  static names(): { [key: string]: string } {
    return {
      createdAt: 'created_at',
      creator: 'creator',
      description: 'description',
      downloadCount: 'download_count',
      driveId: 'drive_id',
      expiration: 'expiration',
      expired: 'expired',
      fileId: 'file_id',
      fileIdList: 'file_id_list',
      filePathList: 'file_path_list',
      previewCount: 'preview_count',
      saveCount: 'save_count',
      shareId: 'share_id',
      shareMsg: 'share_msg',
      shareName: 'share_name',
      sharePolicy: 'share_policy',
      sharePwd: 'share_pwd',
      shareUrl: 'share_url',
      updatedAt: 'updated_at',
    };
  }

  static types(): { [key: string]: any } {
    return {
      createdAt: 'string',
      creator: 'string',
      description: 'string',
      downloadCount: 'number',
      driveId: 'string',
      expiration: 'string',
      expired: 'boolean',
      fileId: 'string',
      fileIdList: { 'type': 'array', 'itemType': 'string' },
      filePathList: { 'type': 'array', 'itemType': 'string' },
      previewCount: 'number',
      saveCount: 'number',
      shareId: 'string',
      shareMsg: 'string',
      shareName: 'string',
      sharePolicy: 'string',
      sharePwd: 'string',
      shareUrl: 'string',
      updatedAt: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List share response
 */
export class BaseShareResponse extends $tea.Model {
  createdAt?: string;
  creator?: string;
  description?: string;
  domainId?: string;
  driveId?: string;
  expiration?: string;
  expired?: boolean;
  owner?: string;
  permissions?: string[];
  shareFileId?: string;
  shareFilePath?: string;
  shareId?: string;
  shareName?: string;
  sharePolicy?: SharePermissionPolicy[];
  status?: string;
  updatedAt?: string;
  static names(): { [key: string]: string } {
    return {
      createdAt: 'created_at',
      creator: 'creator',
      description: 'description',
      domainId: 'domain_id',
      driveId: 'drive_id',
      expiration: 'expiration',
      expired: 'expired',
      owner: 'owner',
      permissions: 'permissions',
      shareFileId: 'share_file_id',
      shareFilePath: 'share_file_path',
      shareId: 'share_id',
      shareName: 'share_name',
      sharePolicy: 'share_policy',
      status: 'status',
      updatedAt: 'updated_at',
    };
  }

  static types(): { [key: string]: any } {
    return {
      createdAt: 'string',
      creator: 'string',
      description: 'string',
      domainId: 'string',
      driveId: 'string',
      expiration: 'string',
      expired: 'boolean',
      owner: 'string',
      permissions: { 'type': 'array', 'itemType': 'string' },
      shareFileId: 'string',
      shareFilePath: 'string',
      shareId: 'string',
      shareName: 'string',
      sharePolicy: { 'type': 'array', 'itemType': SharePermissionPolicy },
      status: 'string',
      updatedAt: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * batch operation response
 */
export class BatchResponse extends $tea.Model {
  responses?: BatchSubResponse[];
  static names(): { [key: string]: string } {
    return {
      responses: 'responses',
    };
  }

  static types(): { [key: string]: any } {
    return {
      responses: { 'type': 'array', 'itemType': BatchSubResponse },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class BatchSubResponse extends $tea.Model {
  body?: {[key: string]: any};
  id?: string;
  status?: number;
  static names(): { [key: string]: string } {
    return {
      body: 'body',
      id: 'id',
      status: 'status',
    };
  }

  static types(): { [key: string]: any } {
    return {
      body: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      id: 'string',
      status: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class CancelLinkRequest extends $tea.Model {
  headers?: { [key: string]: string };
  temporaryToken: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      temporaryToken: 'temporary_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      temporaryToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class Captcha extends $tea.Model {
  captcha: string;
  captchaFormat: string;
  captchaId: string;
  static names(): { [key: string]: string } {
    return {
      captcha: 'captcha',
      captchaFormat: 'captcha_format',
      captchaId: 'captcha_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      captcha: 'string',
      captchaFormat: 'string',
      captchaId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * complete file response
 */
export class CompleteFileResponse extends $tea.Model {
  category?: string;
  characteristicHash?: string;
  contentHash?: string;
  contentHashName?: string;
  contentType?: string;
  crc64Hash?: string;
  createdAt?: string;
  description?: string;
  domainId?: string;
  downloadUrl?: string;
  driveId?: string;
  encryptMode?: string;
  fileExtension?: string;
  fileId?: string;
  hidden?: boolean;
  imageMediaMetadata?: ImageMediaResponse;
  labels?: string[];
  location?: string;
  meta?: string;
  name: string;
  parentFileId?: string;
  punishFlag?: number;
  shareId?: string;
  size?: number;
  starred?: boolean;
  status?: string;
  streamLocations?: {[key: string]: any};
  streamsInfo?: {[key: string]: any};
  thumbnail?: string;
  trashedAt?: string;
  type?: string;
  updatedAt?: string;
  uploadId?: string;
  url?: string;
  userMeta?: string;
  videoMediaMetadata?: VideoMediaResponse;
  videoPreviewMetadata?: VideoPreviewResponse;
  static names(): { [key: string]: string } {
    return {
      category: 'category',
      characteristicHash: 'characteristic_hash',
      contentHash: 'content_hash',
      contentHashName: 'content_hash_name',
      contentType: 'content_type',
      crc64Hash: 'crc64_hash',
      createdAt: 'created_at',
      description: 'description',
      domainId: 'domain_id',
      downloadUrl: 'download_url',
      driveId: 'drive_id',
      encryptMode: 'encrypt_mode',
      fileExtension: 'file_extension',
      fileId: 'file_id',
      hidden: 'hidden',
      imageMediaMetadata: 'image_media_metadata',
      labels: 'labels',
      location: 'location',
      meta: 'meta',
      name: 'name',
      parentFileId: 'parent_file_id',
      punishFlag: 'punish_flag',
      shareId: 'share_id',
      size: 'size',
      starred: 'starred',
      status: 'status',
      streamLocations: 'stream_locations',
      streamsInfo: 'streams_info',
      thumbnail: 'thumbnail',
      trashedAt: 'trashed_at',
      type: 'type',
      updatedAt: 'updated_at',
      uploadId: 'upload_id',
      url: 'url',
      userMeta: 'user_meta',
      videoMediaMetadata: 'video_media_metadata',
      videoPreviewMetadata: 'video_preview_metadata',
    };
  }

  static types(): { [key: string]: any } {
    return {
      category: 'string',
      characteristicHash: 'string',
      contentHash: 'string',
      contentHashName: 'string',
      contentType: 'string',
      crc64Hash: 'string',
      createdAt: 'string',
      description: 'string',
      domainId: 'string',
      downloadUrl: 'string',
      driveId: 'string',
      encryptMode: 'string',
      fileExtension: 'string',
      fileId: 'string',
      hidden: 'boolean',
      imageMediaMetadata: ImageMediaResponse,
      labels: { 'type': 'array', 'itemType': 'string' },
      location: 'string',
      meta: 'string',
      name: 'string',
      parentFileId: 'string',
      punishFlag: 'number',
      shareId: 'string',
      size: 'number',
      starred: 'boolean',
      status: 'string',
      streamLocations: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      streamsInfo: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      thumbnail: 'string',
      trashedAt: 'string',
      type: 'string',
      updatedAt: 'string',
      uploadId: 'string',
      url: 'string',
      userMeta: 'string',
      videoMediaMetadata: VideoMediaResponse,
      videoPreviewMetadata: VideoPreviewResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class ConfirmLinkRequest extends $tea.Model {
  headers?: { [key: string]: string };
  temporaryToken: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      temporaryToken: 'temporary_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      temporaryToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 文件拷贝 response
 */
export class CopyFileResponse extends $tea.Model {
  asyncTaskId?: string;
  domainId?: string;
  driveId?: string;
  fileId?: string;
  static names(): { [key: string]: string } {
    return {
      asyncTaskId: 'async_task_id',
      domainId: 'domain_id',
      driveId: 'drive_id',
      fileId: 'file_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      asyncTaskId: 'string',
      domainId: 'string',
      driveId: 'string',
      fileId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class CorsRule extends $tea.Model {
  allowedHeader?: string[];
  allowedMethod?: string[];
  allowedOrigin?: string[];
  exposeHeader?: string[];
  maxAgeSeconds?: number;
  static names(): { [key: string]: string } {
    return {
      allowedHeader: 'allowed_header',
      allowedMethod: 'allowed_method',
      allowedOrigin: 'allowed_origin',
      exposeHeader: 'expose_header',
      maxAgeSeconds: 'max_age_seconds',
    };
  }

  static types(): { [key: string]: any } {
    return {
      allowedHeader: { 'type': 'array', 'itemType': 'string' },
      allowedMethod: { 'type': 'array', 'itemType': 'string' },
      allowedOrigin: { 'type': 'array', 'itemType': 'string' },
      exposeHeader: { 'type': 'array', 'itemType': 'string' },
      maxAgeSeconds: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class CreateAppRequest extends $tea.Model {
  appName: string;
  description?: string;
  isThirdParty?: boolean;
  logo: string;
  publicKey: string;
  redirectUri?: string;
  scope: string[];
  type: string;
  static names(): { [key: string]: string } {
    return {
      appName: 'app_name',
      description: 'description',
      isThirdParty: 'is_third_party',
      logo: 'logo',
      publicKey: 'public_key',
      redirectUri: 'redirect_uri',
      scope: 'scope',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      appName: 'string',
      description: 'string',
      isThirdParty: 'boolean',
      logo: 'string',
      publicKey: 'string',
      redirectUri: 'string',
      scope: { 'type': 'array', 'itemType': 'string' },
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * create domain request
 */
export class CreateDomainRequest extends $tea.Model {
  authConfig?: {[key: string]: any};
  authDingdingAppId?: string;
  authDingdingAppSecret?: string;
  authDingdingEnable?: boolean;
  authEndpointEnable?: boolean;
  authRamAppId?: string;
  authRamAppSecret?: string;
  authRamEnable?: boolean;
  dataHashName?: string;
  description?: string;
  domainName: string;
  eventFilenameMatches?: string;
  eventMnsEndpoint?: string;
  eventMnsTopic?: string;
  eventNames?: string[];
  eventRoleArn?: string;
  initDriveEnable?: boolean;
  initDriveSize?: number;
  mode: string;
  pathType?: string;
  publishedAppAccessStrategy?: AppAccessStrategy;
  sharable?: boolean;
  storeLevel?: string;
  storeRegionList: string[];
  static names(): { [key: string]: string } {
    return {
      authConfig: 'auth_config',
      authDingdingAppId: 'auth_dingding_app_id',
      authDingdingAppSecret: 'auth_dingding_app_secret',
      authDingdingEnable: 'auth_dingding_enable',
      authEndpointEnable: 'auth_endpoint_enable',
      authRamAppId: 'auth_ram_app_id',
      authRamAppSecret: 'auth_ram_app_secret',
      authRamEnable: 'auth_ram_enable',
      dataHashName: 'data_hash_name',
      description: 'description',
      domainName: 'domain_name',
      eventFilenameMatches: 'event_filename_matches',
      eventMnsEndpoint: 'event_mns_endpoint',
      eventMnsTopic: 'event_mns_topic',
      eventNames: 'event_names',
      eventRoleArn: 'event_role_arn',
      initDriveEnable: 'init_drive_enable',
      initDriveSize: 'init_drive_size',
      mode: 'mode',
      pathType: 'path_type',
      publishedAppAccessStrategy: 'published_app_access_strategy',
      sharable: 'sharable',
      storeLevel: 'store_level',
      storeRegionList: 'store_region_list',
    };
  }

  static types(): { [key: string]: any } {
    return {
      authConfig: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      authDingdingAppId: 'string',
      authDingdingAppSecret: 'string',
      authDingdingEnable: 'boolean',
      authEndpointEnable: 'boolean',
      authRamAppId: 'string',
      authRamAppSecret: 'string',
      authRamEnable: 'boolean',
      dataHashName: 'string',
      description: 'string',
      domainName: 'string',
      eventFilenameMatches: 'string',
      eventMnsEndpoint: 'string',
      eventMnsTopic: 'string',
      eventNames: { 'type': 'array', 'itemType': 'string' },
      eventRoleArn: 'string',
      initDriveEnable: 'boolean',
      initDriveSize: 'number',
      mode: 'string',
      pathType: 'string',
      publishedAppAccessStrategy: AppAccessStrategy,
      sharable: 'boolean',
      storeLevel: 'string',
      storeRegionList: { 'type': 'array', 'itemType': 'string' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Create drive response
 */
export class CreateDriveResponse extends $tea.Model {
  domainId?: string;
  driveId?: string;
  static names(): { [key: string]: string } {
    return {
      domainId: 'domain_id',
      driveId: 'drive_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      domainId: 'string',
      driveId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Create file response
 */
export class CreateFileResponse extends $tea.Model {
  domainId?: string;
  driveId?: string;
  encryptMode?: string;
  exist?: boolean;
  fileId?: string;
  fileName?: string;
  location?: string;
  parentFileId?: string;
  partInfoList?: UploadPartInfo[];
  rapidUpload?: boolean;
  status?: string;
  streamsUploadInfo?: {[key: string]: any};
  type?: string;
  uploadId?: string;
  static names(): { [key: string]: string } {
    return {
      domainId: 'domain_id',
      driveId: 'drive_id',
      encryptMode: 'encrypt_mode',
      exist: 'exist',
      fileId: 'file_id',
      fileName: 'file_name',
      location: 'location',
      parentFileId: 'parent_file_id',
      partInfoList: 'part_info_list',
      rapidUpload: 'rapid_upload',
      status: 'status',
      streamsUploadInfo: 'streams_upload_info',
      type: 'type',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      domainId: 'string',
      driveId: 'string',
      encryptMode: 'string',
      exist: 'boolean',
      fileId: 'string',
      fileName: 'string',
      location: 'string',
      parentFileId: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      rapidUpload: 'boolean',
      status: 'string',
      streamsUploadInfo: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      type: 'string',
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * create_share_link response
 */
export class CreateShareLinkResponse extends $tea.Model {
  description?: string;
  shareId?: string;
  shareMsg?: string;
  shareName?: string;
  sharePolicy?: string;
  sharePwd?: string;
  shareUrl?: string;
  static names(): { [key: string]: string } {
    return {
      description: 'description',
      shareId: 'share_id',
      shareMsg: 'share_msg',
      shareName: 'share_name',
      sharePolicy: 'share_policy',
      sharePwd: 'share_pwd',
      shareUrl: 'share_url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      description: 'string',
      shareId: 'string',
      shareMsg: 'string',
      shareName: 'string',
      sharePolicy: 'string',
      sharePwd: 'string',
      shareUrl: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Create share response
 */
export class CreateShareResponse extends $tea.Model {
  domainId?: string;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      domainId: 'domain_id',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      domainId: 'string',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class CroppingBoundary extends $tea.Model {
  height?: number;
  left?: number;
  top?: number;
  width?: number;
  static names(): { [key: string]: string } {
    return {
      height: 'height',
      left: 'left',
      top: 'top',
      width: 'width',
    };
  }

  static types(): { [key: string]: any } {
    return {
      height: 'number',
      left: 'number',
      top: 'number',
      width: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class CroppingSuggestionItem extends $tea.Model {
  aspectRatio?: string;
  croppingBoundary?: CroppingBoundary;
  score?: number;
  static names(): { [key: string]: string } {
    return {
      aspectRatio: 'aspect_ratio',
      croppingBoundary: 'cropping_boundary',
      score: 'score',
    };
  }

  static types(): { [key: string]: any } {
    return {
      aspectRatio: 'string',
      croppingBoundary: CroppingBoundary,
      score: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class DefaultChangePasswordRequest extends $tea.Model {
  headers?: { [key: string]: string };
  appId: string;
  encryptedKey: string;
  newPassword: string;
  phoneNumber: string;
  phoneRegion?: string;
  state: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      appId: 'app_id',
      encryptedKey: 'encrypted_key',
      newPassword: 'new_password',
      phoneNumber: 'phone_number',
      phoneRegion: 'phone_region',
      state: 'state',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      appId: 'string',
      encryptedKey: 'string',
      newPassword: 'string',
      phoneNumber: 'string',
      phoneRegion: 'string',
      state: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class DefaultSetPasswordRequest extends $tea.Model {
  headers?: { [key: string]: string };
  appId: string;
  encryptedKey: string;
  newPassword: string;
  state: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      appId: 'app_id',
      encryptedKey: 'encrypted_key',
      newPassword: 'new_password',
      state: 'state',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      appId: 'string',
      encryptedKey: 'string',
      newPassword: 'string',
      state: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class DeleteAppRequest extends $tea.Model {
  appId: string;
  static names(): { [key: string]: string } {
    return {
      appId: 'app_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      appId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class DeleteBizCNameAndCertRequest extends $tea.Model {
  bizCname?: string;
  cnameType: string;
  domainId: string;
  isVpc?: boolean;
  static names(): { [key: string]: string } {
    return {
      bizCname: 'biz_cname',
      cnameType: 'cname_type',
      domainId: 'domain_id',
      isVpc: 'is_vpc',
    };
  }

  static types(): { [key: string]: any } {
    return {
      bizCname: 'string',
      cnameType: 'string',
      domainId: 'string',
      isVpc: 'boolean',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class DeleteBizCNameCertRequest extends $tea.Model {
  bizCname?: string;
  certId?: string;
  cnameType: string;
  domainId: string;
  isVpc?: boolean;
  static names(): { [key: string]: string } {
    return {
      bizCname: 'biz_cname',
      certId: 'cert_id',
      cnameType: 'cname_type',
      domainId: 'domain_id',
      isVpc: 'is_vpc',
    };
  }

  static types(): { [key: string]: any } {
    return {
      bizCname: 'string',
      certId: 'string',
      cnameType: 'string',
      domainId: 'string',
      isVpc: 'boolean',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class DeleteDataCNameAndCertRequest extends $tea.Model {
  dataCname: string;
  domainId: string;
  location: string;
  static names(): { [key: string]: string } {
    return {
      dataCname: 'data_cname',
      domainId: 'domain_id',
      location: 'location',
    };
  }

  static types(): { [key: string]: any } {
    return {
      dataCname: 'string',
      domainId: 'string',
      location: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * delete domain request
 */
export class DeleteDomainRequest extends $tea.Model {
  domainId: string;
  static names(): { [key: string]: string } {
    return {
      domainId: 'domain_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      domainId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * delete drive response
 */
export class DeleteDriveResponse extends $tea.Model {
  static names(): { [key: string]: string } {
    return {
    };
  }

  static types(): { [key: string]: any } {
    return {
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 删除文件 response
 */
export class DeleteFileResponse extends $tea.Model {
  asyncTaskId?: string;
  domainId?: string;
  driveId?: string;
  fileId?: string;
  static names(): { [key: string]: string } {
    return {
      asyncTaskId: 'async_task_id',
      domainId: 'domain_id',
      driveId: 'drive_id',
      fileId: 'file_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      asyncTaskId: 'string',
      domainId: 'string',
      driveId: 'string',
      fileId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 批量删除文件 response
 */
export class DeleteFilesResponse extends $tea.Model {
  deletedFileIdList?: string[];
  domainId?: string;
  driveId?: string;
  static names(): { [key: string]: string } {
    return {
      deletedFileIdList: 'deleted_file_id_list',
      domainId: 'domain_id',
      driveId: 'drive_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      deletedFileIdList: { 'type': 'array', 'itemType': 'string' },
      domainId: 'string',
      driveId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class DeviceAuthorizeRequest extends $tea.Model {
  ClientID: string;
  DeviceInfo?: string;
  DeviceName: string;
  LoginType?: string;
  Scope?: string[];
  static names(): { [key: string]: string } {
    return {
      ClientID: 'ClientID',
      DeviceInfo: 'DeviceInfo',
      DeviceName: 'DeviceName',
      LoginType: 'LoginType',
      Scope: 'Scope',
    };
  }

  static types(): { [key: string]: any } {
    return {
      ClientID: 'string',
      DeviceInfo: 'string',
      DeviceName: 'string',
      LoginType: 'string',
      Scope: { 'type': 'array', 'itemType': 'string' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * the file op info
 */
export class FileDeltaResponse extends $tea.Model {
  currentCategory?: string;
  file?: BaseCCPFileResponse;
  fileId?: string;
  op?: string;
  static names(): { [key: string]: string } {
    return {
      currentCategory: 'current_category',
      file: 'file',
      fileId: 'file_id',
      op: 'op',
    };
  }

  static types(): { [key: string]: any } {
    return {
      currentCategory: 'string',
      file: BaseCCPFileResponse,
      fileId: 'string',
      op: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetAccessTokenByLinkInfoRequest extends $tea.Model {
  headers?: { [key: string]: string };
  extra?: string;
  identity: string;
  type: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      extra: 'extra',
      identity: 'identity',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      extra: 'string',
      identity: 'string',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetAppPublicKeyRequest extends $tea.Model {
  appId: string;
  static names(): { [key: string]: string } {
    return {
      appId: 'app_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      appId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetAppRequest extends $tea.Model {
  appId: string;
  static names(): { [key: string]: string } {
    return {
      appId: 'app_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      appId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Get AsyncTask Response
 */
export class GetAsyncTaskResponse extends $tea.Model {
  asyncTaskId?: string;
  consumedProcess?: number;
  errCode?: number;
  message?: string;
  state?: string;
  totalProcess?: number;
  url?: string;
  static names(): { [key: string]: string } {
    return {
      asyncTaskId: 'async_task_id',
      consumedProcess: 'consumed_process',
      errCode: 'err_code',
      message: 'message',
      state: 'state',
      totalProcess: 'total_process',
      url: 'url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      asyncTaskId: 'string',
      consumedProcess: 'number',
      errCode: 'number',
      message: 'string',
      state: 'string',
      totalProcess: 'number',
      url: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetBizCNameInfoRequest extends $tea.Model {
  cnameType: string;
  domainId: string;
  isVpc?: boolean;
  static names(): { [key: string]: string } {
    return {
      cnameType: 'cname_type',
      domainId: 'domain_id',
      isVpc: 'is_vpc',
    };
  }

  static types(): { [key: string]: any } {
    return {
      cnameType: 'string',
      domainId: 'string',
      isVpc: 'boolean',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetByLinkInfoRequest extends $tea.Model {
  headers?: { [key: string]: string };
  extra?: string;
  identity: string;
  type: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      extra: 'extra',
      identity: 'identity',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      extra: 'string',
      identity: 'string',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetCaptchaRequest extends $tea.Model {
  headers?: { [key: string]: string };
  appId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      appId: 'app_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      appId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetCorsRuleListRequest extends $tea.Model {
  domainId: string;
  static names(): { [key: string]: string } {
    return {
      domainId: 'domain_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      domainId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetDataCNameInfoRequest extends $tea.Model {
  domainId: string;
  static names(): { [key: string]: string } {
    return {
      domainId: 'domain_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      domainId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文件夹size信息
 */
export class GetDirSizeInfoResponse extends $tea.Model {
  dirCount?: number;
  fileCount?: number;
  size?: number;
  static names(): { [key: string]: string } {
    return {
      dirCount: 'dir_count',
      fileCount: 'file_count',
      size: 'size',
    };
  }

  static types(): { [key: string]: any } {
    return {
      dirCount: 'number',
      fileCount: 'number',
      size: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * get domain request
 */
export class GetDomainRequest extends $tea.Model {
  domainId: string;
  static names(): { [key: string]: string } {
    return {
      domainId: 'domain_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      domainId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取download url response
 */
export class GetDownloadUrlResponse extends $tea.Model {
  expiration?: string;
  method?: string;
  ratelimit?: RateLimit;
  size?: number;
  streamsUrl?: {[key: string]: any};
  url?: string;
  static names(): { [key: string]: string } {
    return {
      expiration: 'expiration',
      method: 'method',
      ratelimit: 'ratelimit',
      size: 'size',
      streamsUrl: 'streams_url',
      url: 'url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      expiration: 'string',
      method: 'string',
      ratelimit: RateLimit,
      size: 'number',
      streamsUrl: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      url: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Get drive response
 */
export class GetDriveResponse extends $tea.Model {
  creator?: string;
  description?: string;
  domainId?: string;
  driveId?: string;
  driveName?: string;
  driveType?: string;
  encryptDataAccess?: boolean;
  encryptMode?: string;
  owner?: string;
  relativePath?: string;
  status?: string;
  storeId?: string;
  totalSize?: number;
  usedSize?: number;
  static names(): { [key: string]: string } {
    return {
      creator: 'creator',
      description: 'description',
      domainId: 'domain_id',
      driveId: 'drive_id',
      driveName: 'drive_name',
      driveType: 'drive_type',
      encryptDataAccess: 'encrypt_data_access',
      encryptMode: 'encrypt_mode',
      owner: 'owner',
      relativePath: 'relative_path',
      status: 'status',
      storeId: 'store_id',
      totalSize: 'total_size',
      usedSize: 'used_size',
    };
  }

  static types(): { [key: string]: any } {
    return {
      creator: 'string',
      description: 'string',
      domainId: 'string',
      driveId: 'string',
      driveName: 'string',
      driveType: 'string',
      encryptDataAccess: 'boolean',
      encryptMode: 'string',
      owner: 'string',
      relativePath: 'string',
      status: 'string',
      storeId: 'string',
      totalSize: 'number',
      usedSize: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 根据路径获取文件元数据response
 */
export class GetFileByPathResponse extends $tea.Model {
  category?: string;
  characteristicHash?: string;
  contentHash?: string;
  contentHashName?: string;
  contentType?: string;
  crc64Hash?: string;
  createdAt?: string;
  description?: string;
  domainId?: string;
  downloadUrl?: string;
  driveId?: string;
  encryptMode?: string;
  fileExtension?: string;
  fileId?: string;
  hidden?: boolean;
  imageMediaMetadata?: ImageMediaResponse;
  labels?: string[];
  meta?: string;
  name: string;
  parentFileId?: string;
  punishFlag?: number;
  shareId?: string;
  size?: number;
  starred?: boolean;
  status?: string;
  streamsInfo?: {[key: string]: any};
  thumbnail?: string;
  trashedAt?: string;
  type?: string;
  updatedAt?: string;
  uploadId?: string;
  url?: string;
  userMeta?: string;
  videoMediaMetadata?: VideoMediaResponse;
  videoPreviewMetadata?: VideoPreviewResponse;
  static names(): { [key: string]: string } {
    return {
      category: 'category',
      characteristicHash: 'characteristic_hash',
      contentHash: 'content_hash',
      contentHashName: 'content_hash_name',
      contentType: 'content_type',
      crc64Hash: 'crc64_hash',
      createdAt: 'created_at',
      description: 'description',
      domainId: 'domain_id',
      downloadUrl: 'download_url',
      driveId: 'drive_id',
      encryptMode: 'encrypt_mode',
      fileExtension: 'file_extension',
      fileId: 'file_id',
      hidden: 'hidden',
      imageMediaMetadata: 'image_media_metadata',
      labels: 'labels',
      meta: 'meta',
      name: 'name',
      parentFileId: 'parent_file_id',
      punishFlag: 'punish_flag',
      shareId: 'share_id',
      size: 'size',
      starred: 'starred',
      status: 'status',
      streamsInfo: 'streams_info',
      thumbnail: 'thumbnail',
      trashedAt: 'trashed_at',
      type: 'type',
      updatedAt: 'updated_at',
      uploadId: 'upload_id',
      url: 'url',
      userMeta: 'user_meta',
      videoMediaMetadata: 'video_media_metadata',
      videoPreviewMetadata: 'video_preview_metadata',
    };
  }

  static types(): { [key: string]: any } {
    return {
      category: 'string',
      characteristicHash: 'string',
      contentHash: 'string',
      contentHashName: 'string',
      contentType: 'string',
      crc64Hash: 'string',
      createdAt: 'string',
      description: 'string',
      domainId: 'string',
      downloadUrl: 'string',
      driveId: 'string',
      encryptMode: 'string',
      fileExtension: 'string',
      fileId: 'string',
      hidden: 'boolean',
      imageMediaMetadata: ImageMediaResponse,
      labels: { 'type': 'array', 'itemType': 'string' },
      meta: 'string',
      name: 'string',
      parentFileId: 'string',
      punishFlag: 'number',
      shareId: 'string',
      size: 'number',
      starred: 'boolean',
      status: 'string',
      streamsInfo: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      thumbnail: 'string',
      trashedAt: 'string',
      type: 'string',
      updatedAt: 'string',
      uploadId: 'string',
      url: 'string',
      userMeta: 'string',
      videoMediaMetadata: VideoMediaResponse,
      videoPreviewMetadata: VideoPreviewResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文件元数据response
 */
export class GetFileResponse extends $tea.Model {
  category?: string;
  characteristicHash?: string;
  contentHash?: string;
  contentHashName?: string;
  contentType?: string;
  crc64Hash?: string;
  createdAt?: string;
  description?: string;
  domainId?: string;
  downloadUrl?: string;
  driveId?: string;
  encryptMode?: string;
  fileExtension?: string;
  fileId?: string;
  hidden?: boolean;
  imageMediaMetadata?: ImageMediaResponse;
  labels?: string[];
  meta?: string;
  name: string;
  parentFileId?: string;
  punishFlag?: number;
  shareId?: string;
  size?: number;
  starred?: boolean;
  status?: string;
  streamsInfo?: {[key: string]: any};
  thumbnail?: string;
  trashedAt?: string;
  type?: string;
  updatedAt?: string;
  uploadId?: string;
  url?: string;
  userMeta?: string;
  videoMediaMetadata?: VideoMediaResponse;
  videoPreviewMetadata?: VideoPreviewResponse;
  static names(): { [key: string]: string } {
    return {
      category: 'category',
      characteristicHash: 'characteristic_hash',
      contentHash: 'content_hash',
      contentHashName: 'content_hash_name',
      contentType: 'content_type',
      crc64Hash: 'crc64_hash',
      createdAt: 'created_at',
      description: 'description',
      domainId: 'domain_id',
      downloadUrl: 'download_url',
      driveId: 'drive_id',
      encryptMode: 'encrypt_mode',
      fileExtension: 'file_extension',
      fileId: 'file_id',
      hidden: 'hidden',
      imageMediaMetadata: 'image_media_metadata',
      labels: 'labels',
      meta: 'meta',
      name: 'name',
      parentFileId: 'parent_file_id',
      punishFlag: 'punish_flag',
      shareId: 'share_id',
      size: 'size',
      starred: 'starred',
      status: 'status',
      streamsInfo: 'streams_info',
      thumbnail: 'thumbnail',
      trashedAt: 'trashed_at',
      type: 'type',
      updatedAt: 'updated_at',
      uploadId: 'upload_id',
      url: 'url',
      userMeta: 'user_meta',
      videoMediaMetadata: 'video_media_metadata',
      videoPreviewMetadata: 'video_preview_metadata',
    };
  }

  static types(): { [key: string]: any } {
    return {
      category: 'string',
      characteristicHash: 'string',
      contentHash: 'string',
      contentHashName: 'string',
      contentType: 'string',
      crc64Hash: 'string',
      createdAt: 'string',
      description: 'string',
      domainId: 'string',
      downloadUrl: 'string',
      driveId: 'string',
      encryptMode: 'string',
      fileExtension: 'string',
      fileId: 'string',
      hidden: 'boolean',
      imageMediaMetadata: ImageMediaResponse,
      labels: { 'type': 'array', 'itemType': 'string' },
      meta: 'string',
      name: 'string',
      parentFileId: 'string',
      punishFlag: 'number',
      shareId: 'string',
      size: 'number',
      starred: 'boolean',
      status: 'string',
      streamsInfo: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      thumbnail: 'string',
      trashedAt: 'string',
      type: 'string',
      updatedAt: 'string',
      uploadId: 'string',
      url: 'string',
      userMeta: 'string',
      videoMediaMetadata: VideoMediaResponse,
      videoPreviewMetadata: VideoPreviewResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * get last file op cursor response
 */
export class GetLastCursorResponse extends $tea.Model {
  cursor?: string;
  static names(): { [key: string]: string } {
    return {
      cursor: 'cursor',
    };
  }

  static types(): { [key: string]: any } {
    return {
      cursor: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetLinkInfoByUserIDRequest extends $tea.Model {
  headers?: { [key: string]: string };
  userId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      userId: 'user_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      userId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * get_media_play_url response
 */
export class GetMediaPlayURLResponse extends $tea.Model {
  url?: string;
  static names(): { [key: string]: string } {
    return {
      url: 'url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      url: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取office文档在线编辑地址 response
 */
export class GetOfficeEditUrlResponse extends $tea.Model {
  editUrl?: string;
  officeAccessToken?: string;
  officeRefreshToken?: string;
  static names(): { [key: string]: string } {
    return {
      editUrl: 'edit_url',
      officeAccessToken: 'office_access_token',
      officeRefreshToken: 'office_refresh_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      editUrl: 'string',
      officeAccessToken: 'string',
      officeRefreshToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文档预览地址 response
 */
export class GetOfficePreviewUrlResponse extends $tea.Model {
  accessToken?: string;
  previewUrl?: string;
  static names(): { [key: string]: string } {
    return {
      accessToken: 'access_token',
      previewUrl: 'preview_url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      accessToken: 'string',
      previewUrl: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetPublicKeyRequest extends $tea.Model {
  headers?: { [key: string]: string };
  appId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      appId: 'app_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      appId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetPublicKeyResponse extends $tea.Model {
  appId: string;
  keyPairId?: string;
  publicKey: string;
  static names(): { [key: string]: string } {
    return {
      appId: 'app_id',
      keyPairId: 'key_pair_id',
      publicKey: 'public_key',
    };
  }

  static types(): { [key: string]: any } {
    return {
      appId: 'string',
      keyPairId: 'string',
      publicKey: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetRPVerifyResultRequest extends $tea.Model {
  userId: string;
  static names(): { [key: string]: string } {
    return {
      userId: 'user_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      userId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetRPVerifyTokenRequest extends $tea.Model {
  userId: string;
  static names(): { [key: string]: string } {
    return {
      userId: 'user_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      userId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * get_share_link_by_anonymous response
 */
export class GetShareLinkByAnonymousResponse extends $tea.Model {
  avatar?: string;
  creatorId?: string;
  creatorName?: string;
  creatorPhone?: string;
  expiration?: string;
  shareName?: string;
  updatedAt?: string;
  static names(): { [key: string]: string } {
    return {
      avatar: 'avatar',
      creatorId: 'creator_id',
      creatorName: 'creator_name',
      creatorPhone: 'creator_phone',
      expiration: 'expiration',
      shareName: 'share_name',
      updatedAt: 'updated_at',
    };
  }

  static types(): { [key: string]: any } {
    return {
      avatar: 'string',
      creatorId: 'string',
      creatorName: 'string',
      creatorPhone: 'string',
      expiration: 'string',
      shareName: 'string',
      updatedAt: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * get_share_id response
 */
export class GetShareLinkIDResponse extends $tea.Model {
  shareId?: string;
  sharePwd?: string;
  static names(): { [key: string]: string } {
    return {
      shareId: 'share_id',
      sharePwd: 'share_pwd',
    };
  }

  static types(): { [key: string]: any } {
    return {
      shareId: 'string',
      sharePwd: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * get_share_token response
 */
export class GetShareLinkTokenResponse extends $tea.Model {
  expireTime: string;
  expiresIn: number;
  shareToken: string;
  static names(): { [key: string]: string } {
    return {
      expireTime: 'expire_time',
      expiresIn: 'expires_in',
      shareToken: 'share_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      expireTime: 'string',
      expiresIn: 'number',
      shareToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Get share response
 */
export class GetShareResponse extends $tea.Model {
  createdAt?: string;
  creator?: string;
  description?: string;
  domainId?: string;
  driveId?: string;
  expiration?: string;
  expired?: boolean;
  owner?: string;
  permissions?: string[];
  shareFileId?: string;
  shareFilePath?: string;
  shareId?: string;
  shareName?: string;
  sharePolicy?: SharePermissionPolicy[];
  status?: string;
  updatedAt?: string;
  static names(): { [key: string]: string } {
    return {
      createdAt: 'created_at',
      creator: 'creator',
      description: 'description',
      domainId: 'domain_id',
      driveId: 'drive_id',
      expiration: 'expiration',
      expired: 'expired',
      owner: 'owner',
      permissions: 'permissions',
      shareFileId: 'share_file_id',
      shareFilePath: 'share_file_path',
      shareId: 'share_id',
      shareName: 'share_name',
      sharePolicy: 'share_policy',
      status: 'status',
      updatedAt: 'updated_at',
    };
  }

  static types(): { [key: string]: any } {
    return {
      createdAt: 'string',
      creator: 'string',
      description: 'string',
      domainId: 'string',
      driveId: 'string',
      expiration: 'string',
      expired: 'boolean',
      owner: 'string',
      permissions: { 'type': 'array', 'itemType': 'string' },
      shareFileId: 'string',
      shareFilePath: 'string',
      shareId: 'string',
      shareName: 'string',
      sharePolicy: { 'type': 'array', 'itemType': SharePermissionPolicy },
      status: 'string',
      updatedAt: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Get UploadUrl Response
 */
export class GetUploadUrlResponse extends $tea.Model {
  createAt?: string;
  domainId?: string;
  driveId?: string;
  fileId?: string;
  partInfoList?: UploadPartInfo[];
  uploadId?: string;
  static names(): { [key: string]: string } {
    return {
      createAt: 'create_at',
      domainId: 'domain_id',
      driveId: 'drive_id',
      fileId: 'file_id',
      partInfoList: 'part_info_list',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      createAt: 'string',
      domainId: 'string',
      driveId: 'string',
      fileId: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取视频雪碧图地址 url response
 */
export class GetVideoPreviewSpriteURLResponse extends $tea.Model {
  col?: number;
  count?: number;
  frameCount?: number;
  frameHeight?: number;
  frameWidth?: number;
  row?: number;
  spriteUrlList?: string[];
  static names(): { [key: string]: string } {
    return {
      col: 'col',
      count: 'count',
      frameCount: 'frame_count',
      frameHeight: 'frame_height',
      frameWidth: 'frame_width',
      row: 'row',
      spriteUrlList: 'sprite_url_list',
    };
  }

  static types(): { [key: string]: any } {
    return {
      col: 'number',
      count: 'number',
      frameCount: 'number',
      frameHeight: 'number',
      frameWidth: 'number',
      row: 'number',
      spriteUrlList: { 'type': 'array', 'itemType': 'string' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取视频文件播放 url response
 */
export class GetVideoPreviewURLResponse extends $tea.Model {
  previewUrl?: string;
  static names(): { [key: string]: string } {
    return {
      previewUrl: 'preview_url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      previewUrl: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * complete file response
 */
export class HostingCompleteFileResponse extends $tea.Model {
  contentHash?: string;
  contentHashName?: string;
  contentType?: string;
  crc?: string;
  crc64Hash?: string;
  createdAt?: string;
  description?: string;
  domainId?: string;
  downloadUrl?: string;
  driveId?: string;
  fileExtension?: string;
  filePath?: string;
  name: string;
  parentFilePath?: string;
  shareId?: string;
  size?: number;
  status?: string;
  thumbnail?: string;
  trashedAt?: string;
  type?: string;
  updatedAt?: string;
  uploadId?: string;
  url?: string;
  static names(): { [key: string]: string } {
    return {
      contentHash: 'content_hash',
      contentHashName: 'content_hash_name',
      contentType: 'content_type',
      crc: 'crc',
      crc64Hash: 'crc64_hash',
      createdAt: 'created_at',
      description: 'description',
      domainId: 'domain_id',
      downloadUrl: 'download_url',
      driveId: 'drive_id',
      fileExtension: 'file_extension',
      filePath: 'file_path',
      name: 'name',
      parentFilePath: 'parent_file_path',
      shareId: 'share_id',
      size: 'size',
      status: 'status',
      thumbnail: 'thumbnail',
      trashedAt: 'trashed_at',
      type: 'type',
      updatedAt: 'updated_at',
      uploadId: 'upload_id',
      url: 'url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      contentHash: 'string',
      contentHashName: 'string',
      contentType: 'string',
      crc: 'string',
      crc64Hash: 'string',
      createdAt: 'string',
      description: 'string',
      domainId: 'string',
      downloadUrl: 'string',
      driveId: 'string',
      fileExtension: 'string',
      filePath: 'string',
      name: 'string',
      parentFilePath: 'string',
      shareId: 'string',
      size: 'number',
      status: 'string',
      thumbnail: 'string',
      trashedAt: 'string',
      type: 'string',
      updatedAt: 'string',
      uploadId: 'string',
      url: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 文件拷贝 response
 */
export class HostingCopyFileResponse extends $tea.Model {
  asyncTaskId?: string;
  domainId?: string;
  driveId?: string;
  filePath?: string;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      asyncTaskId: 'async_task_id',
      domainId: 'domain_id',
      driveId: 'drive_id',
      filePath: 'file_path',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      asyncTaskId: 'string',
      domainId: 'string',
      driveId: 'string',
      filePath: 'string',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Create file response
 */
export class HostingCreateFileResponse extends $tea.Model {
  domainId?: string;
  driveId?: string;
  filePath?: string;
  partInfoList?: UploadPartInfo[];
  shareId?: string;
  type?: string;
  uploadId?: string;
  static names(): { [key: string]: string } {
    return {
      domainId: 'domain_id',
      driveId: 'drive_id',
      filePath: 'file_path',
      partInfoList: 'part_info_list',
      shareId: 'share_id',
      type: 'type',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      domainId: 'string',
      driveId: 'string',
      filePath: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      shareId: 'string',
      type: 'string',
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 删除文件 response
 */
export class HostingDeleteFileResponse extends $tea.Model {
  asyncTaskId?: string;
  domainId?: string;
  driveId?: string;
  filePath?: string;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      asyncTaskId: 'async_task_id',
      domainId: 'domain_id',
      driveId: 'drive_id',
      filePath: 'file_path',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      asyncTaskId: 'string',
      domainId: 'string',
      driveId: 'string',
      filePath: 'string',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 批量删除文件 response
 */
export class HostingDeleteFilesResponse extends $tea.Model {
  deletedFileIdList?: string[];
  domainId?: string;
  driveId?: string;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      deletedFileIdList: 'deleted_file_id_list',
      domainId: 'domain_id',
      driveId: 'drive_id',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      deletedFileIdList: { 'type': 'array', 'itemType': 'string' },
      domainId: 'string',
      driveId: 'string',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取download url response
 */
export class HostingGetDownloadUrlResponse extends $tea.Model {
  expiration?: string;
  method?: string;
  url?: string;
  static names(): { [key: string]: string } {
    return {
      expiration: 'expiration',
      method: 'method',
      url: 'url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      expiration: 'string',
      method: 'string',
      url: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文件元数据response
 */
export class HostingGetFileResponse extends $tea.Model {
  contentHash?: string;
  contentHashName?: string;
  contentType?: string;
  crc64Hash?: string;
  createdAt?: string;
  description?: string;
  domainId?: string;
  downloadUrl?: string;
  driveId?: string;
  fileExtension?: string;
  filePath?: string;
  name: string;
  parentFilePath?: string;
  shareId?: string;
  size?: number;
  status?: string;
  thumbnail?: string;
  trashedAt?: string;
  type?: string;
  updatedAt?: string;
  uploadId?: string;
  url?: string;
  static names(): { [key: string]: string } {
    return {
      contentHash: 'content_hash',
      contentHashName: 'content_hash_name',
      contentType: 'content_type',
      crc64Hash: 'crc64_hash',
      createdAt: 'created_at',
      description: 'description',
      domainId: 'domain_id',
      downloadUrl: 'download_url',
      driveId: 'drive_id',
      fileExtension: 'file_extension',
      filePath: 'file_path',
      name: 'name',
      parentFilePath: 'parent_file_path',
      shareId: 'share_id',
      size: 'size',
      status: 'status',
      thumbnail: 'thumbnail',
      trashedAt: 'trashed_at',
      type: 'type',
      updatedAt: 'updated_at',
      uploadId: 'upload_id',
      url: 'url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      contentHash: 'string',
      contentHashName: 'string',
      contentType: 'string',
      crc64Hash: 'string',
      createdAt: 'string',
      description: 'string',
      domainId: 'string',
      downloadUrl: 'string',
      driveId: 'string',
      fileExtension: 'string',
      filePath: 'string',
      name: 'string',
      parentFilePath: 'string',
      shareId: 'string',
      size: 'number',
      status: 'string',
      thumbnail: 'string',
      trashedAt: 'string',
      type: 'string',
      updatedAt: 'string',
      uploadId: 'string',
      url: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取secure url response
 */
export class HostingGetSecureUrlResponse extends $tea.Model {
  expiration?: string;
  url?: string;
  static names(): { [key: string]: string } {
    return {
      expiration: 'expiration',
      url: 'url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      expiration: 'string',
      url: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Get UploadUrl Response
 */
export class HostingGetUploadUrlResponse extends $tea.Model {
  createAt?: string;
  domainId?: string;
  driveId?: string;
  filePath?: string;
  partInfoList?: UploadPartInfo[];
  uploadId?: string;
  static names(): { [key: string]: string } {
    return {
      createAt: 'create_at',
      domainId: 'domain_id',
      driveId: 'drive_id',
      filePath: 'file_path',
      partInfoList: 'part_info_list',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      createAt: 'string',
      domainId: 'string',
      driveId: 'string',
      filePath: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List file response
 */
export class HostingListFileResponse extends $tea.Model {
  items?: BaseHostingFileResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': BaseHostingFileResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取签名 response
 */
export class HostingListUploadedPartResponse extends $tea.Model {
  filePath?: string;
  nextPartNumberMarker?: string;
  uploadId?: string;
  uploadedParts?: UploadPartInfo[];
  static names(): { [key: string]: string } {
    return {
      filePath: 'file_path',
      nextPartNumberMarker: 'next_part_number_marker',
      uploadId: 'upload_id',
      uploadedParts: 'uploaded_parts',
    };
  }

  static types(): { [key: string]: any } {
    return {
      filePath: 'string',
      nextPartNumberMarker: 'string',
      uploadId: 'string',
      uploadedParts: { 'type': 'array', 'itemType': UploadPartInfo },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 文件移动 response
 */
export class HostingMoveFileResponse extends $tea.Model {
  asyncTaskId?: string;
  domainId?: string;
  driveId?: string;
  filePath?: string;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      asyncTaskId: 'async_task_id',
      domainId: 'domain_id',
      driveId: 'drive_id',
      filePath: 'file_path',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      asyncTaskId: 'string',
      domainId: 'string',
      driveId: 'string',
      filePath: 'string',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * search file response
 */
export class HostingSearchFileResponse extends $tea.Model {
  items?: BaseHostingFileResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': BaseHostingFileResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 更新文件元数据 response
 */
export class HostingUpdateFileMetaResponse extends $tea.Model {
  contentHash?: string;
  contentHashName?: string;
  contentType?: string;
  crc64Hash?: string;
  createdAt?: string;
  description?: string;
  domainId?: string;
  downloadUrl?: string;
  driveId?: string;
  fileExtension?: string;
  filePath?: string;
  name: string;
  parentFilePath?: string;
  shareId?: string;
  size?: number;
  status?: string;
  thumbnail?: string;
  trashedAt?: string;
  type?: string;
  updatedAt?: string;
  uploadId?: string;
  url?: string;
  static names(): { [key: string]: string } {
    return {
      contentHash: 'content_hash',
      contentHashName: 'content_hash_name',
      contentType: 'content_type',
      crc64Hash: 'crc64_hash',
      createdAt: 'created_at',
      description: 'description',
      domainId: 'domain_id',
      downloadUrl: 'download_url',
      driveId: 'drive_id',
      fileExtension: 'file_extension',
      filePath: 'file_path',
      name: 'name',
      parentFilePath: 'parent_file_path',
      shareId: 'share_id',
      size: 'size',
      status: 'status',
      thumbnail: 'thumbnail',
      trashedAt: 'trashed_at',
      type: 'type',
      updatedAt: 'updated_at',
      uploadId: 'upload_id',
      url: 'url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      contentHash: 'string',
      contentHashName: 'string',
      contentType: 'string',
      crc64Hash: 'string',
      createdAt: 'string',
      description: 'string',
      domainId: 'string',
      downloadUrl: 'string',
      driveId: 'string',
      fileExtension: 'string',
      filePath: 'string',
      name: 'string',
      parentFilePath: 'string',
      shareId: 'string',
      size: 'number',
      status: 'string',
      thumbnail: 'string',
      trashedAt: 'string',
      type: 'string',
      updatedAt: 'string',
      uploadId: 'string',
      url: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * DRM License response
 */
export class HostingVideoDRMLicenseResponse extends $tea.Model {
  data: string;
  deviceInfo: string;
  states: number;
  static names(): { [key: string]: string } {
    return {
      data: 'data',
      deviceInfo: 'device_info',
      states: 'states',
    };
  }

  static types(): { [key: string]: any } {
    return {
      data: 'string',
      deviceInfo: 'string',
      states: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 转码接口response
 */
export class HostingVideoDefinitionResponse extends $tea.Model {
  definitionList?: string[];
  frameRate?: string;
  static names(): { [key: string]: string } {
    return {
      definitionList: 'definition_list',
      frameRate: 'frame_rate',
    };
  }

  static types(): { [key: string]: any } {
    return {
      definitionList: { 'type': 'array', 'itemType': 'string' },
      frameRate: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 转码接口response
 */
export class HostingVideoTranscodeResponse extends $tea.Model {
  definitionList?: string[];
  duration?: number;
  hlsTime?: number;
  static names(): { [key: string]: string } {
    return {
      definitionList: 'definition_list',
      duration: 'duration',
      hlsTime: 'hls_time',
    };
  }

  static types(): { [key: string]: any } {
    return {
      definitionList: { 'type': 'array', 'itemType': 'string' },
      duration: 'number',
      hlsTime: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class ImageMediaResponse extends $tea.Model {
  addressLine?: string;
  city?: string;
  country?: string;
  croppingSuggestion?: CroppingSuggestionItem[];
  district?: string;
  exif?: string;
  faces?: string;
  height?: number;
  imageQuality?: ImageQuality;
  imageTags?: SystemTag[];
  location?: string;
  province?: string;
  storyImageScore?: number;
  time?: string;
  township?: string;
  width?: number;
  static names(): { [key: string]: string } {
    return {
      addressLine: 'address_line',
      city: 'city',
      country: 'country',
      croppingSuggestion: 'cropping_suggestion',
      district: 'district',
      exif: 'exif',
      faces: 'faces',
      height: 'height',
      imageQuality: 'image_quality',
      imageTags: 'image_tags',
      location: 'location',
      province: 'province',
      storyImageScore: 'story_image_score',
      time: 'time',
      township: 'township',
      width: 'width',
    };
  }

  static types(): { [key: string]: any } {
    return {
      addressLine: 'string',
      city: 'string',
      country: 'string',
      croppingSuggestion: { 'type': 'array', 'itemType': CroppingSuggestionItem },
      district: 'string',
      exif: 'string',
      faces: 'string',
      height: 'number',
      imageQuality: ImageQuality,
      imageTags: { 'type': 'array', 'itemType': SystemTag },
      location: 'string',
      province: 'string',
      storyImageScore: 'number',
      time: 'string',
      township: 'string',
      width: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class ImageQuality extends $tea.Model {
  clarity?: number;
  clarityScore?: number;
  color?: number;
  colorScore?: number;
  compositionScore?: number;
  contrast?: number;
  contrastScore?: number;
  exposure?: number;
  exposureScore?: number;
  overallScore?: number;
  static names(): { [key: string]: string } {
    return {
      clarity: 'clarity',
      clarityScore: 'clarity_score',
      color: 'color',
      colorScore: 'color_score',
      compositionScore: 'composition_score',
      contrast: 'contrast',
      contrastScore: 'contrast_score',
      exposure: 'exposure',
      exposureScore: 'exposure_score',
      overallScore: 'overall_score',
    };
  }

  static types(): { [key: string]: any } {
    return {
      clarity: 'number',
      clarityScore: 'number',
      color: 'number',
      colorScore: 'number',
      compositionScore: 'number',
      contrast: 'number',
      contrastScore: 'number',
      exposure: 'number',
      exposureScore: 'number',
      overallScore: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class LdapConfig extends $tea.Model {
  adminDn?: string;
  adminPassword?: string;
  baseDn?: string;
  host?: string;
  port?: number;
  uid?: string;
  static names(): { [key: string]: string } {
    return {
      adminDn: 'admin_dn',
      adminPassword: 'admin_password',
      baseDn: 'base_dn',
      host: 'host',
      port: 'port',
      uid: 'uid',
    };
  }

  static types(): { [key: string]: any } {
    return {
      adminDn: 'string',
      adminPassword: 'string',
      baseDn: 'string',
      host: 'string',
      port: 'number',
      uid: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class LinkInfo extends $tea.Model {
  extra?: string;
  identity?: string;
  type?: string;
  static names(): { [key: string]: string } {
    return {
      extra: 'extra',
      identity: 'identity',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      extra: 'string',
      identity: 'string',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class LinkInfoListResponse extends $tea.Model {
  items: LinkInfoResponse[];
  static names(): { [key: string]: string } {
    return {
      items: 'items',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': LinkInfoResponse },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class LinkInfoResponse extends $tea.Model {
  authenticationType: string;
  createdAt: number;
  domainId: string;
  extra?: string;
  identity: string;
  lastLoginTime: number;
  status: string;
  userId: string;
  static names(): { [key: string]: string } {
    return {
      authenticationType: 'authentication_type',
      createdAt: 'created_at',
      domainId: 'domain_id',
      extra: 'extra',
      identity: 'identity',
      lastLoginTime: 'last_login_time',
      status: 'status',
      userId: 'user_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      authenticationType: 'string',
      createdAt: 'number',
      domainId: 'string',
      extra: 'string',
      identity: 'string',
      lastLoginTime: 'number',
      status: 'string',
      userId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class ListAppsRequest extends $tea.Model {
  limit?: number;
  marker?: string;
  static names(): { [key: string]: string } {
    return {
      limit: 'limit',
      marker: 'marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      limit: 'number',
      marker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list_file_by_anonymous response
 */
export class ListByAnonymousResponse extends $tea.Model {
  items?: BaseFileAnonymousResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': BaseFileAnonymousResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list domain request
 */
export class ListDomainsRequest extends $tea.Model {
  limit?: number;
  marker?: string;
  static names(): { [key: string]: string } {
    return {
      limit: 'limit',
      marker: 'marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      limit: 'number',
      marker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list drive response
 */
export class ListDriveResponse extends $tea.Model {
  items?: BaseDriveResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': BaseDriveResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list file op response
 */
export class ListFileDeltaResponse extends $tea.Model {
  cursor?: string;
  hasMore?: boolean;
  items?: FileDeltaResponse[];
  static names(): { [key: string]: string } {
    return {
      cursor: 'cursor',
      hasMore: 'has_more',
      items: 'items',
    };
  }

  static types(): { [key: string]: any } {
    return {
      cursor: 'string',
      hasMore: 'boolean',
      items: { 'type': 'array', 'itemType': FileDeltaResponse },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List file response
 */
export class ListFileResponse extends $tea.Model {
  items?: BaseCCPFileResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': BaseCCPFileResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list_share_link response
 */
export class ListShareLinkResponse extends $tea.Model {
  items?: BaseShareLinkResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': BaseShareLinkResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List share response
 */
export class ListShareResponse extends $tea.Model {
  items?: BaseShareResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': BaseShareResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List storage file
 */
export class ListStoreFileResponse extends $tea.Model {
  items?: StoreFile[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': StoreFile },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List storage
 */
export class ListStoreResponse extends $tea.Model {
  items?: StoreItemResponse[];
  static names(): { [key: string]: string } {
    return {
      items: 'items',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': StoreItemResponse },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class ListStoresRequest extends $tea.Model {
  domainId: string;
  static names(): { [key: string]: string } {
    return {
      domainId: 'domain_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      domainId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取签名 response
 */
export class ListUploadedPartResponse extends $tea.Model {
  fileId?: string;
  nextPartNumberMarker?: string;
  uploadId?: string;
  uploadedParts?: UploadPartInfo[];
  static names(): { [key: string]: string } {
    return {
      fileId: 'file_id',
      nextPartNumberMarker: 'next_part_number_marker',
      uploadId: 'upload_id',
      uploadedParts: 'uploaded_parts',
    };
  }

  static types(): { [key: string]: any } {
    return {
      fileId: 'string',
      nextPartNumberMarker: 'string',
      uploadId: 'string',
      uploadedParts: { 'type': 'array', 'itemType': UploadPartInfo },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class LoginByCodeRequest extends $tea.Model {
  accessToken?: string;
  appId: string;
  authCode?: string;
  type: string;
  static names(): { [key: string]: string } {
    return {
      accessToken: 'access_token',
      appId: 'app_id',
      authCode: 'auth_code',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      accessToken: 'string',
      appId: 'string',
      authCode: 'string',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class LogoutRequest extends $tea.Model {
  BackUrl?: string;
  ClientID: string;
  LoginType?: string;
  static names(): { [key: string]: string } {
    return {
      BackUrl: 'BackUrl',
      ClientID: 'ClientID',
      LoginType: 'LoginType',
    };
  }

  static types(): { [key: string]: any } {
    return {
      BackUrl: 'string',
      ClientID: 'string',
      LoginType: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class MobileCheckExistRequest extends $tea.Model {
  headers?: { [key: string]: string };
  appId: string;
  phoneNumber: string;
  phoneRegion?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      appId: 'app_id',
      phoneNumber: 'phone_number',
      phoneRegion: 'phone_region',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      appId: 'string',
      phoneNumber: 'string',
      phoneRegion: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class MobileCheckExistResponse extends $tea.Model {
  isExist: boolean;
  phoneNumber: string;
  phoneRegion?: string;
  static names(): { [key: string]: string } {
    return {
      isExist: 'is_exist',
      phoneNumber: 'phone_number',
      phoneRegion: 'phone_region',
    };
  }

  static types(): { [key: string]: any } {
    return {
      isExist: 'boolean',
      phoneNumber: 'string',
      phoneRegion: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class MobileLoginRequest extends $tea.Model {
  headers?: { [key: string]: string };
  appId: string;
  autoRegister?: boolean;
  captchaId?: string;
  captchaText?: string;
  encryptedKey?: string;
  nvcParam: string;
  password?: string;
  phoneNumber: string;
  phoneRegion?: string;
  smsCode?: string;
  smsCodeId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      appId: 'app_id',
      autoRegister: 'auto_register',
      captchaId: 'captcha_id',
      captchaText: 'captcha_text',
      encryptedKey: 'encrypted_key',
      nvcParam: 'nvc_param',
      password: 'password',
      phoneNumber: 'phone_number',
      phoneRegion: 'phone_region',
      smsCode: 'sms_code',
      smsCodeId: 'sms_code_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      appId: 'string',
      autoRegister: 'boolean',
      captchaId: 'string',
      captchaText: 'string',
      encryptedKey: 'string',
      nvcParam: 'string',
      password: 'string',
      phoneNumber: 'string',
      phoneRegion: 'string',
      smsCode: 'string',
      smsCodeId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class MobileRegisterRequest extends $tea.Model {
  headers?: { [key: string]: string };
  appId: string;
  nvcParam: string;
  phoneNumber: string;
  phoneRegion?: string;
  smsCode: string;
  smsCodeId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      appId: 'app_id',
      nvcParam: 'nvc_param',
      phoneNumber: 'phone_number',
      phoneRegion: 'phone_region',
      smsCode: 'sms_code',
      smsCodeId: 'sms_code_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      appId: 'string',
      nvcParam: 'string',
      phoneNumber: 'string',
      phoneRegion: 'string',
      smsCode: 'string',
      smsCodeId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class MobileSendSmsCodeRequest extends $tea.Model {
  headers?: { [key: string]: string };
  appId: string;
  captchaId?: string;
  captchaText?: string;
  nvcParam: string;
  phoneNumber: string;
  phoneRegion?: string;
  type: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      appId: 'app_id',
      captchaId: 'captcha_id',
      captchaText: 'captcha_text',
      nvcParam: 'nvc_param',
      phoneNumber: 'phone_number',
      phoneRegion: 'phone_region',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      appId: 'string',
      captchaId: 'string',
      captchaText: 'string',
      nvcParam: 'string',
      phoneNumber: 'string',
      phoneRegion: 'string',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class MobileSendSmsCodeResponse extends $tea.Model {
  smsCodeId: string;
  static names(): { [key: string]: string } {
    return {
      smsCodeId: 'sms_code_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      smsCodeId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 文件移动 response
 */
export class MoveFileResponse extends $tea.Model {
  asyncTaskId?: string;
  domainId?: string;
  driveId?: string;
  fileId?: string;
  static names(): { [key: string]: string } {
    return {
      asyncTaskId: 'async_task_id',
      domainId: 'domain_id',
      driveId: 'drive_id',
      fileId: 'file_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      asyncTaskId: 'string',
      domainId: 'string',
      driveId: 'string',
      fileId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Pre hash check Response
 */
export class PreHashCheckSuccessResponse extends $tea.Model {
  code?: string;
  fileName?: string;
  message?: string;
  parentFileId: string;
  preHash?: string;
  static names(): { [key: string]: string } {
    return {
      code: 'code',
      fileName: 'file_name',
      message: 'message',
      parentFileId: 'parent_file_id',
      preHash: 'pre_hash',
    };
  }

  static types(): { [key: string]: any } {
    return {
      code: 'string',
      fileName: 'string',
      message: 'string',
      parentFileId: 'string',
      preHash: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class RPVerifyTokenResponse extends $tea.Model {
  needRpVerify: boolean;
  verifyToken: VerifyTokenResponse;
  static names(): { [key: string]: string } {
    return {
      needRpVerify: 'need_rp_verify',
      verifyToken: 'verify_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      needRpVerify: 'boolean',
      verifyToken: VerifyTokenResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 下载限速配置
 */
export class RateLimit extends $tea.Model {
  partSize?: number;
  partSpeed?: number;
  static names(): { [key: string]: string } {
    return {
      partSize: 'part_size',
      partSpeed: 'part_speed',
    };
  }

  static types(): { [key: string]: any } {
    return {
      partSize: 'number',
      partSpeed: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 刷新office文档在线编辑凭证 response
 */
export class RefreshOfficeEditTokenResponse extends $tea.Model {
  officeAccessToken?: string;
  officeRefreshToken?: string;
  static names(): { [key: string]: string } {
    return {
      officeAccessToken: 'office_access_token',
      officeRefreshToken: 'office_refresh_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      officeAccessToken: 'string',
      officeRefreshToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class RemoveStoreRequest extends $tea.Model {
  domainId: string;
  storeId: string;
  static names(): { [key: string]: string } {
    return {
      domainId: 'domain_id',
      storeId: 'store_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      domainId: 'string',
      storeId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class RevokeRequest extends $tea.Model {
  headers?: { [key: string]: string };
  appId: string;
  refreshToken: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      appId: 'app_id',
      refreshToken: 'refresh_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      appId: 'string',
      refreshToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * scan file meta response
 */
export class ScanFileMetaResponse extends $tea.Model {
  items?: BaseCCPFileResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': BaseCCPFileResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * search file response
 */
export class SearchFileResponse extends $tea.Model {
  items?: BaseCCPFileResponse[];
  nextMarker?: string;
  totalCount?: number;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
      totalCount: 'total_count',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': BaseCCPFileResponse },
      nextMarker: 'string',
      totalCount: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class SetAppPublicKeyRequest extends $tea.Model {
  appId: string;
  publicKey: string;
  static names(): { [key: string]: string } {
    return {
      appId: 'app_id',
      publicKey: 'public_key',
    };
  }

  static types(): { [key: string]: any } {
    return {
      appId: 'string',
      publicKey: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class SetBizCNameCertRequest extends $tea.Model {
  CertID?: string;
  bizCname?: string;
  certBody: string;
  certName: string;
  certPrivatekey: string;
  cnameType: string;
  domainId: string;
  isVpc?: boolean;
  static names(): { [key: string]: string } {
    return {
      CertID: 'CertID',
      bizCname: 'biz_cname',
      certBody: 'cert_body',
      certName: 'cert_name',
      certPrivatekey: 'cert_privatekey',
      cnameType: 'cname_type',
      domainId: 'domain_id',
      isVpc: 'is_vpc',
    };
  }

  static types(): { [key: string]: any } {
    return {
      CertID: 'string',
      bizCname: 'string',
      certBody: 'string',
      certName: 'string',
      certPrivatekey: 'string',
      cnameType: 'string',
      domainId: 'string',
      isVpc: 'boolean',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class SetBizCNameRequest extends $tea.Model {
  bizCname: string;
  cnameType: string;
  domainId: string;
  isVpc?: boolean;
  static names(): { [key: string]: string } {
    return {
      bizCname: 'biz_cname',
      cnameType: 'cname_type',
      domainId: 'domain_id',
      isVpc: 'is_vpc',
    };
  }

  static types(): { [key: string]: any } {
    return {
      bizCname: 'string',
      cnameType: 'string',
      domainId: 'string',
      isVpc: 'boolean',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list cors rule request
 */
export class SetCorsRuleListRequest extends $tea.Model {
  corsRuleList: CorsRule[];
  domainId: string;
  static names(): { [key: string]: string } {
    return {
      corsRuleList: 'cors_rule_list',
      domainId: 'domain_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      corsRuleList: { 'type': 'array', 'itemType': CorsRule },
      domainId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class SetDataCNameRequest extends $tea.Model {
  dataCname: string;
  domainId: string;
  location: string;
  static names(): { [key: string]: string } {
    return {
      dataCname: 'data_cname',
      domainId: 'domain_id',
      location: 'location',
    };
  }

  static types(): { [key: string]: any } {
    return {
      dataCname: 'string',
      domainId: 'string',
      location: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class SharePermissionPolicy extends $tea.Model {
  fileId?: string;
  filePath?: string;
  permissionInheritable?: boolean;
  permissionList?: string[];
  permissionType?: string;
  static names(): { [key: string]: string } {
    return {
      fileId: 'file_id',
      filePath: 'file_path',
      permissionInheritable: 'permission_inheritable',
      permissionList: 'permission_list',
      permissionType: 'permission_type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      fileId: 'string',
      filePath: 'string',
      permissionInheritable: 'boolean',
      permissionList: { 'type': 'array', 'itemType': 'string' },
      permissionType: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class StoreFile extends $tea.Model {
  domainId?: string;
  name?: string;
  parentFilePath?: string;
  storeId?: string;
  type?: string;
  static names(): { [key: string]: string } {
    return {
      domainId: 'domain_id',
      name: 'name',
      parentFilePath: 'parent_file_path',
      storeId: 'store_id',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      domainId: 'string',
      name: 'string',
      parentFilePath: 'string',
      storeId: 'string',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class StoreItemResponse extends $tea.Model {
  accelerateEndpoint?: string;
  basePath?: string;
  bucket: string;
  cdnEndpoint?: string;
  customizedAccelerateEndpoint?: string;
  customizedCdnEndpoint?: string;
  customizedEndpoint?: string;
  customizedInternalEndpoint?: string;
  domainId?: string;
  endpoint: string;
  internalEndpoint?: string;
  location?: string;
  ownership: string;
  policy: string;
  roleArn?: string;
  storeId: string;
  type: string;
  static names(): { [key: string]: string } {
    return {
      accelerateEndpoint: 'accelerate_endpoint',
      basePath: 'base_path',
      bucket: 'bucket',
      cdnEndpoint: 'cdn_endpoint',
      customizedAccelerateEndpoint: 'customized_accelerate_endpoint',
      customizedCdnEndpoint: 'customized_cdn_endpoint',
      customizedEndpoint: 'customized_endpoint',
      customizedInternalEndpoint: 'customized_internal_endpoint',
      domainId: 'domain_id',
      endpoint: 'endpoint',
      internalEndpoint: 'internal_endpoint',
      location: 'location',
      ownership: 'ownership',
      policy: 'policy',
      roleArn: 'role_arn',
      storeId: 'store_id',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      accelerateEndpoint: 'string',
      basePath: 'string',
      bucket: 'string',
      cdnEndpoint: 'string',
      customizedAccelerateEndpoint: 'string',
      customizedCdnEndpoint: 'string',
      customizedEndpoint: 'string',
      customizedInternalEndpoint: 'string',
      domainId: 'string',
      endpoint: 'string',
      internalEndpoint: 'string',
      location: 'string',
      ownership: 'string',
      policy: 'string',
      roleArn: 'string',
      storeId: 'string',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class StreamInfo extends $tea.Model {
  crc64Hash?: string;
  downloadUrl?: string;
  size?: number;
  thumbnail?: string;
  url?: string;
  static names(): { [key: string]: string } {
    return {
      crc64Hash: 'crc64_hash',
      downloadUrl: 'download_url',
      size: 'size',
      thumbnail: 'thumbnail',
      url: 'url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      crc64Hash: 'string',
      downloadUrl: 'string',
      size: 'number',
      thumbnail: 'string',
      url: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class StreamUploadInfo extends $tea.Model {
  location?: string;
  partInfoList?: UploadPartInfo[];
  preRapidUpload?: boolean;
  rapidUpload?: boolean;
  uploadId?: string;
  static names(): { [key: string]: string } {
    return {
      location: 'location',
      partInfoList: 'part_info_list',
      preRapidUpload: 'pre_rapid_upload',
      rapidUpload: 'rapid_upload',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      location: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      preRapidUpload: 'boolean',
      rapidUpload: 'boolean',
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class SystemTag extends $tea.Model {
  confidence?: number;
  enName?: string;
  name?: string;
  parentEnName?: string;
  parentName?: string;
  selected?: boolean;
  source?: string;
  tagLevel?: number;
  static names(): { [key: string]: string } {
    return {
      confidence: 'confidence',
      enName: 'en_name',
      name: 'name',
      parentEnName: 'parent_en_name',
      parentName: 'parent_name',
      selected: 'selected',
      source: 'source',
      tagLevel: 'tag_level',
    };
  }

  static types(): { [key: string]: any } {
    return {
      confidence: 'number',
      enName: 'string',
      name: 'string',
      parentEnName: 'string',
      parentName: 'string',
      selected: 'boolean',
      source: 'string',
      tagLevel: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class TokenRequest extends $tea.Model {
  Assertion?: string;
  ClientID: string;
  ClientSecret: string;
  Code?: string;
  DeviceCode?: string;
  GrantType: string;
  RedirectUri?: string;
  RefreshToken?: string;
  static names(): { [key: string]: string } {
    return {
      Assertion: 'Assertion',
      ClientID: 'ClientID',
      ClientSecret: 'ClientSecret',
      Code: 'Code',
      DeviceCode: 'DeviceCode',
      GrantType: 'GrantType',
      RedirectUri: 'RedirectUri',
      RefreshToken: 'RefreshToken',
    };
  }

  static types(): { [key: string]: any } {
    return {
      Assertion: 'string',
      ClientID: 'string',
      ClientSecret: 'string',
      Code: 'string',
      DeviceCode: 'string',
      GrantType: 'string',
      RedirectUri: 'string',
      RefreshToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class UpdateAppRequest extends $tea.Model {
  appId: string;
  appName?: string;
  description?: string;
  logo?: string;
  redirectUri?: string;
  scope?: string[];
  type?: string;
  static names(): { [key: string]: string } {
    return {
      appId: 'app_id',
      appName: 'app_name',
      description: 'description',
      logo: 'logo',
      redirectUri: 'redirect_uri',
      scope: 'scope',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      appId: 'string',
      appName: 'string',
      description: 'string',
      logo: 'string',
      redirectUri: 'string',
      scope: { 'type': 'array', 'itemType': 'string' },
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * update domain request
 */
export class UpdateDomainRequest extends $tea.Model {
  authConfig?: {[key: string]: any};
  authDingdingAppId?: string;
  authDingdingAppSecret?: string;
  authDingdingEnable?: boolean;
  authEndpointEnable?: boolean;
  authRamAppId?: string;
  authRamAppSecret?: string;
  authRamEnable?: boolean;
  dataHashName?: string;
  description?: string;
  domainId: string;
  domainName?: string;
  eventFilenameMatches?: string;
  eventMnsEndpoint?: string;
  eventMnsTopic?: string;
  eventNames?: string[];
  eventRoleArn?: string;
  initDriveEnable?: boolean;
  initDriveSize?: number;
  initDriveStoreId?: string;
  publishedAppAccessStrategy?: AppAccessStrategy;
  sharable?: boolean;
  static names(): { [key: string]: string } {
    return {
      authConfig: 'auth_config',
      authDingdingAppId: 'auth_dingding_app_id',
      authDingdingAppSecret: 'auth_dingding_app_secret',
      authDingdingEnable: 'auth_dingding_enable',
      authEndpointEnable: 'auth_endpoint_enable',
      authRamAppId: 'auth_ram_app_id',
      authRamAppSecret: 'auth_ram_app_secret',
      authRamEnable: 'auth_ram_enable',
      dataHashName: 'data_hash_name',
      description: 'description',
      domainId: 'domain_id',
      domainName: 'domain_name',
      eventFilenameMatches: 'event_filename_matches',
      eventMnsEndpoint: 'event_mns_endpoint',
      eventMnsTopic: 'event_mns_topic',
      eventNames: 'event_names',
      eventRoleArn: 'event_role_arn',
      initDriveEnable: 'init_drive_enable',
      initDriveSize: 'init_drive_size',
      initDriveStoreId: 'init_drive_store_id',
      publishedAppAccessStrategy: 'published_app_access_strategy',
      sharable: 'sharable',
    };
  }

  static types(): { [key: string]: any } {
    return {
      authConfig: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      authDingdingAppId: 'string',
      authDingdingAppSecret: 'string',
      authDingdingEnable: 'boolean',
      authEndpointEnable: 'boolean',
      authRamAppId: 'string',
      authRamAppSecret: 'string',
      authRamEnable: 'boolean',
      dataHashName: 'string',
      description: 'string',
      domainId: 'string',
      domainName: 'string',
      eventFilenameMatches: 'string',
      eventMnsEndpoint: 'string',
      eventMnsTopic: 'string',
      eventNames: { 'type': 'array', 'itemType': 'string' },
      eventRoleArn: 'string',
      initDriveEnable: 'boolean',
      initDriveSize: 'number',
      initDriveStoreId: 'string',
      publishedAppAccessStrategy: AppAccessStrategy,
      sharable: 'boolean',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Update drive response
 */
export class UpdateDriveResponse extends $tea.Model {
  creator?: string;
  description?: string;
  domainId?: string;
  driveId?: string;
  driveName?: string;
  driveType?: string;
  encryptDataAccess?: boolean;
  encryptMode?: string;
  owner?: string;
  relativePath?: string;
  status?: string;
  storeId?: string;
  totalSize?: number;
  usedSize?: number;
  static names(): { [key: string]: string } {
    return {
      creator: 'creator',
      description: 'description',
      domainId: 'domain_id',
      driveId: 'drive_id',
      driveName: 'drive_name',
      driveType: 'drive_type',
      encryptDataAccess: 'encrypt_data_access',
      encryptMode: 'encrypt_mode',
      owner: 'owner',
      relativePath: 'relative_path',
      status: 'status',
      storeId: 'store_id',
      totalSize: 'total_size',
      usedSize: 'used_size',
    };
  }

  static types(): { [key: string]: any } {
    return {
      creator: 'string',
      description: 'string',
      domainId: 'string',
      driveId: 'string',
      driveName: 'string',
      driveType: 'string',
      encryptDataAccess: 'boolean',
      encryptMode: 'string',
      owner: 'string',
      relativePath: 'string',
      status: 'string',
      storeId: 'string',
      totalSize: 'number',
      usedSize: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 更新文件元数据 response
 */
export class UpdateFileMetaResponse extends $tea.Model {
  category?: string;
  characteristicHash?: string;
  contentHash?: string;
  contentHashName?: string;
  contentType?: string;
  crc64Hash?: string;
  createdAt?: string;
  description?: string;
  domainId?: string;
  downloadUrl?: string;
  driveId?: string;
  encryptMode?: string;
  fileExtension?: string;
  fileId?: string;
  hidden?: boolean;
  imageMediaMetadata?: ImageMediaResponse;
  labels?: string[];
  meta?: string;
  name: string;
  parentFileId?: string;
  punishFlag?: number;
  shareId?: string;
  size?: number;
  starred?: boolean;
  status?: string;
  streamsInfo?: {[key: string]: any};
  thumbnail?: string;
  trashedAt?: string;
  type?: string;
  updatedAt?: string;
  uploadId?: string;
  url?: string;
  userMeta?: string;
  videoMediaMetadata?: VideoMediaResponse;
  videoPreviewMetadata?: VideoPreviewResponse;
  static names(): { [key: string]: string } {
    return {
      category: 'category',
      characteristicHash: 'characteristic_hash',
      contentHash: 'content_hash',
      contentHashName: 'content_hash_name',
      contentType: 'content_type',
      crc64Hash: 'crc64_hash',
      createdAt: 'created_at',
      description: 'description',
      domainId: 'domain_id',
      downloadUrl: 'download_url',
      driveId: 'drive_id',
      encryptMode: 'encrypt_mode',
      fileExtension: 'file_extension',
      fileId: 'file_id',
      hidden: 'hidden',
      imageMediaMetadata: 'image_media_metadata',
      labels: 'labels',
      meta: 'meta',
      name: 'name',
      parentFileId: 'parent_file_id',
      punishFlag: 'punish_flag',
      shareId: 'share_id',
      size: 'size',
      starred: 'starred',
      status: 'status',
      streamsInfo: 'streams_info',
      thumbnail: 'thumbnail',
      trashedAt: 'trashed_at',
      type: 'type',
      updatedAt: 'updated_at',
      uploadId: 'upload_id',
      url: 'url',
      userMeta: 'user_meta',
      videoMediaMetadata: 'video_media_metadata',
      videoPreviewMetadata: 'video_preview_metadata',
    };
  }

  static types(): { [key: string]: any } {
    return {
      category: 'string',
      characteristicHash: 'string',
      contentHash: 'string',
      contentHashName: 'string',
      contentType: 'string',
      crc64Hash: 'string',
      createdAt: 'string',
      description: 'string',
      domainId: 'string',
      downloadUrl: 'string',
      driveId: 'string',
      encryptMode: 'string',
      fileExtension: 'string',
      fileId: 'string',
      hidden: 'boolean',
      imageMediaMetadata: ImageMediaResponse,
      labels: { 'type': 'array', 'itemType': 'string' },
      meta: 'string',
      name: 'string',
      parentFileId: 'string',
      punishFlag: 'number',
      shareId: 'string',
      size: 'number',
      starred: 'boolean',
      status: 'string',
      streamsInfo: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      thumbnail: 'string',
      trashedAt: 'string',
      type: 'string',
      updatedAt: 'string',
      uploadId: 'string',
      url: 'string',
      userMeta: 'string',
      videoMediaMetadata: VideoMediaResponse,
      videoPreviewMetadata: VideoPreviewResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Update share response
 */
export class UpdateShareResponse extends $tea.Model {
  createdAt?: string;
  creator?: string;
  description?: string;
  domainId?: string;
  driveId?: string;
  expiration?: string;
  expired?: boolean;
  owner?: string;
  permissions?: string[];
  shareFileId?: string;
  shareFilePath?: string;
  shareId?: string;
  shareName?: string;
  sharePolicy?: SharePermissionPolicy[];
  status?: string;
  updatedAt?: string;
  static names(): { [key: string]: string } {
    return {
      createdAt: 'created_at',
      creator: 'creator',
      description: 'description',
      domainId: 'domain_id',
      driveId: 'drive_id',
      expiration: 'expiration',
      expired: 'expired',
      owner: 'owner',
      permissions: 'permissions',
      shareFileId: 'share_file_id',
      shareFilePath: 'share_file_path',
      shareId: 'share_id',
      shareName: 'share_name',
      sharePolicy: 'share_policy',
      status: 'status',
      updatedAt: 'updated_at',
    };
  }

  static types(): { [key: string]: any } {
    return {
      createdAt: 'string',
      creator: 'string',
      description: 'string',
      domainId: 'string',
      driveId: 'string',
      expiration: 'string',
      expired: 'boolean',
      owner: 'string',
      permissions: { 'type': 'array', 'itemType': 'string' },
      shareFileId: 'string',
      shareFilePath: 'string',
      shareId: 'string',
      shareName: 'string',
      sharePolicy: { 'type': 'array', 'itemType': SharePermissionPolicy },
      status: 'string',
      updatedAt: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class UploadPartInfo extends $tea.Model {
  contentType?: string;
  etag?: string;
  partNumber?: number;
  partSize?: number;
  uploadUrl?: string;
  static names(): { [key: string]: string } {
    return {
      contentType: 'content_type',
      etag: 'etag',
      partNumber: 'part_number',
      partSize: 'part_size',
      uploadUrl: 'upload_url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      contentType: 'string',
      etag: 'string',
      partNumber: 'number',
      partSize: 'number',
      uploadUrl: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class UserAuthentication extends $tea.Model {
  AuthenticationType: string;
  CreatedAt: number;
  Detail: string;
  DomainID: string;
  Identity: string;
  LastLoginTime: number;
  Status: string;
  UserID: string;
  extra?: string;
  static names(): { [key: string]: string } {
    return {
      AuthenticationType: 'AuthenticationType',
      CreatedAt: 'CreatedAt',
      Detail: 'Detail',
      DomainID: 'DomainID',
      Identity: 'Identity',
      LastLoginTime: 'LastLoginTime',
      Status: 'Status',
      UserID: 'UserID',
      extra: 'extra',
    };
  }

  static types(): { [key: string]: any } {
    return {
      AuthenticationType: 'string',
      CreatedAt: 'number',
      Detail: 'string',
      DomainID: 'string',
      Identity: 'string',
      LastLoginTime: 'number',
      Status: 'string',
      UserID: 'string',
      extra: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class VerifyCodeRequest extends $tea.Model {
  headers?: { [key: string]: string };
  appId: string;
  phoneNumber: string;
  phoneRegion?: string;
  smsCode: string;
  smsCodeId: string;
  verifyType?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      appId: 'app_id',
      phoneNumber: 'phone_number',
      phoneRegion: 'phone_region',
      smsCode: 'sms_code',
      smsCodeId: 'sms_code_id',
      verifyType: 'verify_type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      appId: 'string',
      phoneNumber: 'string',
      phoneRegion: 'string',
      smsCode: 'string',
      smsCodeId: 'string',
      verifyType: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class VerifyCodeResponse extends $tea.Model {
  state: string;
  static names(): { [key: string]: string } {
    return {
      state: 'state',
    };
  }

  static types(): { [key: string]: any } {
    return {
      state: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class VerifyTokenResponse extends $tea.Model {
  token: string;
  ttl: number;
  url: string;
  static names(): { [key: string]: string } {
    return {
      token: 'token',
      ttl: 'ttl',
      url: 'url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      token: 'string',
      ttl: 'number',
      url: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class VideoMediaAudioStream extends $tea.Model {
  bitRate?: string;
  channelLayout?: string;
  channels?: number;
  codeName?: string;
  duration?: string;
  sampleRate?: string;
  static names(): { [key: string]: string } {
    return {
      bitRate: 'bit_rate',
      channelLayout: 'channel_layout',
      channels: 'channels',
      codeName: 'code_name',
      duration: 'duration',
      sampleRate: 'sample_rate',
    };
  }

  static types(): { [key: string]: any } {
    return {
      bitRate: 'string',
      channelLayout: 'string',
      channels: 'number',
      codeName: 'string',
      duration: 'string',
      sampleRate: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class VideoMediaResponse extends $tea.Model {
  addressLine?: string;
  city?: string;
  country?: string;
  district?: string;
  duration?: string;
  height?: number;
  imageTags?: SystemTag[];
  location?: string;
  province?: string;
  time?: string;
  township?: string;
  videoMediaAudioStream?: VideoMediaAudioStream[];
  videoMediaVideoStream?: VideoMediaVideoStream[];
  width?: number;
  static names(): { [key: string]: string } {
    return {
      addressLine: 'address_line',
      city: 'city',
      country: 'country',
      district: 'district',
      duration: 'duration',
      height: 'height',
      imageTags: 'image_tags',
      location: 'location',
      province: 'province',
      time: 'time',
      township: 'township',
      videoMediaAudioStream: 'video_media_audio_stream',
      videoMediaVideoStream: 'video_media_video_stream',
      width: 'width',
    };
  }

  static types(): { [key: string]: any } {
    return {
      addressLine: 'string',
      city: 'string',
      country: 'string',
      district: 'string',
      duration: 'string',
      height: 'number',
      imageTags: { 'type': 'array', 'itemType': SystemTag },
      location: 'string',
      province: 'string',
      time: 'string',
      township: 'string',
      videoMediaAudioStream: { 'type': 'array', 'itemType': VideoMediaAudioStream },
      videoMediaVideoStream: { 'type': 'array', 'itemType': VideoMediaVideoStream },
      width: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class VideoMediaVideoStream extends $tea.Model {
  bitrate?: string;
  clarity?: string;
  codeName?: string;
  duration?: string;
  fps?: string;
  rotate?: string;
  static names(): { [key: string]: string } {
    return {
      bitrate: 'bitrate',
      clarity: 'clarity',
      codeName: 'code_name',
      duration: 'duration',
      fps: 'fps',
      rotate: 'rotate',
    };
  }

  static types(): { [key: string]: any } {
    return {
      bitrate: 'string',
      clarity: 'string',
      codeName: 'string',
      duration: 'string',
      fps: 'string',
      rotate: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class VideoPreviewAudioMeta extends $tea.Model {
  bitrate?: number;
  channels?: number;
  duration?: number;
  sampleRate?: number;
  static names(): { [key: string]: string } {
    return {
      bitrate: 'bitrate',
      channels: 'channels',
      duration: 'duration',
      sampleRate: 'sample_rate',
    };
  }

  static types(): { [key: string]: any } {
    return {
      bitrate: 'number',
      channels: 'number',
      duration: 'number',
      sampleRate: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class VideoPreviewAudioMusicMeta extends $tea.Model {
  album?: string;
  artist?: string;
  coverUrl?: string;
  title?: string;
  static names(): { [key: string]: string } {
    return {
      album: 'album',
      artist: 'artist',
      coverUrl: 'cover_url',
      title: 'title',
    };
  }

  static types(): { [key: string]: any } {
    return {
      album: 'string',
      artist: 'string',
      coverUrl: 'string',
      title: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class VideoPreviewResponse extends $tea.Model {
  audioChannels?: number;
  audioFormat?: string;
  audioMeta?: VideoPreviewAudioMeta;
  audioMusicMeta?: VideoPreviewAudioMusicMeta;
  audioSampleRate?: string;
  audioTemplateList?: VideoPreviewTranscode[];
  bitrate?: string;
  duration?: string;
  frameRate?: string;
  height?: number;
  spriteInfo?: VideoPreviewSprite;
  templateList?: VideoPreviewTranscode[];
  thumbnail?: string;
  videoFormat?: string;
  width?: number;
  static names(): { [key: string]: string } {
    return {
      audioChannels: 'audio_channels',
      audioFormat: 'audio_format',
      audioMeta: 'audio_meta',
      audioMusicMeta: 'audio_music_meta',
      audioSampleRate: 'audio_sample_rate',
      audioTemplateList: 'audio_template_list',
      bitrate: 'bitrate',
      duration: 'duration',
      frameRate: 'frame_rate',
      height: 'height',
      spriteInfo: 'sprite_info',
      templateList: 'template_list',
      thumbnail: 'thumbnail',
      videoFormat: 'video_format',
      width: 'width',
    };
  }

  static types(): { [key: string]: any } {
    return {
      audioChannels: 'number',
      audioFormat: 'string',
      audioMeta: VideoPreviewAudioMeta,
      audioMusicMeta: VideoPreviewAudioMusicMeta,
      audioSampleRate: 'string',
      audioTemplateList: { 'type': 'array', 'itemType': VideoPreviewTranscode },
      bitrate: 'string',
      duration: 'string',
      frameRate: 'string',
      height: 'number',
      spriteInfo: VideoPreviewSprite,
      templateList: { 'type': 'array', 'itemType': VideoPreviewTranscode },
      thumbnail: 'string',
      videoFormat: 'string',
      width: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class VideoPreviewSprite extends $tea.Model {
  col?: number;
  count?: number;
  frameCount?: number;
  frameHeight?: number;
  frameWidth?: number;
  row?: number;
  status?: string;
  static names(): { [key: string]: string } {
    return {
      col: 'col',
      count: 'count',
      frameCount: 'frame_count',
      frameHeight: 'frame_height',
      frameWidth: 'frame_width',
      row: 'row',
      status: 'status',
    };
  }

  static types(): { [key: string]: any } {
    return {
      col: 'number',
      count: 'number',
      frameCount: 'number',
      frameHeight: 'number',
      frameWidth: 'number',
      row: 'number',
      status: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class VideoPreviewTranscode extends $tea.Model {
  status?: string;
  templateId?: string;
  static names(): { [key: string]: string } {
    return {
      status: 'status',
      templateId: 'template_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      status: 'string',
      templateId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class AdminListStoresModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListStoresResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListStoresResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetUserAccessTokenModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: AccessTokenResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: AccessTokenResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class AddStoreResponse extends $tea.Model {
  accelerateEndpoint?: string;
  basePath?: string;
  bucket: string;
  cdnEndpoint?: string;
  customizedAccelerateEndpoint?: string;
  customizedCdnEndpoint?: string;
  customizedEndpoint?: string;
  customizedInternalEndpoint?: string;
  domainId: string;
  endpoint: string;
  internalEndpoint?: string;
  location?: string;
  ownership: string;
  policy: string;
  roleArn?: string;
  storeId: string;
  type: string;
  static names(): { [key: string]: string } {
    return {
      accelerateEndpoint: 'accelerate_endpoint',
      basePath: 'base_path',
      bucket: 'bucket',
      cdnEndpoint: 'cdn_endpoint',
      customizedAccelerateEndpoint: 'customized_accelerate_endpoint',
      customizedCdnEndpoint: 'customized_cdn_endpoint',
      customizedEndpoint: 'customized_endpoint',
      customizedInternalEndpoint: 'customized_internal_endpoint',
      domainId: 'domain_id',
      endpoint: 'endpoint',
      internalEndpoint: 'internal_endpoint',
      location: 'location',
      ownership: 'ownership',
      policy: 'policy',
      roleArn: 'role_arn',
      storeId: 'store_id',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      accelerateEndpoint: 'string',
      basePath: 'string',
      bucket: 'string',
      cdnEndpoint: 'string',
      customizedAccelerateEndpoint: 'string',
      customizedCdnEndpoint: 'string',
      customizedEndpoint: 'string',
      customizedInternalEndpoint: 'string',
      domainId: 'string',
      endpoint: 'string',
      internalEndpoint: 'string',
      location: 'string',
      ownership: 'string',
      policy: 'string',
      roleArn: 'string',
      storeId: 'string',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class AdminListStoresRequest extends $tea.Model {
  headers?: { [key: string]: string };
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * base domain response
 */
export class BaseDomainResponse extends $tea.Model {
  apiCname?: string;
  appCname?: string;
  authAlipayAppId?: string;
  authAlipayEnable?: boolean;
  authAlipayPrivateKey?: string;
  authCname?: string;
  authConfig?: {[key: string]: any};
  authDingdingAppId?: string;
  authDingdingAppSecret?: string;
  authDingdingEnable?: boolean;
  authEndpointEnable?: boolean;
  authRamAppId?: string;
  authRamAppSecret?: string;
  authRamEnable?: boolean;
  createdAt?: string;
  dataHashName?: string;
  description?: string;
  domainId?: string;
  domainName?: string;
  eventFilenameMatches?: string;
  eventMnsEndpoint?: string;
  eventMnsTopic?: string;
  eventNames?: string[];
  eventRoleArn?: string;
  initDriveEnable?: boolean;
  initDriveSize?: number;
  initDriveStoreId?: string;
  mode?: string;
  pathType?: string;
  publishedAppAccessStrategy?: AppAccessStrategy;
  sharable?: boolean;
  storeLevel?: string;
  storeRegionList?: string[];
  updatedAt?: string;
  static names(): { [key: string]: string } {
    return {
      apiCname: 'api_cname',
      appCname: 'app_cname',
      authAlipayAppId: 'auth_alipay_app_id',
      authAlipayEnable: 'auth_alipay_enable',
      authAlipayPrivateKey: 'auth_alipay_private_key',
      authCname: 'auth_cname',
      authConfig: 'auth_config',
      authDingdingAppId: 'auth_dingding_app_id',
      authDingdingAppSecret: 'auth_dingding_app_secret',
      authDingdingEnable: 'auth_dingding_enable',
      authEndpointEnable: 'auth_endpoint_enable',
      authRamAppId: 'auth_ram_app_id',
      authRamAppSecret: 'auth_ram_app_secret',
      authRamEnable: 'auth_ram_enable',
      createdAt: 'created_at',
      dataHashName: 'data_hash_name',
      description: 'description',
      domainId: 'domain_id',
      domainName: 'domain_name',
      eventFilenameMatches: 'event_filename_matches',
      eventMnsEndpoint: 'event_mns_endpoint',
      eventMnsTopic: 'event_mns_topic',
      eventNames: 'event_names',
      eventRoleArn: 'event_role_arn',
      initDriveEnable: 'init_drive_enable',
      initDriveSize: 'init_drive_size',
      initDriveStoreId: 'init_drive_store_id',
      mode: 'mode',
      pathType: 'path_type',
      publishedAppAccessStrategy: 'published_app_access_strategy',
      sharable: 'sharable',
      storeLevel: 'store_level',
      storeRegionList: 'store_region_list',
      updatedAt: 'updated_at',
    };
  }

  static types(): { [key: string]: any } {
    return {
      apiCname: 'string',
      appCname: 'string',
      authAlipayAppId: 'string',
      authAlipayEnable: 'boolean',
      authAlipayPrivateKey: 'string',
      authCname: 'string',
      authConfig: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      authDingdingAppId: 'string',
      authDingdingAppSecret: 'string',
      authDingdingEnable: 'boolean',
      authEndpointEnable: 'boolean',
      authRamAppId: 'string',
      authRamAppSecret: 'string',
      authRamEnable: 'boolean',
      createdAt: 'string',
      dataHashName: 'string',
      description: 'string',
      domainId: 'string',
      domainName: 'string',
      eventFilenameMatches: 'string',
      eventMnsEndpoint: 'string',
      eventMnsTopic: 'string',
      eventNames: { 'type': 'array', 'itemType': 'string' },
      eventRoleArn: 'string',
      initDriveEnable: 'boolean',
      initDriveSize: 'number',
      initDriveStoreId: 'string',
      mode: 'string',
      pathType: 'string',
      publishedAppAccessStrategy: AppAccessStrategy,
      sharable: 'boolean',
      storeLevel: 'string',
      storeRegionList: { 'type': 'array', 'itemType': 'string' },
      updatedAt: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class BaseMediaResponse extends $tea.Model {
  addressLine?: string;
  city?: string;
  country?: string;
  district?: string;
  height?: number;
  imageTags?: SystemTag[];
  location?: string;
  province?: string;
  time?: string;
  township?: string;
  width?: number;
  static names(): { [key: string]: string } {
    return {
      addressLine: 'address_line',
      city: 'city',
      country: 'country',
      district: 'district',
      height: 'height',
      imageTags: 'image_tags',
      location: 'location',
      province: 'province',
      time: 'time',
      township: 'township',
      width: 'width',
    };
  }

  static types(): { [key: string]: any } {
    return {
      addressLine: 'string',
      city: 'string',
      country: 'string',
      district: 'string',
      height: 'number',
      imageTags: { 'type': 'array', 'itemType': SystemTag },
      location: 'string',
      province: 'string',
      time: 'string',
      township: 'string',
      width: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class CNameStatus extends $tea.Model {
  bingdingState: string;
  legalState: string;
  remark: string;
  static names(): { [key: string]: string } {
    return {
      bingdingState: 'bingding_state',
      legalState: 'legal_state',
      remark: 'remark',
    };
  }

  static types(): { [key: string]: any } {
    return {
      bingdingState: 'string',
      legalState: 'string',
      remark: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * create domain response
 */
export class CreateDomainResponse extends $tea.Model {
  apiCname?: string;
  appCname?: string;
  authAlipayAppId?: string;
  authAlipayEnable?: boolean;
  authAlipayPrivateKey?: string;
  authCname?: string;
  authConfig?: {[key: string]: any};
  authDingdingAppId?: string;
  authDingdingAppSecret?: string;
  authDingdingEnable?: boolean;
  authEndpointEnable?: boolean;
  authRamAppId?: string;
  authRamAppSecret?: string;
  authRamEnable?: boolean;
  createdAt?: string;
  dataHashName?: string;
  description?: string;
  domainId?: string;
  domainName?: string;
  eventFilenameMatches?: string;
  eventMnsEndpoint?: string;
  eventMnsTopic?: string;
  eventNames?: string[];
  eventRoleArn?: string;
  initDriveEnable?: boolean;
  initDriveSize?: number;
  initDriveStoreId?: string;
  mode?: string;
  pathType?: string;
  publishedAppAccessStrategy?: AppAccessStrategy;
  sharable?: boolean;
  storeLevel?: string;
  storeRegionList?: string[];
  updatedAt?: string;
  static names(): { [key: string]: string } {
    return {
      apiCname: 'api_cname',
      appCname: 'app_cname',
      authAlipayAppId: 'auth_alipay_app_id',
      authAlipayEnable: 'auth_alipay_enable',
      authAlipayPrivateKey: 'auth_alipay_private_key',
      authCname: 'auth_cname',
      authConfig: 'auth_config',
      authDingdingAppId: 'auth_dingding_app_id',
      authDingdingAppSecret: 'auth_dingding_app_secret',
      authDingdingEnable: 'auth_dingding_enable',
      authEndpointEnable: 'auth_endpoint_enable',
      authRamAppId: 'auth_ram_app_id',
      authRamAppSecret: 'auth_ram_app_secret',
      authRamEnable: 'auth_ram_enable',
      createdAt: 'created_at',
      dataHashName: 'data_hash_name',
      description: 'description',
      domainId: 'domain_id',
      domainName: 'domain_name',
      eventFilenameMatches: 'event_filename_matches',
      eventMnsEndpoint: 'event_mns_endpoint',
      eventMnsTopic: 'event_mns_topic',
      eventNames: 'event_names',
      eventRoleArn: 'event_role_arn',
      initDriveEnable: 'init_drive_enable',
      initDriveSize: 'init_drive_size',
      initDriveStoreId: 'init_drive_store_id',
      mode: 'mode',
      pathType: 'path_type',
      publishedAppAccessStrategy: 'published_app_access_strategy',
      sharable: 'sharable',
      storeLevel: 'store_level',
      storeRegionList: 'store_region_list',
      updatedAt: 'updated_at',
    };
  }

  static types(): { [key: string]: any } {
    return {
      apiCname: 'string',
      appCname: 'string',
      authAlipayAppId: 'string',
      authAlipayEnable: 'boolean',
      authAlipayPrivateKey: 'string',
      authCname: 'string',
      authConfig: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      authDingdingAppId: 'string',
      authDingdingAppSecret: 'string',
      authDingdingEnable: 'boolean',
      authEndpointEnable: 'boolean',
      authRamAppId: 'string',
      authRamAppSecret: 'string',
      authRamEnable: 'boolean',
      createdAt: 'string',
      dataHashName: 'string',
      description: 'string',
      domainId: 'string',
      domainName: 'string',
      eventFilenameMatches: 'string',
      eventMnsEndpoint: 'string',
      eventMnsTopic: 'string',
      eventNames: { 'type': 'array', 'itemType': 'string' },
      eventRoleArn: 'string',
      initDriveEnable: 'boolean',
      initDriveSize: 'number',
      initDriveStoreId: 'string',
      mode: 'string',
      pathType: 'string',
      publishedAppAccessStrategy: AppAccessStrategy,
      sharable: 'boolean',
      storeLevel: 'string',
      storeRegionList: { 'type': 'array', 'itemType': 'string' },
      updatedAt: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class DataCName extends $tea.Model {
  dataCname: string;
  location: string;
  static names(): { [key: string]: string } {
    return {
      dataCname: 'data_cname',
      location: 'location',
    };
  }

  static types(): { [key: string]: any } {
    return {
      dataCname: 'string',
      location: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class DomainCNameResponse extends $tea.Model {
  dataCnameList: DataCName[];
  domainId: string;
  static names(): { [key: string]: string } {
    return {
      dataCnameList: 'data_cname_list',
      domainId: 'domain_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      dataCnameList: { 'type': 'array', 'itemType': DataCName },
      domainId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetAppPublicKeyResponse extends $tea.Model {
  appId: string;
  publicKey: string;
  static names(): { [key: string]: string } {
    return {
      appId: 'app_id',
      publicKey: 'public_key',
    };
  }

  static types(): { [key: string]: any } {
    return {
      appId: 'string',
      publicKey: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetAppResponse extends $tea.Model {
  aliOwnerId: string;
  appId: string;
  appName: string;
  appSecret: string;
  createdAt: string;
  description: string;
  logo: string;
  provider: string;
  redirectUri: string;
  scope: string[];
  screenshots: string[];
  stage: string;
  type: string;
  updatedAt: string;
  static names(): { [key: string]: string } {
    return {
      aliOwnerId: 'ali_owner_id',
      appId: 'app_id',
      appName: 'app_name',
      appSecret: 'app_secret',
      createdAt: 'created_at',
      description: 'description',
      logo: 'logo',
      provider: 'provider',
      redirectUri: 'redirect_uri',
      scope: 'scope',
      screenshots: 'screenshots',
      stage: 'stage',
      type: 'type',
      updatedAt: 'updated_at',
    };
  }

  static types(): { [key: string]: any } {
    return {
      aliOwnerId: 'string',
      appId: 'string',
      appName: 'string',
      appSecret: 'string',
      createdAt: 'string',
      description: 'string',
      logo: 'string',
      provider: 'string',
      redirectUri: 'string',
      scope: { 'type': 'array', 'itemType': 'string' },
      screenshots: { 'type': 'array', 'itemType': 'string' },
      stage: 'string',
      type: 'string',
      updatedAt: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetBizCNameInfoResponse extends $tea.Model {
  bizCname?: string;
  certId?: string;
  certName?: string;
  cnameStatus?: CNameStatus;
  cnameType?: string;
  domainId: string;
  isVpc?: boolean;
  static names(): { [key: string]: string } {
    return {
      bizCname: 'biz_cname',
      certId: 'cert_id',
      certName: 'cert_name',
      cnameStatus: 'cname_status',
      cnameType: 'cname_type',
      domainId: 'domain_id',
      isVpc: 'is_vpc',
    };
  }

  static types(): { [key: string]: any } {
    return {
      bizCname: 'string',
      certId: 'string',
      certName: 'string',
      cnameStatus: CNameStatus,
      cnameType: 'string',
      domainId: 'string',
      isVpc: 'boolean',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * get domain response
 */
export class GetDomainResponse extends $tea.Model {
  apiCname?: string;
  appCname?: string;
  authAlipayAppId?: string;
  authAlipayEnable?: boolean;
  authAlipayPrivateKey?: string;
  authCname?: string;
  authConfig?: {[key: string]: any};
  authDingdingAppId?: string;
  authDingdingAppSecret?: string;
  authDingdingEnable?: boolean;
  authEndpointEnable?: boolean;
  authRamAppId?: string;
  authRamAppSecret?: string;
  authRamEnable?: boolean;
  createdAt?: string;
  dataHashName?: string;
  description?: string;
  domainId?: string;
  domainName?: string;
  eventFilenameMatches?: string;
  eventMnsEndpoint?: string;
  eventMnsTopic?: string;
  eventNames?: string[];
  eventRoleArn?: string;
  initDriveEnable?: boolean;
  initDriveSize?: number;
  initDriveStoreId?: string;
  mode?: string;
  pathType?: string;
  publishedAppAccessStrategy?: AppAccessStrategy;
  sharable?: boolean;
  storeLevel?: string;
  storeRegionList?: string[];
  updatedAt?: string;
  static names(): { [key: string]: string } {
    return {
      apiCname: 'api_cname',
      appCname: 'app_cname',
      authAlipayAppId: 'auth_alipay_app_id',
      authAlipayEnable: 'auth_alipay_enable',
      authAlipayPrivateKey: 'auth_alipay_private_key',
      authCname: 'auth_cname',
      authConfig: 'auth_config',
      authDingdingAppId: 'auth_dingding_app_id',
      authDingdingAppSecret: 'auth_dingding_app_secret',
      authDingdingEnable: 'auth_dingding_enable',
      authEndpointEnable: 'auth_endpoint_enable',
      authRamAppId: 'auth_ram_app_id',
      authRamAppSecret: 'auth_ram_app_secret',
      authRamEnable: 'auth_ram_enable',
      createdAt: 'created_at',
      dataHashName: 'data_hash_name',
      description: 'description',
      domainId: 'domain_id',
      domainName: 'domain_name',
      eventFilenameMatches: 'event_filename_matches',
      eventMnsEndpoint: 'event_mns_endpoint',
      eventMnsTopic: 'event_mns_topic',
      eventNames: 'event_names',
      eventRoleArn: 'event_role_arn',
      initDriveEnable: 'init_drive_enable',
      initDriveSize: 'init_drive_size',
      initDriveStoreId: 'init_drive_store_id',
      mode: 'mode',
      pathType: 'path_type',
      publishedAppAccessStrategy: 'published_app_access_strategy',
      sharable: 'sharable',
      storeLevel: 'store_level',
      storeRegionList: 'store_region_list',
      updatedAt: 'updated_at',
    };
  }

  static types(): { [key: string]: any } {
    return {
      apiCname: 'string',
      appCname: 'string',
      authAlipayAppId: 'string',
      authAlipayEnable: 'boolean',
      authAlipayPrivateKey: 'string',
      authCname: 'string',
      authConfig: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      authDingdingAppId: 'string',
      authDingdingAppSecret: 'string',
      authDingdingEnable: 'boolean',
      authEndpointEnable: 'boolean',
      authRamAppId: 'string',
      authRamAppSecret: 'string',
      authRamEnable: 'boolean',
      createdAt: 'string',
      dataHashName: 'string',
      description: 'string',
      domainId: 'string',
      domainName: 'string',
      eventFilenameMatches: 'string',
      eventMnsEndpoint: 'string',
      eventMnsTopic: 'string',
      eventNames: { 'type': 'array', 'itemType': 'string' },
      eventRoleArn: 'string',
      initDriveEnable: 'boolean',
      initDriveSize: 'number',
      initDriveStoreId: 'string',
      mode: 'string',
      pathType: 'string',
      publishedAppAccessStrategy: AppAccessStrategy,
      sharable: 'boolean',
      storeLevel: 'string',
      storeRegionList: { 'type': 'array', 'itemType': 'string' },
      updatedAt: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class GetUserAccessTokenRequest extends $tea.Model {
  headers?: { [key: string]: string };
  role?: string;
  userId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      role: 'role',
      userId: 'user_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      role: 'string',
      userId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class ListAppsResponse extends $tea.Model {
  items: GetAppResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': GetAppResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list domain cors response
 */
export class ListDomainCORSRuleResponse extends $tea.Model {
  corsRuleList?: CorsRule[];
  domainId?: string;
  static names(): { [key: string]: string } {
    return {
      corsRuleList: 'cors_rule_list',
      domainId: 'domain_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      corsRuleList: { 'type': 'array', 'itemType': CorsRule },
      domainId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list domain response
 */
export class ListDomainsResponse extends $tea.Model {
  items?: BaseDomainResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': BaseDomainResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class ListStoresResponse extends $tea.Model {
  items: Store[];
  static names(): { [key: string]: string } {
    return {
      items: 'items',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': Store },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class SetBizCNameCertResponse extends $tea.Model {
  bizCname?: string;
  certName?: string;
  cnameType?: string;
  domainId: string;
  isVpc?: boolean;
  static names(): { [key: string]: string } {
    return {
      bizCname: 'biz_cname',
      certName: 'cert_name',
      cnameType: 'cname_type',
      domainId: 'domain_id',
      isVpc: 'is_vpc',
    };
  }

  static types(): { [key: string]: any } {
    return {
      bizCname: 'string',
      certName: 'string',
      cnameType: 'string',
      domainId: 'string',
      isVpc: 'boolean',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class SetBizCNameResponse extends $tea.Model {
  bizCname?: string;
  cnameStatus?: CNameStatus;
  cnameType?: string;
  domainId: string;
  isVpc?: boolean;
  static names(): { [key: string]: string } {
    return {
      bizCname: 'biz_cname',
      cnameStatus: 'cname_status',
      cnameType: 'cname_type',
      domainId: 'domain_id',
      isVpc: 'is_vpc',
    };
  }

  static types(): { [key: string]: any } {
    return {
      bizCname: 'string',
      cnameStatus: CNameStatus,
      cnameType: 'string',
      domainId: 'string',
      isVpc: 'boolean',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class SetDataCNameResponse extends $tea.Model {
  dataCname: string;
  domainId: string;
  location: string;
  static names(): { [key: string]: string } {
    return {
      dataCname: 'data_cname',
      domainId: 'domain_id',
      location: 'location',
    };
  }

  static types(): { [key: string]: any } {
    return {
      dataCname: 'string',
      domainId: 'string',
      location: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class Store extends $tea.Model {
  accelerateEndpoint?: string;
  basePath?: string;
  bucket: string;
  cdnEndpoint?: string;
  customizedAccelerateEndpoint?: string;
  customizedCdnEndpoint?: string;
  customizedEndpoint?: string;
  customizedInternalEndpoint?: string;
  endpoint: string;
  internalEndpoint?: string;
  location?: string;
  ownership: string;
  policy: string;
  roleArn?: string;
  storeId: string;
  type: string;
  static names(): { [key: string]: string } {
    return {
      accelerateEndpoint: 'accelerate_endpoint',
      basePath: 'base_path',
      bucket: 'bucket',
      cdnEndpoint: 'cdn_endpoint',
      customizedAccelerateEndpoint: 'customized_accelerate_endpoint',
      customizedCdnEndpoint: 'customized_cdn_endpoint',
      customizedEndpoint: 'customized_endpoint',
      customizedInternalEndpoint: 'customized_internal_endpoint',
      endpoint: 'endpoint',
      internalEndpoint: 'internal_endpoint',
      location: 'location',
      ownership: 'ownership',
      policy: 'policy',
      roleArn: 'role_arn',
      storeId: 'store_id',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      accelerateEndpoint: 'string',
      basePath: 'string',
      bucket: 'string',
      cdnEndpoint: 'string',
      customizedAccelerateEndpoint: 'string',
      customizedCdnEndpoint: 'string',
      customizedEndpoint: 'string',
      customizedInternalEndpoint: 'string',
      endpoint: 'string',
      internalEndpoint: 'string',
      location: 'string',
      ownership: 'string',
      policy: 'string',
      roleArn: 'string',
      storeId: 'string',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * create domain response
 */
export class UpdateDomainResponse extends $tea.Model {
  apiCname?: string;
  appCname?: string;
  authAlipayAppId?: string;
  authAlipayEnable?: boolean;
  authAlipayPrivateKey?: string;
  authCname?: string;
  authConfig?: {[key: string]: any};
  authDingdingAppId?: string;
  authDingdingAppSecret?: string;
  authDingdingEnable?: boolean;
  authEndpointEnable?: boolean;
  authRamAppId?: string;
  authRamAppSecret?: string;
  authRamEnable?: boolean;
  createdAt?: string;
  dataHashName?: string;
  description?: string;
  domainId?: string;
  domainName?: string;
  eventFilenameMatches?: string;
  eventMnsEndpoint?: string;
  eventMnsTopic?: string;
  eventNames?: string[];
  eventRoleArn?: string;
  initDriveEnable?: boolean;
  initDriveSize?: number;
  initDriveStoreId?: string;
  mode?: string;
  pathType?: string;
  publishedAppAccessStrategy?: AppAccessStrategy;
  sharable?: boolean;
  storeLevel?: string;
  storeRegionList?: string[];
  updatedAt?: string;
  static names(): { [key: string]: string } {
    return {
      apiCname: 'api_cname',
      appCname: 'app_cname',
      authAlipayAppId: 'auth_alipay_app_id',
      authAlipayEnable: 'auth_alipay_enable',
      authAlipayPrivateKey: 'auth_alipay_private_key',
      authCname: 'auth_cname',
      authConfig: 'auth_config',
      authDingdingAppId: 'auth_dingding_app_id',
      authDingdingAppSecret: 'auth_dingding_app_secret',
      authDingdingEnable: 'auth_dingding_enable',
      authEndpointEnable: 'auth_endpoint_enable',
      authRamAppId: 'auth_ram_app_id',
      authRamAppSecret: 'auth_ram_app_secret',
      authRamEnable: 'auth_ram_enable',
      createdAt: 'created_at',
      dataHashName: 'data_hash_name',
      description: 'description',
      domainId: 'domain_id',
      domainName: 'domain_name',
      eventFilenameMatches: 'event_filename_matches',
      eventMnsEndpoint: 'event_mns_endpoint',
      eventMnsTopic: 'event_mns_topic',
      eventNames: 'event_names',
      eventRoleArn: 'event_role_arn',
      initDriveEnable: 'init_drive_enable',
      initDriveSize: 'init_drive_size',
      initDriveStoreId: 'init_drive_store_id',
      mode: 'mode',
      pathType: 'path_type',
      publishedAppAccessStrategy: 'published_app_access_strategy',
      sharable: 'sharable',
      storeLevel: 'store_level',
      storeRegionList: 'store_region_list',
      updatedAt: 'updated_at',
    };
  }

  static types(): { [key: string]: any } {
    return {
      apiCname: 'string',
      appCname: 'string',
      authAlipayAppId: 'string',
      authAlipayEnable: 'boolean',
      authAlipayPrivateKey: 'string',
      authCname: 'string',
      authConfig: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      authDingdingAppId: 'string',
      authDingdingAppSecret: 'string',
      authDingdingEnable: 'boolean',
      authEndpointEnable: 'boolean',
      authRamAppId: 'string',
      authRamAppSecret: 'string',
      authRamEnable: 'boolean',
      createdAt: 'string',
      dataHashName: 'string',
      description: 'string',
      domainId: 'string',
      domainName: 'string',
      eventFilenameMatches: 'string',
      eventMnsEndpoint: 'string',
      eventMnsTopic: 'string',
      eventNames: { 'type': 'array', 'itemType': 'string' },
      eventRoleArn: 'string',
      initDriveEnable: 'boolean',
      initDriveSize: 'number',
      initDriveStoreId: 'string',
      mode: 'string',
      pathType: 'string',
      publishedAppAccessStrategy: AppAccessStrategy,
      sharable: 'boolean',
      storeLevel: 'string',
      storeRegionList: { 'type': 'array', 'itemType': 'string' },
      updatedAt: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetAsyncTaskInfoModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetAsyncTaskResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetAsyncTaskResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class BatchOperationModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: BatchResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: BatchResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class CreateDriveModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: CreateDriveResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: CreateDriveResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class DeleteDriveModel extends $tea.Model {
  headers?: { [key: string]: string };
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetDriveModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetDriveResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetDriveResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetDefaultDriveModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetDriveResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetDriveResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListDrivesModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListDriveResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListDriveResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListMyDrivesModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListDriveResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListDriveResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class UpdateDriveModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: UpdateDriveResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: UpdateDriveResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class CompleteFileModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: CompleteFileResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: CompleteFileResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class CopyFileModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: CopyFileResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: CopyFileResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class CreateFileModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: CreateFileResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: CreateFileResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class DeleteFileModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: DeleteFileResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: DeleteFileResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetFileModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetFileResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetFileResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetFileByPathModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetFileByPathResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetFileByPathResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetDownloadUrlModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetDownloadUrlResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetDownloadUrlResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetLastCursorModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetLastCursorResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetLastCursorResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetMediaPlayUrlModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetMediaPlayURLResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetMediaPlayURLResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetOfficeEditUrlModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetOfficeEditUrlResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetOfficeEditUrlResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetOfficePreviewUrlModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetOfficePreviewUrlResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetOfficePreviewUrlResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetUploadUrlModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetUploadUrlResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetUploadUrlResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetVideoPreviewSpriteUrlModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetVideoPreviewSpriteURLResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetVideoPreviewSpriteURLResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetVideoPreviewUrlModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetVideoPreviewURLResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetVideoPreviewURLResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListFileModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListFileResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListFileResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListFileByAnonymousModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListByAnonymousResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListByAnonymousResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListFileByCustomIndexKeyModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListFileResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListFileResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListFileDeltaModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListFileDeltaResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListFileDeltaResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListUploadedPartsModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListUploadedPartResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListUploadedPartResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class MoveFileModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: MoveFileResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: MoveFileResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class TokenModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: RefreshOfficeEditTokenResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: RefreshOfficeEditTokenResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ScanFileMetaModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ScanFileMetaResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ScanFileMetaResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class SearchFileModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: SearchFileResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: SearchFileResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class UpdateFileModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: UpdateFileMetaResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: UpdateFileMetaResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class CreateShareModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: CreateShareResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: CreateShareResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class DeleteShareModel extends $tea.Model {
  headers?: { [key: string]: string };
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetShareModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetShareResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetShareResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListShareModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListShareResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListShareResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class UpdateShareModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: UpdateShareResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: UpdateShareResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class CancelShareLinkModel extends $tea.Model {
  headers?: { [key: string]: string };
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class CreateShareLinkModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: CreateShareLinkResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: CreateShareLinkResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetShareByAnonymousModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetShareLinkByAnonymousResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetShareLinkByAnonymousResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetShareIdModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetShareLinkIDResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetShareLinkIDResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetShareTokenModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetShareLinkTokenResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetShareLinkTokenResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListShareLinkModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListShareLinkResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListShareLinkResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * complete file request
 */
export class BaseCompleteFileRequest extends $tea.Model {
  additionData?: {[key: string]: any};
  driveId?: string;
  partInfoList?: UploadPartInfo[];
  shareId?: string;
  uploadId?: string;
  static names(): { [key: string]: string } {
    return {
      additionData: 'addition_data',
      driveId: 'drive_id',
      partInfoList: 'part_info_list',
      shareId: 'share_id',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      driveId: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      shareId: 'string',
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * create file request
 */
export class BaseCreateFileRequest extends $tea.Model {
  additionData?: {[key: string]: any};
  contentMd5?: string;
  contentType?: string;
  name: string;
  partInfoList?: UploadPartInfo[];
  size?: number;
  type: string;
  static names(): { [key: string]: string } {
    return {
      additionData: 'addition_data',
      contentMd5: 'content_md5',
      contentType: 'content_type',
      name: 'name',
      partInfoList: 'part_info_list',
      size: 'size',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      contentMd5: 'string',
      contentType: 'string',
      name: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      size: 'number',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class BaseFileProcessRequest extends $tea.Model {
  imageCroppingAspectRatios?: string[];
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      imageCroppingAspectRatios: 'image_cropping_aspect_ratios',
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      imageCroppingAspectRatios: { 'type': 'array', 'itemType': 'string' },
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class BaseFileRequest extends $tea.Model {
  additionData?: {[key: string]: any};
  static names(): { [key: string]: string } {
    return {
      additionData: 'addition_data',
    };
  }

  static types(): { [key: string]: any } {
    return {
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文件上传URL
 */
export class BaseGetUploadUrlRequest extends $tea.Model {
  contentMd5?: string;
  driveId?: string;
  partInfoList?: UploadPartInfo[];
  shareId?: string;
  uploadId: string;
  static names(): { [key: string]: string } {
    return {
      contentMd5: 'content_md5',
      driveId: 'drive_id',
      partInfoList: 'part_info_list',
      shareId: 'share_id',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      contentMd5: 'string',
      driveId: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      shareId: 'string',
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Base image process
 */
export class BaseImageProcessRequest extends $tea.Model {
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list file request
 */
export class BaseListFileRequest extends $tea.Model {
  additionData?: {[key: string]: any};
  driveId?: string;
  imageCroppingAspectRatios?: string[];
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  limit?: number;
  marker?: string;
  referer?: string;
  shareId?: string;
  signToken?: string;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      additionData: 'addition_data',
      driveId: 'drive_id',
      imageCroppingAspectRatios: 'image_cropping_aspect_ratios',
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      limit: 'limit',
      marker: 'marker',
      referer: 'referer',
      shareId: 'share_id',
      signToken: 'sign_token',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      driveId: 'string',
      imageCroppingAspectRatios: { 'type': 'array', 'itemType': 'string' },
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      limit: 'number',
      marker: 'string',
      referer: 'string',
      shareId: 'string',
      signToken: 'string',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 文件移动请求
 */
export class BaseMoveFileRequest extends $tea.Model {
  driveId: string;
  newName?: string;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      newName: 'new_name',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      newName: 'string',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 批处理
 */
export class BatchRequest extends $tea.Model {
  headers?: { [key: string]: string };
  requests: BatchSubRequest[];
  resource: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      requests: 'requests',
      resource: 'resource',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      requests: { 'type': 'array', 'itemType': BatchSubRequest },
      resource: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class BatchSubRequest extends $tea.Model {
  body?: {[key: string]: any};
  headers?: {[key: string]: any};
  id: string;
  method: string;
  url: string;
  static names(): { [key: string]: string } {
    return {
      body: 'body',
      headers: 'headers',
      id: 'id',
      method: 'method',
      url: 'url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      body: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      id: 'string',
      method: 'string',
      url: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文件夹size信息
 */
export class CCPGetDirSizeInfoRequest extends $tea.Model {
  driveId?: string;
  fileId: string;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      fileId: 'file_id',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      fileId: 'string',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * cancel_share_link request
 */
export class CancelShareLinkRequest extends $tea.Model {
  headers?: { [key: string]: string };
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 合并文件上传任务
 */
export class CompleteFileRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  driveId?: string;
  fileId: string;
  partInfoList?: UploadPartInfo[];
  shareId?: string;
  uploadId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      driveId: 'drive_id',
      fileId: 'file_id',
      partInfoList: 'part_info_list',
      shareId: 'share_id',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      driveId: 'string',
      fileId: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      shareId: 'string',
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 文件拷贝
 */
export class CopyFileRequest extends $tea.Model {
  headers?: { [key: string]: string };
  autoRename?: boolean;
  driveId?: string;
  fileId: string;
  fileIdPath?: string;
  newName?: string;
  shareId?: string;
  toDriveId?: string;
  toParentFileId: string;
  toShareId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      autoRename: 'auto_rename',
      driveId: 'drive_id',
      fileId: 'file_id',
      fileIdPath: 'file_id_path',
      newName: 'new_name',
      shareId: 'share_id',
      toDriveId: 'to_drive_id',
      toParentFileId: 'to_parent_file_id',
      toShareId: 'to_share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      autoRename: 'boolean',
      driveId: 'string',
      fileId: 'string',
      fileIdPath: 'string',
      newName: 'string',
      shareId: 'string',
      toDriveId: 'string',
      toParentFileId: 'string',
      toShareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * create drive request
 */
export class CreateDriveRequest extends $tea.Model {
  headers?: { [key: string]: string };
  default?: boolean;
  description?: string;
  driveName: string;
  driveType?: string;
  encryptMode?: string;
  location?: string;
  owner: string;
  relativePath?: string;
  status?: string;
  storeId?: string;
  totalSize?: number;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      default: 'default',
      description: 'description',
      driveName: 'drive_name',
      driveType: 'drive_type',
      encryptMode: 'encrypt_mode',
      location: 'location',
      owner: 'owner',
      relativePath: 'relative_path',
      status: 'status',
      storeId: 'store_id',
      totalSize: 'total_size',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      default: 'boolean',
      description: 'string',
      driveName: 'string',
      driveType: 'string',
      encryptMode: 'string',
      location: 'string',
      owner: 'string',
      relativePath: 'string',
      status: 'string',
      storeId: 'string',
      totalSize: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 创建文件
 */
export class CreateFileRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  autoRename?: boolean;
  checkNameMode?: string;
  contentHash?: string;
  contentHashName?: string;
  contentMd5?: string;
  contentType?: string;
  description?: string;
  driveId?: string;
  encryptMode?: string;
  fileId?: string;
  forceUploadToLocation?: boolean;
  hidden?: boolean;
  imageMediaMetadata?: ImageMediaMetadata;
  labels?: string[];
  lastUpdatedAt?: string;
  location?: string;
  meta?: string;
  name: string;
  parentFileId: string;
  parentFileIdPath?: string;
  partInfoList?: UploadPartInfo[];
  preHash?: string;
  shareId?: string;
  size?: number;
  streamsInfo?: {[key: string]: any};
  type: string;
  userMeta?: string;
  videoMediaMetadata?: VideoMediaMetadata;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      autoRename: 'auto_rename',
      checkNameMode: 'check_name_mode',
      contentHash: 'content_hash',
      contentHashName: 'content_hash_name',
      contentMd5: 'content_md5',
      contentType: 'content_type',
      description: 'description',
      driveId: 'drive_id',
      encryptMode: 'encrypt_mode',
      fileId: 'file_id',
      forceUploadToLocation: 'force_upload_to_location',
      hidden: 'hidden',
      imageMediaMetadata: 'image_media_metadata',
      labels: 'labels',
      lastUpdatedAt: 'last_updated_at',
      location: 'location',
      meta: 'meta',
      name: 'name',
      parentFileId: 'parent_file_id',
      parentFileIdPath: 'parent_file_id_path',
      partInfoList: 'part_info_list',
      preHash: 'pre_hash',
      shareId: 'share_id',
      size: 'size',
      streamsInfo: 'streams_info',
      type: 'type',
      userMeta: 'user_meta',
      videoMediaMetadata: 'video_media_metadata',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      autoRename: 'boolean',
      checkNameMode: 'string',
      contentHash: 'string',
      contentHashName: 'string',
      contentMd5: 'string',
      contentType: 'string',
      description: 'string',
      driveId: 'string',
      encryptMode: 'string',
      fileId: 'string',
      forceUploadToLocation: 'boolean',
      hidden: 'boolean',
      imageMediaMetadata: ImageMediaMetadata,
      labels: { 'type': 'array', 'itemType': 'string' },
      lastUpdatedAt: 'string',
      location: 'string',
      meta: 'string',
      name: 'string',
      parentFileId: 'string',
      parentFileIdPath: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      preHash: 'string',
      shareId: 'string',
      size: 'number',
      streamsInfo: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      type: 'string',
      userMeta: 'string',
      videoMediaMetadata: VideoMediaMetadata,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * create_share_link request
 */
export class CreateShareLinkRequest extends $tea.Model {
  headers?: { [key: string]: string };
  description?: string;
  driveId: string;
  expiration: string;
  fileId: string;
  fileIdList: string[];
  filePathList: string[];
  shareName?: string;
  sharePwd?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      description: 'description',
      driveId: 'drive_id',
      expiration: 'expiration',
      fileId: 'file_id',
      fileIdList: 'file_id_list',
      filePathList: 'file_path_list',
      shareName: 'share_name',
      sharePwd: 'share_pwd',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      description: 'string',
      driveId: 'string',
      expiration: 'string',
      fileId: 'string',
      fileIdList: { 'type': 'array', 'itemType': 'string' },
      filePathList: { 'type': 'array', 'itemType': 'string' },
      shareName: 'string',
      sharePwd: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * create share request
 */
export class CreateShareRequest extends $tea.Model {
  headers?: { [key: string]: string };
  description?: string;
  driveId: string;
  expiration?: string;
  owner: string;
  ownerType?: string;
  permissions?: string[];
  shareFileId?: string;
  shareFilePath?: string;
  shareName?: string;
  sharePolicy?: SharePermissionPolicy[];
  status?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      description: 'description',
      driveId: 'drive_id',
      expiration: 'expiration',
      owner: 'owner',
      ownerType: 'owner_type',
      permissions: 'permissions',
      shareFileId: 'share_file_id',
      shareFilePath: 'share_file_path',
      shareName: 'share_name',
      sharePolicy: 'share_policy',
      status: 'status',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      description: 'string',
      driveId: 'string',
      expiration: 'string',
      owner: 'string',
      ownerType: 'string',
      permissions: { 'type': 'array', 'itemType': 'string' },
      shareFileId: 'string',
      shareFilePath: 'string',
      shareName: 'string',
      sharePolicy: { 'type': 'array', 'itemType': SharePermissionPolicy },
      status: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Delete drive request
 */
export class DeleteDriveRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 删除文件请求
 */
export class DeleteFileRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId?: string;
  fileId?: string;
  fileIdPath?: string;
  permanently?: boolean;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
      fileId: 'file_id',
      fileIdPath: 'file_id_path',
      permanently: 'permanently',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
      fileId: 'string',
      fileIdPath: 'string',
      permanently: 'boolean',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 批量删除文件请求
 */
export class DeleteFilesRequest extends $tea.Model {
  driveId?: string;
  fileIdList: string[];
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      fileIdList: 'file_id_list',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      fileIdList: { 'type': 'array', 'itemType': 'string' },
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * delete share request
 */
export class DeleteShareRequest extends $tea.Model {
  headers?: { [key: string]: string };
  shareId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 下载文件请求body
 */
export class DownloadRequest extends $tea.Model {
  DriveID?: string;
  FileID: string;
  ImageThumbnailProcess?: string;
  ShareID?: string;
  VideoThumbnailProcess?: string;
  fileIdPath?: string;
  location?: string;
  referer?: string;
  signToken?: string;
  static names(): { [key: string]: string } {
    return {
      DriveID: 'DriveID',
      FileID: 'FileID',
      ImageThumbnailProcess: 'ImageThumbnailProcess',
      ShareID: 'ShareID',
      VideoThumbnailProcess: 'VideoThumbnailProcess',
      fileIdPath: 'file_id_path',
      location: 'location',
      referer: 'referer',
      signToken: 'sign_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      DriveID: 'string',
      FileID: 'string',
      ImageThumbnailProcess: 'string',
      ShareID: 'string',
      VideoThumbnailProcess: 'string',
      fileIdPath: 'string',
      location: 'string',
      referer: 'string',
      signToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取异步人去信息
 */
export class GetAsyncTaskRequest extends $tea.Model {
  headers?: { [key: string]: string };
  asyncTaskId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      asyncTaskId: 'async_task_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      asyncTaskId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Get default drive request
 */
export class GetDefaultDriveRequest extends $tea.Model {
  headers?: { [key: string]: string };
  userId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      userId: 'user_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      userId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文件下载地址的请求body
 */
export class GetDownloadUrlRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  driveId: string;
  expireSec?: number;
  fileId: string;
  fileIdPath?: string;
  fileName?: string;
  location?: string;
  referer?: string;
  shareId?: string;
  signToken?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      driveId: 'drive_id',
      expireSec: 'expire_sec',
      fileId: 'file_id',
      fileIdPath: 'file_id_path',
      fileName: 'file_name',
      location: 'location',
      referer: 'referer',
      shareId: 'share_id',
      signToken: 'sign_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      driveId: 'string',
      expireSec: 'number',
      fileId: 'string',
      fileIdPath: 'string',
      fileName: 'string',
      location: 'string',
      referer: 'string',
      shareId: 'string',
      signToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Get drive request
 */
export class GetDriveRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 根据路径获取 File 接口 body
 */
export class GetFileByPathRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  driveId: string;
  filePath?: string;
  imageCroppingAspectRatios?: string[];
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  referer?: string;
  signToken?: string;
  urlExpireSec?: number;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      driveId: 'drive_id',
      filePath: 'file_path',
      imageCroppingAspectRatios: 'image_cropping_aspect_ratios',
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      referer: 'referer',
      signToken: 'sign_token',
      urlExpireSec: 'url_expire_sec',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      driveId: 'string',
      filePath: 'string',
      imageCroppingAspectRatios: { 'type': 'array', 'itemType': 'string' },
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      referer: 'string',
      signToken: 'string',
      urlExpireSec: 'number',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文件元数据
 */
export class GetFileRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  driveId: string;
  fields?: string;
  fileId: string;
  fileIdPath?: string;
  imageCroppingAspectRatios?: string[];
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  location?: string;
  referer?: string;
  shareId?: string;
  signToken?: string;
  urlExpireSec?: number;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      driveId: 'drive_id',
      fields: 'fields',
      fileId: 'file_id',
      fileIdPath: 'file_id_path',
      imageCroppingAspectRatios: 'image_cropping_aspect_ratios',
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      location: 'location',
      referer: 'referer',
      shareId: 'share_id',
      signToken: 'sign_token',
      urlExpireSec: 'url_expire_sec',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      driveId: 'string',
      fields: 'string',
      fileId: 'string',
      fileIdPath: 'string',
      imageCroppingAspectRatios: { 'type': 'array', 'itemType': 'string' },
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      location: 'string',
      referer: 'string',
      shareId: 'string',
      signToken: 'string',
      urlExpireSec: 'number',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取最新游标
 */
export class GetLastCursorRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * get_media_play_url request
 */
export class GetMediaPlayURLRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  fileId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
      fileId: 'file_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
      fileId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取office文档在线编辑地址
 */
export class GetOfficeEditUrlRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  driveId: string;
  fileId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      driveId: 'drive_id',
      fileId: 'file_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      driveId: 'string',
      fileId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取office文档预览地址
 */
export class GetOfficePreviewUrlRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  driveId: string;
  fileId: string;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      driveId: 'drive_id',
      fileId: 'file_id',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      driveId: 'string',
      fileId: 'string',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * get_share_link_by_anonymous request
 */
export class GetShareLinkByAnonymousRequest extends $tea.Model {
  headers?: { [key: string]: string };
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * get_share_id request
 */
export class GetShareLinkIDRequest extends $tea.Model {
  headers?: { [key: string]: string };
  shareMsg?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      shareMsg: 'share_msg',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      shareMsg: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * get_share_token request
 */
export class GetShareLinkTokenRequest extends $tea.Model {
  headers?: { [key: string]: string };
  shareId?: string;
  sharePwd?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      shareId: 'share_id',
      sharePwd: 'share_pwd',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      shareId: 'string',
      sharePwd: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * get share request
 */
export class GetShareRequest extends $tea.Model {
  headers?: { [key: string]: string };
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文件上传URL
 */
export class GetUploadUrlRequest extends $tea.Model {
  headers?: { [key: string]: string };
  contentMd5?: string;
  driveId?: string;
  fileId: string;
  partInfoList?: UploadPartInfo[];
  shareId?: string;
  uploadId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      contentMd5: 'content_md5',
      driveId: 'drive_id',
      fileId: 'file_id',
      partInfoList: 'part_info_list',
      shareId: 'share_id',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      contentMd5: 'string',
      driveId: 'string',
      fileId: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      shareId: 'string',
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取视频雪碧图地址的请求body
 */
export class GetVideoPreviewSpriteURLRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  expireSec?: number;
  fileId: string;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
      expireSec: 'expire_sec',
      fileId: 'file_id',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
      expireSec: 'number',
      fileId: 'string',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取视频文件播放地址的请求body
 */
export class GetVideoPreviewURLRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  audioTemplateId?: string;
  driveId: string;
  expireSec?: number;
  fileId: string;
  shareId?: string;
  templateId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      audioTemplateId: 'audio_template_id',
      driveId: 'drive_id',
      expireSec: 'expire_sec',
      fileId: 'file_id',
      shareId: 'share_id',
      templateId: 'template_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      audioTemplateId: 'string',
      driveId: 'string',
      expireSec: 'number',
      fileId: 'string',
      shareId: 'string',
      templateId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * complete file request
 */
export class HostingCompleteFileRequest extends $tea.Model {
  additionData?: {[key: string]: any};
  driveId?: string;
  filePath?: string;
  forbidOverwrite?: boolean;
  partInfoList?: UploadPartInfo[];
  shareId?: string;
  uploadId?: string;
  static names(): { [key: string]: string } {
    return {
      additionData: 'addition_data',
      driveId: 'drive_id',
      filePath: 'file_path',
      forbidOverwrite: 'forbid_overwrite',
      partInfoList: 'part_info_list',
      shareId: 'share_id',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      driveId: 'string',
      filePath: 'string',
      forbidOverwrite: 'boolean',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      shareId: 'string',
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * copy file request
 */
export class HostingCopyFileRequest extends $tea.Model {
  driveId?: string;
  filePath: string;
  newName?: string;
  overwrite?: boolean;
  shareId?: string;
  toDriveId?: string;
  toParentFilePath: string;
  toShareId?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      filePath: 'file_path',
      newName: 'new_name',
      overwrite: 'overwrite',
      shareId: 'share_id',
      toDriveId: 'to_drive_id',
      toParentFilePath: 'to_parent_file_path',
      toShareId: 'to_share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      filePath: 'string',
      newName: 'string',
      overwrite: 'boolean',
      shareId: 'string',
      toDriveId: 'string',
      toParentFilePath: 'string',
      toShareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * create file request
 */
export class HostingCreateFileRequest extends $tea.Model {
  additionData?: {[key: string]: any};
  contentMd5?: string;
  contentType?: string;
  driveId?: string;
  forbidOverwrite?: boolean;
  name: string;
  parentFilePath: string;
  partInfoList?: UploadPartInfo[];
  shareId?: string;
  size?: number;
  type: string;
  static names(): { [key: string]: string } {
    return {
      additionData: 'addition_data',
      contentMd5: 'content_md5',
      contentType: 'content_type',
      driveId: 'drive_id',
      forbidOverwrite: 'forbid_overwrite',
      name: 'name',
      parentFilePath: 'parent_file_path',
      partInfoList: 'part_info_list',
      shareId: 'share_id',
      size: 'size',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      contentMd5: 'string',
      contentType: 'string',
      driveId: 'string',
      forbidOverwrite: 'boolean',
      name: 'string',
      parentFilePath: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      shareId: 'string',
      size: 'number',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 删除文件请求
 */
export class HostingDeleteFileRequest extends $tea.Model {
  driveId?: string;
  filePath: string;
  permanently?: boolean;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      filePath: 'file_path',
      permanently: 'permanently',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      filePath: 'string',
      permanently: 'boolean',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文件下载地址的请求body
 */
export class HostingGetDownloadUrlRequest extends $tea.Model {
  driveId?: string;
  expireSec?: number;
  fileName?: string;
  filePath: string;
  referer?: string;
  shareId?: string;
  signToken?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      expireSec: 'expire_sec',
      fileName: 'file_name',
      filePath: 'file_path',
      referer: 'referer',
      shareId: 'share_id',
      signToken: 'sign_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      expireSec: 'number',
      fileName: 'string',
      filePath: 'string',
      referer: 'string',
      shareId: 'string',
      signToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文件元数据
 */
export class HostingGetFileRequest extends $tea.Model {
  driveId?: string;
  filePath: string;
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  referer?: string;
  shareId?: string;
  signToken?: string;
  urlExpireSec?: number;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      filePath: 'file_path',
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      referer: 'referer',
      shareId: 'share_id',
      signToken: 'sign_token',
      urlExpireSec: 'url_expire_sec',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      filePath: 'string',
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      referer: 'string',
      shareId: 'string',
      signToken: 'string',
      urlExpireSec: 'number',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文件安全地址的请求body
 */
export class HostingGetSecureUrlRequest extends $tea.Model {
  driveId?: string;
  expireSec?: number;
  filePath: string;
  secureIp?: string;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      expireSec: 'expire_sec',
      filePath: 'file_path',
      secureIp: 'secure_ip',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      expireSec: 'number',
      filePath: 'string',
      secureIp: 'string',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取文件上传URL
 */
export class HostingGetUploadUrlRequest extends $tea.Model {
  contentMd5?: string;
  driveId?: string;
  filePath: string;
  partInfoList?: UploadPartInfo[];
  shareId?: string;
  uploadId: string;
  static names(): { [key: string]: string } {
    return {
      contentMd5: 'content_md5',
      driveId: 'drive_id',
      filePath: 'file_path',
      partInfoList: 'part_info_list',
      shareId: 'share_id',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      contentMd5: 'string',
      driveId: 'string',
      filePath: 'string',
      partInfoList: { 'type': 'array', 'itemType': UploadPartInfo },
      shareId: 'string',
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list file request
 */
export class HostingListFileRequest extends $tea.Model {
  additionData?: {[key: string]: any};
  driveId?: string;
  imageCroppingAspectRatios?: string[];
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  limit?: number;
  marker?: string;
  parentFilePath: string;
  referer?: string;
  shareId?: string;
  signToken?: string;
  urlExpireSec?: number;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      additionData: 'addition_data',
      driveId: 'drive_id',
      imageCroppingAspectRatios: 'image_cropping_aspect_ratios',
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      limit: 'limit',
      marker: 'marker',
      parentFilePath: 'parent_file_path',
      referer: 'referer',
      shareId: 'share_id',
      signToken: 'sign_token',
      urlExpireSec: 'url_expire_sec',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      driveId: 'string',
      imageCroppingAspectRatios: { 'type': 'array', 'itemType': 'string' },
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      limit: 'number',
      marker: 'string',
      parentFilePath: 'string',
      referer: 'string',
      shareId: 'string',
      signToken: 'string',
      urlExpireSec: 'number',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 列举uploadID对应的已上传分片
 */
export class HostingListUploadedPartRequest extends $tea.Model {
  driveId?: string;
  filePath: string;
  limit?: number;
  partNumberMarker?: number;
  shareId?: string;
  uploadId?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      filePath: 'file_path',
      limit: 'limit',
      partNumberMarker: 'part_number_marker',
      shareId: 'share_id',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      filePath: 'string',
      limit: 'number',
      partNumberMarker: 'number',
      shareId: 'string',
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 文件移动请求
 */
export class HostingMoveFileRequest extends $tea.Model {
  driveId?: string;
  filePath?: string;
  newName?: string;
  overwrite?: boolean;
  shareId?: string;
  toParentFilePath?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      filePath: 'file_path',
      newName: 'new_name',
      overwrite: 'overwrite',
      shareId: 'share_id',
      toParentFilePath: 'to_parent_file_path',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      filePath: 'string',
      newName: 'string',
      overwrite: 'boolean',
      shareId: 'string',
      toParentFilePath: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取视频DRM License
 */
export class HostingVideoDRMLicenseRequest extends $tea.Model {
  drmType: string;
  licenseRequest: string;
  static names(): { [key: string]: string } {
    return {
      drmType: 'drmType',
      licenseRequest: 'licenseRequest',
    };
  }

  static types(): { [key: string]: any } {
    return {
      drmType: 'string',
      licenseRequest: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取视频分辨率列表
 */
export class HostingVideoDefinitionRequest extends $tea.Model {
  driveId?: string;
  filePath: string;
  protectionScheme?: string;
  shareId?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      filePath: 'file_path',
      protectionScheme: 'protection_scheme',
      shareId: 'share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      filePath: 'string',
      protectionScheme: 'string',
      shareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取视频的m3u8文件
 */
export class HostingVideoM3U8Request extends $tea.Model {
  definition?: string;
  driveId?: string;
  expireSec?: number;
  filePath: string;
  protectionScheme?: string;
  shareId?: string;
  signToken: string;
  static names(): { [key: string]: string } {
    return {
      definition: 'definition',
      driveId: 'drive_id',
      expireSec: 'expire_sec',
      filePath: 'file_path',
      protectionScheme: 'protection_scheme',
      shareId: 'share_id',
      signToken: 'sign_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      definition: 'string',
      driveId: 'string',
      expireSec: 'number',
      filePath: 'string',
      protectionScheme: 'string',
      shareId: 'string',
      signToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 启动视频转码请求
 */
export class HostingVideoTranscodeRequest extends $tea.Model {
  driveId?: string;
  filePath: string;
  hlsTime?: number;
  protectionScheme?: string;
  remarks?: string;
  shareId?: string;
  transcode?: boolean;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      filePath: 'file_path',
      hlsTime: 'hls_time',
      protectionScheme: 'protection_scheme',
      remarks: 'remarks',
      shareId: 'share_id',
      transcode: 'transcode',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      filePath: 'string',
      hlsTime: 'number',
      protectionScheme: 'string',
      remarks: 'string',
      shareId: 'string',
      transcode: 'boolean',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class ImageMediaMetadata extends $tea.Model {
  height?: number;
  width?: number;
  static names(): { [key: string]: string } {
    return {
      height: 'height',
      width: 'width',
    };
  }

  static types(): { [key: string]: any } {
    return {
      height: 'number',
      width: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list_file_by_anonymous request
 */
export class ListByAnonymousRequest extends $tea.Model {
  headers?: { [key: string]: string };
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  limit?: number;
  marker?: string;
  parentFileId: string;
  referer?: string;
  shareId: string;
  signToken?: string;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      limit: 'limit',
      marker: 'marker',
      parentFileId: 'parent_file_id',
      referer: 'referer',
      shareId: 'share_id',
      signToken: 'sign_token',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      limit: 'number',
      marker: 'string',
      parentFileId: 'string',
      referer: 'string',
      shareId: 'string',
      signToken: 'string',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List drive request
 */
export class ListDriveRequest extends $tea.Model {
  headers?: { [key: string]: string };
  limit?: number;
  marker?: string;
  owner?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      limit: 'limit',
      marker: 'marker',
      owner: 'owner',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      limit: 'number',
      marker: 'string',
      owner: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 列举文件
 */
export class ListFileByCustomIndexKeyRequest extends $tea.Model {
  headers?: { [key: string]: string };
  Starred?: boolean;
  additionData?: {[key: string]: any};
  category?: string;
  customIndexKey: string;
  driveId?: string;
  encryptMode?: string;
  fields?: string;
  imageCroppingAspectRatios?: string[];
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  limit?: number;
  marker?: string;
  orderDirection?: string;
  referer?: string;
  shareId?: string;
  signToken?: string;
  status?: string;
  type?: string;
  urlExpireSec?: number;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      Starred: 'Starred',
      additionData: 'addition_data',
      category: 'category',
      customIndexKey: 'custom_index_key',
      driveId: 'drive_id',
      encryptMode: 'encrypt_mode',
      fields: 'fields',
      imageCroppingAspectRatios: 'image_cropping_aspect_ratios',
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      limit: 'limit',
      marker: 'marker',
      orderDirection: 'order_direction',
      referer: 'referer',
      shareId: 'share_id',
      signToken: 'sign_token',
      status: 'status',
      type: 'type',
      urlExpireSec: 'url_expire_sec',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      Starred: 'boolean',
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      category: 'string',
      customIndexKey: 'string',
      driveId: 'string',
      encryptMode: 'string',
      fields: 'string',
      imageCroppingAspectRatios: { 'type': 'array', 'itemType': 'string' },
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      limit: 'number',
      marker: 'string',
      orderDirection: 'string',
      referer: 'string',
      shareId: 'string',
      signToken: 'string',
      status: 'string',
      type: 'string',
      urlExpireSec: 'number',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取增量文件操作记录
 */
export class ListFileDeltaRequest extends $tea.Model {
  headers?: { [key: string]: string };
  cursor?: string;
  driveId: string;
  imageCroppingAspectRatios?: string[];
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  limit?: number;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      cursor: 'cursor',
      driveId: 'drive_id',
      imageCroppingAspectRatios: 'image_cropping_aspect_ratios',
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      limit: 'limit',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      cursor: 'string',
      driveId: 'string',
      imageCroppingAspectRatios: { 'type': 'array', 'itemType': 'string' },
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      limit: 'number',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 列举文件
 */
export class ListFileRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  all?: boolean;
  category?: string;
  driveId?: string;
  fields?: string;
  imageCroppingAspectRatios?: string[];
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  limit?: number;
  location?: string;
  marker?: string;
  orderBy?: string;
  orderDirection?: string;
  parentFileId: string;
  parentFileIdPath?: string;
  referer?: string;
  shareId?: string;
  signToken?: string;
  starred?: boolean;
  status?: string;
  type?: string;
  urlExpireSec?: number;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      all: 'all',
      category: 'category',
      driveId: 'drive_id',
      fields: 'fields',
      imageCroppingAspectRatios: 'image_cropping_aspect_ratios',
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      limit: 'limit',
      location: 'location',
      marker: 'marker',
      orderBy: 'order_by',
      orderDirection: 'order_direction',
      parentFileId: 'parent_file_id',
      parentFileIdPath: 'parent_file_id_path',
      referer: 'referer',
      shareId: 'share_id',
      signToken: 'sign_token',
      starred: 'starred',
      status: 'status',
      type: 'type',
      urlExpireSec: 'url_expire_sec',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      all: 'boolean',
      category: 'string',
      driveId: 'string',
      fields: 'string',
      imageCroppingAspectRatios: { 'type': 'array', 'itemType': 'string' },
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      limit: 'number',
      location: 'string',
      marker: 'string',
      orderBy: 'string',
      orderDirection: 'string',
      parentFileId: 'string',
      parentFileIdPath: 'string',
      referer: 'string',
      shareId: 'string',
      signToken: 'string',
      starred: 'boolean',
      status: 'string',
      type: 'string',
      urlExpireSec: 'number',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List my drive request
 */
export class ListMyDriveRequest extends $tea.Model {
  headers?: { [key: string]: string };
  limit?: number;
  marker?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      limit: 'limit',
      marker: 'marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      limit: 'number',
      marker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list_share_link request
 */
export class ListShareLinkRequest extends $tea.Model {
  headers?: { [key: string]: string };
  creator?: string;
  limit?: number;
  marker?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      creator: 'creator',
      limit: 'limit',
      marker: 'marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      creator: 'string',
      limit: 'number',
      marker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list share request
 */
export class ListShareRequest extends $tea.Model {
  headers?: { [key: string]: string };
  creator?: string;
  driveId?: string;
  limit?: number;
  marker?: string;
  owner?: string;
  ownerType?: string;
  shareFilePath?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      creator: 'creator',
      driveId: 'drive_id',
      limit: 'limit',
      marker: 'marker',
      owner: 'owner',
      ownerType: 'owner_type',
      shareFilePath: 'share_file_path',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      creator: 'string',
      driveId: 'string',
      limit: 'number',
      marker: 'string',
      owner: 'string',
      ownerType: 'string',
      shareFilePath: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list store file
 */
export class ListStoreFileRequest extends $tea.Model {
  limit?: number;
  marker?: string;
  parentFilePath?: string;
  storeId?: string;
  type?: string;
  static names(): { [key: string]: string } {
    return {
      limit: 'limit',
      marker: 'marker',
      parentFilePath: 'parent_file_path',
      storeId: 'store_id',
      type: 'type',
    };
  }

  static types(): { [key: string]: any } {
    return {
      limit: 'number',
      marker: 'string',
      parentFilePath: 'string',
      storeId: 'string',
      type: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * list storage file
 */
export class ListStoreRequest extends $tea.Model {
  domainId?: string;
  static names(): { [key: string]: string } {
    return {
      domainId: 'domain_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      domainId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 列举uploadID对应的已上传分片
 */
export class ListUploadedPartRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  fileId: string;
  fileIdPath?: string;
  limit?: number;
  partNumberMarker?: number;
  shareId?: string;
  uploadId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
      fileId: 'file_id',
      fileIdPath: 'file_id_path',
      limit: 'limit',
      partNumberMarker: 'part_number_marker',
      shareId: 'share_id',
      uploadId: 'upload_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
      fileId: 'string',
      fileIdPath: 'string',
      limit: 'number',
      partNumberMarker: 'number',
      shareId: 'string',
      uploadId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 文件移动请求
 */
export class MoveFileRequest extends $tea.Model {
  headers?: { [key: string]: string };
  autoRename?: boolean;
  driveId: string;
  fileId: string;
  fileIdPath?: string;
  newName?: string;
  shareId?: string;
  toDriveId?: string;
  toParentFileId: string;
  toShareId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      autoRename: 'auto_rename',
      driveId: 'drive_id',
      fileId: 'file_id',
      fileIdPath: 'file_id_path',
      newName: 'new_name',
      shareId: 'share_id',
      toDriveId: 'to_drive_id',
      toParentFileId: 'to_parent_file_id',
      toShareId: 'to_share_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      autoRename: 'boolean',
      driveId: 'string',
      fileId: 'string',
      fileIdPath: 'string',
      newName: 'string',
      shareId: 'string',
      toDriveId: 'string',
      toParentFileId: 'string',
      toShareId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * play_media request
 */
export class PlayMediaRequest extends $tea.Model {
  AuthKey: string;
  DriveID: string;
  FileID: string;
  static names(): { [key: string]: string } {
    return {
      AuthKey: 'AuthKey',
      DriveID: 'DriveID',
      FileID: 'FileID',
    };
  }

  static types(): { [key: string]: any } {
    return {
      AuthKey: 'string',
      DriveID: 'string',
      FileID: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 刷新office文档在线编辑凭证
 */
export class RefreshOfficeEditTokenRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  location?: string;
  officeAccessToken: string;
  officeRefreshToken: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      location: 'location',
      officeAccessToken: 'office_access_token',
      officeRefreshToken: 'office_refresh_token',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      location: 'string',
      officeAccessToken: 'string',
      officeRefreshToken: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 全量获取file元信息的请求body
 */
export class ScanFileMetaRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  category?: string;
  driveId: string;
  imageCroppingAspectRatios?: string[];
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  limit?: number;
  marker?: string;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      category: 'category',
      driveId: 'drive_id',
      imageCroppingAspectRatios: 'image_cropping_aspect_ratios',
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      limit: 'limit',
      marker: 'marker',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      category: 'string',
      driveId: 'string',
      imageCroppingAspectRatios: { 'type': 'array', 'itemType': 'string' },
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      limit: 'number',
      marker: 'string',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 搜索文件元数据
 */
export class SearchFileRequest extends $tea.Model {
  headers?: { [key: string]: string };
  additionData?: {[key: string]: any};
  driveId: string;
  imageCroppingAspectRatios?: string[];
  imageThumbnailProcess?: string;
  imageUrlProcess?: string;
  limit?: number;
  location?: string;
  marker?: string;
  orderBy?: string;
  query?: string;
  referer?: string;
  returnTotalCount?: boolean;
  signToken?: string;
  urlExpireSec?: number;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      additionData: 'addition_data',
      driveId: 'drive_id',
      imageCroppingAspectRatios: 'image_cropping_aspect_ratios',
      imageThumbnailProcess: 'image_thumbnail_process',
      imageUrlProcess: 'image_url_process',
      limit: 'limit',
      location: 'location',
      marker: 'marker',
      orderBy: 'order_by',
      query: 'query',
      referer: 'referer',
      returnTotalCount: 'return_total_count',
      signToken: 'sign_token',
      urlExpireSec: 'url_expire_sec',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      additionData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      driveId: 'string',
      imageCroppingAspectRatios: { 'type': 'array', 'itemType': 'string' },
      imageThumbnailProcess: 'string',
      imageUrlProcess: 'string',
      limit: 'number',
      location: 'string',
      marker: 'string',
      orderBy: 'string',
      query: 'string',
      referer: 'string',
      returnTotalCount: 'boolean',
      signToken: 'string',
      urlExpireSec: 'number',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * UCGetObjectInfoByObjectKeyRequest
 */
export class UCGetObjectInfoByObjectKeyRequest extends $tea.Model {
  objectKey?: string;
  static names(): { [key: string]: string } {
    return {
      objectKey: 'object_key',
    };
  }

  static types(): { [key: string]: any } {
    return {
      objectKey: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * UCGetObjectInfoBySha1Request
 */
export class UCGetObjectInfoBySha1Request extends $tea.Model {
  sha1?: string;
  static names(): { [key: string]: string } {
    return {
      sha1: 'sha1',
    };
  }

  static types(): { [key: string]: any } {
    return {
      sha1: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Update drive request
 */
export class UpdateDriveRequest extends $tea.Model {
  headers?: { [key: string]: string };
  description?: string;
  driveId: string;
  driveName?: string;
  encryptDataAccess?: boolean;
  encryptMode?: string;
  status?: string;
  totalSize?: number;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      description: 'description',
      driveId: 'drive_id',
      driveName: 'drive_name',
      encryptDataAccess: 'encrypt_data_access',
      encryptMode: 'encrypt_mode',
      status: 'status',
      totalSize: 'total_size',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      description: 'string',
      driveId: 'string',
      driveName: 'string',
      encryptDataAccess: 'boolean',
      encryptMode: 'string',
      status: 'string',
      totalSize: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 更新文件元数据
 */
export class UpdateFileMetaRequest extends $tea.Model {
  headers?: { [key: string]: string };
  checkNameMode?: string;
  customIndexKey?: string;
  description?: string;
  driveId: string;
  encryptMode?: string;
  fileId: string;
  fileIdPath?: string;
  hidden?: boolean;
  labels?: string[];
  meta?: string;
  name?: string;
  referer?: string;
  shareId?: string;
  signToken?: string;
  starred?: boolean;
  userMeta?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      checkNameMode: 'check_name_mode',
      customIndexKey: 'custom_index_key',
      description: 'description',
      driveId: 'drive_id',
      encryptMode: 'encrypt_mode',
      fileId: 'file_id',
      fileIdPath: 'file_id_path',
      hidden: 'hidden',
      labels: 'labels',
      meta: 'meta',
      name: 'name',
      referer: 'referer',
      shareId: 'share_id',
      signToken: 'sign_token',
      starred: 'starred',
      userMeta: 'user_meta',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      checkNameMode: 'string',
      customIndexKey: 'string',
      description: 'string',
      driveId: 'string',
      encryptMode: 'string',
      fileId: 'string',
      fileIdPath: 'string',
      hidden: 'boolean',
      labels: { 'type': 'array', 'itemType': 'string' },
      meta: 'string',
      name: 'string',
      referer: 'string',
      shareId: 'string',
      signToken: 'string',
      starred: 'boolean',
      userMeta: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * update share request
 */
export class UpdateShareRequest extends $tea.Model {
  headers?: { [key: string]: string };
  description?: string;
  expiration?: string;
  permissions?: string[];
  shareId: string;
  shareName?: string;
  sharePolicy?: SharePermissionPolicy[];
  status?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      description: 'description',
      expiration: 'expiration',
      permissions: 'permissions',
      shareId: 'share_id',
      shareName: 'share_name',
      sharePolicy: 'share_policy',
      status: 'status',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      description: 'string',
      expiration: 'string',
      permissions: { 'type': 'array', 'itemType': 'string' },
      shareId: 'string',
      shareName: 'string',
      sharePolicy: { 'type': 'array', 'itemType': SharePermissionPolicy },
      status: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class VideoMediaMetadata extends $tea.Model {
  duration?: string;
  static names(): { [key: string]: string } {
    return {
      duration: 'duration',
    };
  }

  static types(): { [key: string]: any } {
    return {
      duration: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class CreateUserModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: CreateUserResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: CreateUserResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class DeleteUserModel extends $tea.Model {
  headers?: { [key: string]: string };
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetUserModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetUserResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetUserResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListUsersModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListUserResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListUserResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class SearchUserModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListUserResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListUserResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class UpdateUserModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: UpdateUserResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: UpdateUserResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Base user response
 */
export class BaseUserResponse extends $tea.Model {
  avatar?: string;
  createdAt?: number;
  defaultDriveId?: string;
  description?: string;
  domainId?: string;
  email?: string;
  nickName?: string;
  phone?: string;
  role?: string;
  status?: string;
  updatedAt?: number;
  userData?: {[key: string]: any};
  userId?: string;
  userName?: string;
  static names(): { [key: string]: string } {
    return {
      avatar: 'avatar',
      createdAt: 'created_at',
      defaultDriveId: 'default_drive_id',
      description: 'description',
      domainId: 'domain_id',
      email: 'email',
      nickName: 'nick_name',
      phone: 'phone',
      role: 'role',
      status: 'status',
      updatedAt: 'updated_at',
      userData: 'user_data',
      userId: 'user_id',
      userName: 'user_name',
    };
  }

  static types(): { [key: string]: any } {
    return {
      avatar: 'string',
      createdAt: 'number',
      defaultDriveId: 'string',
      description: 'string',
      domainId: 'string',
      email: 'string',
      nickName: 'string',
      phone: 'string',
      role: 'string',
      status: 'string',
      updatedAt: 'number',
      userData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      userId: 'string',
      userName: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Create user request
 */
export class CreateUserRequest extends $tea.Model {
  headers?: { [key: string]: string };
  avatar?: string;
  description?: string;
  email?: string;
  location?: string;
  nickName?: string;
  phone?: string;
  role?: string;
  status?: string;
  userData?: {[key: string]: any};
  userId: string;
  userName?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      avatar: 'avatar',
      description: 'description',
      email: 'email',
      location: 'location',
      nickName: 'nick_name',
      phone: 'phone',
      role: 'role',
      status: 'status',
      userData: 'user_data',
      userId: 'user_id',
      userName: 'user_name',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      avatar: 'string',
      description: 'string',
      email: 'string',
      location: 'string',
      nickName: 'string',
      phone: 'string',
      role: 'string',
      status: 'string',
      userData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      userId: 'string',
      userName: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Create user response
 */
export class CreateUserResponse extends $tea.Model {
  avatar?: string;
  createdAt?: number;
  defaultDriveId?: string;
  description?: string;
  domainId?: string;
  email?: string;
  nickName?: string;
  phone?: string;
  role?: string;
  status?: string;
  updatedAt?: number;
  userData?: {[key: string]: any};
  userId?: string;
  userName?: string;
  static names(): { [key: string]: string } {
    return {
      avatar: 'avatar',
      createdAt: 'created_at',
      defaultDriveId: 'default_drive_id',
      description: 'description',
      domainId: 'domain_id',
      email: 'email',
      nickName: 'nick_name',
      phone: 'phone',
      role: 'role',
      status: 'status',
      updatedAt: 'updated_at',
      userData: 'user_data',
      userId: 'user_id',
      userName: 'user_name',
    };
  }

  static types(): { [key: string]: any } {
    return {
      avatar: 'string',
      createdAt: 'number',
      defaultDriveId: 'string',
      description: 'string',
      domainId: 'string',
      email: 'string',
      nickName: 'string',
      phone: 'string',
      role: 'string',
      status: 'string',
      updatedAt: 'number',
      userData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      userId: 'string',
      userName: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Delete user request
 */
export class DeleteUserRequest extends $tea.Model {
  headers?: { [key: string]: string };
  userId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      userId: 'user_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      userId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Delete user response
 */
export class DeleteUserResponse extends $tea.Model {
  static names(): { [key: string]: string } {
    return {
    };
  }

  static types(): { [key: string]: any } {
    return {
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Get user request
 */
export class GetUserRequest extends $tea.Model {
  headers?: { [key: string]: string };
  userId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      userId: 'user_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      userId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Get user response
 */
export class GetUserResponse extends $tea.Model {
  avatar?: string;
  createdAt?: number;
  defaultDriveId?: string;
  description?: string;
  domainId?: string;
  email?: string;
  nickName?: string;
  phone?: string;
  role?: string;
  status?: string;
  updatedAt?: number;
  userData?: {[key: string]: any};
  userId?: string;
  userName?: string;
  static names(): { [key: string]: string } {
    return {
      avatar: 'avatar',
      createdAt: 'created_at',
      defaultDriveId: 'default_drive_id',
      description: 'description',
      domainId: 'domain_id',
      email: 'email',
      nickName: 'nick_name',
      phone: 'phone',
      role: 'role',
      status: 'status',
      updatedAt: 'updated_at',
      userData: 'user_data',
      userId: 'user_id',
      userName: 'user_name',
    };
  }

  static types(): { [key: string]: any } {
    return {
      avatar: 'string',
      createdAt: 'number',
      defaultDriveId: 'string',
      description: 'string',
      domainId: 'string',
      email: 'string',
      nickName: 'string',
      phone: 'string',
      role: 'string',
      status: 'string',
      updatedAt: 'number',
      userData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      userId: 'string',
      userName: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List user request
 */
export class ListUserRequest extends $tea.Model {
  headers?: { [key: string]: string };
  limit?: number;
  marker?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      limit: 'limit',
      marker: 'marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      limit: 'number',
      marker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List user response
 */
export class ListUserResponse extends $tea.Model {
  items?: BaseUserResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': BaseUserResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Search user request
 */
export class SearchUserRequest extends $tea.Model {
  headers?: { [key: string]: string };
  email?: string;
  limit?: number;
  marker?: string;
  nickName?: string;
  phone?: string;
  role?: string;
  status?: string;
  userName?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      email: 'email',
      limit: 'limit',
      marker: 'marker',
      nickName: 'nick_name',
      phone: 'phone',
      role: 'role',
      status: 'status',
      userName: 'user_name',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      email: 'string',
      limit: 'number',
      marker: 'string',
      nickName: 'string',
      phone: 'string',
      role: 'string',
      status: 'string',
      userName: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Update user request
 */
export class UpdateUserRequest extends $tea.Model {
  headers?: { [key: string]: string };
  avatar?: string;
  description?: string;
  email?: string;
  nickName?: string;
  phone?: string;
  role?: string;
  status?: string;
  userData?: {[key: string]: any};
  userId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      avatar: 'avatar',
      description: 'description',
      email: 'email',
      nickName: 'nick_name',
      phone: 'phone',
      role: 'role',
      status: 'status',
      userData: 'user_data',
      userId: 'user_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      avatar: 'string',
      description: 'string',
      email: 'string',
      nickName: 'string',
      phone: 'string',
      role: 'string',
      status: 'string',
      userData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      userId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Update user response
 */
export class UpdateUserResponse extends $tea.Model {
  avatar?: string;
  createdAt?: number;
  defaultDriveId?: string;
  description?: string;
  domainId?: string;
  email?: string;
  nickName?: string;
  phone?: string;
  role?: string;
  status?: string;
  updatedAt?: number;
  userData?: {[key: string]: any};
  userId?: string;
  userName?: string;
  static names(): { [key: string]: string } {
    return {
      avatar: 'avatar',
      createdAt: 'created_at',
      defaultDriveId: 'default_drive_id',
      description: 'description',
      domainId: 'domain_id',
      email: 'email',
      nickName: 'nick_name',
      phone: 'phone',
      role: 'role',
      status: 'status',
      updatedAt: 'updated_at',
      userData: 'user_data',
      userId: 'user_id',
      userName: 'user_name',
    };
  }

  static types(): { [key: string]: any } {
    return {
      avatar: 'string',
      createdAt: 'number',
      defaultDriveId: 'string',
      description: 'string',
      domainId: 'string',
      email: 'string',
      nickName: 'string',
      phone: 'string',
      role: 'string',
      status: 'string',
      updatedAt: 'number',
      userData: { 'type': 'map', 'keyType': 'string', 'valueType': 'any' },
      userId: 'string',
      userName: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class CreateStoryModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: CreateStoryResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: CreateStoryResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetPhotoCountModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetImageCountResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetImageCountResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class GetStoryDetailModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: GetStoryDetailResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: GetStoryDetailResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListAddressGroupsModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListImageAddressGroupsResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListImageAddressGroupsResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListFacegroupsModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListImageFaceGroupsResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListImageFaceGroupsResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListStoryModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListStoryResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListStoryResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ListTagsModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ListImageTagsResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ListImageTagsResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class ParseKeywordsModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: ParseKeywordsResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: ParseKeywordsResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class RemoveStoryImagesModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: RemoveStoryImagesResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: RemoveStoryImagesResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class SearchAddressGroupsModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: SearchImageAddressGroupsResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: SearchImageAddressGroupsResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

export class UpdateFacegroupInfoModel extends $tea.Model {
  headers?: { [key: string]: string };
  body: UpdateFaceGroupInfoResponse;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      body: 'body',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      body: UpdateFaceGroupInfoResponse,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class Address extends $tea.Model {
  city?: string;
  country?: string;
  district?: string;
  province?: string;
  township?: string;
  static names(): { [key: string]: string } {
    return {
      city: 'city',
      country: 'country',
      district: 'district',
      province: 'province',
      township: 'township',
    };
  }

  static types(): { [key: string]: any } {
    return {
      city: 'string',
      country: 'string',
      district: 'string',
      province: 'string',
      township: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Create story request
 */
export class CreateStoryRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 生成故事
 */
export class CreateStoryResponse extends $tea.Model {
  driveId?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Get photo count request
 */
export class GetImageCountRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 获取云照片个数结果
 */
export class GetImageCountResponse extends $tea.Model {
  imageCount?: number;
  static names(): { [key: string]: string } {
    return {
      imageCount: 'image_count',
    };
  }

  static types(): { [key: string]: any } {
    return {
      imageCount: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Get story detail request
 */
export class GetStoryDetailRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  storyId: string;
  videoUrlExpireSec?: number;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
      storyId: 'story_id',
      videoUrlExpireSec: 'video_url_expire_sec',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
      storyId: 'string',
      videoUrlExpireSec: 'number',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 故事详情
 */
export class GetStoryDetailResponse extends $tea.Model {
  coverFileId?: string;
  createdAt?: string;
  items?: BaseCCPFileResponse[];
  score?: number;
  storyId?: string;
  storyImagesDateRange?: number[];
  subTitle?: string;
  title?: string;
  updatedAt?: string;
  videoStatus?: string;
  videoUrl?: string;
  static names(): { [key: string]: string } {
    return {
      coverFileId: 'cover_file_id',
      createdAt: 'created_at',
      items: 'items',
      score: 'score',
      storyId: 'story_id',
      storyImagesDateRange: 'story_images_date_range',
      subTitle: 'sub_title',
      title: 'title',
      updatedAt: 'updated_at',
      videoStatus: 'video_status',
      videoUrl: 'video_url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      coverFileId: 'string',
      createdAt: 'string',
      items: { 'type': 'array', 'itemType': BaseCCPFileResponse },
      score: 'number',
      storyId: 'string',
      storyImagesDateRange: { 'type': 'array', 'itemType': 'number' },
      subTitle: 'string',
      title: 'string',
      updatedAt: 'string',
      videoStatus: 'string',
      videoUrl: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class ImageAddressResponse extends $tea.Model {
  addressDetail?: Address;
  count?: number;
  coverFileId?: string;
  coverUrl?: string;
  location?: string;
  name?: string;
  static names(): { [key: string]: string } {
    return {
      addressDetail: 'address_detail',
      count: 'count',
      coverFileId: 'cover_file_id',
      coverUrl: 'cover_url',
      location: 'location',
      name: 'name',
    };
  }

  static types(): { [key: string]: any } {
    return {
      addressDetail: Address,
      count: 'number',
      coverFileId: 'string',
      coverUrl: 'string',
      location: 'string',
      name: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class ImageFaceGroupResponse extends $tea.Model {
  coverFileId?: string;
  createdAt?: string;
  faceCount?: number;
  groupCoverUrl?: string;
  groupId?: string;
  groupName?: string;
  imageCount?: number;
  updatedAt?: string;
  static names(): { [key: string]: string } {
    return {
      coverFileId: 'cover_file_id',
      createdAt: 'created_at',
      faceCount: 'face_count',
      groupCoverUrl: 'group_cover_url',
      groupId: 'group_id',
      groupName: 'group_name',
      imageCount: 'image_count',
      updatedAt: 'updated_at',
    };
  }

  static types(): { [key: string]: any } {
    return {
      coverFileId: 'string',
      createdAt: 'string',
      faceCount: 'number',
      groupCoverUrl: 'string',
      groupId: 'string',
      groupName: 'string',
      imageCount: 'number',
      updatedAt: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class ImageTagResponse extends $tea.Model {
  count?: number;
  coverFileId?: string;
  coverUrl?: string;
  name?: string;
  static names(): { [key: string]: string } {
    return {
      count: 'count',
      coverFileId: 'cover_file_id',
      coverUrl: 'cover_url',
      name: 'name',
    };
  }

  static types(): { [key: string]: any } {
    return {
      count: 'number',
      coverFileId: 'string',
      coverUrl: 'string',
      name: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List image address groups request
 */
export class ListImageAddressGroupsRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  imageThumbnailProcess?: string;
  limit?: number;
  marker?: string;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
      imageThumbnailProcess: 'image_thumbnail_process',
      limit: 'limit',
      marker: 'marker',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
      imageThumbnailProcess: 'string',
      limit: 'number',
      marker: 'string',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 展示地点分组集合
 */
export class ListImageAddressGroupsResponse extends $tea.Model {
  items?: ImageAddressResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': ImageAddressResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List image face groups request
 */
export class ListImageFaceGroupsRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  limit?: number;
  marker?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
      limit: 'limit',
      marker: 'marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
      limit: 'number',
      marker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 展示人脸分组集合
 */
export class ListImageFaceGroupsResponse extends $tea.Model {
  items?: ImageFaceGroupResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': ImageFaceGroupResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List image tags request
 */
export class ListImageTagsRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  imageThumbnailProcess?: string;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
      imageThumbnailProcess: 'image_thumbnail_process',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
      imageThumbnailProcess: 'string',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 展示标签集合
 */
export class ListImageTagsResponse extends $tea.Model {
  tags?: ImageTagResponse[];
  static names(): { [key: string]: string } {
    return {
      tags: 'tags',
    };
  }

  static types(): { [key: string]: any } {
    return {
      tags: { 'type': 'array', 'itemType': ImageTagResponse },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * List story request
 */
export class ListStoryRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  limit?: number;
  marker?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
      limit: 'limit',
      marker: 'marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
      limit: 'number',
      marker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 故事列表
 */
export class ListStoryResponse extends $tea.Model {
  items?: StoryResponse[];
  nextMarker?: string;
  static names(): { [key: string]: string } {
    return {
      items: 'items',
      nextMarker: 'next_marker',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': StoryResponse },
      nextMarker: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Parse keywords request
 */
export class ParseKeywordsRequest extends $tea.Model {
  headers?: { [key: string]: string };
  keywords?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      keywords: 'keywords',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      keywords: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Parse keywords response
 */
export class ParseKeywordsResponse extends $tea.Model {
  addressLine?: string;
  tags?: SystemTag[];
  timeRange?: TimeRange;
  static names(): { [key: string]: string } {
    return {
      addressLine: 'address_line',
      tags: 'tags',
      timeRange: 'time_range',
    };
  }

  static types(): { [key: string]: any } {
    return {
      addressLine: 'string',
      tags: { 'type': 'array', 'itemType': SystemTag },
      timeRange: TimeRange,
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Remove story images request
 */
export class RemoveStoryImagesRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId?: string;
  fileIds?: string[];
  storyId?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
      fileIds: 'file_ids',
      storyId: 'story_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
      fileIds: { 'type': 'array', 'itemType': 'string' },
      storyId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Remove story images response
 */
export class RemoveStoryImagesResponse extends $tea.Model {
  driveId?: string;
  fileIds?: string[];
  results?: RemoveStoryImagesResultItem[];
  storyId?: string;
  successFileIds?: string[];
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      fileIds: 'file_ids',
      results: 'results',
      storyId: 'story_id',
      successFileIds: 'success_file_ids',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      fileIds: { 'type': 'array', 'itemType': 'string' },
      results: { 'type': 'array', 'itemType': RemoveStoryImagesResultItem },
      storyId: 'string',
      successFileIds: { 'type': 'array', 'itemType': 'string' },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class RemoveStoryImagesResultItem extends $tea.Model {
  code?: string;
  fileId?: string;
  isSucceed?: boolean;
  message?: string;
  static names(): { [key: string]: string } {
    return {
      code: 'code',
      fileId: 'file_id',
      isSucceed: 'is_succeed',
      message: 'message',
    };
  }

  static types(): { [key: string]: any } {
    return {
      code: 'string',
      fileId: 'string',
      isSucceed: 'boolean',
      message: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Search image address groups request
 */
export class SearchImageAddressGroupsRequest extends $tea.Model {
  headers?: { [key: string]: string };
  addressLevel?: string;
  addressNames?: string[];
  brGeoPoint?: string;
  driveId: string;
  imageThumbnailProcess?: string;
  tlGeoPoint?: string;
  videoThumbnailProcess?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      addressLevel: 'address_level',
      addressNames: 'address_names',
      brGeoPoint: 'br_geo_point',
      driveId: 'drive_id',
      imageThumbnailProcess: 'image_thumbnail_process',
      tlGeoPoint: 'tl_geo_point',
      videoThumbnailProcess: 'video_thumbnail_process',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      addressLevel: 'string',
      addressNames: { 'type': 'array', 'itemType': 'string' },
      brGeoPoint: 'string',
      driveId: 'string',
      imageThumbnailProcess: 'string',
      tlGeoPoint: 'string',
      videoThumbnailProcess: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 展示地点分组列表
 */
export class SearchImageAddressGroupsResponse extends $tea.Model {
  items?: ImageAddressResponse[];
  static names(): { [key: string]: string } {
    return {
      items: 'items',
    };
  }

  static types(): { [key: string]: any } {
    return {
      items: { 'type': 'array', 'itemType': ImageAddressResponse },
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class StoryResponse extends $tea.Model {
  coverFileId?: string;
  createdAt?: string;
  score?: number;
  storyId?: string;
  storyImagesDateRange?: number[];
  subTitle?: string;
  title?: string;
  updatedAt?: string;
  videoStatus?: string;
  videoUrl?: string;
  static names(): { [key: string]: string } {
    return {
      coverFileId: 'cover_file_id',
      createdAt: 'created_at',
      score: 'score',
      storyId: 'story_id',
      storyImagesDateRange: 'story_images_date_range',
      subTitle: 'sub_title',
      title: 'title',
      updatedAt: 'updated_at',
      videoStatus: 'video_status',
      videoUrl: 'video_url',
    };
  }

  static types(): { [key: string]: any } {
    return {
      coverFileId: 'string',
      createdAt: 'string',
      score: 'number',
      storyId: 'string',
      storyImagesDateRange: { 'type': 'array', 'itemType': 'number' },
      subTitle: 'string',
      title: 'string',
      updatedAt: 'string',
      videoStatus: 'string',
      videoUrl: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 
 */
export class TimeRange extends $tea.Model {
  end?: string;
  start?: string;
  static names(): { [key: string]: string } {
    return {
      end: 'end',
      start: 'start',
    };
  }

  static types(): { [key: string]: any } {
    return {
      end: 'string',
      start: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * Update face group info request
 */
export class UpdateFaceGroupInfoRequest extends $tea.Model {
  headers?: { [key: string]: string };
  driveId: string;
  groupId: string;
  groupName?: string;
  static names(): { [key: string]: string } {
    return {
      headers: 'headers',
      driveId: 'drive_id',
      groupId: 'group_id',
      groupName: 'group_name',
    };
  }

  static types(): { [key: string]: any } {
    return {
      headers: { 'type': 'map', 'keyType': 'string', 'valueType': 'string' },
      driveId: 'string',
      groupId: 'string',
      groupName: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}

/**
 * 更新人脸分组信息结果
 */
export class UpdateFaceGroupInfoResponse extends $tea.Model {
  driveId?: string;
  groupId?: string;
  static names(): { [key: string]: string } {
    return {
      driveId: 'drive_id',
      groupId: 'group_id',
    };
  }

  static types(): { [key: string]: any } {
    return {
      driveId: 'string',
      groupId: 'string',
    };
  }

  constructor(map?: { [key: string]: any }) {
    super(map);
  }
}


export default class Client {
  _domainId: string;
  _accessTokenCredential: AccessTokenCredential;
  _endpoint: string;
  _protocol: string;
  _nickname: string;
  _userAgent: string;
  _credential: Credential;

  constructor(config: Config) {
    if (Util.isUnset($tea.toMap(config))) {
      throw $tea.newError({
        name: "ParameterMissing",
        message: "'config' can not be unset",
      });
    }

    Util.validateModel(config);
    if (!Util.empty(config.accessToken) || !Util.empty(config.refreshToken)) {
      let accessConfig = new $AccessTokenCredential.Config({
        accessToken: config.accessToken,
        endpoint: config.endpoint,
        domainId: config.domainId,
        clientId: config.clientId,
        refreshToken: config.refreshToken,
        clientSecret: config.clientSecret,
        expireTime: config.expireTime,
      });
      this._accessTokenCredential = new AccessTokenCredential(accessConfig);
    }

    if (!Util.empty(config.accessKeyId)) {
      if (Util.empty(config.type)) {
        config.type = "access_key";
      }

      let credentialConfig = new $Credential.Config({
        accessKeyId: config.accessKeyId,
        type: config.type,
        accessKeySecret: config.accessKeySecret,
        securityToken: config.securityToken,
      });
      this._credential = new Credential(credentialConfig);
    }

    this._endpoint = config.endpoint;
    this._protocol = config.protocol;
    this._userAgent = config.userAgent;
    this._nickname = config.nickname;
    this._domainId = config.domainId;
  }

  /**
   * 取消绑定关系，生成新用户，返回访问令牌
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async cancelLinkEx(request: CancelLinkRequest, runtime: RuntimeOptions): Promise<CancelLinkModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/cancel_link`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<CancelLinkModel>({
            body: respMap,
            headers: response_.headers,
          }, new CancelLinkModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async confirmLinkEx(request: ConfirmLinkRequest, runtime: RuntimeOptions): Promise<ConfirmLinkModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/confirm_link`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ConfirmLinkModel>({
            body: respMap,
            headers: response_.headers,
          }, new ConfirmLinkModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 修改手机登录密码，密码必须包含数字和字母，长度8-20个字符
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async changePasswordEx(request: DefaultChangePasswordRequest, runtime: RuntimeOptions): Promise<ChangePasswordModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/default/change_password`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ChangePasswordModel>({
            body: respMap,
            headers: response_.headers,
          }, new ChangePasswordModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 设置手机登录密码，密码必须包含数字和字母，长度8-20个字符
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async setPasswordEx(request: DefaultSetPasswordRequest, runtime: RuntimeOptions): Promise<SetPasswordModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/default/set_password`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 204)) {
          return $tea.cast<SetPasswordModel>({
            headers: response_.headers,
          }, new SetPasswordModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 校验手机短信验证码，用于重置密码时校验手机，通过校验后返回state，可通过state重新设置密码
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async verifyCodeEx(request: VerifyCodeRequest, runtime: RuntimeOptions): Promise<VerifyCodeModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/default/verify_code`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<VerifyCodeModel>({
            body: respMap,
            headers: response_.headers,
          }, new VerifyCodeModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 管理员通过账号信息直接获取用户的访问令牌
   * @tags account
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async getAccessTokenByLinkInfoEx(request: GetAccessTokenByLinkInfoRequest, runtime: RuntimeOptions): Promise<GetAccessTokenByLinkInfoModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/get_access_token_by_link_info`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetAccessTokenByLinkInfoModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetAccessTokenByLinkInfoModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取图片验证码，用于人机校验，默认不需要
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async getCaptchaEx(request: GetCaptchaRequest, runtime: RuntimeOptions): Promise<GetCaptchaModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/get_captcha`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetCaptchaModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetCaptchaModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取用户认证方式详情
   * @tags account
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async getLinkInfoEx(request: GetByLinkInfoRequest, runtime: RuntimeOptions): Promise<GetLinkInfoModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/get_link_info`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetLinkInfoModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetLinkInfoModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取用户的所有绑定信息
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async getLinkInfoByUserIdEx(request: GetLinkInfoByUserIDRequest, runtime: RuntimeOptions): Promise<GetLinkInfoByUserIdModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/get_link_info_by_user_id`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetLinkInfoByUserIdModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetLinkInfoByUserIdModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取公钥，用于加密对称密钥
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async getPublicKeyEx(request: GetPublicKeyRequest, runtime: RuntimeOptions): Promise<GetPublicKeyModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/get_public_key`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetPublicKeyModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetPublicKeyModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async linkEx(request: AccountLinkRequest, runtime: RuntimeOptions): Promise<LinkModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/link`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<LinkModel>({
            body: respMap,
            headers: response_.headers,
          }, new LinkModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 查询手机号是否已被注册
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async checkExistEx(request: MobileCheckExistRequest, runtime: RuntimeOptions): Promise<CheckExistModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/mobile/check_exist`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<CheckExistModel>({
            body: respMap,
            headers: response_.headers,
          }, new CheckExistModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 通过手机号+短信或密码登录，返回刷新令牌和访问令牌
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async loginEx(request: MobileLoginRequest, runtime: RuntimeOptions): Promise<LoginModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/mobile/login`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<LoginModel>({
            body: respMap,
            headers: response_.headers,
          }, new LoginModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async registerEx(request: MobileRegisterRequest, runtime: RuntimeOptions): Promise<RegisterModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/mobile/register`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<RegisterModel>({
            body: respMap,
            headers: response_.headers,
          }, new RegisterModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 发送短信验证码，用于登录、注册、修改密码、绑定等
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async mobileSendSmsCodeEx(request: MobileSendSmsCodeRequest, runtime: RuntimeOptions): Promise<MobileSendSmsCodeModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/mobile/send_sms_code`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<MobileSendSmsCodeModel>({
            body: respMap,
            headers: response_.headers,
          }, new MobileSendSmsCodeModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 用户退出登录
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async accountRevokeEx(request: RevokeRequest, runtime: RuntimeOptions): Promise<AccountRevokeModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/revoke`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 204)) {
          return $tea.cast<AccountRevokeModel>({
            headers: response_.headers,
          }, new AccountRevokeModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 用户通过刷新令牌（refresh_token）获取访问令牌（access_token）
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async accountTokenEx(request: AccountTokenRequest, runtime: RuntimeOptions): Promise<AccountTokenModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/account/token`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.auth.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<AccountTokenModel>({
            body: respMap,
            headers: response_.headers,
          }, new AccountTokenModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 列举Store列表
   * @tags admin
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async adminListStoresEx(request: AdminListStoresRequest, runtime: RuntimeOptions): Promise<AdminListStoresModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/domain/list_stores`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<AdminListStoresModel>({
            body: respMap,
            headers: response_.headers,
          }, new AdminListStoresModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async getUserAccessTokenEx(request: GetUserAccessTokenRequest, runtime: RuntimeOptions): Promise<GetUserAccessTokenModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/user/get_access_token`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetUserAccessTokenModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetUserAccessTokenModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 如果目录拷贝、目录删除不能在限定时间内完成，将访问一个异步任务id，
   * 通过此接口获取异步任务的信息，以确定任务是否执行成功。
   * @tags async_task
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getAsyncTaskInfoEx(request: GetAsyncTaskRequest, runtime: RuntimeOptions): Promise<GetAsyncTaskInfoModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/async_task/get`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetAsyncTaskInfoModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetAsyncTaskInfoModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 对多个原子操作封装成一个批处理请求，服务端并行处理并打包返回每个操作的执行结果。
   * 支持对文件和文件夹的移动、删除、修改，每个批处理请求最多包含100个原则操作。
   * @tags batch
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async batchOperationEx(request: BatchRequest, runtime: RuntimeOptions): Promise<BatchOperationModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/batch`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<BatchOperationModel>({
            body: respMap,
            headers: response_.headers,
          }, new BatchOperationModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async createDriveEx(request: CreateDriveRequest, runtime: RuntimeOptions): Promise<CreateDriveModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/drive/create`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 201)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<CreateDriveModel>({
            body: respMap,
            headers: response_.headers,
          }, new CreateDriveModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async deleteDriveEx(request: DeleteDriveRequest, runtime: RuntimeOptions): Promise<DeleteDriveModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/drive/delete`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 204)) {
          return $tea.cast<DeleteDriveModel>({
            headers: response_.headers,
          }, new DeleteDriveModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async getDriveEx(request: GetDriveRequest, runtime: RuntimeOptions): Promise<GetDriveModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/drive/get`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetDriveModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetDriveModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async getDefaultDriveEx(request: GetDefaultDriveRequest, runtime: RuntimeOptions): Promise<GetDefaultDriveModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/drive/get_default_drive`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetDefaultDriveModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetDefaultDriveModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async listDrivesEx(request: ListDriveRequest, runtime: RuntimeOptions): Promise<ListDrivesModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/drive/list`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListDrivesModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListDrivesModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async listMyDrivesEx(request: ListMyDriveRequest, runtime: RuntimeOptions): Promise<ListMyDrivesModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/drive/list_my_drives`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListMyDrivesModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListMyDrivesModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async updateDriveEx(request: UpdateDriveRequest, runtime: RuntimeOptions): Promise<UpdateDriveModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/drive/update`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<UpdateDriveModel>({
            body: respMap,
            headers: response_.headers,
          }, new UpdateDriveModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 完成文件上传。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async completeFileEx(request: CompleteFileRequest, runtime: RuntimeOptions): Promise<CompleteFileModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/complete`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<CompleteFileModel>({
            body: respMap,
            headers: response_.headers,
          }, new CompleteFileModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 指定源文件或文件夹，拷贝到指定的文件夹。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async copyFileEx(request: CopyFileRequest, runtime: RuntimeOptions): Promise<CopyFileModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/copy`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 201)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<CopyFileModel>({
            body: respMap,
            headers: response_.headers,
          }, new CopyFileModel({}));
        }

        if (Util.equalNumber(response_.statusCode, 202)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<CopyFileModel>({
            body: respMap,
            headers: response_.headers,
          }, new CopyFileModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 在指定文件夹下创建文件或者文件夹，
   * 根文件夹用root表示，其他文件夹使用创建文件夹时返回的file_id。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error AlreadyExist {resource} has already exists. {extra_msg}
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async createFileEx(request: CreateFileRequest, runtime: RuntimeOptions): Promise<CreateFileModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/create`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 201)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<CreateFileModel>({
            body: respMap,
            headers: response_.headers,
          }, new CreateFileModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 指定文件或文件夹ID，删除文件或者文件夹。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async deleteFileEx(request: DeleteFileRequest, runtime: RuntimeOptions): Promise<DeleteFileModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/delete`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 202)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<DeleteFileModel>({
            body: respMap,
            headers: response_.headers,
          }, new DeleteFileModel({}));
        }

        if (Util.equalNumber(response_.statusCode, 204)) {
          return $tea.cast<DeleteFileModel>({
            headers: response_.headers,
          }, new DeleteFileModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取指定文件或文件夹ID的信息。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getFileEx(request: GetFileRequest, runtime: RuntimeOptions): Promise<GetFileModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/get`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetFileModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetFileModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 根据路径获取指定文件或文件夹的信息。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getFileByPathEx(request: GetFileByPathRequest, runtime: RuntimeOptions): Promise<GetFileByPathModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/get_by_path`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetFileByPathModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetFileByPathModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取文件的下载地址，调用者可自己设置range头并发下载。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getDownloadUrlEx(request: GetDownloadUrlRequest, runtime: RuntimeOptions): Promise<GetDownloadUrlModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/get_download_url`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetDownloadUrlModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetDownloadUrlModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取drive内，增量数据最新的游标
   * @tags file_delta
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getLastCursorEx(request: GetLastCursorRequest, runtime: RuntimeOptions): Promise<GetLastCursorModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/get_last_cursor`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetLastCursorModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetLastCursorModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取media文件播放URL地址（当前仅支持m3u8）
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getMediaPlayUrlEx(request: GetMediaPlayURLRequest, runtime: RuntimeOptions): Promise<GetMediaPlayUrlModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/get_media_play_url`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetMediaPlayUrlModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetMediaPlayUrlModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取文档的在线编辑地址
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getOfficeEditUrlEx(request: GetOfficeEditUrlRequest, runtime: RuntimeOptions): Promise<GetOfficeEditUrlModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/get_office_edit_url`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetOfficeEditUrlModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetOfficeEditUrlModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取文档的预览地址（office文档）
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getOfficePreviewUrlEx(request: GetOfficePreviewUrlRequest, runtime: RuntimeOptions): Promise<GetOfficePreviewUrlModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/get_office_preview_url`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetOfficePreviewUrlModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetOfficePreviewUrlModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async getUploadUrlEx(request: GetUploadUrlRequest, runtime: RuntimeOptions): Promise<GetUploadUrlModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/get_upload_url`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetUploadUrlModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetUploadUrlModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取视频雪碧图地址
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getVideoPreviewSpriteUrlEx(request: GetVideoPreviewSpriteURLRequest, runtime: RuntimeOptions): Promise<GetVideoPreviewSpriteUrlModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/get_video_preview_sprite_url`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetVideoPreviewSpriteUrlModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetVideoPreviewSpriteUrlModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取视频播放地址
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getVideoPreviewUrlEx(request: GetVideoPreviewURLRequest, runtime: RuntimeOptions): Promise<GetVideoPreviewUrlModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/get_video_preview_url`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetVideoPreviewUrlModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetVideoPreviewUrlModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 列举指定目录下的文件或文件夹。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listFileEx(request: ListFileRequest, runtime: RuntimeOptions): Promise<ListFileModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/list`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListFileModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListFileModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 查看分享中的文件列表
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error ShareLinkTokenInvalid ShareToken is invalid. {message}
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listFileByAnonymousEx(request: ListByAnonymousRequest, runtime: RuntimeOptions): Promise<ListFileByAnonymousModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/list_by_anonymous`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListFileByAnonymousModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListFileByAnonymousModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 根据自定义同步索引键列举文件或文件夹。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listFileByCustomIndexKeyEx(request: ListFileByCustomIndexKeyRequest, runtime: RuntimeOptions): Promise<ListFileByCustomIndexKeyModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/list_by_custom_index_key`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListFileByCustomIndexKeyModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListFileByCustomIndexKeyModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 获取drive内，增量数据列表
   * @tags file_delta
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listFileDeltaEx(request: ListFileDeltaRequest, runtime: RuntimeOptions): Promise<ListFileDeltaModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/list_delta`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListFileDeltaModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListFileDeltaModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 列举upload_id对应的已上传分片。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listUploadedPartsEx(request: ListUploadedPartRequest, runtime: RuntimeOptions): Promise<ListUploadedPartsModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/list_uploaded_parts`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListUploadedPartsModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListUploadedPartsModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 指定源文件或文件夹，移动到指定的文件夹。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async moveFileEx(request: MoveFileRequest, runtime: RuntimeOptions): Promise<MoveFileModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/move`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<MoveFileModel>({
            body: respMap,
            headers: response_.headers,
          }, new MoveFileModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 刷新在线编辑Token
   * @tags file, refresh, office, edit
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async tokenEx(request: RefreshOfficeEditTokenRequest, runtime: RuntimeOptions): Promise<TokenModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/refresh_office_edit_token`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<TokenModel>({
            body: respMap,
            headers: response_.headers,
          }, new TokenModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 在指定drive下全量获取文件元信息。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async scanFileMetaEx(request: ScanFileMetaRequest, runtime: RuntimeOptions): Promise<ScanFileMetaModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/scan`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ScanFileMetaModel>({
            body: respMap,
            headers: response_.headers,
          }, new ScanFileMetaModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 根据筛选条件，在指定drive下搜索文件。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async searchFileEx(request: SearchFileRequest, runtime: RuntimeOptions): Promise<SearchFileModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/search`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<SearchFileModel>({
            body: respMap,
            headers: response_.headers,
          }, new SearchFileModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 对指定的文件或文件夹更新信息。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error AlreadyExist {resource} has already exists. {extra_msg}
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async updateFileEx(request: UpdateFileMetaRequest, runtime: RuntimeOptions): Promise<UpdateFileModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/file/update`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<UpdateFileModel>({
            body: respMap,
            headers: response_.headers,
          }, new UpdateFileModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async createShareEx(request: CreateShareRequest, runtime: RuntimeOptions): Promise<CreateShareModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/share/create`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 201)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<CreateShareModel>({
            body: respMap,
            headers: response_.headers,
          }, new CreateShareModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async deleteShareEx(request: DeleteShareRequest, runtime: RuntimeOptions): Promise<DeleteShareModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/share/delete`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 204)) {
          return $tea.cast<DeleteShareModel>({
            headers: response_.headers,
          }, new DeleteShareModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async getShareEx(request: GetShareRequest, runtime: RuntimeOptions): Promise<GetShareModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/share/get`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetShareModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetShareModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async listShareEx(request: ListShareRequest, runtime: RuntimeOptions): Promise<ListShareModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/share/list`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListShareModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListShareModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async updateShareEx(request: UpdateShareRequest, runtime: RuntimeOptions): Promise<UpdateShareModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/share/update`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<UpdateShareModel>({
            body: respMap,
            headers: response_.headers,
          }, new UpdateShareModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 取消指定分享
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async cancelShareLinkEx(request: CancelShareLinkRequest, runtime: RuntimeOptions): Promise<CancelShareLinkModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/share_link/cancel`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 204)) {
          return $tea.cast<CancelShareLinkModel>({
            headers: response_.headers,
          }, new CancelShareLinkModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 创建分享。
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async createShareLinkEx(request: CreateShareLinkRequest, runtime: RuntimeOptions): Promise<CreateShareLinkModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/share_link/create`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 201)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<CreateShareLinkModel>({
            body: respMap,
            headers: response_.headers,
          }, new CreateShareLinkModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 查看分享的基本信息，比如分享者、到期时间等
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getShareByAnonymousEx(request: GetShareLinkByAnonymousRequest, runtime: RuntimeOptions): Promise<GetShareByAnonymousModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/share_link/get_by_anonymous`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetShareByAnonymousModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetShareByAnonymousModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 使用分享口令换取分享id
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getShareIdEx(request: GetShareLinkIDRequest, runtime: RuntimeOptions): Promise<GetShareIdModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/share_link/get_share_id`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetShareIdModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetShareIdModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 使用分享码+提取码换取分享token
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getShareTokenEx(request: GetShareLinkTokenRequest, runtime: RuntimeOptions): Promise<GetShareTokenModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/share_link/get_share_token`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetShareTokenModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetShareTokenModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 列举指定用户的分享
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listShareLinkEx(request: ListShareLinkRequest, runtime: RuntimeOptions): Promise<ListShareLinkModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/share_link/list`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListShareLinkModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListShareLinkModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async createUserEx(request: CreateUserRequest, runtime: RuntimeOptions): Promise<CreateUserModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/user/create`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 201)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<CreateUserModel>({
            body: respMap,
            headers: response_.headers,
          }, new CreateUserModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async deleteUserEx(request: DeleteUserRequest, runtime: RuntimeOptions): Promise<DeleteUserModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/user/delete`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 204)) {
          return $tea.cast<DeleteUserModel>({
            headers: response_.headers,
          }, new DeleteUserModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async getUserEx(request: GetUserRequest, runtime: RuntimeOptions): Promise<GetUserModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/user/get`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetUserModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetUserModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async listUsersEx(request: ListUserRequest, runtime: RuntimeOptions): Promise<ListUsersModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/user/list`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListUsersModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListUsersModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async searchUserEx(request: SearchUserRequest, runtime: RuntimeOptions): Promise<SearchUserModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/user/search`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<SearchUserModel>({
            body: respMap,
            headers: response_.headers,
          }, new SearchUserModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
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
  async updateUserEx(request: UpdateUserRequest, runtime: RuntimeOptions): Promise<UpdateUserModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/user/update`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<UpdateUserModel>({
            body: respMap,
            headers: response_.headers,
          }, new UpdateUserModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 该接口将会创建故事
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async createStoryEx(request: CreateStoryRequest, runtime: RuntimeOptions): Promise<CreateStoryModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/image/create_story`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<CreateStoryModel>({
            body: respMap,
            headers: response_.headers,
          }, new CreateStoryModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 该接口将返回用户Drive下的云照片个数
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getPhotoCountEx(request: GetImageCountRequest, runtime: RuntimeOptions): Promise<GetPhotoCountModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/image/get_photo_count`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetPhotoCountModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetPhotoCountModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 该接口将会获取故事详情
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getStoryDetailEx(request: GetStoryDetailRequest, runtime: RuntimeOptions): Promise<GetStoryDetailModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/image/get_story_detail`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<GetStoryDetailModel>({
            body: respMap,
            headers: response_.headers,
          }, new GetStoryDetailModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 该接口将会展示用户图片的地点分组
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listAddressGroupsEx(request: ListImageAddressGroupsRequest, runtime: RuntimeOptions): Promise<ListAddressGroupsModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/image/list_address_groups`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListAddressGroupsModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListAddressGroupsModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 该接口将会列举人脸分组
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listFacegroupsEx(request: ListImageFaceGroupsRequest, runtime: RuntimeOptions): Promise<ListFacegroupsModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/image/list_facegroups`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListFacegroupsModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListFacegroupsModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 该接口将会获取故事列表
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listStoryEx(request: ListStoryRequest, runtime: RuntimeOptions): Promise<ListStoryModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/image/list_story`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListStoryModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListStoryModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 该接口将会展示场景标记
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listTagsEx(request: ListImageTagsRequest, runtime: RuntimeOptions): Promise<ListTagsModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/image/list_tags`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ListTagsModel>({
            body: respMap,
            headers: response_.headers,
          }, new ListTagsModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 该接口将会对用户输入内容语义解析出标签，地点，时间
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async parseKeywordsEx(request: ParseKeywordsRequest, runtime: RuntimeOptions): Promise<ParseKeywordsModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/image/parse_keywords`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<ParseKeywordsModel>({
            body: respMap,
            headers: response_.headers,
          }, new ParseKeywordsModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 该接口将会移除故事中的照片
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async removeStoryImagesEx(request: RemoveStoryImagesRequest, runtime: RuntimeOptions): Promise<RemoveStoryImagesModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/image/remove_story_images`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<RemoveStoryImagesModel>({
            body: respMap,
            headers: response_.headers,
          }, new RemoveStoryImagesModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 该接口将会展示用户图片的地点分组
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async searchAddressGroupsEx(request: SearchImageAddressGroupsRequest, runtime: RuntimeOptions): Promise<SearchAddressGroupsModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/image/search_address_groups`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<SearchAddressGroupsModel>({
            body: respMap,
            headers: response_.headers,
          }, new SearchAddressGroupsModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 该接口将会更新人脸分组信息
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async updateFacegroupInfoEx(request: UpdateFaceGroupInfoRequest, runtime: RuntimeOptions): Promise<UpdateFacegroupInfoModel> {
    let _runtime: { [key: string]: any } = {
      timeouted: "retry",
      readTimeout: runtime.readTimeout,
      connectTimeout: runtime.connectTimeout,
      localAddr: runtime.localAddr,
      httpProxy: runtime.httpProxy,
      httpsProxy: runtime.httpsProxy,
      noProxy: runtime.noProxy,
      maxIdleConns: runtime.maxIdleConns,
      socks5Proxy: runtime.socks5Proxy,
      socks5NetWork: runtime.socks5NetWork,
      retry: {
        retryable: runtime.autoretry,
        maxAttempts: Util.defaultNumber(runtime.maxAttempts, 3),
      },
      backoff: {
        policy: Util.defaultString(runtime.backoffPolicy, "no"),
        period: Util.defaultNumber(runtime.backoffPeriod, 1),
      },
      ignoreSSL: runtime.ignoreSSL,
    }

    let _lastRequest = null;
    let _now = Date.now();
    let _retryTimes = 0;
    while ($tea.allowRetry(_runtime['retry'], _retryTimes, _now)) {
      if (_retryTimes > 0) {
        let _backoffTime = $tea.getBackoffTime(_runtime['backoff'], _retryTimes);
        if (_backoffTime > 0) {
          await $tea.sleep(_backoffTime);
        }
      }

      _retryTimes = _retryTimes + 1;
      try {
        let request_ = new $tea.Request();
        let accesskeyId = await this.getAccessKeyId();
        let accessKeySecret = await this.getAccessKeySecret();
        let securityToken = await this.getSecurityToken();
        let accessToken = await this.getAccessToken();
        let realReq = Util.toMap(request);
        request_.protocol = Util.defaultString(this._protocol, "https");
        request_.method = "POST";
        request_.pathname = this.getPathname(this._nickname, `/v2/image/update_facegroup_info`);
        request_.headers = {
          'user-agent': this.getUserAgent(),
          host: Util.defaultString(this._endpoint, `${this._domainId}.api.aliyunpds.com`),
          'content-type': "application/json; charset=utf-8",
          ...request.headers,
        };
        realReq["headers"] = null;
        if (!Util.empty(accessToken)) {
          request_.headers["authorization"] = `Bearer ${accessToken}`;
        } else if (!Util.empty(accesskeyId) && !Util.empty(accessKeySecret)) {
          if (!Util.empty(securityToken)) {
            request_.headers["x-acs-security-token"] = securityToken;
          }

          request_.headers["date"] = Util.getDateUTCString();
          request_.headers["accept"] = "application/json";
          request_.headers["x-acs-signature-method"] = "HMAC-SHA1";
          request_.headers["x-acs-signature-version"] = "1.0";
          let stringToSign = ROAUtil.getStringToSign(request_);
          request_.headers["authorization"] = `acs ${accesskeyId}:${ROAUtil.getSignature(stringToSign, accessKeySecret)}`;
        }

        request_.body = new $tea.BytesReadable(Util.toJSONString(realReq));
        _lastRequest = request_;
        let response_ = await $tea.doAction(request_, _runtime);

        let respMap : {[key: string]: any} = null;
        let obj : any = null;
        if (Util.equalNumber(response_.statusCode, 200)) {
          obj = await Util.readAsJSON(response_.body);
          respMap = Util.assertAsMap(obj);
          return $tea.cast<UpdateFacegroupInfoModel>({
            body: respMap,
            headers: response_.headers,
          }, new UpdateFacegroupInfoModel({}));
        }

        if (!Util.empty(response_.headers["x-ca-error-message"])) {
          throw $tea.newError({
            data: {
              requestId: response_.headers["x-ca-request-id"],
              statusCode: response_.statusCode,
              statusMessage: response_.statusMessage,
            },
            message: response_.headers["x-ca-error-message"],
          });
        }

        obj = await Util.readAsJSON(response_.body);
        respMap = Util.assertAsMap(obj);
        throw $tea.newError({
          data: {
            requestId: response_.headers["x-ca-request-id"],
            statusCode: response_.statusCode,
            statusMessage: response_.statusMessage,
          },
          ...respMap,
        });
      } catch (ex) {
        if ($tea.isRetryable(ex)) {
          continue;
        }
        throw ex;
      }
    }

    throw $tea.newUnretryableError(_lastRequest);
  }

  /**
   * 取消绑定关系，生成新用户，返回访问令牌
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async cancelLink(request: CancelLinkRequest): Promise<CancelLinkModel> {
    let runtime = new RuntimeOptions({ });
    return await this.cancelLinkEx(request, runtime);
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
  async confirmLink(request: ConfirmLinkRequest): Promise<ConfirmLinkModel> {
    let runtime = new RuntimeOptions({ });
    return await this.confirmLinkEx(request, runtime);
  }

  /**
   * 修改手机登录密码，密码必须包含数字和字母，长度8-20个字符
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async changePassword(request: DefaultChangePasswordRequest): Promise<ChangePasswordModel> {
    let runtime = new RuntimeOptions({ });
    return await this.changePasswordEx(request, runtime);
  }

  /**
   * 设置手机登录密码，密码必须包含数字和字母，长度8-20个字符
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async setPassword(request: DefaultSetPasswordRequest): Promise<SetPasswordModel> {
    let runtime = new RuntimeOptions({ });
    return await this.setPasswordEx(request, runtime);
  }

  /**
   * 校验手机短信验证码，用于重置密码时校验手机，通过校验后返回state，可通过state重新设置密码
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async verifyCode(request: VerifyCodeRequest): Promise<VerifyCodeModel> {
    let runtime = new RuntimeOptions({ });
    return await this.verifyCodeEx(request, runtime);
  }

  /**
   * 管理员通过账号信息直接获取用户的访问令牌
   * @tags account
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async getAccessTokenByLinkInfo(request: GetAccessTokenByLinkInfoRequest): Promise<GetAccessTokenByLinkInfoModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getAccessTokenByLinkInfoEx(request, runtime);
  }

  /**
   * 获取图片验证码，用于人机校验，默认不需要
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async getCaptcha(request: GetCaptchaRequest): Promise<GetCaptchaModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getCaptchaEx(request, runtime);
  }

  /**
   * 获取用户认证方式详情
   * @tags account
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async getLinkInfo(request: GetByLinkInfoRequest): Promise<GetLinkInfoModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getLinkInfoEx(request, runtime);
  }

  /**
   * 获取用户的所有绑定信息
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async getLinkInfoByUserId(request: GetLinkInfoByUserIDRequest): Promise<GetLinkInfoByUserIdModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getLinkInfoByUserIdEx(request, runtime);
  }

  /**
   * 获取公钥，用于加密对称密钥
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async getPublicKey(request: GetPublicKeyRequest): Promise<GetPublicKeyModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getPublicKeyEx(request, runtime);
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
  async link(request: AccountLinkRequest): Promise<LinkModel> {
    let runtime = new RuntimeOptions({ });
    return await this.linkEx(request, runtime);
  }

  /**
   * 查询手机号是否已被注册
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async checkExist(request: MobileCheckExistRequest): Promise<CheckExistModel> {
    let runtime = new RuntimeOptions({ });
    return await this.checkExistEx(request, runtime);
  }

  /**
   * 通过手机号+短信或密码登录，返回刷新令牌和访问令牌
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async login(request: MobileLoginRequest): Promise<LoginModel> {
    let runtime = new RuntimeOptions({ });
    return await this.loginEx(request, runtime);
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
  async register(request: MobileRegisterRequest): Promise<RegisterModel> {
    let runtime = new RuntimeOptions({ });
    return await this.registerEx(request, runtime);
  }

  /**
   * 发送短信验证码，用于登录、注册、修改密码、绑定等
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async mobileSendSmsCode(request: MobileSendSmsCodeRequest): Promise<MobileSendSmsCodeModel> {
    let runtime = new RuntimeOptions({ });
    return await this.mobileSendSmsCodeEx(request, runtime);
  }

  /**
   * 用户退出登录
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async accountRevoke(request: RevokeRequest): Promise<AccountRevokeModel> {
    let runtime = new RuntimeOptions({ });
    return await this.accountRevokeEx(request, runtime);
  }

  /**
   * 用户通过刷新令牌（refresh_token）获取访问令牌（access_token）
   * @tags account
   * @error InvalidParameterMissing The input parameter {parameter_name} is missing.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async accountToken(request: AccountTokenRequest): Promise<AccountTokenModel> {
    let runtime = new RuntimeOptions({ });
    return await this.accountTokenEx(request, runtime);
  }

  /**
   * 列举Store列表
   * @tags admin
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error Forbidden User not authorized to operate on the specified APIs.
   * @error InternalError The request has been failed due to some unknown error.
   */
  async adminListStores(request: AdminListStoresRequest): Promise<AdminListStoresModel> {
    let runtime = new RuntimeOptions({ });
    return await this.adminListStoresEx(request, runtime);
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
  async getUserAccessToken(request: GetUserAccessTokenRequest): Promise<GetUserAccessTokenModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getUserAccessTokenEx(request, runtime);
  }

  /**
   * 如果目录拷贝、目录删除不能在限定时间内完成，将访问一个异步任务id，
   * 通过此接口获取异步任务的信息，以确定任务是否执行成功。
   * @tags async_task
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getAsyncTaskInfo(request: GetAsyncTaskRequest): Promise<GetAsyncTaskInfoModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getAsyncTaskInfoEx(request, runtime);
  }

  /**
   * 对多个原子操作封装成一个批处理请求，服务端并行处理并打包返回每个操作的执行结果。
   * 支持对文件和文件夹的移动、删除、修改，每个批处理请求最多包含100个原则操作。
   * @tags batch
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async batchOperation(request: BatchRequest): Promise<BatchOperationModel> {
    let runtime = new RuntimeOptions({ });
    return await this.batchOperationEx(request, runtime);
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
  async createDrive(request: CreateDriveRequest): Promise<CreateDriveModel> {
    let runtime = new RuntimeOptions({ });
    return await this.createDriveEx(request, runtime);
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
  async deleteDrive(request: DeleteDriveRequest): Promise<DeleteDriveModel> {
    let runtime = new RuntimeOptions({ });
    return await this.deleteDriveEx(request, runtime);
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
  async getDrive(request: GetDriveRequest): Promise<GetDriveModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getDriveEx(request, runtime);
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
  async getDefaultDrive(request: GetDefaultDriveRequest): Promise<GetDefaultDriveModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getDefaultDriveEx(request, runtime);
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
  async listDrives(request: ListDriveRequest): Promise<ListDrivesModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listDrivesEx(request, runtime);
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
  async listMyDrives(request: ListMyDriveRequest): Promise<ListMyDrivesModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listMyDrivesEx(request, runtime);
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
  async updateDrive(request: UpdateDriveRequest): Promise<UpdateDriveModel> {
    let runtime = new RuntimeOptions({ });
    return await this.updateDriveEx(request, runtime);
  }

  /**
   * 完成文件上传。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async completeFile(request: CompleteFileRequest): Promise<CompleteFileModel> {
    let runtime = new RuntimeOptions({ });
    return await this.completeFileEx(request, runtime);
  }

  /**
   * 指定源文件或文件夹，拷贝到指定的文件夹。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async copyFile(request: CopyFileRequest): Promise<CopyFileModel> {
    let runtime = new RuntimeOptions({ });
    return await this.copyFileEx(request, runtime);
  }

  /**
   * 在指定文件夹下创建文件或者文件夹，
   * 根文件夹用root表示，其他文件夹使用创建文件夹时返回的file_id。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error AlreadyExist {resource} has already exists. {extra_msg}
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async createFile(request: CreateFileRequest): Promise<CreateFileModel> {
    let runtime = new RuntimeOptions({ });
    return await this.createFileEx(request, runtime);
  }

  /**
   * 指定文件或文件夹ID，删除文件或者文件夹。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async deleteFile(request: DeleteFileRequest): Promise<DeleteFileModel> {
    let runtime = new RuntimeOptions({ });
    return await this.deleteFileEx(request, runtime);
  }

  /**
   * 获取指定文件或文件夹ID的信息。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getFile(request: GetFileRequest): Promise<GetFileModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getFileEx(request, runtime);
  }

  /**
   * 根据路径获取指定文件或文件夹的信息。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getFileByPath(request: GetFileByPathRequest): Promise<GetFileByPathModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getFileByPathEx(request, runtime);
  }

  /**
   * 获取文件的下载地址，调用者可自己设置range头并发下载。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getDownloadUrl(request: GetDownloadUrlRequest): Promise<GetDownloadUrlModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getDownloadUrlEx(request, runtime);
  }

  /**
   * 获取drive内，增量数据最新的游标
   * @tags file_delta
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getLastCursor(request: GetLastCursorRequest): Promise<GetLastCursorModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getLastCursorEx(request, runtime);
  }

  /**
   * 获取media文件播放URL地址（当前仅支持m3u8）
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getMediaPlayUrl(request: GetMediaPlayURLRequest): Promise<GetMediaPlayUrlModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getMediaPlayUrlEx(request, runtime);
  }

  /**
   * 获取文档的在线编辑地址
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getOfficeEditUrl(request: GetOfficeEditUrlRequest): Promise<GetOfficeEditUrlModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getOfficeEditUrlEx(request, runtime);
  }

  /**
   * 获取文档的预览地址（office文档）
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getOfficePreviewUrl(request: GetOfficePreviewUrlRequest): Promise<GetOfficePreviewUrlModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getOfficePreviewUrlEx(request, runtime);
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
  async getUploadUrl(request: GetUploadUrlRequest): Promise<GetUploadUrlModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getUploadUrlEx(request, runtime);
  }

  /**
   * 获取视频雪碧图地址
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getVideoPreviewSpriteUrl(request: GetVideoPreviewSpriteURLRequest): Promise<GetVideoPreviewSpriteUrlModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getVideoPreviewSpriteUrlEx(request, runtime);
  }

  /**
   * 获取视频播放地址
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getVideoPreviewUrl(request: GetVideoPreviewURLRequest): Promise<GetVideoPreviewUrlModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getVideoPreviewUrlEx(request, runtime);
  }

  /**
   * 列举指定目录下的文件或文件夹。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listFile(request: ListFileRequest): Promise<ListFileModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listFileEx(request, runtime);
  }

  /**
   * 查看分享中的文件列表
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error ShareLinkTokenInvalid ShareToken is invalid. {message}
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listFileByAnonymous(request: ListByAnonymousRequest): Promise<ListFileByAnonymousModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listFileByAnonymousEx(request, runtime);
  }

  /**
   * 根据自定义同步索引键列举文件或文件夹。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listFileByCustomIndexKey(request: ListFileByCustomIndexKeyRequest): Promise<ListFileByCustomIndexKeyModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listFileByCustomIndexKeyEx(request, runtime);
  }

  /**
   * 获取drive内，增量数据列表
   * @tags file_delta
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listFileDelta(request: ListFileDeltaRequest): Promise<ListFileDeltaModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listFileDeltaEx(request, runtime);
  }

  /**
   * 列举upload_id对应的已上传分片。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listUploadedParts(request: ListUploadedPartRequest): Promise<ListUploadedPartsModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listUploadedPartsEx(request, runtime);
  }

  /**
   * 指定源文件或文件夹，移动到指定的文件夹。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async moveFile(request: MoveFileRequest): Promise<MoveFileModel> {
    let runtime = new RuntimeOptions({ });
    return await this.moveFileEx(request, runtime);
  }

  /**
   * 刷新在线编辑Token
   * @tags file, refresh, office, edit
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async token(request: RefreshOfficeEditTokenRequest): Promise<TokenModel> {
    let runtime = new RuntimeOptions({ });
    return await this.tokenEx(request, runtime);
  }

  /**
   * 在指定drive下全量获取文件元信息。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async scanFileMeta(request: ScanFileMetaRequest): Promise<ScanFileMetaModel> {
    let runtime = new RuntimeOptions({ });
    return await this.scanFileMetaEx(request, runtime);
  }

  /**
   * 根据筛选条件，在指定drive下搜索文件。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async searchFile(request: SearchFileRequest): Promise<SearchFileModel> {
    let runtime = new RuntimeOptions({ });
    return await this.searchFileEx(request, runtime);
  }

  /**
   * 对指定的文件或文件夹更新信息。
   * @tags file
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error AlreadyExist {resource} has already exists. {extra_msg}
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async updateFile(request: UpdateFileMetaRequest): Promise<UpdateFileModel> {
    let runtime = new RuntimeOptions({ });
    return await this.updateFileEx(request, runtime);
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
  async createShare(request: CreateShareRequest): Promise<CreateShareModel> {
    let runtime = new RuntimeOptions({ });
    return await this.createShareEx(request, runtime);
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
  async deleteShare(request: DeleteShareRequest): Promise<DeleteShareModel> {
    let runtime = new RuntimeOptions({ });
    return await this.deleteShareEx(request, runtime);
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
  async getShare(request: GetShareRequest): Promise<GetShareModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getShareEx(request, runtime);
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
  async listShare(request: ListShareRequest): Promise<ListShareModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listShareEx(request, runtime);
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
  async updateShare(request: UpdateShareRequest): Promise<UpdateShareModel> {
    let runtime = new RuntimeOptions({ });
    return await this.updateShareEx(request, runtime);
  }

  /**
   * 取消指定分享
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async cancelShareLink(request: CancelShareLinkRequest): Promise<CancelShareLinkModel> {
    let runtime = new RuntimeOptions({ });
    return await this.cancelShareLinkEx(request, runtime);
  }

  /**
   * 创建分享。
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async createShareLink(request: CreateShareLinkRequest): Promise<CreateShareLinkModel> {
    let runtime = new RuntimeOptions({ });
    return await this.createShareLinkEx(request, runtime);
  }

  /**
   * 查看分享的基本信息，比如分享者、到期时间等
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getShareByAnonymous(request: GetShareLinkByAnonymousRequest): Promise<GetShareByAnonymousModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getShareByAnonymousEx(request, runtime);
  }

  /**
   * 使用分享口令换取分享id
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getShareId(request: GetShareLinkIDRequest): Promise<GetShareIdModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getShareIdEx(request, runtime);
  }

  /**
   * 使用分享码+提取码换取分享token
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getShareToken(request: GetShareLinkTokenRequest): Promise<GetShareTokenModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getShareTokenEx(request, runtime);
  }

  /**
   * 列举指定用户的分享
   * @tags share_link
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listShareLink(request: ListShareLinkRequest): Promise<ListShareLinkModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listShareLinkEx(request, runtime);
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
  async createUser(request: CreateUserRequest): Promise<CreateUserModel> {
    let runtime = new RuntimeOptions({ });
    return await this.createUserEx(request, runtime);
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
  async deleteUser(request: DeleteUserRequest): Promise<DeleteUserModel> {
    let runtime = new RuntimeOptions({ });
    return await this.deleteUserEx(request, runtime);
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
  async getUser(request: GetUserRequest): Promise<GetUserModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getUserEx(request, runtime);
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
  async listUsers(request: ListUserRequest): Promise<ListUsersModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listUsersEx(request, runtime);
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
  async searchUser(request: SearchUserRequest): Promise<SearchUserModel> {
    let runtime = new RuntimeOptions({ });
    return await this.searchUserEx(request, runtime);
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
  async updateUser(request: UpdateUserRequest): Promise<UpdateUserModel> {
    let runtime = new RuntimeOptions({ });
    return await this.updateUserEx(request, runtime);
  }

  /**
   * 该接口将会创建故事
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async createStory(request: CreateStoryRequest): Promise<CreateStoryModel> {
    let runtime = new RuntimeOptions({ });
    return await this.createStoryEx(request, runtime);
  }

  /**
   * 该接口将返回用户Drive下的云照片个数
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getPhotoCount(request: GetImageCountRequest): Promise<GetPhotoCountModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getPhotoCountEx(request, runtime);
  }

  /**
   * 该接口将会获取故事详情
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async getStoryDetail(request: GetStoryDetailRequest): Promise<GetStoryDetailModel> {
    let runtime = new RuntimeOptions({ });
    return await this.getStoryDetailEx(request, runtime);
  }

  /**
   * 该接口将会展示用户图片的地点分组
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listAddressGroups(request: ListImageAddressGroupsRequest): Promise<ListAddressGroupsModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listAddressGroupsEx(request, runtime);
  }

  /**
   * 该接口将会列举人脸分组
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listFacegroups(request: ListImageFaceGroupsRequest): Promise<ListFacegroupsModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listFacegroupsEx(request, runtime);
  }

  /**
   * 该接口将会获取故事列表
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listStory(request: ListStoryRequest): Promise<ListStoryModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listStoryEx(request, runtime);
  }

  /**
   * 该接口将会展示场景标记
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async listTags(request: ListImageTagsRequest): Promise<ListTagsModel> {
    let runtime = new RuntimeOptions({ });
    return await this.listTagsEx(request, runtime);
  }

  /**
   * 该接口将会对用户输入内容语义解析出标签，地点，时间
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async parseKeywords(request: ParseKeywordsRequest): Promise<ParseKeywordsModel> {
    let runtime = new RuntimeOptions({ });
    return await this.parseKeywordsEx(request, runtime);
  }

  /**
   * 该接口将会移除故事中的照片
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async removeStoryImages(request: RemoveStoryImagesRequest): Promise<RemoveStoryImagesModel> {
    let runtime = new RuntimeOptions({ });
    return await this.removeStoryImagesEx(request, runtime);
  }

  /**
   * 该接口将会展示用户图片的地点分组
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async searchAddressGroups(request: SearchImageAddressGroupsRequest): Promise<SearchAddressGroupsModel> {
    let runtime = new RuntimeOptions({ });
    return await this.searchAddressGroupsEx(request, runtime);
  }

  /**
   * 该接口将会更新人脸分组信息
   * @tags image
   * @error InvalidParameter The input parameter {parameter_name} is not valid.
   * @error AccessTokenInvalid AccessToken is invalid. {message}
   * @error ForbiddenNoPermission No Permission to access resource {resource_name}.
   * @error NotFound The resource {resource_name} cannot be found. Please check.
   * @error InternalError The request has been failed due to some unknown error.
   * @error ServiceUnavailable The request has failed due to a temporary failure of the server.
   */
  async updateFacegroupInfo(request: UpdateFaceGroupInfoRequest): Promise<UpdateFacegroupInfoModel> {
    let runtime = new RuntimeOptions({ });
    return await this.updateFacegroupInfoEx(request, runtime);
  }

  getPathname(nickname: string, path: string): string {
    if (Util.empty(nickname)) {
      return path;
    }

    return `/${nickname}${path}`;
  }

  async setExpireTime(expireTime: string): Promise<void> {
    if (Util.isUnset(this._accessTokenCredential)) {
      return ;
    }

    this._accessTokenCredential.setExpireTime(expireTime);
  }

  getExpireTime(): string {
    if (Util.isUnset(this._accessTokenCredential)) {
      return "";
    }

    let expireTime = this._accessTokenCredential.getExpireTime();
    return expireTime;
  }

  setRefreshToken(token: string): void {
    if (Util.isUnset(this._accessTokenCredential)) {
      return ;
    }

    this._accessTokenCredential.setRefreshToken(token);
  }

  getRefreshToken(): string {
    if (Util.isUnset(this._accessTokenCredential)) {
      return "";
    }

    let token = this._accessTokenCredential.getRefreshToken();
    return token;
  }

  setAccessToken(token: string): void {
    if (Util.isUnset(this._accessTokenCredential)) {
      return ;
    }

    this._accessTokenCredential.setAccessToken(token);
  }

  async getAccessToken(): Promise<string> {
    if (Util.isUnset(this._accessTokenCredential)) {
      return "";
    }

    let token = await this._accessTokenCredential.getAccessToken();
    return token;
  }

  setUserAgent(userAgent: string): void {
    this._userAgent = userAgent;
  }

  appendUserAgent(userAgent: string): void {
    this._userAgent = `${this._userAgent} ${userAgent}`;
  }

  getUserAgent(): string {
    let userAgent = Util.getUserAgent(this._userAgent);
    return userAgent;
  }

  async getAccessKeyId(): Promise<string> {
    if (Util.isUnset(this._credential)) {
      return "";
    }

    let accessKeyId = await this._credential.getAccessKeyId();
    return accessKeyId;
  }

  async getAccessKeySecret(): Promise<string> {
    if (Util.isUnset(this._credential)) {
      return "";
    }

    let secret = await this._credential.getAccessKeySecret();
    return secret;
  }

  async getSecurityToken(): Promise<string> {
    if (Util.isUnset(this._credential)) {
      return "";
    }

    let token = await this._credential.getSecurityToken();
    return token;
  }

}
