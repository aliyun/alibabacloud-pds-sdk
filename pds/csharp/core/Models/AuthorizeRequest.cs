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
    public class AuthorizeRequest : TeaModel {
        /// <summary>
        /// Client ID, 此处填写创建App时返回的AppID
        /// </summary>
        [NameInMap("ClientID")]
        [Validation(Required=true)]
        public string ClientID { get; set; }

        /// <summary>
        /// 鉴权方式，目前支持ding,ram鉴权
        /// </summary>
        [NameInMap("LoginType")]
        [Validation(Required=false)]
        public string LoginType { get; set; }

        /// <summary>
        /// 回调地址, 此处填写创建App时填写的回调地址
        /// </summary>
        [NameInMap("RedirectUri")]
        [Validation(Required=true)]
        public string RedirectUri { get; set; }

        /// <summary>
        /// 返回类型, 只能填写code
        /// </summary>
        [NameInMap("ResponseType")]
        [Validation(Required=true)]
        public string ResponseType { get; set; }

        /// <summary>
        /// 申请的权限列表, 默认为所有权限
        /// </summary>
        [NameInMap("Scope")]
        [Validation(Required=false)]
        public List<string> Scope { get; set; }

        /// <summary>
        /// 用户自定义字段，会在鉴权成功后的callback带回
        /// </summary>
        [NameInMap("State")]
        [Validation(Required=false)]
        public string State { get; set; }

    }

}
