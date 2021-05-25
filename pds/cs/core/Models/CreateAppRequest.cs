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
    public class CreateAppRequest : TeaModel {
        /// <summary>
        /// App名称
        /// </summary>
        [NameInMap("app_name")]
        [Validation(Required=true, MaxLength=128)]
        public string AppName { get; set; }

        /// <summary>
        /// App描述
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=false, MaxLength=128)]
        public string Description { get; set; }

        /// <summary>
        /// 是否是domain私有App
        /// </summary>
        [NameInMap("is_third_party")]
        [Validation(Required=false)]
        public bool? IsThirdParty { get; set; }

        /// <summary>
        /// App图标
        /// </summary>
        [NameInMap("logo")]
        [Validation(Required=true)]
        public string Logo { get; set; }

        /// <summary>
        /// RSA加密算法的公钥, PEM格式
        /// </summary>
        [NameInMap("public_key")]
        [Validation(Required=true)]
        public string PublicKey { get; set; }

        /// <summary>
        /// App回调地址
        /// </summary>
        [NameInMap("redirect_uri")]
        [Validation(Required=false)]
        public string RedirectUri { get; set; }

        /// <summary>
        /// App权限列表
        /// </summary>
        [NameInMap("scope")]
        [Validation(Required=true)]
        public List<string> Scope { get; set; }

        /// <summary>
        /// App类型
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=true)]
        public string Type { get; set; }

    }

}
