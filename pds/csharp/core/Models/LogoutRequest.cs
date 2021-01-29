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
    public class LogoutRequest : TeaModel {
        /// <summary>
        /// 登出之后的跳转地址，默认跳转到App的域名下
        /// </summary>
        [NameInMap("BackUrl")]
        [Validation(Required=false)]
        public string BackUrl { get; set; }

        /// <summary>
        /// Client ID, 此处填写创建App时返回的AppID
        /// </summary>
        [NameInMap("ClientID")]
        [Validation(Required=true)]
        public string ClientID { get; set; }

        /// <summary>
        /// 用户自定义字段，会在鉴权成功后的callback带回
        /// </summary>
        [NameInMap("LoginType")]
        [Validation(Required=false)]
        public string LoginType { get; set; }

    }

}
