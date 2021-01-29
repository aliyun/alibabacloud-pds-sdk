<?php

// This file is auto-generated, don't edit it. Thanks.
namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * Parse keywords request
 */
class ParseKeywordsRequest extends Model {
    protected $_name = [
        'keywords' => 'keywords',
    ];
    public function validate() {}
    public function toMap() {
        $res = [];
        if (null !== $this->headers) {
            $res['headers'] = $this->headers;
        }
        if (null !== $this->keywords) {
            $res['keywords'] = $this->keywords;
        }
        return $res;
    }
    /**
     * @param array $map
     * @return ParseKeywordsRequest
     */
    public static function fromMap($map = []) {
        $model = new self();
        if(isset($map['headers'])){
            $model->headers = $map['headers'];
        }
        if(isset($map['keywords'])){
            $model->keywords = $map['keywords'];
        }
        return $model;
    }
    public $headers;

    /**
     * @var string
     */
    public $keywords;

}
