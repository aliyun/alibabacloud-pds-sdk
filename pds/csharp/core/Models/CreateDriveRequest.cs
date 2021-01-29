// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * create drive request
     */
    public class CreateDriveRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// 是否默认drive, 只允许设置一个默认drive
        /// </summary>
        [NameInMap("default")]
        [Validation(Required=false)]
        public bool? Default { get; set; }

        /// <summary>
        /// 描述信息
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=false, MaxLength=1024)]
        public string Description { get; set; }

        /// <summary>
        /// Drive 名称
        /// </summary>
        [NameInMap("drive_name")]
        [Validation(Required=true, MaxLength=1024)]
        public string DriveName { get; set; }

        /// <summary>
        /// Drive类型
        /// </summary>
        [NameInMap("drive_type")]
        [Validation(Required=false)]
        public string DriveType { get; set; }

        [NameInMap("encrypt_mode")]
        [Validation(Required=false)]
        public string EncryptMode { get; set; }

        /// <summary>
        /// location
        /// </summary>
        [NameInMap("location")]
        [Validation(Required=false)]
        public string Location { get; set; }

        /// <summary>
        /// 所属者
        /// </summary>
        [NameInMap("owner")]
        [Validation(Required=true)]
        public string Owner { get; set; }

        /// <summary>
        /// domain的PathType为OSSPath时必选。 Drive存储基于store的相对路径
        /// </summary>
        [NameInMap("relative_path")]
        [Validation(Required=false)]
        public string RelativePath { get; set; }

        /// <summary>
        /// 状态
        /// </summary>
        [NameInMap("status")]
        [Validation(Required=false)]
        public string Status { get; set; }

        /// <summary>
        /// StoreID , domain的PathType为OSSPath时必选
        /// </summary>
        [NameInMap("store_id")]
        [Validation(Required=false)]
        public string StoreId { get; set; }

        /// <summary>
        /// 总大小,单位Byte [如果设置 -1 代表不限制]
        /// </summary>
        [NameInMap("total_size")]
        [Validation(Required=false)]
        public long? TotalSize { get; set; }

    }

}
