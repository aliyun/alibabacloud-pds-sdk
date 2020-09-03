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
    public class DefaultChangePasswordRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// App ID, 当前访问的App
        /// </summary>
        [NameInMap("app_id")]
        [Validation(Required=true)]
        public string AppId { get; set; }

        /// <summary>
        /// AES-256对称加密密钥，通过App公钥加密后传输
        /// </summary>
        [NameInMap("encrypted_key")]
        [Validation(Required=true)]
        public string EncryptedKey { get; set; }

        /// <summary>
        /// 新密码，必须包含数字和字母，长度8-20个字符
        /// </summary>
        [NameInMap("new_password")]
        [Validation(Required=true)]
        public string NewPassword { get; set; }

        /// <summary>
        /// 手机号
        /// </summary>
        [NameInMap("phone_number")]
        [Validation(Required=true)]
        public string PhoneNumber { get; set; }

        /// <summary>
        /// 国家编号，默认86，不需要填+号，直接填数字
        /// </summary>
        [NameInMap("phone_region")]
        [Validation(Required=false)]
        public string PhoneRegion { get; set; }

        /// <summary>
        /// 修改密码的临时授权码
        /// </summary>
        [NameInMap("state")]
        [Validation(Required=true)]
        public string State { get; set; }

    }

}
