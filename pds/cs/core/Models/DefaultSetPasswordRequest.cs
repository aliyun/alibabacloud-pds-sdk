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
    public class DefaultSetPasswordRequest : TeaModel {
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
        /// 新密码，必须包含数字和字母，长度8-20个字符，使用AES-256对称加密后传输（CBC模式, 填充算法为PKCS7Padding，生成base64字符串）
        /// </summary>
        [NameInMap("new_password")]
        [Validation(Required=true)]
        public string NewPassword { get; set; }

        /// <summary>
        /// 修改密码的临时授权码
        /// </summary>
        [NameInMap("state")]
        [Validation(Required=true)]
        public string State { get; set; }

    }

}
