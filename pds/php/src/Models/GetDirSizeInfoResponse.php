<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取文件夹size信息
 */
class GetDirSizeInfoResponse extends Model {
    protected $_name = [
        'dirCount' => 'dir_count',
        'fileCount' => 'file_count',
        'size' => 'size',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->dirCount) {
            $res['dir_count'] = $this->dirCount;
        }
        if (null !== $this->fileCount) {
            $res['file_count'] = $this->fileCount;
        }
        if (null !== $this->size) {
            $res['size'] = $this->size;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return GetDirSizeInfoResponse
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['dir_count'])){
            $model->dirCount = $map['dir_count'];
        }
        if(isset($map['file_count'])){
            $model->fileCount = $map['file_count'];
        }
        if(isset($map['size'])){
            $model->size = $map['size'];
        }
        return $model;
    }
    /**
     * @description dir_count
     * @example 1000
     * @var int
     */
    public $dirCount;

    /**
     * @description file_count
     * @example 100000
     * @var int
     */
    public $fileCount;

    /**
     * @description size
     * @example 1024576
     * @var int
     */
    public $size;

}
