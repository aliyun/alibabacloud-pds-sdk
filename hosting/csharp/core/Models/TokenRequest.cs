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
    public class TokenRequest : TeaModel {
        /// <summary>
        /// JWT方式授权需要传此参数，传入JWT签名的声明，用于更换accessToken
        /// </summary>
        [NameInMap("Assertion")]
        [Validation(Required=false)]
        public string Assertion { get; set; }

        /// <summary>
        /// Client ID, 此处填写创建App时返回的AppID
        /// </summary>
        [NameInMap("ClientID")]
        [Validation(Required=true)]
        public string ClientID { get; set; }

        /// <summary>
        /// Client ID, 此处填写创建App时返回的AppSecret
        /// </summary>
        [NameInMap("ClientSecret")]
        [Validation(Required=true)]
        public string ClientSecret { get; set; }

        /// <summary>
        /// 认证后回调参数中的code
        /// </summary>
        [NameInMap("Code")]
        [Validation(Required=false)]
        public string Code { get; set; }

        /// <summary>
        /// OAuth2.0 device flow换取token参数
        /// </summary>
        [NameInMap("DeviceCode")]
        [Validation(Required=false)]
        public string DeviceCode { get; set; }

        /// <summary>
        /// 通过code获取accessToken或者通过refresh_token获取accessToken
        /// </summary>
        [NameInMap("GrantType")]
        [Validation(Required=true)]
        public string GrantType { get; set; }

        /// <summary>
        /// 回调地址, 此处填写创建App时填写的回调地址，OAuth方式登录时需要传入
        /// </summary>
        [NameInMap("RedirectUri")]
        [Validation(Required=false)]
        public string RedirectUri { get; set; }

        /// <summary>
        /// 刷新accessToken使用的refreshToken
        /// </summary>
        [NameInMap("RefreshToken")]
        [Validation(Required=false)]
        public string RefreshToken { get; set; }

    }

}
