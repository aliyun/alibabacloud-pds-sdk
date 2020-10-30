// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * Update drive request
     */
    public class UpdateDriveRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// 描述信息
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=false, MaxLength=1024)]
        public string Description { get; set; }

        /// <summary>
        /// Drive ID
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=true)]
        public string DriveId { get; set; }

        /// <summary>
        /// Drive 名称
        /// </summary>
        [NameInMap("drive_name")]
        [Validation(Required=false, MaxLength=1024)]
        public string DriveName { get; set; }

        /// <summary>
        /// 授权访问加密数据
        /// </summary>
        [NameInMap("encrypt_data_access")]
        [Validation(Required=false)]
        public bool? EncryptDataAccess { get; set; }

        /// <summary>
        /// 加密模式
        /// </summary>
        [NameInMap("encrypt_mode")]
        [Validation(Required=false)]
        public string EncryptMode { get; set; }

        /// <summary>
        /// 状态
        /// </summary>
        [NameInMap("status")]
        [Validation(Required=false)]
        public string Status { get; set; }

        /// <summary>
        /// 总大小,单位Byte [如果设置 -1 代表不限制]
        /// </summary>
        [NameInMap("total_size")]
        [Validation(Required=false)]
        public long? TotalSize { get; set; }

    }

}
