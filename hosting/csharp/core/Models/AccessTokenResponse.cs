// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 
     */
    public class AccessTokenResponse : TeaModel {
        /// <summary>
        /// 用于调用业务接口的accessToken
        /// </summary>
        [NameInMap("access_token")]
        [Validation(Required=true)]
        public string AccessToken { get; set; }

        /// <summary>
        /// Default Drive ID
        /// </summary>
        [NameInMap("default_drive_id")]
        [Validation(Required=true)]
        public string DefaultDriveId { get; set; }

        /// <summary>
        /// accessToken过期时间，ISO时间
        /// </summary>
        [NameInMap("expire_time")]
        [Validation(Required=true)]
        public string ExpireTime { get; set; }

        /// <summary>
        /// accessToken过期时间，单位秒
        /// </summary>
        [NameInMap("expires_in")]
        [Validation(Required=true)]
        public long? ExpiresIn { get; set; }

        /// <summary>
        /// 用于刷新accessToken
        /// </summary>
        [NameInMap("refresh_token")]
        [Validation(Required=true)]
        public string RefreshToken { get; set; }

        /// <summary>
        /// 当前用户角色
        /// </summary>
        [NameInMap("role")]
        [Validation(Required=true)]
        public string Role { get; set; }

        /// <summary>
        /// accessToken类型，Bearer
        /// </summary>
        [NameInMap("token_type")]
        [Validation(Required=true)]
        public string TokenType { get; set; }

        /// <summary>
        /// 当前用户ID
        /// </summary>
        [NameInMap("user_id")]
        [Validation(Required=true)]
        public string UserId { get; set; }

    }

}
