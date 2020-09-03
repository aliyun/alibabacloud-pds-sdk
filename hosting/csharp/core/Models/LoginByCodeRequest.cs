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
    public class LoginByCodeRequest : TeaModel {
        /// <summary>
        /// 鉴权后返回的accessToken，淘宝登录需要此字段
        /// </summary>
        [NameInMap("access_token")]
        [Validation(Required=false)]
        public string AccessToken { get; set; }

        /// <summary>
        /// App ID, 当前访问的App
        /// </summary>
        [NameInMap("app_id")]
        [Validation(Required=true)]
        public string AppId { get; set; }

        /// <summary>
        /// 鉴权后返回的AuthCode，支付宝登录需要此字段
        /// </summary>
        [NameInMap("auth_code")]
        [Validation(Required=false)]
        public string AuthCode { get; set; }

        /// <summary>
        /// 鉴权类型，淘宝、支付宝
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=true)]
        public string Type { get; set; }

    }

}
