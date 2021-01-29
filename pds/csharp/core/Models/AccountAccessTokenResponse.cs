// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class AccountAccessTokenResponse : TeaModel {
        /// <summary>
        /// 用于调用业务接口的accessToken
        /// </summary>
        [NameInMap("access_token")]
        [Validation(Required=true)]
        public string AccessToken { get; set; }

        /// <summary>
        /// 当前用户头像
        /// </summary>
        [NameInMap("avatar")]
        [Validation(Required=false)]
        public string Avatar { get; set; }

        /// <summary>
        /// Default Drive ID
        /// </summary>
        [NameInMap("default_drive_id")]
        [Validation(Required=false)]
        public string DefaultDriveId { get; set; }

        /// <summary>
        /// Default Sbox Drive ID
        /// </summary>
        [NameInMap("default_sbox_drive_id")]
        [Validation(Required=false)]
        public string DefaultSboxDriveId { get; set; }

        /// <summary>
        /// device_id 通过device flow 绑定的设备ID
        /// </summary>
        [NameInMap("device_id")]
        [Validation(Required=false)]
        public string DeviceId { get; set; }

        /// <summary>
        /// device_name 通过device flow 绑定的设备名
        /// </summary>
        [NameInMap("device_name")]
        [Validation(Required=false)]
        public string DeviceName { get; set; }

        /// <summary>
        /// 当前用户已存在的登录方式
        /// </summary>
        [NameInMap("exist_link")]
        [Validation(Required=false)]
        public List<LinkInfo> ExistLink { get; set; }

        /// <summary>
        /// accessToken过期时间，ISO时间
        /// </summary>
        [NameInMap("expire_time")]
        [Validation(Required=false)]
        public string ExpireTime { get; set; }

        /// <summary>
        /// accessToken过期时间，单位秒
        /// </summary>
        [NameInMap("expires_in")]
        [Validation(Required=false)]
        public long? ExpiresIn { get; set; }

        /// <summary>
        /// 用户是否为第一次登录
        /// </summary>
        [NameInMap("is_first_login")]
        [Validation(Required=false)]
        public bool? IsFirstLogin { get; set; }

        /// <summary>
        /// 是否需要绑定
        /// </summary>
        [NameInMap("need_link")]
        [Validation(Required=true)]
        public bool? NeedLink { get; set; }

        /// <summary>
        /// 用户是否需要进行的实人认证
        /// </summary>
        [NameInMap("need_rp_verify")]
        [Validation(Required=false)]
        public bool? NeedRpVerify { get; set; }

        /// <summary>
        /// 当前用户昵称
        /// </summary>
        [NameInMap("nick_name")]
        [Validation(Required=false)]
        public string NickName { get; set; }

        /// <summary>
        /// 用户的数据密码是否设置过
        /// </summary>
        [NameInMap("pin_setup")]
        [Validation(Required=false)]
        public bool? PinSetup { get; set; }

        /// <summary>
        /// 用于刷新accessToken
        /// </summary>
        [NameInMap("refresh_token")]
        [Validation(Required=false)]
        public string RefreshToken { get; set; }

        /// <summary>
        /// 当前用户角色
        /// </summary>
        [NameInMap("role")]
        [Validation(Required=false)]
        public string Role { get; set; }

        /// <summary>
        /// 临时权限，用于登录成功后设置密码
        /// </summary>
        [NameInMap("state")]
        [Validation(Required=false)]
        public string State { get; set; }

        /// <summary>
        /// accessToken类型，Bearer
        /// </summary>
        [NameInMap("token_type")]
        [Validation(Required=false)]
        public string TokenType { get; set; }

        /// <summary>
        /// 用户自定义数据，格式为json，可用于配置项、少量临时数据等存储，不超过1K
        /// </summary>
        [NameInMap("user_data")]
        [Validation(Required=false)]
        public Dictionary<string, object> UserData { get; set; }

        /// <summary>
        /// 当前用户ID
        /// </summary>
        [NameInMap("user_id")]
        [Validation(Required=false)]
        public string UserId { get; set; }

        /// <summary>
        /// 当前用户名
        /// </summary>
        [NameInMap("user_name")]
        [Validation(Required=false)]
        public string UserName { get; set; }

    }

}
